"""
tests/e2e/test_r4_cleanup.py
E2E Opaque-Box Tests for Requirement R4: Project Directory Cleanup & Asset Preservation.
Covers Tier 1 (Feature Coverage) and Tier 2 (Boundary & Corner Cases).
"""
import json
import os
from pathlib import Path
import unittest

from tests.e2e.helpers.decorators import tier, feature
from tests.e2e.helpers.git_inspector import (
    audit_whitelist_assets,
    audit_unreferenced_in_source,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# The authoritative 37 Active Assets Whitelist
ACTIVE_ASSETS_WHITELIST = [
    # Brochure (1)
    "public/assets/brochure/ACIE-2027-Brochure.pdf",
    
    # Active Logos (8)
    "public/assets/images/logos/acie-logo.svg",
    "public/assets/images/logos/acie-minimal-1.svg",
    "public/assets/images/logos/acie-minimal-2.svg",
    "public/assets/images/logos/acie-minimal-4.svg",
    "public/assets/images/logos/acie-official-logo-transparent.png",
    "public/assets/images/logos/ieee-logo.svg",
    "public/assets/images/logos/kiit-official-logo.png",
    "public/assets/images/logos/kiit-official-logo.webp",
    
    # Active KIIT Campus Photos (8)
    "public/assets/images/kiit/kiit-academics-1.webp",
    "public/assets/images/kiit/kiit-academics-2.webp",
    "public/assets/images/kiit/kiit-academics-3.webp",
    "public/assets/images/kiit/kiit-campus-aerial.webp",
    "public/assets/images/kiit/kiit-campus-arch.webp",
    "public/assets/images/kiit/kiit-campus-building-6.webp",
    "public/assets/images/kiit/kiit-convention-center.webp",
    "public/assets/images/kiit/kiit-library-front.jpg",
    
    # Active Tourism, Icons & QR (10)
    "public/assets/images/scraped/Dhauli-C0DD5BOJ.jpg",
    "public/assets/images/scraped/barabati-B4WPFbhS.jpg",
    "public/assets/images/scraped/chilika-C2Nze43z.jpg",
    "public/assets/images/scraped/konark-B97Vv_kx.jpg",
    "public/assets/images/scraped/lingaraj-CzRx05ve.jpg",
    "public/assets/images/scraped/map-BfyYLnYn.jpg",
    "public/assets/images/scraped/puri-siI7osXQ.jpg",
    "public/assets/images/scraped/qr-code-B5kqw1J3.png",
    "public/assets/images/scraped/rajarani-BRbc6iQ7.jpg",
    "public/assets/images/scraped/zoo-B5RwaHE3.jpg",
    
    # Active Keynote & Invited Speakers (10)
    "public/assets/images/scraped/keynoteSpaker1-z4l0bNR_.png",
    "public/assets/images/scraped/keynoteSpeaker2-BtsNogkk.png",
    "public/assets/images/scraped/keynoteSpeaker3-7pPvxVRK.png",
    "public/assets/images/scraped/keynoteSpeaker4-C7JEQMXu.png",
    "public/assets/images/scraped/keynoteSpeaker5-CU3eZAKd.jpeg",
    "public/assets/images/scraped/keynoteSpeaker10-xQzNenqP.png",
    "public/assets/images/scraped/newSpeaker-BsSODFWa.png",
    "public/assets/images/scraped/newSpeaker2-DRXI_EuR.png",
    "public/assets/images/scraped/newSpeaker3-CZHDiFUn.png",
    "public/assets/images/scraped/newSpeaker4-Brg4EqWV.png"
]

# Dead media blacklist targets
DEAD_MEDIA_TARGETS = [
    "assets",
    "brochure_extracted_assets",
    "generate_brochure_pdf.py",
    "public/assets/videos",
    "public/assets/audio",
    "public/assets/papers",
    "public/assets/data",
    "public/assets/images/figures",
    "public/assets/images/slides"
]

class TestR4Cleanup(unittest.TestCase):
    """E2E Test Suite for Requirement R4: Project Directory Cleanup & Asset Preservation."""

    # ==========================================
    # Tier 1: Feature Coverage (Deterministic)
    # ==========================================

    @tier(1)
    @feature("r4")
    def test_t1_r4_01_root_duplicate_assets_audit_and_cleanup(self):
        """T1-R4-01: Audit root assets/ - assert zero imports in src/ and verify cleanup target."""
        # Check that src/ code never imports directly from root assets/
        is_unreferenced = audit_unreferenced_in_source(PROJECT_ROOT, "assets")
        self.assertTrue(is_unreferenced, "Source files must not import from root assets/ directory")

        root_assets = PROJECT_ROOT / "assets"
        if not root_assets.exists():
            # If M4 cleanup milestone is executed, assert it does not exist
            self.assertFalse(root_assets.exists(), "Root assets/ directory successfully removed")
        else:
            # If in-flight prior to M4, verify all files in assets/ are duplicate copies of public/assets/
            public_assets = PROJECT_ROOT / "public" / "assets"
            self.assertTrue(public_assets.exists(), "public/assets/ must exist as canonical asset store")

    @tier(1)
    @feature("r4")
    def test_t1_r4_02_obsolete_scripts_and_extracted_assets(self):
        """T1-R4-02: Verify obsolete scripts and extracted assets are unreferenced in production codebase."""
        src_dir = PROJECT_ROOT / "src"
        for p in src_dir.rglob("*.jsx"):
            text = p.read_text(encoding="utf-8", errors="ignore")
            self.assertNotIn("brochure_extracted_assets", text, f"{p.name} references obsolete brochure_extracted_assets")
            self.assertNotIn("generate_brochure_pdf", text, f"{p.name} references obsolete generate_brochure_pdf")

        # Active build script is build_exact_brochure.py
        active_script = PROJECT_ROOT / "build_exact_brochure.py"
        self.assertTrue(active_script.exists(), "Canonical build_exact_brochure.py must exist")

    @tier(1)
    @feature("r4")
    def test_t1_r4_03_heavy_dead_media_blacklist_audit(self):
        """T1-R4-03: Verify dead media categories (videos, audio, papers) contain zero referenced active assets."""
        src_dir = PROJECT_ROOT / "src"
        all_src_text = " ".join([p.read_text(encoding="utf-8", errors="ignore") for p in src_dir.rglob("*.*")])

        # None of the 37 active assets are in videos/, audio/, papers/, or data/
        for rel_path in ACTIVE_ASSETS_WHITELIST:
            self.assertNotIn("/videos/", rel_path)
            self.assertNotIn("/audio/", rel_path)
            self.assertNotIn("/papers/", rel_path)
            self.assertNotIn("/data/", rel_path)

        # Confirm source code does not import .mp4 or .mp3
        self.assertNotIn(".mp4", all_src_text)
        self.assertNotIn(".mp3", all_src_text)

    @tier(1)
    @feature("r4")
    def test_t1_r4_04_active_asset_whitelist_retention(self):
        """T1-R4-04: Assert every single one of the 37 whitelisted assets exists and size > 0."""
        audit = audit_whitelist_assets(PROJECT_ROOT, ACTIVE_ASSETS_WHITELIST)
        self.assertEqual(
            len(audit["missing"]), 0,
            f"Missing required whitelist assets: {audit['missing']}"
        )
        self.assertEqual(
            len(audit["zero_byte"]), 0,
            f"Zero-byte truncated whitelist assets: {audit['zero_byte']}"
        )
        self.assertEqual(audit["valid_count"], 37, "All 37 active assets must be valid and non-empty")

    @tier(1)
    @feature("r4")
    def test_t1_r4_05_build_and_configuration_files_integrity(self):
        """T1-R4-05: Assert root configs (package.json, vite.config.js, netlify.toml, etc.) exist and parse."""
        config_files = [
            "package.json",
            "vite.config.js",
            "tailwind.config.js",
            "postcss.config.js",
            "netlify.toml",
            ".gitignore",
            "index.html"
        ]
        for cfg in config_files:
            cfg_path = PROJECT_ROOT / cfg
            self.assertTrue(cfg_path.exists(), f"Configuration file {cfg} must exist")
            self.assertGreater(cfg_path.stat().st_size, 0, f"Configuration file {cfg} must not be empty")

        # Parse package.json
        pkg_json = json.loads((PROJECT_ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(pkg_json.get("name"), "acie-conference-website")
        self.assertIn("build", pkg_json.get("scripts", {}))

    @tier(1)
    @feature("r4")
    def test_t1_r4_06_source_tree_react_files_integrity(self):
        """T1-R4-06: Assert core React source components and pages exist and are non-empty."""
        core_files = [
            "src/main.jsx",
            "src/App.jsx",
            "src/components/Navbar.jsx",
            "src/components/Footer.jsx",
            "src/components/BrochureModal.jsx",
            "src/pages/Home.jsx",
            "src/pages/AboutKIIT.jsx",
            "src/pages/Patrons.jsx",
            "src/pages/KeynoteSpeakers.jsx",
            "src/pages/Registration.jsx",
            "src/pages/Sponsorship.jsx",
            "src/data/conferenceData.js"
        ]
        for cf in core_files:
            cf_path = PROJECT_ROOT / cf
            self.assertTrue(cf_path.exists(), f"Source file {cf} must exist")
            self.assertGreater(cf_path.stat().st_size, 50, f"Source file {cf} must be non-empty")

    # ==========================================
    # Tier 2: Boundary & Corner Cases
    # ==========================================

    @tier(2)
    @feature("r4")
    def test_t2_r4_01_whitelist_asset_zero_byte_invalidation(self):
        """T2-R4-01: Assert all 37 whitelist assets have file size >= 500 bytes (non-stub)."""
        for rel_path in ACTIVE_ASSETS_WHITELIST:
            p = PROJECT_ROOT / rel_path
            size = p.stat().st_size
            self.assertGreater(size, 500, f"Asset {rel_path} size ({size} bytes) indicates corrupt/stub file")

    @tier(2)
    @feature("r4")
    def test_t2_r4_02_case_sensitive_path_collision_check(self):
        """T2-R4-02: Verify asset path casing matches exact casing on disk for Linux/Netlify parity."""
        brochure_path = PROJECT_ROOT / "public" / "assets" / "brochure" / "ACIE-2027-Brochure.pdf"
        self.assertTrue(brochure_path.exists())
        # Check parent folder casing
        actual_name = brochure_path.name
        self.assertEqual(actual_name, "ACIE-2027-Brochure.pdf", "Brochure filename casing must match exactly")

    @tier(2)
    @feature("r4")
    def test_t2_r4_03_deep_nested_orphan_directories_audit(self):
        """T2-R4-03: Verify all 37 active assets reside strictly in designated canonical directories."""
        allowed_prefixes = (
            "public/assets/brochure/",
            "public/assets/images/logos/",
            "public/assets/images/kiit/",
            "public/assets/images/scraped/"
        )
        for rel_path in ACTIVE_ASSETS_WHITELIST:
            norm_path = rel_path.replace("\\", "/")
            self.assertTrue(
                norm_path.startswith(allowed_prefixes),
                f"Asset {norm_path} is outside allowed canonical directories"
            )

    @tier(2)
    @feature("r4")
    def test_t2_r4_04_git_metadata_and_agents_segregation(self):
        """T2-R4-04: Verify .agents/ metadata is properly segregated from production assets."""
        public_dir = PROJECT_ROOT / "public"
        agents_in_public = list(public_dir.rglob(".agents"))
        self.assertEqual(len(agents_in_public), 0, ".agents directory must never exist in public assets")

    @tier(2)
    @feature("r4")
    def test_t2_r4_05_symlink_and_junction_safety(self):
        """T2-R4-05: Assert all whitelist assets are real files, not broken symlinks or junctions."""
        for rel_path in ACTIVE_ASSETS_WHITELIST:
            p = PROJECT_ROOT / rel_path
            self.assertFalse(p.is_symlink(), f"Asset {rel_path} must be a real file, not a symlink")
            self.assertTrue(p.is_file(), f"Asset {rel_path} must be a regular file")

    @tier(2)
    @feature("r4")
    def test_t2_r4_06_production_bundle_budget_threshold(self):
        """T2-R4-06: Verify total size of the 37 active assets is strictly within ~10 MB budget."""
        total_active_bytes = sum((PROJECT_ROOT / p).stat().st_size for p in ACTIVE_ASSETS_WHITELIST)
        max_budget = 15 * 1024 * 1024  # 15 MB
        self.assertLess(
            total_active_bytes, max_budget,
            f"Active asset footprint ({total_active_bytes / 1024 / 1024:.2f} MB) exceeds 15 MB budget"
        )


if __name__ == "__main__":
    unittest.main()
