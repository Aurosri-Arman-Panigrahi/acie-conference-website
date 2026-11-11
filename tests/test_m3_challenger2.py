import os
import re
import sys

def main():
    print("=" * 60)
    print("CHALLENGER 2 EMPIRICAL TEST SUITE (M3)")
    print("=" * 60)

    pass_count = 0
    fail_count = 0

    def check(cond, name):
        nonlocal pass_count, fail_count
        if cond:
            print(f" [PASS] {name}")
            pass_count += 1
        else:
            print(f" [FAIL] {name}")
            fail_count += 1

    # --------------------------------------------------------------------------
    # TASK 1: Build & Bundle Inspection
    # --------------------------------------------------------------------------
    print("\n--- TASK 1: Production Bundle Inspection in dist/ ---")
    dist_dir = "dist"
    assert os.path.exists(dist_dir), "dist directory does not exist!"

    assets_dir = os.path.join(dist_dir, "assets")
    js_files = [os.path.join(assets_dir, f) for f in os.listdir(assets_dir) if f.endswith(".js")]
    css_files = [os.path.join(assets_dir, f) for f in os.listdir(assets_dir) if f.endswith(".css")]
    html_file = os.path.join(dist_dir, "index.html")

    all_bundle_content = ""
    with open(html_file, "r", encoding="utf-8") as f:
        all_bundle_content += f.read() + "\n"
    for fpath in js_files + css_files:
        with open(fpath, "r", encoding="utf-8") as f:
            all_bundle_content += f.read() + "\n"

    check("suchismita" not in all_bundle_content.lower(), "Zero occurrences of 'suchismita' in production bundle (JS/CSS/HTML)")
    check("Prof. Dr. Subhas Chinara" in all_bundle_content, "Compiled bundle strings contain 'Prof. Dr. Subhas Chinara'")
    check("sponsorship@acieopen.com" in all_bundle_content, "Compiled bundle strings contain 'sponsorship@acieopen.com'")
    check("subhradebdas" in all_bundle_content, "Compiled bundle strings contain 'subhradebdas'")
    check("1234567890" in all_bundle_content, "Compiled bundle strings contain '1234567890'")
    check("tel:1234567890" in all_bundle_content, "Compiled bundle contains functional 'tel:1234567890' hyperlink")
    check("mailto:sponsorship@acieopen.com" in all_bundle_content, "Compiled bundle contains functional 'mailto:sponsorship@acieopen.com' hyperlink")

    # --------------------------------------------------------------------------
    # TASK 2: Structure & Styling Stress in Home.jsx
    # --------------------------------------------------------------------------
    print("\n--- TASK 2: Structure & Styling Stress in Home.jsx ---")
    with open("src/pages/Home.jsx", "r", encoding="utf-8") as f:
        home_jsx = f.read()

    check('className="absolute inset-0 z-10 pointer-events-none bg-transparent"' in home_jsx, "Hero overlay div explicitly uses 'bg-transparent' with pointer-events-none")
    check("relative w-full h-screen overflow-hidden" in home_jsx, "Hero container has 'h-screen overflow-hidden' ensuring zero layout overflow")
    check("0 1px 4px rgba(255,255,255,0.95), 0 2px 8px rgba(255,255,255,0.85)" in home_jsx, "Double-layer white halo textShadow on h1 provides strong contrast over animated slides")
    check("0 1px 3px rgba(255,255,255,0.95), 0 2px 6px rgba(255,255,255,0.85)" in home_jsx, "Double-layer white halo textShadow on p provides strong contrast over animated slides")
    check("bg-blue-100 text-blue-900" in home_jsx, "Metadata pills have solid high-contrast badges (bg-blue-100)")

    # --------------------------------------------------------------------------
    # TASK 3: Patrons.jsx Committee Lists & JSX Validity
    # --------------------------------------------------------------------------
    print("\n--- TASK 3: Patrons.jsx Committee Lists & JSX Validity ---")
    with open("src/pages/Patrons.jsx", "r", encoding="utf-8") as f:
        patrons_jsx = f.read()

    check("Prof. Dr. Subhas Chinara, NIT Rourkela, India" in patrons_jsx, "Patrons.jsx lists 'Prof. Dr. Subhas Chinara, NIT Rourkela, India'")
    check("subhradebdas (Phone: 1234567890, Email: sponsorship@acieopen.com)" in patrons_jsx, "Patrons.jsx lists 'subhradebdas (Phone: 1234567890, Email: sponsorship@acieopen.com) – Sponsorship Coordinator'")
    check("Rakesh Kumar Ray" not in patrons_jsx, "Outdated CUTM chair 'Rakesh Kumar Ray' completely removed")
    check("Jyoti Prakash Giri" not in patrons_jsx, "Outdated CUTM chair 'Jyoti Prakash Giri' completely removed")
    check("Deepak Kumar Sahu" not in patrons_jsx, "Outdated CUTM chair 'Deepak Kumar Sahu' completely removed")

    div_open = len(re.findall(r"<div(\s+[^>]*)?>", patrons_jsx))
    div_close = len(re.findall(r"</div>", patrons_jsx))
    check(div_open == div_close and div_open > 0, f"Patrons.jsx <div> tags balanced ({div_open} open, {div_close} close)")

    ul_open = len(re.findall(r"<ul(\s+[^>]*)?>", patrons_jsx))
    ul_close = len(re.findall(r"</ul>", patrons_jsx))
    check(ul_open == ul_close and ul_open > 0, f"Patrons.jsx <ul> tags balanced ({ul_open} open, {ul_close} close)")

    li_open = len(re.findall(r"<li(\s+[^>]*)?>", patrons_jsx))
    li_close = len(re.findall(r"</li>", patrons_jsx))
    check(li_open == li_close and li_open > 0, f"Patrons.jsx <li> tags balanced ({li_open} open, {li_close} close)")

    h3_open = len(re.findall(r"<h3(\s+[^>]*)?>", patrons_jsx))
    h3_close = len(re.findall(r"</h3>", patrons_jsx))
    check(h3_open == h3_close and h3_open > 0, f"Patrons.jsx <h3> tags balanced ({h3_open} open, {h3_close} close)")

    # --------------------------------------------------------------------------
    # TASK 4: Whole-Codebase Stale Pattern Sweep (excluding test files themselves)
    # --------------------------------------------------------------------------
    print("\n--- TASK 4: Codebase Stale Pattern Sweep ---")
    exclude_dirs = {'.git', 'node_modules', 'dist', '.agents', 'tests'}
    suchismita_matches = []
    cutm_matches = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for f in files:
            fpath = os.path.join(root, f)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
                    for line_idx, line in enumerate(fp, 1):
                        if "suchismita" in line.lower():
                            suchismita_matches.append(f"{fpath}:{line_idx}")
                        if "rakesh kumar ray" in line.lower() or "jyoti prakash giri" in line.lower() or "deepak kumar sahu" in line.lower():
                            cutm_matches.append(f"{fpath}:{line_idx}")
            except Exception:
                pass

    check(len(suchismita_matches) == 0, f"Codebase has zero occurrences of 'suchismita' (found {len(suchismita_matches)})")
    check(len(cutm_matches) == 0, f"Codebase has zero occurrences of outdated CUTM chairs (found {len(cutm_matches)})")

    print("\n" + "=" * 60)
    print(f"RESULTS: {pass_count} PASSED, {fail_count} FAILED")
    print("=" * 60)

    if fail_count > 0:
        print("VERDICT: REQUEST_CHANGES")
        sys.exit(1)
    else:
        print("VERDICT: APPROVE")
        sys.exit(0)

if __name__ == "__main__":
    main()
