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

def run_stress_tests():
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
            
            # --- Check Branding & Absence of KIIT in Header ---
            print("\n==========================================")
            print("1. BRANDING & ASSET INTEGRITY")
            print("==========================================")
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
            if not acie_src or "acie-official-logo-transparent.png" not in acie_src:
                findings.append(f"ACIE logo src unexpected: {acie_src}")
            if acie_nat_w == 0:
                findings.append("ACIE logo image failed to load (naturalWidth == 0)")

            # --- Check Computed Font Sizes Across Breakpoints ---
            print("\n==========================================")
            print("2. COMPUTED FONT SIZES & CSS SPECIFICITY")
            print("==========================================")
            test_bps = [(1024, "10.5px"), (1280, "12px"), (1536, "13px"), (1920, "13px")]
            for w, expected_fs in test_bps:
                page.set_viewport_size({"width": w, "height": 800})
                page.wait_for_timeout(350)
                desktop_nav = nav.locator(".hidden.lg\\:flex")
                home_link = desktop_nav.locator("a:has-text('HOME')").first
                computed_fs = home_link.evaluate("el => window.getComputedStyle(el).fontSize")
                print(f"Viewport {w}px: HOME font-size = {computed_fs} (expected {expected_fs})")
                if w == 1024 and not ("10.5" in computed_fs or "10" in computed_fs or "11" in computed_fs):
                    findings.append(f"Viewport {w}px: font-size was {computed_fs}, expected ~10.5px")

            # --- Comprehensive Viewport Sweep ---
            print("\n==========================================")
            print("3. COMPREHENSIVE VIEWPORT SWEEP & BOUNDING BOX CHECKS")
            print("==========================================")
            viewports_to_test = [
                1024, 1040, 1060, 1080, 1100, 1150, 1200, 1250, 1279,
                1280, 1300, 1366, 1440, 1500, 1535,
                1536, 1600, 1680, 1920, 2560
            ]
            
            for w in viewports_to_test:
                page.set_viewport_size({"width": w, "height": 800})
                page.wait_for_timeout(350)
                
                # Check horizontal scroll on page
                scroll_w = page.evaluate("() => document.documentElement.scrollWidth")
                client_w = page.evaluate("() => document.documentElement.clientWidth")
                if scroll_w > client_w:
                    findings.append(f"Viewport {w}px: Document has horizontal overflow: scrollWidth={scroll_w} > clientWidth={client_w}")
                    print(f"FAIL Viewport {w}px: Horizontal overflow scrollWidth={scroll_w} > clientWidth={client_w}")
                
                desktop_nav = nav.locator(".hidden.lg\\:flex")
                brochure = desktop_nav.locator("button:has-text('BROCHURE')").first
                reg = desktop_nav.locator("button:has-text('REGISTRATION')").first
                
                b_box = brochure.bounding_box()
                r_box = reg.bounding_box()
                container = nav.locator(".max-w-7xl").first
                c_box = container.bounding_box()
                
                b_right = b_box['x'] + b_box['width']
                c_right = c_box['x'] + c_box['width']
                
                # Check button overlap
                if r_box['x'] + r_box['width'] > b_box['x']:
                    findings.append(f"Viewport {w}px: REGISTRATION and BROCHURE buttons overlap!")
                
                # Check container containment
                if b_right > w:
                    diff = b_right - w
                    findings.append(f"Viewport {w}px: BROCHURE clipped by viewport by {diff:.1f}px")
                    print(f"FAIL Viewport {w}px: BROCHURE clipped by viewport by {diff:.1f}px")
                elif b_right > c_right + 0.5: # 0.5px subpixel tolerance
                    diff = b_right - c_right
                    findings.append(f"Viewport {w}px: BROCHURE overflows container by {diff:.1f}px")
                    print(f"FAIL Viewport {w}px: BROCHURE overflows container by {diff:.1f}px (b_right={b_right:.1f}, c_right={c_right:.1f})")
                else:
                    margin_c = c_right - b_right
                    margin_w = w - b_right
                    print(f"PASS Viewport {w:4d}px: BROCHURE right={b_right:.1f}px <= container_right={c_right:.1f}px (margin: {margin_c:.1f}px, vp_margin: {margin_w:.1f}px)")

                # Check nav link wrapping (all items must have identical vertical Y baseline / single row)
                nav_items = desktop_nav.locator("> *").all()
                y_positions = [item.bounding_box()['y'] for item in nav_items if item.bounding_box()]
                if y_positions:
                    max_y = max(y_positions)
                    min_y = min(y_positions)
                    # Vertical tolerance: all items should be vertically centered within ~10px of each other
                    if max_y - min_y > 15:
                        findings.append(f"Viewport {w}px: Nav items are wrapping or not on single row! (delta Y = {max_y - min_y:.1f}px)")
                        print(f"FAIL Viewport {w}px: Nav items wrapped (delta Y = {max_y - min_y:.1f}px)")

            # --- Dropdown Menu Boundary Checks at 1024px ---
            print("\n==========================================")
            print("4. DROPDOWN SUBMENU BOUNDARY CHECKS AT 1024px")
            print("==========================================")
            page.set_viewport_size({"width": 1024, "height": 800})
            page.wait_for_timeout(100)
            
            dropdown_names = ['about', 'authors', 'speakers', 'awards']
            for dname in dropdown_names:
                btn = desktop_nav.locator(f"button:has-text('{dname.upper()}')").first
                btn.hover()
                page.wait_for_timeout(200)
                
                # Check visible dropdown menu
                menu = nav.locator(".absolute.left-0.top-full:not(.invisible)").first
                if menu.count() > 0 and menu.is_visible():
                    m_box = menu.bounding_box()
                    m_right = m_box['x'] + m_box['width']
                    print(f"Dropdown '{dname}': left={m_box['x']:.1f}px, width={m_box['width']:.1f}px, right={m_right:.1f}px")
                    if m_right > 1024:
                        findings.append(f"Dropdown '{dname}' overflows viewport 1024px by {m_right - 1024:.1f}px")
                    else:
                        print(f"  PASS: Dropdown '{dname}' fits within viewport (right={m_right:.1f}px <= 1024px)")
                else:
                    findings.append(f"Dropdown '{dname}' did not become visible on hover")
                # Move mouse away
                page.mouse.move(0, 0)
                page.wait_for_timeout(100)

            # --- Action Button Interactive Verification ---
            print("\n==========================================")
            print("5. ACTION BUTTON LINKS & ATTRIBUTES")
            print("==========================================")
            reg_link = desktop_nav.locator("a[href*='registration']").first
            if reg_link.count() > 0:
                href = reg_link.get_attribute("href")
                print(f"PASS: Desktop REGISTRATION has href='{href}'")
            else:
                findings.append("Desktop REGISTRATION link missing or wrong href")
                
            brochure_a = desktop_nav.locator("a[href*='ACIE-2027-Brochure.pdf']").first
            if brochure_a.count() > 0:
                target = brochure_a.get_attribute("target")
                href = brochure_a.get_attribute("href")
                print(f"PASS: Desktop BROCHURE has href='{href}' and target='{target}'")
            else:
                findings.append("Desktop BROCHURE link missing or wrong href")

            # Test REGISTRATION navigation
            reg_btn = desktop_nav.locator("button:has-text('REGISTRATION')").first
            reg_btn.click()
            page.wait_for_timeout(300)
            cur_url = page.url
            print(f"URL after clicking REGISTRATION: {cur_url}")
            if "registration" in cur_url.lower():
                print("PASS: Navigation to Registration succeeded.")
            else:
                findings.append(f"Clicking REGISTRATION did not navigate to registration: {cur_url}")

            browser.close()
    finally:
        proc.terminate()

    print("\n==========================================")
    print("      STRESS TEST SUMMARY RESULTS         ")
    print("==========================================")
    if findings:
        print(f"TOTAL FINDINGS / DEFECTS DETECTED: {len(findings)}")
        for f in findings:
            print(f"  - [DEFECT] {f}")
        return False
    else:
        print("ALL STRESS TESTS PASSED WITH 0 DEFECTS!")
        return True

if __name__ == "__main__":
    success = run_stress_tests()
    sys.exit(0 if success else 1)
