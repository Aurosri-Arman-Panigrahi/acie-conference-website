"""
tests/e2e/test_r1_brochure.py
E2E Opaque-Box Tests for Requirement R1: Brochure PDF Updates.
Covers Tier 1 (Feature Coverage) and Tier 2 (Boundary & Corner Cases).
"""
import io
import os
from pathlib import Path
import unittest
import fitz

from tests.e2e.helpers.decorators import tier, feature
from tests.e2e.helpers.pdf_inspector import (
    open_brochure_pdf,
    get_white_background_boxes,
    extract_vector_text,
    get_embedded_fonts,
    find_embedded_images,
    sample_pixel_color,
    get_page_redactions,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
BROCHURE_PATH = PROJECT_ROOT / "public" / "assets" / "brochure" / "ACIE-2027-Brochure.pdf"

class TestR1Brochure(unittest.TestCase):
    """E2E Test Suite for Requirement R1: Brochure PDF Updates."""

    @classmethod
    def setUpClass(cls):
        if not BROCHURE_PATH.exists():
            raise FileNotFoundError(f"Brochure PDF not found at {BROCHURE_PATH}")
        cls.doc = open_brochure_pdf(BROCHURE_PATH)
        cls.p1 = cls.doc[0]
        cls.p2 = cls.doc[1]

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, "doc") and cls.doc:
            cls.doc.close()

    # ==========================================
    # Tier 1: Feature Coverage (Deterministic)
    # ==========================================

    @tier(1)
    @feature("r1")
    def test_t1_r1_01_file_existence_and_magic(self):
        """T1-R1-01: Verify brochure exists, size > 1MB, and starts with %PDF- header."""
        self.assertTrue(BROCHURE_PATH.exists(), "Brochure PDF must exist on disk")
        size = BROCHURE_PATH.stat().st_size
        self.assertGreater(size, 1_000_000, f"Brochure size ({size} bytes) should exceed 1 MB")
        with open(BROCHURE_PATH, "rb") as f:
            header = f.read(5)
            self.assertEqual(header, b"%PDF-", "File magic header must be %PDF-")

    @tier(1)
    @feature("r1")
    def test_t1_r1_02_page_count_and_orientation(self):
        """T1-R1-02: Verify brochure contains exactly 2 landscape US-Letter pages."""
        self.assertEqual(len(self.doc), 2, "Brochure must contain exactly 2 pages")
        for i, page in enumerate(self.doc):
            rect = page.rect
            self.assertAlmostEqual(rect.width, 849.75, delta=1.0, msg=f"Page {i+1} width should be ~849.75")
            self.assertAlmostEqual(rect.height, 612.0, delta=1.0, msg=f"Page {i+1} height should be ~612.0")
            self.assertGreater(rect.width, rect.height, f"Page {i+1} must be in landscape orientation")

    @tier(1)
    @feature("r1")
    def test_t1_r1_03_zero_non_canvas_white_boxes(self):
        """T1-R1-03: Assert zero non-canvas white rect drawings exist on either page."""
        p1_white = get_white_background_boxes(self.p1)
        p2_white = get_white_background_boxes(self.p2)
        self.assertEqual(len(p1_white), 0, f"Page 1 has {len(p1_white)} unexpected white boxes: {p1_white}")
        self.assertEqual(len(p2_white), 0, f"Page 2 has {len(p2_white)} unexpected white boxes: {p2_white}")

    @tier(1)
    @feature("r1")
    def test_t1_r1_04_kiit_logo_dimensions_and_location(self):
        """T1-R1-04: Verify KIIT logo replaces Centurion logo at top-right of Page 1 without white background."""
        images_p1 = find_embedded_images(self.p1)
        # Verify Centurion logo (243x115) does not exist anywhere on Page 1
        centurion_imgs = [img for img in images_p1 if img["width"] == 243 and img["height"] == 115]
        self.assertEqual(len(centurion_imgs), 0, "Centurion logo (243x115) must not exist in brochure")

        # Verify KIIT official logo (163x259) is placed in the top right header (replacing Centurion logo)
        kiit_imgs = [
            img for img in images_p1
            if img["width"] == 163 and img["height"] == 259 and img["bbox"].x0 >= 550 and img["bbox"].y0 <= 100
        ]
        self.assertGreaterEqual(len(kiit_imgs), 1, "Official KIIT logo (163x259) must be present at top-right header of Page 1")

        # Verify no duplicate KIIT logo exists at bottom-right of Page 1
        bottom_right_kiit = [
            img for img in images_p1
            if img["width"] == 600 and img["height"] == 108 and img["bbox"].x0 >= 650 and img["bbox"].y0 >= 500
        ]
        self.assertEqual(len(bottom_right_kiit), 0, "No duplicate KIIT logo should remain at bottom-right of Page 1")

    @tier(1)
    @feature("r1")
    def test_t1_r1_05_vector_searchable_text_integrity(self):
        """T1-R1-05: Verify text is extractable vector text containing core ACIE 2027 information."""
        text_p1 = extract_vector_text(self.p1)
        text_p2 = extract_vector_text(self.p2)

        self.assertGreater(len(text_p1), 400, "Page 1 vector text length should exceed 400 chars")
        self.assertGreater(len(text_p2), 3000, "Page 2 vector text length should exceed 3000 chars")

        self.assertIn("ACIE", text_p1, "Page 1 text must contain 'ACIE'")
        self.assertIn("2027", text_p1, "Page 1 text must contain '2027'")
        self.assertIn("Kalinga Institute of Industrial Technology", text_p1, "Page 1 text must reference KIIT")

    @tier(1)
    @feature("r1")
    def test_t1_r1_06_qr_code_image_preservation(self):
        """T1-R1-06: Verify QR code embedded images are preserved on Page 1."""
        images_p1 = find_embedded_images(self.p1)
        # QR codes are square images with width == height >= 200
        qr_images = [img for img in images_p1 if abs(img["width"] - img["height"]) <= 5 and img["width"] >= 200]
        self.assertGreaterEqual(len(qr_images), 2, "Page 1 must contain at least 2 high-res QR code images")

    # ==========================================
    # Tier 2: Boundary & Corner Cases
    # ==========================================

    @tier(2)
    @feature("r1")
    def test_t2_r1_01_viewport_boundary_and_canvas_bbox(self):
        """T2-R1-01: Verify viewport boundaries, aspect ratio, and rotation across pages."""
        for i, page in enumerate(self.doc):
            cbox = page.cropbox
            prect = page.rect
            self.assertEqual(prect, fitz.Rect(0.0, 0.0, 849.75, 612.0), f"Page {i+1} rect must match standard US-Letter Landscape")
            self.assertEqual(cbox, fitz.Rect(0.0, 0.0, 849.75, 612.0), f"Page {i+1} CropBox must be Rect(0, 0, 849.75, 612)")
            self.assertAlmostEqual(page.mediabox.width, 849.75, delta=1.0)
            self.assertAlmostEqual(page.mediabox.height, 612.0, delta=1.0)
            self.assertEqual(page.rotation, 0, f"Page {i+1} rotation must be 0 degrees")

    @tier(2)
    @feature("r1")
    def test_t2_r1_02_redaction_annotations_elimination(self):
        """T2-R1-02: Assert zero unapplied / square redaction annotations exist."""
        p1_redacts = get_page_redactions(self.p1)
        p2_redacts = get_page_redactions(self.p2)
        self.assertEqual(len(p1_redacts), 0, "Page 1 must not contain unapplied redaction annotations")
        self.assertEqual(len(p2_redacts), 0, "Page 2 must not contain unapplied redaction annotations")

    @tier(2)
    @feature("r1")
    def test_t2_r1_03_high_dpi_pixmap_rendering(self):
        """T2-R1-03: Render at 300 DPI and assert high-resolution pixel dimensions."""
        pix = self.p1.get_pixmap(dpi=300)
        self.assertGreaterEqual(pix.width, 3500, "300 DPI width must exceed 3500 pixels")
        self.assertGreaterEqual(pix.height, 2500, "300 DPI height must exceed 2500 pixels")
        self.assertGreater(len(pix.samples), 0, "Rendered pixmap buffer must be non-empty")

    @tier(2)
    @feature("r1")
    def test_t2_r1_04_corrupted_pdf_exception_resiliency(self):
        """T2-R1-04: Test exception resiliency when presented with corrupt PDF bytes."""
        corrupt_data = b"NOT_A_VALID_PDF_HEADER_OR_BODY"
        with self.assertRaises(Exception):
            fitz.open(stream=corrupt_data, filetype="pdf")

    @tier(2)
    @feature("r1")
    def test_t2_r1_05_non_ascii_and_personnel_strings(self):
        """T2-R1-05: Verify Prof. Dr. Subhas Chinara is cleanly extractable without encoding corruption."""
        text_p2 = extract_vector_text(self.p2)
        expected_personnel = "Prof. Dr. Subhas Chinara, NIT Rourkela, India"
        self.assertIn(expected_personnel, text_p2, f"Brochure Page 2 must contain exact string '{expected_personnel}'")
        self.assertNotIn("\ufffd", text_p2, "Vector text should not contain unicode replacement characters")

    @tier(2)
    @feature("r1")
    def test_t2_r1_06_absence_of_cutm_centurion_visible_text(self):
        """T2-R1-06: Assert 'centurion' and 'cutm' are absent from visible extracted text on both pages."""
        text_p1 = extract_vector_text(self.p1).lower()
        text_p2 = extract_vector_text(self.p2).lower()
        self.assertNotIn("centurion", text_p1, "Visible text on Page 1 must not contain 'centurion'")
        self.assertNotIn("cutm", text_p1, "Visible text on Page 1 must not contain 'cutm'")
        self.assertNotIn("centurion", text_p2, "Visible text on Page 2 must not contain 'centurion'")
        self.assertNotIn("cutm", text_p2, "Visible text on Page 2 must not contain 'cutm'")


if __name__ == "__main__":
    unittest.main()
