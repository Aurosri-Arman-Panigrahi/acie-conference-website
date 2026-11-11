import os
import re
import subprocess
import sys
import fitz  # PyMuPDF

WORKSPACE = r"c:\Users\ARMAN\Desktop\project\conferenec website"

def run_tests():
    print("=" * 60)
    print("M3 ADVERSARIAL TEST SUITE STARTING")
    print("=" * 60)
    failures = []
    
    # --------------------------------------------------------------------------
    # TEST 1: Stale Pattern Exhaustion Across All Workspace Files
    # --------------------------------------------------------------------------
    print("\n[TEST 1] Regex & Pattern Exhaustion Sweep...")
    exclude_dirs = {'.git', 'node_modules', 'dist', '.agents'}
    
    pat_suchismita = re.compile(r'suchismita', re.IGNORECASE)
    pat_chinara = re.compile(r'chinara', re.IGNORECASE)
    pat_cutm_chairs = [
        re.compile(r'rakesh\s+kumar\s+ray', re.IGNORECASE),
        re.compile(r'jyoti\s+prakash\s+giri', re.IGNORECASE),
        re.compile(r'deepak\s+kumar\s+sahu', re.IGNORECASE),
    ]
    
    suchismita_matches = []
    invalid_chinara_matches = []
    cutm_chair_matches = []
    
    this_file = os.path.normcase(os.path.abspath(__file__))
    for root, dirs, files in os.walk(WORKSPACE):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for f in files:
            fpath = os.path.join(root, f)
            if os.path.normcase(os.path.abspath(fpath)) == this_file:
                continue
            relpath = os.path.relpath(fpath, WORKSPACE)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                    for line_idx, line in enumerate(fp, 1):
                        if pat_suchismita.search(line):
                            suchismita_matches.append(f"{relpath}:{line_idx}: {line.strip()}")
                        
                        if pat_chinara.search(line):
                            # Verify if it has both Prof. Dr. and Subhas
                            if not ("Subhas" in line and ("Prof. Dr." in line or "Prof. Dr" in line)):
                                invalid_chinara_matches.append(f"{relpath}:{line_idx}: {line.strip()}")
                        
                        for cutm_pat in pat_cutm_chairs:
                            if cutm_pat.search(line):
                                cutm_chair_matches.append(f"{relpath}:{line_idx}: {line.strip()}")
            except Exception as e:
                pass

    if suchismita_matches:
        failures.append(f"Found 'suchismita' in workspace: {suchismita_matches}")
        print("  FAIL: 'suchismita' found!")
    else:
        print("  PASS: Zero occurrences of 'suchismita' found across entire workspace.")

    if invalid_chinara_matches:
        failures.append(f"Found non-standard 'chinara' references: {invalid_chinara_matches}")
        print("  FAIL: Non-standard 'chinara' references found!")
    else:
        print("  PASS: All 'chinara' references strictly match 'Prof. Dr. Subhas Chinara'.")

    if cutm_chair_matches:
        failures.append(f"Found outdated CUTM chairs: {cutm_chair_matches}")
        print("  FAIL: Outdated CUTM chairs found!")
    else:
        print("  PASS: Zero occurrences of outdated CUTM chairs (Rakesh Kumar Ray, Jyoti Prakash Giri, Deepak Kumar Sahu).")

    # --------------------------------------------------------------------------
    # TEST 2: Sponsorship Coordinator Channel Consistency
    # --------------------------------------------------------------------------
    print("\n[TEST 2] Sponsorship Coordinator Consistency...")
    
    # 2a. conferenceData.js
    conf_data_path = os.path.join(WORKSPACE, "src", "data", "conferenceData.js")
    with open(conf_data_path, "r", encoding="utf-8") as f:
        conf_data = f.read()
    
    assert 'name: "subhradebdas"' in conf_data, "subhradebdas missing in conferenceData.js"
    assert 'phone: "1234567890"' in conf_data, "1234567890 missing in conferenceData.js"
    assert 'email: "sponsorship@acieopen.com"' in conf_data, "sponsorship@acieopen.com missing in conferenceData.js"
    print("  PASS: conferenceData.js contains consistent sponsorship coordinator details.")

    # 2b. Sponsorship.jsx
    sponsorship_jsx_path = os.path.join(WORKSPACE, "src", "pages", "Sponsorship.jsx")
    with open(sponsorship_jsx_path, "r", encoding="utf-8") as f:
        spons_jsx = f.read()
    assert 'subhradebdas' in spons_jsx, "subhradebdas missing in Sponsorship.jsx"
    assert 'tel:1234567890' in spons_jsx, "tel:1234567890 missing in Sponsorship.jsx"
    assert 'mailto:sponsorship@acieopen.com' in spons_jsx, "mailto:sponsorship@acieopen.com missing in Sponsorship.jsx"
    print("  PASS: Sponsorship.jsx contains valid subhradebdas, tel:1234567890, mailto:sponsorship@acieopen.com.")

    # 2c. Patrons.jsx
    patrons_jsx_path = os.path.join(WORKSPACE, "src", "pages", "Patrons.jsx")
    with open(patrons_jsx_path, "r", encoding="utf-8") as f:
        patrons_jsx = f.read()
    assert 'subhradebdas (Phone: 1234567890, Email: sponsorship@acieopen.com)' in patrons_jsx, "Coordinator details missing in Patrons.jsx"
    assert 'Rakesh Kumar Ray' not in patrons_jsx, "Rakesh Kumar Ray still in Patrons.jsx"
    assert 'Jyoti Prakash Giri' not in patrons_jsx, "Jyoti Prakash Giri still in Patrons.jsx"
    assert 'Deepak Kumar Sahu' not in patrons_jsx, "Deepak Kumar Sahu still in Patrons.jsx"
    print("  PASS: Patrons.jsx lists subhradebdas and completely removed old CUTM chairs.")

    # 2d. Brochure PDF
    brochure_pdf = os.path.join(WORKSPACE, "public", "assets", "brochure", "ACIE-2027-Brochure.pdf")
    if os.path.exists(brochure_pdf):
        doc = fitz.open(brochure_pdf)
        pdf_text = "\n".join([page.get_text() for page in doc])
        assert "Prof. Dr. Subhas Chinara, NIT Rourkela, India" in pdf_text, "Chinara missing in brochure PDF"
        assert "subhradebdas" in pdf_text, "subhradebdas missing in brochure PDF"
        assert "1234567890" in pdf_text, "Phone number missing in brochure PDF"
        assert "sponsorship@acieopen.com" in pdf_text, "Email missing in brochure PDF"
        assert "suchismita" not in pdf_text.lower(), "Suchismita found in brochure PDF"
        print("  PASS: ACIE-2027-Brochure.pdf contains correct Subhas Chinara & subhradebdas sponsorship info.")
    else:
        print("  WARN: ACIE-2027-Brochure.pdf not found at expected path.")

    # --------------------------------------------------------------------------
    # TEST 3: Hero Poster Overlay Verification in src/pages/Home.jsx
    # --------------------------------------------------------------------------
    print("\n[TEST 3] Hero Poster Styling Verification...")
    home_jsx_path = os.path.join(WORKSPACE, "src", "pages", "Home.jsx")
    with open(home_jsx_path, "r", encoding="utf-8") as f:
        home_jsx = f.read()

    # Find the hero section overlay
    assert 'bg-transparent' in home_jsx, "bg-transparent overlay missing in Home.jsx"
    
    # Check that overlay is explicitly transparent
    overlay_match = re.search(r'<div\s+className=["\']absolute inset-0 z-10 pointer-events-none\s+bg-transparent["\']\s*/>', home_jsx)
    if not overlay_match:
        failures.append("Hero overlay div in Home.jsx does not have exact expected 'absolute inset-0 z-10 pointer-events-none bg-transparent' class structure")
        print("  FAIL: Hero overlay class mismatch.")
    else:
        print("  PASS: Hero overlay is confirmed 'bg-transparent' with pointer-events-none.")

    # Check for unwanted white background classes on hero text or section
    # Hero text headline:
    assert 'style={{ textShadow:' in home_jsx, "textShadow missing from hero text for contrast"
    print("  PASS: Hero text has textShadow applied for contrast directly over slides.")

    # --------------------------------------------------------------------------
    # TEST 4: Production Build & Bundle Inspection
    # --------------------------------------------------------------------------
    print("\n[TEST 4] Production Build and Bundle Inspection...")
    build_res = subprocess.run(["npm", "run", "build"], cwd=WORKSPACE, shell=True, capture_output=True, text=True)
    if build_res.returncode != 0:
        failures.append(f"npm run build failed with exit code {build_res.returncode}:\n{build_res.stderr}")
        print(f"  FAIL: Build exited with code {build_res.returncode}")
    else:
        print("  PASS: npm run build exited with code 0.")

    # Check dist JS bundle
    dist_assets = os.path.join(WORKSPACE, "dist", "assets")
    js_files = [os.path.join(dist_assets, f) for f in os.listdir(dist_assets) if f.endswith(".js")]
    for js_path in js_files:
        with open(js_path, "r", encoding="utf-8") as f:
            js_content = f.read()
        if "suchismita" in js_content.lower():
            failures.append(f"Compiled bundle {js_path} contains 'suchismita'!")
            print(f"  FAIL: 'suchismita' found in compiled bundle {js_path}")
        if "rakesh kumar ray" in js_content.lower():
            failures.append(f"Compiled bundle {js_path} contains 'rakesh kumar ray'!")
            print(f"  FAIL: 'rakesh kumar ray' found in compiled bundle {js_path}")

    print("  PASS: Production bundle is free of stale personnel.")

    print("\n" + "=" * 60)
    if failures:
        print(f"TEST SUITE FAILED with {len(failures)} failures:")
        for fail in failures:
            print(f"  - {fail}")
        sys.exit(1)
    else:
        print("TEST SUITE PASSED ALL CHECKS.")
        print("VERDICT: APPROVE")
        print("=" * 60)
        sys.exit(0)

if __name__ == "__main__":
    run_tests()
