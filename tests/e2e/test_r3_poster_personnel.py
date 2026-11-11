"""
tests/e2e/test_r3_poster_personnel.py
E2E Opaque-Box Tests for Requirement R3: Poster Section & Personnel Content Updates.
Covers Tier 1 (Feature Coverage) and Tier 2 (Boundary & Corner Cases).
"""
from pathlib import Path
import re
import unittest

from tests.e2e.helpers.decorators import tier, feature
from tests.e2e.helpers.dom_inspector import (
    inspect_hero_carousel_overlay,
    scan_personnel_occurrences,
    scan_subhas_chinara,
    scan_sponsorship_coordinator
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
HOME_PATH = PROJECT_ROOT / "src" / "pages" / "Home.jsx"
CONF_DATA_PATH = PROJECT_ROOT / "src" / "data" / "conferenceData.js"
PATRONS_PATH = PROJECT_ROOT / "src" / "pages" / "Patrons.jsx"
SPONSORSHIP_PATH = PROJECT_ROOT / "src" / "pages" / "Sponsorship.jsx"
FOOTER_PATH = PROJECT_ROOT / "src" / "components" / "Footer.jsx"

class TestR3PosterPersonnel(unittest.TestCase):
    """E2E Test Suite for Requirement R3: Poster Section and Personnel Content Updates."""

    @classmethod
    def setUpClass(cls):
        if not HOME_PATH.exists():
            raise FileNotFoundError(f"Home page not found at {HOME_PATH}")
        cls.home_content = HOME_PATH.read_text(encoding="utf-8")
        cls.hero_info = inspect_hero_carousel_overlay(HOME_PATH)

    # ==========================================
    # Tier 1: Feature Coverage (Deterministic)
    # ==========================================

    @tier(1)
    @feature("r3")
    def test_t1_r3_01_hero_carousel_transparent_overlay(self):
        """T1-R3-01: Assert hero poster section removes white overlay in favor of bg-transparent."""
        self.assertTrue(
            self.hero_info["is_transparent"],
            f"Hero overlay element must include 'bg-transparent', got classes: '{self.hero_info['overlay_classes']}'"
        )
        self.assertFalse(
            self.hero_info["has_white_bg"],
            f"Hero overlay element must NOT include white background classes: '{self.hero_info['overlay_classes']}'"
        )

    @tier(1)
    @feature("r3")
    def test_t1_r3_02_hero_carousel_animated_slides_structure(self):
        """T1-R3-02: Verify carousel contains slide array and 5-second auto-advance timer."""
        self.assertTrue(
            self.hero_info["has_slides_array"],
            "Home component must define slides array and track currentSlide"
        )
        self.assertTrue(
            self.hero_info["has_5s_interval"],
            "Carousel slide transition interval must be set to 5000ms"
        )

    @tier(1)
    @feature("r3")
    def test_t1_r3_03_codebase_wide_purge_of_suchismita(self):
        """T1-R3-03: Verify 0 occurrences of 'Suchismita' anywhere in the repository source code."""
        matches = scan_personnel_occurrences(PROJECT_ROOT, target_name="suchismita")
        self.assertEqual(
            len(matches), 0,
            f"Found forbidden occurrences of Suchismita in repository: {matches}"
        )

    @tier(1)
    @feature("r3")
    def test_t1_r3_04_canonical_adoption_of_subhas_chinara(self):
        """T1-R3-04: Assert 'Prof. Dr. Subhas Chinara, NIT Rourkela, India' is canonically present."""
        res = scan_subhas_chinara(PROJECT_ROOT)
        self.assertTrue(
            res["in_conference_data"],
            "conferenceData.js must contain 'Prof. Dr. Subhas Chinara' and 'NIT Rourkela, India'"
        )
        self.assertTrue(
            res["in_patrons_page"],
            "Patrons.jsx must contain 'Prof. Dr. Subhas Chinara, NIT Rourkela, India'"
        )

    @tier(1)
    @feature("r3")
    def test_t1_r3_05_sponsorship_coordinator_name(self):
        """T1-R3-05: Assert coordinator name is set to 'subhradebdas' across all touchpoints."""
        coord_info = scan_sponsorship_coordinator(PROJECT_ROOT)
        for comp_name, status in coord_info.items():
            if not status.get("missing"):
                self.assertTrue(
                    status["has_name"],
                    f"{comp_name} must display coordinator name 'subhradebdas'"
                )

    @tier(1)
    @feature("r3")
    def test_t1_r3_06_sponsorship_coordinator_phone_and_email(self):
        """T1-R3-06: Assert coordinator phone '1234567890' and email 'sponsorship@acieopen.com'."""
        coord_info = scan_sponsorship_coordinator(PROJECT_ROOT)
        self.assertTrue(
            coord_info.get("conferenceData.js", {}).get("has_phone"),
            "conferenceData.js must contain coordinator phone '1234567890'"
        )
        self.assertTrue(
            coord_info.get("conferenceData.js", {}).get("has_email"),
            "conferenceData.js must contain coordinator email 'sponsorship@acieopen.com'"
        )

    # ==========================================
    # Tier 2: Boundary & Corner Cases
    # ==========================================

    @tier(2)
    @feature("r3")
    def test_t2_r3_01_carousel_slide_index_boundary_wrapping(self):
        """T2-R3-01: Verify slide index wraps around from last slide to first slide cleanly."""
        wrap_match = re.search(r"%\s*(?:HERO_)?slides\.length", self.home_content, re.IGNORECASE)
        self.assertIsNotNone(
            wrap_match,
            "Carousel slide transition logic must implement modulo wrap (% HERO_SLIDES.length)"
        )

    @tier(2)
    @feature("r3")
    def test_t2_r3_02_hero_text_shadow_contrast_styling(self):
        """T2-R3-02: Verify hero text has drop-shadows or textShadow contrast styling."""
        has_shadow = "textShadow" in self.home_content or "drop-shadow" in self.home_content
        self.assertTrue(
            has_shadow,
            "Hero headline text must use textShadow or drop-shadow styling for contrast over transparent overlay"
        )

    @tier(2)
    @feature("r3")
    def test_t2_r3_03_punctuation_agnostic_regex_old_name(self):
        """T2-R3-03: Punctuation-agnostic search across permutations for Suchismita."""
        regex_variants = [
            r"\b[Ss]uchismita\b",
            r"\b[Dd]r\.?\s*[Ss]uchismita\b",
            r"[Ss]uchismita[\s_\.-]*[Cc]hinara"
        ]
        for pattern_str in regex_variants:
            pat = re.compile(pattern_str)
            for f in [CONF_DATA_PATH, PATRONS_PATH, SPONSORSHIP_PATH, FOOTER_PATH, HOME_PATH]:
                if f.exists():
                    text = f.read_text(encoding="utf-8")
                    self.assertIsNone(
                        pat.search(text),
                        f"Found forbidden match for '{pattern_str}' in {f.name}"
                    )

    @tier(2)
    @feature("r3")
    def test_t2_r3_04_coordinator_protocol_link_schemes(self):
        """T2-R3-04: Verify click-to-call 'tel:' and 'mailto:' protocol URIs."""
        if SPONSORSHIP_PATH.exists():
            spons_text = SPONSORSHIP_PATH.read_text(encoding="utf-8")
            self.assertIn('href="tel:1234567890"', spons_text, "Sponsorship.jsx must contain href='tel:1234567890'")
            self.assertIn('href="mailto:sponsorship@acieopen.com"', spons_text, "Sponsorship.jsx must contain href='mailto:sponsorship@acieopen.com'")

    @tier(2)
    @feature("r3")
    def test_t2_r3_05_speaker_card_institution_layout(self):
        """T2-R3-05: Verify keynote speaker card entry includes NIT Rourkela affiliation."""
        conf_text = CONF_DATA_PATH.read_text(encoding="utf-8")
        # Subhas Chinara should have NIT Rourkela, India attached
        self.assertIn("Prof. Dr. Subhas Chinara", conf_text)
        self.assertIn("NIT Rourkela, India", conf_text)

    @tier(2)
    @feature("r3")
    def test_t2_r3_06_personnel_object_field_integrity(self):
        """T2-R3-06: Verify conference data structures define non-empty speaker and patron lists."""
        conf_text = CONF_DATA_PATH.read_text(encoding="utf-8")
        self.assertIn("KEYNOTE_SPEAKERS", conf_text)
        self.assertIn("COMMITTEE", conf_text)
        self.assertIn("advisoryBoard", conf_text)


if __name__ == "__main__":
    unittest.main()
