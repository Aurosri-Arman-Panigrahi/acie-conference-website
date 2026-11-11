"""
tests/test_challenger_m4_stress.py
Adversarial Stress Test Suite for Milestone M4 (Project Directory Cleanup)
Authored by Challenger 2 (Empirical Challenger)
"""
import os
import shutil
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Canonical 37 active assets whitelist
WHITELIST_RELATIVE = [
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
    "public/assets/images/scraped/newSpeaker4-Brg4EqWV.png",
]

class TestM4EmpiricalStress(unittest.TestCase):
    """Adversarial stress harness for project directory cleanup."""

    def test_01_deleted_targets_strictly_absent_on_disk(self):
        """Assert all obsolete root folders, dead media directories, and temporary files do not exist."""
        forbidden_targets = [
            PROJECT_ROOT / "assets",
            PROJECT_ROOT / "brochure_extracted_assets",
            PROJECT_ROOT / "generate_brochure_pdf.py",
            PROJECT_ROOT / "temp_test.pdf",
            PROJECT_ROOT / "public/assets/videos",
            PROJECT_ROOT / "public/assets/audio",
            PROJECT_ROOT / "public/assets/papers",
            PROJECT_ROOT / "public/assets/data",
            PROJECT_ROOT / "public/assets/images/figures",
            PROJECT_ROOT / "public/assets/images/slides",
            PROJECT_ROOT / "public/assets/images/authors",
        ]
        for target in forbidden_targets:
            self.assertFalse(target.exists(), f"Target '{target}' must not exist on disk!")

    def test_02_whitelist_exact_count_and_no_extraneous_in_public_assets(self):
        """Assert public/assets/ contains exactly the 37 whitelisted files and zero unwhitelisted files."""
        pub_assets_dir = PROJECT_ROOT / "public/assets"
        self.assertTrue(pub_assets_dir.exists(), "public/assets directory must exist")

        actual_files = set(p.resolve() for p in pub_assets_dir.rglob("*") if p.is_file())
        expected_files = set((PROJECT_ROOT / p).resolve() for p in WHITELIST_RELATIVE)

        self.assertEqual(len(actual_files), 37, f"Expected 37 files in public/assets, found {len(actual_files)}")
        self.assertEqual(actual_files, expected_files, "Discrepancy between actual files and whitelist!")

    def test_03_zero_zombie_empty_directories_in_public_assets(self):
        """Assert public/assets contains zero empty zombie directories."""
        pub_assets_dir = PROJECT_ROOT / "public/assets"
        all_dirs = [p for p in pub_assets_dir.rglob("*") if p.is_dir()]
        empty_dirs = [d for d in all_dirs if not any(d.iterdir())]
        self.assertEqual(len(empty_dirs), 0, f"Found empty zombie directories: {empty_dirs}")

    def test_04_no_symlinks_or_reparse_junctions(self):
        """Assert all 37 whitelisted files are regular physical files (no symlinks, no Windows junctions)."""
        for rel in WHITELIST_RELATIVE:
            path = PROJECT_ROOT / rel
            self.assertTrue(path.exists(), f"File {rel} does not exist")
            self.assertFalse(path.is_symlink(), f"File {rel} must not be a symlink")
            # Check Windows reparse point attribute (0x400 = 1024)
            stat_info = os.lstat(path)
            is_reparse = bool(stat_info.st_file_attributes & 1024) if hasattr(stat_info, "st_file_attributes") else False
            self.assertFalse(is_reparse, f"File {rel} must not be a reparse point / junction")
            self.assertGreater(stat_info.st_size, 500, f"File {rel} is suspiciously small: {stat_info.st_size} bytes")

    def test_05_clean_scratch_build_and_bundle_byte_size(self):
        """Run clean build from scratch and verify dist size is <= 15 MB (target ~10.5 MB)."""
        dist_dir = PROJECT_ROOT / "dist"
        if dist_dir.exists():
            subprocess.run(["powershell", "-Command", "Remove-Item -Recurse -Force dist"], cwd=str(PROJECT_ROOT), check=False)

        build_proc = subprocess.run(
            ["npm.cmd", "run", "build"],
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True,
            check=False
        )
        self.assertEqual(build_proc.returncode, 0, f"Build failed: {build_proc.stderr}")
        self.assertTrue(dist_dir.exists(), "dist/ must exist after build")

        dist_files = list(dist_dir.rglob("*"))
        dist_file_count = sum(1 for f in dist_files if f.is_file())
        dist_bytes = sum(f.stat().st_size for f in dist_files if f.is_file())

        self.assertEqual(dist_file_count, 40, f"dist should contain exactly 40 files (37 assets + 3 bundle files), found {dist_file_count}")
        self.assertLessEqual(dist_bytes, 15 * 1024 * 1024, f"dist size ({dist_bytes} bytes) exceeds 15 MB limit")
        self.assertGreaterEqual(dist_bytes, 9 * 1024 * 1024, f"dist size ({dist_bytes} bytes) suspiciously small")

    def test_06_no_leaked_assets_in_dist(self):
        """Assert no deleted categories leaked into dist/."""
        dist_dir = PROJECT_ROOT / "dist"
        leaked = []
        for f in dist_dir.rglob("*"):
            if f.is_file():
                rel = str(f.relative_to(dist_dir)).replace("\\", "/")
                for forbidden in ["videos/", "audio/", "papers/", "figures/", "slides/", "brochure_extracted_assets"]:
                    if forbidden in rel:
                        leaked.append(rel)
        self.assertEqual(len(leaked), 0, f"Leaked forbidden assets in dist: {leaked}")

    def test_07_all_assets_integrity_and_parsable(self):
        """Assert all 37 assets are structurally valid files (valid image/SVG/PDF)."""
        for rel in WHITELIST_RELATIVE:
            p = PROJECT_ROOT / rel
            ext = p.suffix.lower()
            if ext in [".png", ".jpg", ".jpeg", ".webp"]:
                with Image.open(p) as img:
                    img.verify()
            elif ext == ".svg":
                tree = ET.parse(p)
                self.assertIsNotNone(tree.getroot())
            elif ext == ".pdf":
                with open(p, "rb") as f:
                    header = f.read(5)
                    self.assertEqual(header, b"%PDF-")

if __name__ == "__main__":
    unittest.main()
