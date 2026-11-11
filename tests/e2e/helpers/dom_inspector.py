"""
tests/e2e/helpers/dom_inspector.py
Static and AST/regex inspection utilities for JSX components and data files.
"""
import os
from pathlib import Path
import re
from typing import Any, Dict, List, Optional

def inspect_navbar_jsx(navbar_path: Path | str) -> Dict[str, Any]:
    """Inspects src/components/Navbar.jsx for required branding and layout properties."""
    p = Path(navbar_path)
    if not p.exists():
        raise FileNotFoundError(f"Navbar component not found at: {p}")

    content = p.read_text(encoding="utf-8")

    # Image elements
    img_tags = re.findall(r"<img[^>]+>", content)
    kiit_img_tags = [img for img in img_tags if re.search(r"kiit", img, re.I)]

    # ACIE logo path
    acie_logo_match = re.search(r'src=["\']([^"\']*acie-official-logo[^"\']*)["\']', content)
    acie_logo_src = acie_logo_match.group(1) if acie_logo_match else ""

    # Container classes
    container_match = re.search(r'className=["\']([^"\']*max-w-7xl[^"\']*)["\']', content)
    has_max_w_7xl = bool(container_match)

    # Action buttons
    has_registration = bool(re.search(r">\s*REGISTRATION\s*<", content, re.I))
    has_brochure = bool(re.search(r">\s*BROCHURE\s*<", content, re.I))

    # Single line flex layout on desktop
    has_flex_nowrap = "flex-nowrap" in content
    has_desktop_flex = "hidden lg:flex" in content or "lg:flex" in content

    # Navigation items
    nav_items = ["HOME", "ABOUT", "AUTHORS", "SPEAKERS", "COMMITTEE", "AWARDS", "ACCOMODATION", "SCHEDULE", "SPONSORSHIP"]
    present_nav_items = [item for item in nav_items if item in content.upper()]

    # Mobile menu toggle
    has_mobile_drawer = "lg:hidden" in content and any(var in content for var in ["mobileMenuOpen", "isOpen", "isMenuOpen"])

    return {
        "img_tags_count": len(img_tags),
        "kiit_img_tags": kiit_img_tags,
        "has_kiit_logo_img": len(kiit_img_tags) > 0,
        "acie_logo_src": acie_logo_src,
        "has_max_w_7xl": has_max_w_7xl,
        "has_registration_button": has_registration,
        "has_brochure_button": has_brochure,
        "has_flex_nowrap": has_flex_nowrap,
        "has_desktop_flex": has_desktop_flex,
        "nav_items_found": present_nav_items,
        "all_nav_items_present": len(present_nav_items) == len(nav_items),
        "has_mobile_drawer": has_mobile_drawer,
    }

def inspect_hero_carousel_overlay(home_path: Path | str) -> Dict[str, Any]:
    """Inspects src/pages/Home.jsx for hero section carousel styling."""
    p = Path(home_path)
    if not p.exists():
        raise FileNotFoundError(f"Home page not found at: {p}")

    content = p.read_text(encoding="utf-8")

    # Look for all absolute inset-0 overlay elements
    all_overlays = re.findall(r'<div[^>]*className=["\']([^"\']*absolute inset-0[^"\']*)["\']', content)
    is_transparent = any("bg-transparent" in cls for cls in all_overlays)
    has_white_bg = any(
        any(w in cls for w in ["bg-white", "bg-white/80", "bg-white/90", "bg-slate-100"])
        for cls in all_overlays
    )

    # Slide array and timer
    has_slides_array = ("HERO_SLIDES" in content or "slides" in content) and "currentSlide" in content
    has_5s_interval = "5000" in content

    return {
        "overlay_classes": " | ".join(all_overlays),
        "is_transparent": is_transparent,
        "has_white_bg": has_white_bg,
        "has_slides_array": has_slides_array,
        "has_5s_interval": has_5s_interval,
    }

def scan_personnel_occurrences(root_path: Path | str, target_name: str = "suchismita") -> List[Dict[str, Any]]:
    """
    Recursively scans all workspace files (excluding .git, node_modules, dist, .agents, tests)
    for case-insensitive occurrences of the deprecated personnel name.
    """
    root = Path(root_path)
    matches = []
    pattern = re.compile(rf"\b(dr\.?\s*)?{target_name}\b", re.IGNORECASE)

    ignored_dirs = {".git", "node_modules", "dist", ".agents", "tests"}

    for dirpath, dirnames, filenames in os.walk(root):
        # Exclude ignored directories in-place
        dirnames[:] = [d for d in dirnames if d not in ignored_dirs and not d.startswith(".")]

        for fn in filenames:
            file_path = Path(dirpath) / fn
            # Only check text or source files
            if file_path.suffix.lower() in [".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".json", ".py", ".md", ".txt"]:
                try:
                    text = file_path.read_text(encoding="utf-8", errors="ignore")
                    for line_num, line in enumerate(text.splitlines(), start=1):
                        if pattern.search(line):
                            matches.append({
                                "file": str(file_path.relative_to(root)),
                                "line": line_num,
                                "text": line.strip()
                            })
                except Exception:
                    pass

    return matches

def scan_subhas_chinara(root_path: Path | str) -> Dict[str, Any]:
    """Verifies canonical adoption of Prof. Dr. Subhas Chinara, NIT Rourkela, India."""
    root = Path(root_path)
    target_phrase = "Prof. Dr. Subhas Chinara"
    affiliation = "NIT Rourkela, India"

    data_file = root / "src" / "data" / "conferenceData.js"
    patrons_file = root / "src" / "pages" / "Patrons.jsx"

    data_text = data_file.read_text(encoding="utf-8") if data_file.exists() else ""
    patrons_text = patrons_file.read_text(encoding="utf-8") if patrons_file.exists() else ""

    return {
        "in_conference_data": target_phrase in data_text and affiliation in data_text,
        "in_patrons_page": target_phrase in patrons_text and affiliation in patrons_text,
    }

def scan_sponsorship_coordinator(root_path: Path | str) -> Dict[str, Any]:
    """Verifies subhradebdas coordinator contact across data and pages."""
    root = Path(root_path)
    expected_name = "subhradebdas"
    expected_phone = "1234567890"
    expected_email = "sponsorship@acieopen.com"

    files_to_check = [
        root / "src" / "data" / "conferenceData.js",
        root / "src" / "pages" / "Patrons.jsx",
        root / "src" / "pages" / "Sponsorship.jsx",
        root / "src" / "components" / "Footer.jsx"
    ]

    results = {}
    for f in files_to_check:
        if f.exists():
            content = f.read_text(encoding="utf-8")
            results[f.name] = {
                "has_name": expected_name in content,
                "has_phone": expected_phone in content,
                "has_email": expected_email in content,
            }
        else:
            results[f.name] = {"missing": True}

    return results
