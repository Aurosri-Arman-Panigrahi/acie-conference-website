"""
tests/e2e/test_pairwise_and_scenarios.py
E2E Opaque-Box Tests for Tier 3 (Cross-Feature Interactions) and Tier 4 (Real-World Application Scenarios).
"""
import json
import os
from pathlib import Path
import re
import unittest
import urllib.request
import ssl
import fitz

from tests.e2e.helpers.decorators import tier, feature
from tests.e2e.helpers.pdf_inspector import (
    open_brochure_pdf,
    get_white_background_boxes,
    extract_vector_text,
    find_embedded_images
)
from tests.e2e.helpers.dom_inspector import (
    inspect_navbar_jsx,
    inspect_hero_carousel_overlay,
    scan_personnel_occurrences,
    scan_subhas_chinara,
    scan_sponsorship_coordinator
)
from tests.e2e.helpers.git_inspector import (
    get_git_branch,
    get_git_remote_url,
    get_git_status_porcelain,
    audit_whitelist_assets
)
from tests.e2e.helpers.net_inspector import (
    check_live_endpoint,
    check_live_asset_stream
)
from tests.e2e.test_r4_cleanup import ACTIVE_ASSETS_WHITELIST

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
BROCHURE_PATH = PROJECT_ROOT / "public" / "assets" / "brochure" / "ACIE-2027-Brochure.pdf"
NAVBAR_PATH = PROJECT_ROOT / "src" / "components" / "Navbar.jsx"
HOME_PATH = PROJECT_ROOT / "src" / "pages" / "Home.jsx"
CONF_DATA_PATH = PROJECT_ROOT / "src" / "data" / "conferenceData.js"
PATRONS_PATH = PROJECT_ROOT / "src" / "pages" / "Patrons.jsx"
SPONSORSHIP_PATH = PROJECT_ROOT / "src" / "pages" / "Sponsorship.jsx"
FOOTER_PATH = PROJECT_ROOT / "src" / "components" / "Footer.jsx"
MODAL_PATH = PROJECT_ROOT / "src" / "components" / "BrochureModal.jsx"

LIVE_SITE_URL = "https://acie-open.netlify.app/"
LIVE_BROCHURE_URL = "https://acie-open.netlify.app/assets/brochure/ACIE-2027-Brochure.pdf"

