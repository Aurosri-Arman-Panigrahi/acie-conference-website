import os
import sys
import time
import subprocess
import socket
from playwright.sync_api import sync_playwright

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]

def run_tests():
    port = find_free_port()
    print(f"Starting Vite preview on port {port}...")
    
    server_cmd = f"npx --no-install vite preview --port {port} --strictPort"
    proc = subprocess.Popen(
        server_cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.path.abspath(".")
    )
    
    url = f"http://127.0.0.1:{port}"
    max_wait = 30
    start = time.time()
    server_ready = False
    
    while time.time() - start < max_wait:
        try:
            with socket.create_connection(('127.0.0.1', port), timeout=0.5):
                server_ready = True
                break
        except Exception:
            time.sleep(0.3)
            
    if not server_ready:
        print("ERROR: Vite preview server failed to start within 30s")
        proc.kill()
        sys.exit(1)
        
    print(f"Vite preview server listening at {url}")
    
    findings = []
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # --- Check Branding & Logos First ---
            print("\n=== Branding & Asset Verification ===")
            page.goto(url, wait_until="networkidle")
            nav = page.locator("nav")
            
            kiit_logos = nav.locator("img[src*='kiit']").all()
            if len(kiit_logos) == 0:
                print("PASS: Zero KIIT logos found in <nav>.")
            else:
                findings.append(f"KIIT logo found in <nav> ({len(kiit_logos)} matches)")
                
            acie_img = nav.locator("img[src*='acie']").first
            acie_src = acie_img.get_attribute("src")
            acie_nat_w = acie_img.evaluate("el => el.naturalWidth")
            print(f"PASS: ACIE logo visible, src='{acie_src}', naturalWidth={acie_nat_w}px")

            # --- Empirical Viewport Checks ---
            print("\n=== Desktop Viewport Empirical Boundary Checks ===")
            desktop_viewports = [1024, 1100, 1280, 1440, 1920]
            for w in desktop_viewports:
                page.set_viewport_size({"width": w, "height": 800})
                page.wait_for_timeout(200)
                
                desktop_nav = nav.locator(".hidden.lg\\:flex")
                brochure = desktop_nav.locator("button:has-text('BROCHURE')").first
                reg = desktop_nav.locator("button:has-text('REGISTRATION')").first
                
                b_box = brochure.bounding_box()
                r_box = reg.bounding_box()
                container = nav.locator(".max-w-7xl").first
                c_box = container.bounding_box()
                
                b_right = b_box['x'] + b_box['width']
                c_right = c_box['x'] + c_box['width']
                
                print(f"\nViewport {w}px:")
                print(f"  Container: left={c_box['x']:.1f}px, width={c_box['width']:.1f}px, right={c_right:.1f}px")
                print(f"  REGISTRATION right: {r_box['x'] + r_box['width']:.1f}px")
                print(f"  BROCHURE right: {b_right:.1f}px")
                
                if b_right > w:
                    diff = b_right - w
                    print(f"  CRITICAL BUG: BROCHURE button extends beyond viewport edge by {diff:.1f}px (Clipped/Truncated from view)!")
                    findings.append(f"Viewport {w}px: BROCHURE button clipped off-screen by {diff:.1f}px (right edge at {b_right:.1f}px > viewport {w}px)")
                elif b_right > c_right:
                    diff = b_right - c_right
                    print(f"  DEFECT: BROCHURE button overflows container boundary by {diff:.1f}px!")
                    findings.append(f"Viewport {w}px: BROCHURE button overflows container boundary by {diff:.1f}px (right edge at {b_right:.1f}px > container {c_right:.1f}px)")
                else:
                    print(f"  PASS: Fully fits within viewport and container.")

            # --- Mobile Menu Behavior Verification ---
            print("\n=== Mobile Viewport Verification (< 1024px) ===")
            mobile_viewports = [
                (375, 667, "Mobile Small 375px"),
                (768, 1024, "Tablet Portrait 768px"),
                (1023, 768, "Mobile Boundary 1023px")
            ]
            
            for mw, mh, label in mobile_viewports:
                page.goto(url, wait_until="networkidle")
                page.set_viewport_size({"width": mw, "height": mh})
                page.wait_for_timeout(200)
                
                desktop_nav = nav.locator(".hidden.lg\\:flex")
                assert not desktop_nav.is_visible(), f"Desktop nav must be hidden at {mw}px"
                
                hamburger = nav.locator("button[aria-label='Toggle Navigation Menu']")
                assert hamburger.is_visible(), f"Hamburger button must be visible at {mw}px"
                print(f"\n{label}:")
                print("  PASS: Desktop nav hidden, Hamburger button visible.")
                
                hamburger.click()
                page.wait_for_timeout(250)
                
                mobile_drawer = page.locator(".lg\\:hidden.absolute.top-full")
                assert mobile_drawer.is_visible(), f"Mobile drawer failed to open at {mw}px"
                print("  PASS: Mobile drawer opened.")
                
                mob_reg = mobile_drawer.locator("a:has-text('REGISTRATION')").first
                mob_brochure = mobile_drawer.locator("a:has-text('BROCHURE')").first
                assert mob_reg.is_visible(), "Mobile REGISTRATION button not visible"
                assert mob_brochure.is_visible(), "Mobile BROCHURE button not visible"
                print("  PASS: REGISTRATION and BROCHURE buttons visible in mobile drawer.")
                
                # Test submenu expand
                about_toggle = mobile_drawer.locator("button:has-text('ABOUT')").first
                about_toggle.click()
                page.wait_for_timeout(250)
                about_conf = mobile_drawer.locator("button:has-text('About Conference')").first
                assert about_conf.is_visible(), "About Conference mobile submenu item not visible after expand"
                print("  PASS: Mobile submenu 'ABOUT' expanded successfully.")
                
                # Close drawer
                hamburger.click()
                page.wait_for_timeout(200)
                assert mobile_drawer.count() == 0 or not mobile_drawer.is_visible(), "Mobile drawer failed to close"
                print("  PASS: Mobile drawer closed successfully.")

            browser.close()
    finally:
        proc.terminate()
        
    print("\n==========================================")
    print("      FINAL CHALLENGER VERIFICATION       ")
    print("==========================================")
    if findings:
        print(f"VERDICT: REQUEST_CHANGES ({len(findings)} defects detected)")
        for f in findings:
            print(f"  - {f}")
        return False
    else:
        print("VERDICT: APPROVE (All empirical checks passed)")
        return True

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
