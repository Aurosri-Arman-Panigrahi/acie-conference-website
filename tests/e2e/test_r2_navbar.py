"""
tests/e2e/test_r2_navbar.py
E2E Opaque-Box Tests for Requirement R2: Website Header and Navigation.
Covers Tier 1 (Feature Coverage) and Tier 2 (Boundary & Corner Cases).
"""
import os
from pathlib import Path
import re
import unittest
from PIL import Image

from tests.e2e.helpers.decorators import tier, feature
from tests.e2e.helpers.dom_inspector import inspect_navbar_jsx

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
NAVBAR_PATH = PROJECT_ROOT / "src" / "components" / "Navbar.jsx"
ACIE_TRANSPARENT_LOGO_PATH = PROJECT_ROOT / "public" / "assets" / "images" / "logos" / "acie-official-logo-transparent.png"
MASTER_LOGO_PATH = PROJECT_ROOT / "acie logo" / "acie logo.png"

class TestR2Navbar(unittest.TestCase):
    """E2E Test Suite for Requirement R2: Website Header and Navigation."""

    @classmethod
    def setUpClass(cls):
        if not NAVBAR_PATH.exists():
            raise FileNotFoundError(f"Navbar component not found at {NAVBAR_PATH}")
        cls.navbar_content = NAVBAR_PATH.read_text(encoding="utf-8")
        cls.navbar_info = inspect_navbar_jsx(NAVBAR_PATH)

    # ==========================================
    # Tier 1: Feature Coverage (Deterministic)
    # ==========================================

    @tier(1)
    @feature("r2")
    def test_t1_r2_01_header_acie_brand_logo_source(self):
        """T1-R2-01: Verify Navbar renders ACIE logo using the transparent official master asset."""
        self.assertIn(
            "acie-official-logo-transparent.png",
            self.navbar_info["acie_logo_src"],
            f"Navbar ACIE logo source must reference acie-official-logo-transparent.png, got: {self.navbar_info['acie_logo_src']}"
        )
        self.assertTrue(
            ACIE_TRANSPARENT_LOGO_PATH.exists(),
            f"Transparent ACIE logo asset must physically exist at {ACIE_TRANSPARENT_LOGO_PATH}"
        )

    @tier(1)
    @feature("r2")
    def test_t1_r2_02_absolute_absence_of_kiit_logo_img(self):
        """T1-R2-02: Assert zero <img> elements in Navbar render a KIIT logo."""
        self.assertFalse(
            self.navbar_info["has_kiit_logo_img"],
            f"Navbar must not render any KIIT logo <img> elements, found: {self.navbar_info['kiit_img_tags']}"
        )
        self.assertEqual(
            len(self.navbar_info["kiit_img_tags"]), 0,
            "Total KIIT image elements in header must be exactly 0"
        )

    @tier(1)
    @feature("r2")
    def test_t1_r2_03_header_action_buttons_presence(self):
        """T1-R2-03: Verify both 'REGISTRATION' and 'BROCHURE' action buttons exist in Navbar."""
        self.assertTrue(
            self.navbar_info["has_registration_button"],
            "Navbar must contain the 'REGISTRATION' action button"
        )
        self.assertTrue(
            self.navbar_info["has_brochure_button"],
            "Navbar must contain the 'BROCHURE' action button"
        )

    @tier(1)
    @feature("r2")
    def test_t1_r2_04_desktop_container_constraint(self):
        """T1-R2-04: Assert Navbar wrapper enforces max-w-7xl mx-auto layout matching reference."""
        self.assertTrue(
            self.navbar_info["has_max_w_7xl"],
            "Navbar container must use 'max-w-7xl mx-auto px-4 sm:px-6 lg:px-8' styling"
        )

    @tier(1)
    @feature("r2")
    def test_t1_r2_05_site_wide_acie_logo_consistency(self):
        """T1-R2-05: Verify all other ACIE logo instances across site match master transparent logo."""
        components_to_check = [
            PROJECT_ROOT / "src" / "components" / "Footer.jsx",
            PROJECT_ROOT / "src" / "components" / "BrochureModal.jsx",
            PROJECT_ROOT / "src" / "pages" / "Home.jsx"
        ]
        for comp in components_to_check:
            if comp.exists():
                text = comp.read_text(encoding="utf-8")
                # If component renders acie logo, verify it does not use outdated non-transparent variants
                if "acie" in text.lower() and "<img" in text:
                    self.assertNotIn(
                        "acie-official-logo.png",
                        text,
                        f"{comp.name} should use transparent logo variant instead of opaque acie-official-logo.png"
                    )

    @tier(1)
    @feature("r2")
    def test_t1_r2_06_mobile_navigation_menu_toggle_structure(self):
        """T1-R2-06: Verify mobile navigation hamburger button and responsive drawer exist."""
        self.assertTrue(
            self.navbar_info["has_mobile_drawer"],
            "Navbar must provide mobile navigation drawer and toggle button"
        )

    # ==========================================
    # Tier 2: Boundary & Corner Cases
    # ==========================================

    @tier(2)
    @feature("r2")
    def test_t2_r2_01_responsive_breakpoint_classes(self):
        """T2-R2-01: Verify navbar layout classes maintain layout integrity across desktop and mobile."""
        self.assertTrue(
            self.navbar_info["has_desktop_flex"],
            "Desktop navigation must use 'hidden lg:flex' or 'lg:flex'"
        )
        self.assertTrue(
            self.navbar_info["has_flex_nowrap"],
            "Desktop navigation links must use 'flex-nowrap' to prevent multi-line wrap"
        )

    @tier(2)
    @feature("r2")
    def test_t2_r2_02_missing_logo_graceful_alt_attribute(self):
        """T2-R2-02: Verify logo <img> element has required non-empty alt attribute."""
        alt_match = re.search(r'<img[^>]+alt=["\']([^"\']+)["\']', self.navbar_content)
        self.assertIsNotNone(alt_match, "Navbar logo <img> must have an alt attribute")
        self.assertIn("ACIE", alt_match.group(1), "Alt attribute must describe ACIE logo")

    @tier(2)
    @feature("r2")
    def test_t2_r2_03_high_dpi_retina_scaling_classes(self):
        """T2-R2-03: Verify logo image styling preserves aspect ratio without stretching."""
        self.assertIn("object-contain", self.navbar_content, "Logo must use 'object-contain'")
        self.assertIn("w-auto", self.navbar_content, "Logo must use 'w-auto' for proportional scaling")

    @tier(2)
    @feature("r2")
    def test_t2_r2_04_action_buttons_pill_styling(self):
        """T2-R2-04: Verify action buttons use pill style (rounded-full) and primary blue color."""
        self.assertIn("rounded-full", self.navbar_content, "Action buttons must use 'rounded-full' pill design")
        self.assertIn("bg-blue-600", self.navbar_content, "Action buttons must use 'bg-blue-600' primary color")

    @tier(2)
    @feature("r2")
    def test_t2_r2_05_brochure_button_direct_href(self):
        """T2-R2-05: Verify brochure button links directly to the brochure PDF asset."""
        self.assertIn(
            "/assets/brochure/ACIE-2027-Brochure.pdf",
            self.navbar_content,
            "Navbar must link directly to /assets/brochure/ACIE-2027-Brochure.pdf"
        )

    @tier(2)
    @feature("r2")
    def test_t2_r2_06_navbar_fixed_or_sticky_z_index(self):
        """T2-R2-06: Verify Navbar container stays above the hero section with high z-index."""
        self.assertTrue(
            "fixed" in self.navbar_content or "sticky" in self.navbar_content,
            "Navbar must be 'fixed' or 'sticky'"
        )
        self.assertTrue(
            "z-50" in self.navbar_content or "z-40" in self.navbar_content,
            "Navbar must use z-40 or z-50 to layer over carousel"
        )


if __name__ == "__main__":
    unittest.main()