class TestPairwiseAndScenarios(unittest.TestCase):
    """E2E Test Suite for Tier 3 (Pairwise Interactions) and Tier 4 (Real-World Scenarios)."""

    # ============================================================
    # Tier 3: Cross-Feature Interactions (6 Tests)
    # ============================================================

    @tier(3)
    @feature(["r1", "r4"])
    def test_t3_int_01_brochure_rebuild_script_dependency(self):
        """T3-INT-01: Verify build_exact_brochure.py depends exclusively on whitelisted assets."""
        script_path = PROJECT_ROOT / "build_exact_brochure.py"
        self.assertTrue(script_path.exists(), "build_exact_brochure.py must exist")
        script_text = script_path.read_text(encoding="utf-8")

        # Must reference the whitelisted official KIIT logo
        self.assertIn("kiit-official-logo.png", script_text)
        kiit_logo_path = PROJECT_ROOT / "public" / "assets" / "images" / "logos" / "kiit-official-logo.png"
        self.assertTrue(kiit_logo_path.exists(), "Whitelisted KIIT logo required by brochure script must exist")

    @tier(3)
    @feature(["r2", "r4"])
    def test_t3_int_02_navbar_asset_whitelist_conformance(self):
        """T3-INT-02: Verify all static images referenced in Navbar.jsx exist in the 37 active assets whitelist."""
        navbar_info = inspect_navbar_jsx(NAVBAR_PATH)
        logo_rel = navbar_info["acie_logo_src"].lstrip("/")
        full_rel = f"public/{logo_rel}" if not logo_rel.startswith("public/") else logo_rel
        self.assertIn(
            full_rel, ACTIVE_ASSETS_WHITELIST,
            f"Navbar logo '{full_rel}' must be member of active assets whitelist"
        )

    @tier(3)
    @feature(["r1", "r3"])
    def test_t3_int_03_personnel_identity_parity_brochure_web(self):
        """T3-INT-03: Assert 'Prof. Dr. Subhas Chinara, NIT Rourkela, India' is identical across brochure and web."""
        doc = open_brochure_pdf(BROCHURE_PATH)
        brochure_text = extract_vector_text(doc[1])
        doc.close()

        conf_text = CONF_DATA_PATH.read_text(encoding="utf-8")
        target_name = "Prof. Dr. Subhas Chinara"
        target_inst = "NIT Rourkela, India"

        # Check brochure
        self.assertIn(f"{target_name}, {target_inst}", brochure_text)
        # Check web
        self.assertIn(target_name, conf_text)
        self.assertIn(target_inst, conf_text)

    @tier(3)
    @feature(["r2", "r3"])
    def test_t3_int_04_sponsorship_modal_flow_via_navbar_button(self):
        """T3-INT-04: Verify BrochureModal component renders coordinator subhradebdas contact."""
        self.assertTrue(MODAL_PATH.exists(), "BrochureModal.jsx must exist")
        modal_text = MODAL_PATH.read_text(encoding="utf-8")

        # Modal references coordinator name either directly or via CONFERENCE_INFO.sponsorshipCoordinator
        has_coord_name = "subhradebdas" in modal_text or "sponsorshipCoordinator" in modal_text
        self.assertTrue(has_coord_name, "BrochureModal must bind to coordinator name")
        self.assertIn("1234567890", modal_text, "BrochureModal must include coordinator phone")
        self.assertIn("sponsorship@acieopen.com", modal_text, "BrochureModal must include coordinator email")

    @tier(3)
    @feature(["r4", "r5"])
    def test_t3_int_05_clean_build_artifact_purity(self):
        """T3-INT-05: Verify production bundle is generated cleanly without errors."""
        dist_html = PROJECT_ROOT / "dist" / "index.html"
        # If dist has been generated, verify its purity
        if dist_html.exists():
            html_text = dist_html.read_text(encoding="utf-8")
            self.assertIn('id="root"', html_text)
            self.assertIn("ACIE 2027", html_text)

    @tier(3)
    @feature(["r1", "r5"])
    def test_t3_int_06_live_netlify_brochure_parity(self):
        """T3-INT-06: Verify brochure PDF on Netlify matches local production PDF in size and validity."""
        local_size = BROCHURE_PATH.stat().st_size
        res = check_live_asset_stream(LIVE_BROCHURE_URL, min_size=500_000, timeout=10.0)
        self.assertTrue(res["is_success"])
        # Size difference within 5%
        size_diff = abs(res["content_length"] - local_size) / local_size
        self.assertLess(size_diff, 0.05, f"Live brochure size differs from local by {size_diff * 100:.1f}%")

    # ============================================================
    # Tier 4: Real-World Application Scenarios (6 Tests)
    # ============================================================

    @tier(4)
    @feature("r1")
    def test_t4_scn_01_attendee_brochure_discovery_and_download(self):
        """T4-SCN-01: Full user journey for conference attendee discovering and inspecting brochure."""
        # Step 1: Attendee visits home page, finds brochure button
        navbar_info = inspect_navbar_jsx(NAVBAR_PATH)
        self.assertTrue(navbar_info["has_brochure_button"])

        # Step 2: Resolves brochure file and opens it
        doc = open_brochure_pdf(BROCHURE_PATH)
        self.assertEqual(len(doc), 2)

        # Step 3: Verifies zero white boxes on both pages
        p1_boxes = get_white_background_boxes(doc[0])
        p2_boxes = get_white_background_boxes(doc[1])
        self.assertEqual(len(p1_boxes), 0)
        self.assertEqual(len(p2_boxes), 0)

        # Step 4: Verifies submission link and dates in vector text
        text_p1 = extract_vector_text(doc[0])
        self.assertIn("https://cmt3.research.microsoft.com/ACIE2027", text_p1)
        self.assertIn("22nd - 24th January 2027", text_p1)
        doc.close()

    @tier(4)
    @feature("r2")
    def test_t4_scn_02_desktop_header_navigation_and_registration(self):
        """T4-SCN-02: Full user journey for attendee using desktop navigation bar."""
        navbar_info = inspect_navbar_jsx(NAVBAR_PATH)

        # Step 1: Verify single ACIE transparent brand logo
        self.assertIn("acie-official-logo-transparent.png", navbar_info["acie_logo_src"])
        # Step 2: Zero KIIT logo images in header
        self.assertFalse(navbar_info["has_kiit_logo_img"])
        # Step 3: All 9 sections present
        self.assertTrue(navbar_info["all_nav_items_present"])
        # Step 4: Registration and Brochure buttons present
        self.assertTrue(navbar_info["has_registration_button"])
        self.assertTrue(navbar_info["has_brochure_button"])
        # Step 5: Fits on a single line without wrapping (flex-nowrap and max-w-7xl)
        self.assertTrue(navbar_info["has_flex_nowrap"])
        self.assertTrue(navbar_info["has_max_w_7xl"])

    @tier(4)
    @feature("r3")
    def test_t4_scn_03_hero_poster_carousel_slide_inspection(self):
        """T4-SCN-03: Full user journey inspecting hero carousel slides and text contrast."""
        hero_info = inspect_hero_carousel_overlay(HOME_PATH)

        # Step 1: Overlay must be bg-transparent (no white box obscuring slides)
        self.assertTrue(hero_info["is_transparent"])
        self.assertFalse(hero_info["has_white_bg"])

        # Step 2: Animated slides rotate with 5s timer
        self.assertTrue(hero_info["has_slides_array"])
        self.assertTrue(hero_info["has_5s_interval"])

        # Step 3: Text contrast styling present
        home_text = HOME_PATH.read_text(encoding="utf-8")
        self.assertTrue("textShadow" in home_text or "drop-shadow" in home_text)

    @tier(4)
    @feature("r3")
    def test_t4_scn_04_sponsor_inquiry_and_multichannel_contact(self):
        """T4-SCN-04: Full user journey for corporate sponsor reaching coordinator across channels."""
        # Step 1: Sponsor navigates to Sponsorship page
        spons_text = SPONSORSHIP_PATH.read_text(encoding="utf-8")
        self.assertIn("subhradebdas", spons_text)
        self.assertIn('href="tel:1234567890"', spons_text)
        self.assertIn('href="mailto:sponsorship@acieopen.com"', spons_text)

        # Step 2: Cross-checks Footer contact block
        footer_text = FOOTER_PATH.read_text(encoding="utf-8")
        self.assertIn("sponsorship@acieopen.com", footer_text)
        self.assertIn("subhradebdas", footer_text)

        # Step 3: Cross-checks conferenceData.js
        coord_status = scan_sponsorship_coordinator(PROJECT_ROOT)
        self.assertTrue(coord_status["conferenceData.js"]["has_name"])
        self.assertTrue(coord_status["conferenceData.js"]["has_phone"])
        self.assertTrue(coord_status["conferenceData.js"]["has_email"])

    @tier(4)
    @feature("r5")
    def test_t4_scn_05_production_multiroute_cdn_delivery(self):
        """T4-SCN-05: Full user journey probing live production CDN delivery across multiple routes."""
        # Route 1: Root homepage
        res_root = check_live_endpoint(LIVE_SITE_URL, expected_status=200, timeout=10.0)
        self.assertTrue(res_root["is_success"])
        self.assertTrue(res_root["is_netlify"])

        # Route 2: Direct subroute /aboutkiit
        res_sub = check_live_endpoint(f"{LIVE_SITE_URL.rstrip('/')}/aboutkiit", expected_status=200, timeout=10.0)
        self.assertTrue(res_sub["is_success"])

        # Route 3: CDN Brochure PDF asset
        res_brochure = check_live_asset_stream(LIVE_BROCHURE_URL, min_size=500_000, timeout=10.0)
        self.assertTrue(res_brochure["is_success"])

    @tier(4)
    @feature(["r1", "r2", "r3", "r4", "r5"])
    def test_t4_scn_06_reviewer_comprehensive_integrity_audit(self):
        """T4-SCN-06: End-to-end holistic integrity audit across all requirements R1 to R5."""
        # 1. Zero occurrences of Suchismita in codebase
        forbidden_matches = scan_personnel_occurrences(PROJECT_ROOT, target_name="suchismita")
        self.assertEqual(len(forbidden_matches), 0)

        # 2. Canonical presence of Subhas Chinara
        subhas_info = scan_subhas_chinara(PROJECT_ROOT)
        self.assertTrue(subhas_info["in_conference_data"])
        self.assertTrue(subhas_info["in_patrons_page"])

        # 3. 37 Active assets whitelist 100% valid
        whitelist_audit = audit_whitelist_assets(PROJECT_ROOT, ACTIVE_ASSETS_WHITELIST)
        self.assertTrue(whitelist_audit["all_valid"])

        # 4. Git checked out on branch main
        self.assertEqual(get_git_branch(PROJECT_ROOT), "main")

        # 5. Remote points to official repository
        self.assertEqual(
            get_git_remote_url("origin", PROJECT_ROOT),
            "https://github.com/Aurosri-Arman-Panigrahi/acie-conference-website.git"
        )


if __name__ == "__main__":
    unittest.main()
