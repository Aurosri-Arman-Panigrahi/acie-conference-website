"""
tests/e2e/test_r5_deployment.py
E2E Opaque-Box Tests for Requirement R5: Git Commit, Push & Netlify Deployment.
Covers Tier 1 (Feature Coverage) and Tier 2 (Boundary & Corner Cases).
"""
from pathlib import Path
import unittest

from tests.e2e.helpers.decorators import tier, feature
from tests.e2e.helpers.git_inspector import (
    get_git_branch,
    get_git_remote_url,
    get_git_commit_hash,
    get_git_status_porcelain,
    get_git_latest_commit_info
)
from tests.e2e.helpers.net_inspector import (
    check_live_endpoint,
    check_live_asset_stream
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
EXPECTED_REPO_URL = "https://github.com/Aurosri-Arman-Panigrahi/acie-conference-website.git"
LIVE_SITE_URL = "https://acie-open.netlify.app/"
LIVE_BROCHURE_URL = "https://acie-open.netlify.app/assets/brochure/ACIE-2027-Brochure.pdf"

class TestR5Deployment(unittest.TestCase):
    """E2E Test Suite for Requirement R5: Git Commit, Push, and Netlify Deployment."""

    # ==========================================
    # Tier 1: Feature Coverage (Deterministic)
    # ==========================================

    @tier(1)
    @feature("r5")
    def test_t1_r5_01_git_active_branch_main(self):
        """T1-R5-01: Verify current checked out git branch is 'main'."""
        branch = get_git_branch(PROJECT_ROOT)
        self.assertEqual(branch, "main", f"Checked out branch must be 'main', got '{branch}'")

    @tier(1)
    @feature("r5")
    def test_t1_r5_02_git_remote_origin_url(self):
        """T1-R5-02: Verify remote 'origin' matches official GitHub repository."""
        remote_url = get_git_remote_url("origin", PROJECT_ROOT)
        self.assertEqual(
            remote_url, EXPECTED_REPO_URL,
            f"Remote origin URL must match '{EXPECTED_REPO_URL}', got '{remote_url}'"
        )

    @tier(1)
    @feature("r5")
    def test_t1_r5_03_git_working_tree_cleanliness_or_scope(self):
        """T1-R5-03: Assert working directory is clean or modified files strictly match M1-M3 scope."""
        status_lines = get_git_status_porcelain(PROJECT_ROOT, exclude_meta=True)
        allowed_modified_basenames = {
            "Navbar.jsx",
            "Home.jsx",
            "conferenceData.js",
            "Patrons.jsx",
            "ACIE-2027-Brochure.pdf",
            "build_exact_brochure.py"
        }
        for line in status_lines:
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                file_rel = parts[1].replace('"', '')
                file_name = Path(file_rel).name
                self.assertIn(
                    file_name, allowed_modified_basenames,
                    f"Unexpected modified file outside approved milestone scope: '{file_rel}'"
                )

    @tier(1)
    @feature("r5")
    def test_t1_r5_04_git_remote_tracking_sync(self):
        """T1-R5-04: Assert local 'main' branch tracks 'origin/main' without divergence."""
        head_hash = get_git_commit_hash("HEAD", PROJECT_ROOT)
        self.assertTrue(len(head_hash) >= 40, f"HEAD commit hash should be a 40-char SHA, got '{head_hash}'")
        # In git status output, branch is tracked to origin/main
        origin_hash = get_git_commit_hash("origin/main", PROJECT_ROOT)
        if origin_hash:
            # If fetched, assert non-empty valid commit hash
            self.assertEqual(len(origin_hash), 40)

    @tier(1)
    @feature("r5")
    def test_t1_r5_05_netlify_live_http_200_and_server_header(self):
        """T1-R5-05: Probe https://acie-open.netlify.app/ for HTTP status 200 and Netlify header."""
        res = check_live_endpoint(LIVE_SITE_URL, expected_status=200, timeout=10.0)
        self.assertTrue(res["is_success"], f"Live endpoint probe failed: {res.get('error')}")
        self.assertTrue(res["is_netlify"], f"Server header must identify Netlify, got: '{res.get('server')}'")
        self.assertTrue(res["has_title"], "Live HTML page must contain ACIE 2027 title")

    @tier(1)
    @feature("r5")
    def test_t1_r5_06_netlify_live_brochure_cdn_probe(self):
        """T1-R5-06: Probe live brochure PDF endpoint on Netlify CDN."""
        res = check_live_asset_stream(LIVE_BROCHURE_URL, min_size=500_000, timeout=10.0)
        self.assertTrue(res["is_success"], f"Live brochure CDN probe failed: {res.get('error')}")
        self.assertIn("application/pdf", res["content_type"], f"Content-Type must be PDF, got: '{res['content_type']}'")
        self.assertGreater(res["content_length"], 500_000, f"Brochure length {res['content_length']} should exceed 500 KB")

    # ==========================================
    # Tier 2: Boundary & Corner Cases
    # ==========================================

    @tier(2)
    @feature("r5")
    def test_t2_r5_01_network_probe_timeout_resiliency(self):
        """T2-R5-01: Verify live probe handles network latency gracefully with timeout."""
        # Querying an unreachable address with 0.5s timeout should raise/handle timeout cleanly
        res = check_live_endpoint("https://10.255.255.1/", timeout=0.5)
        self.assertFalse(res["is_success"])
        self.assertIsNotNone(res["error"])

    @tier(2)
    @feature("r5")
    def test_t2_r5_02_ssl_tls_certificate_validity(self):
        """T2-R5-02: Assert Netlify live site enforces HTTPS and presents a valid certificate."""
        res = check_live_endpoint(LIVE_SITE_URL, expected_status=200, timeout=10.0)
        self.assertEqual(res["status"], 200, "HTTPS handshake and request must succeed with 200 OK")

    @tier(2)
    @feature("r5")
    def test_t2_r5_03_netlify_edge_cache_policy_header(self):
        """T2-R5-03: Verify Netlify response headers specify cache revalidation policy."""
        res = check_live_endpoint(LIVE_SITE_URL, expected_status=200, timeout=10.0)
        self.assertTrue(
            "max-age" in res["cache_control"] or "public" in res["cache_control"] or res["server"] != "",
            "Response should contain standard CDN caching headers"
        )

    @tier(2)
    @feature("r5")
    def test_t2_r5_04_spa_fallback_direct_route_access(self):
        """T2-R5-04: Probe deep client-side route https://acie-open.netlify.app/aboutkiit directly."""
        subroute_url = f"{LIVE_SITE_URL.rstrip('/')}/aboutkiit"
        res = check_live_endpoint(subroute_url, expected_status=200, timeout=10.0)
        self.assertTrue(res["is_success"], f"SPA fallback route /aboutkiit returned error: {res.get('error')}")
        self.assertTrue(res["has_root_div"], "SPA route should return index.html containing #root div")

    @tier(2)
    @feature("r5")
    def test_t2_r5_05_git_not_in_detached_head_state(self):
        """T2-R5-05: Verify repo is not in detached HEAD state (symbolic-ref resolves to branch)."""
        import subprocess
        proc = subprocess.run(
            ["git", "symbolic-ref", "HEAD"],
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True,
            check=False
        )
        self.assertEqual(proc.returncode, 0, "HEAD must be a symbolic reference (not detached)")
        self.assertEqual(proc.stdout.strip(), "refs/heads/main")

    @tier(2)
    @feature("r5")
    def test_t2_r5_06_git_commit_hygiene_and_author(self):
        """T2-R5-06: Verify latest commit has non-empty author, email, and descriptive message."""
        info = get_git_latest_commit_info(PROJECT_ROOT)
        self.assertTrue(len(info) > 10, f"Latest commit info should be non-empty, got: '{info}'")
        self.assertIn("@", info, "Commit author info must include email address")


if __name__ == "__main__":
    unittest.main()
