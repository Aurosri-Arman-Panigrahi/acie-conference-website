"""
Adversarial Verification Script for Milestone M4 (Project Directory Cleanup)
Challenger 1
"""
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def check_exact_casing_on_disk(base_dir: Path, rel_path: str) -> tuple[bool, str, str]:
    """
    Traverse path segments on physical filesystem using os.listdir()
    to ensure exact case match (preventing Linux 404s on Netlify).
    Returns (is_match, expected_casing, actual_casing_on_disk).
    """
    segments = Path(rel_path).parts
    current = base_dir.resolve()
    
    for seg in segments:
        if not current.exists():
            return False, rel_path, f"Directory does not exist: {current}"
        try:
            entries = os.listdir(current)
        except Exception as e:
            return False, rel_path, str(e)
            
        # Exact match
        if seg in entries:
            current = current / seg
        else:
            # Check case-insensitive match to detect casing discrepancy
            lower_map = {e.lower(): e for e in entries}
            if seg.lower() in lower_map:
                actual_seg = lower_map[seg.lower()]
                return False, seg, actual_seg
            else:
                return False, seg, f"Not found in {entries}"
                
    return True, rel_path, str(current)

def verify_file_integrity(file_path: Path) -> tuple[bool, str]:
    """Check if file can be opened/read properly without corruption."""
    size = file_path.stat().st_size
    if size == 0:
        return False, "Zero byte file"
        
    ext = file_path.suffix.lower()
    try:
        if ext in ['.png', '.jpg', '.jpeg', '.webp']:
            with Image.open(file_path) as img:
                img.verify()
        elif ext == '.svg':
            ET.parse(file_path)
        elif ext == '.pdf':
            # Check PDF header
            with open(file_path, 'rb') as f:
                header = f.read(5)
                if header != b'%PDF-':
                    return False, f"Invalid PDF header: {header}"
        elif ext in ['.json', '.js', '.jsx', '.html', '.css', '.md', '.txt']:
            file_path.read_text(encoding='utf-8')
        else:
            with open(file_path, 'rb') as f:
                f.read(1024)
        return True, f"OK ({size} bytes)"
    except Exception as e:
        return False, f"Corrupted: {e}"

def check_relative_imports_and_broken_relative_paths(root: Path):
    """Ensure no source file uses relative paths like '../assets' or broken relative imports."""
    src_dir = root / "src"
    issues = []
    rel_pattern = re.compile(r"""(?:import|from|href|src)\s*[=]?\s*['"](\.{1,2}/assets/[^'"]+)['"]""")
    for p in src_dir.rglob("*.*"):
        if p.suffix in [".jsx", ".js", ".css"]:
            txt = p.read_text(encoding="utf-8", errors="ignore")
            for m in rel_pattern.finditer(txt):
                issues.append(f"{p.name} contains relative asset reference: {m.group(1)}")
    return issues

def crawl_codebase_asset_references(root: Path):
    """Scan all source files and extract asset references."""
    targets = []
    # Collect all src files, index.html, build_exact_brochure.py
    src_dir = root / "src"
    for ext in ("*.jsx", "*.js", "*.css", "*.json", "*.html"):
        targets.extend(src_dir.rglob(ext))
    targets.append(root / "index.html")
    if (root / "build_exact_brochure.py").exists():
        targets.append(root / "build_exact_brochure.py")

    # Regex patterns to capture asset strings
    patterns = [
        re.compile(r"""(?:["'`])((?:public/assets/|/assets/|assets/)[^"'`\s]+)(?:["'`])"""),
        re.compile(r"""url\((?:['"]?)(/(?:assets/[^'")\s]+))(?:['"]?)\)"""),
        re.compile(r"""url\((?:['"]?)(assets/[^'")\s]+)(?:['"]?)\)""")
    ]

    references = {}
    for target in targets:
        if not target.exists():
            continue
        try:
            content = target.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        for pat in patterns:
            for match in pat.finditer(content):
                ref = match.group(1).strip()
                # Clean query strings or hash if any
                ref_clean = ref.split('?')[0].split('#')[0]
                if ref_clean not in references:
                    references[ref_clean] = []
                references[ref_clean].append(str(target.relative_to(root)))

    return references

def run_adversarial_suite():
    print("======================================================================")
    print("CHALLENGER 1: ADVERSARIAL VERIFICATION FOR MILESTONE M4")
    print("======================================================================")
    
    errors = []
    warnings = []
    
    # 1. Crawl codebase
    relative_issues = check_relative_imports_and_broken_relative_paths(PROJECT_ROOT)
    if relative_issues:
        for r_issue in relative_issues:
            print(f"  ❌ {r_issue}")
            errors.append(r_issue)
    else:
        print("  ✅ Confirmed zero relative asset imports/paths in src/ (Vite canonical /assets/ compliant)")

    refs = crawl_codebase_asset_references(PROJECT_ROOT)
    print(f"\n[1] Crawled codebase: found {len(refs)} unique static asset references across {sum(len(v) for v in refs.values())} occurrences.")
    
    # 2. Verify each reference
    print("\n[2] Verifying physical existence, integrity, and exact case-matching on disk:")
    
    public_dir = PROJECT_ROOT / "public"
    
    for ref, locations in sorted(refs.items()):
        # Normalize relative path under public
        if ref.startswith("public/"):
            rel_in_public = ref.replace("public/", "", 1)
        elif ref.startswith("/"):
            rel_in_public = ref.lstrip("/")
        elif ref.startswith("assets/"):
            rel_in_public = ref
        else:
            rel_in_public = ref

        full_disk_path = public_dir / rel_in_public
        
        # Check existence
        if not full_disk_path.exists():
            msg = f"BROKEN LINK: Asset '{ref}' referenced in {locations} does NOT exist at '{full_disk_path}'"
            print(f"  ❌ {msg}")
            errors.append(msg)
            continue
            
        # Check exact casing
        casing_ok, expected_seg, actual_seg = check_exact_casing_on_disk(public_dir, rel_in_public)
        if not casing_ok:
            msg = f"CASING MISMATCH: Asset '{ref}' expected segment '{expected_seg}' but physical disk has '{actual_seg}'. This will 404 on Netlify (Linux)!"
            print(f"  ❌ {msg}")
            errors.append(msg)
        else:
            # Check integrity
            integrity_ok, int_msg = verify_file_integrity(full_disk_path)
            if not integrity_ok:
                msg = f"FILE INTEGRITY FAILED: Asset '{ref}' failed integrity check: {int_msg}"
                print(f"  ❌ {msg}")
                errors.append(msg)
            else:
                print(f"  ✅ [EXACT CASE & VALID] {ref} ({int_msg}) <- referenced in {len(locations)} file(s)")

    # 3. Check for root assets/ directory and obsolete directories/files
    print("\n[3] Checking deletion of clutter targets:")
    targets_to_be_absent = [
        "assets",
        "brochure_extracted_assets",
        "generate_brochure_pdf.py",
        "temp_test.pdf",
        "public/assets/videos",
        "public/assets/audio",
        "public/assets/papers",
        "public/assets/data",
        "public/assets/images/figures",
        "public/assets/images/slides"
    ]
    for target in targets_to_be_absent:
        target_path = PROJECT_ROOT / target
        if target_path.exists():
            msg = f"LEFTOVER CLUTTER: '{target}' was supposed to be removed but still exists on disk!"
            print(f"  ❌ {msg}")
            errors.append(msg)
        else:
            print(f"  ✅ Verified absent: {target}")

    # 4. Check active assets whitelist completeness
    print("\n[4] Checking active assets in public/assets:")
    public_assets = list((public_dir / "assets").rglob("*.*"))
    print(f"  Found {len(public_assets)} files in public/assets/")
    
    # 5. Summary and Verdict
    print("\n======================================================================")
    print("VERIFICATION SUMMARY")
    print("======================================================================")
    print(f"Total references checked: {len(refs)}")
    print(f"Total errors: {len(errors)}")
    print(f"Total warnings: {len(warnings)}")
    
    if errors:
        print("\nVERDICT: REJECT")
        for err in errors:
            print(f"  - {err}")
        return 1
    else:
        print("\nVERDICT: APPROVE (Confirmed zero broken links, perfect casing, clean removal)")
        return 0

if __name__ == "__main__":
    sys.exit(run_adversarial_suite())
