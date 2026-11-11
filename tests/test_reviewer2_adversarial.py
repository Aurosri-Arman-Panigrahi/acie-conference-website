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

def run_adversarial_suite():
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
    
    defects = []
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # --- 1. Logo & Branding Integrity Check ---
            print("\n[TEST 1] Logo & Branding Integrity Check")
            page.goto(url, wait_until="networkidle")
            nav = page.locator("nav")
            
            # KIIT logo presence
            kiit_imgs = nav.locator("img[src*='kiit'], img[alt*='KIIT']").all()
            if len(kiit_imgs) > 0:
                defects.append(f"KIIT logo detected in <nav>: {len(kiit_imgs)} elements")
            else:
                print("  PASS: Zero KIIT logos found in <nav>.")
                
            # ACIE logo presence and transparency
            acie_img = nav.locator("img[src*='acie']").first
            acie_src = acie_img.get_attribute("src")
            acie_nat_w = acie_img.evaluate("el => el.naturalWidth")
            acie_nat_h = acie_img.evaluate("el => el.naturalHeight")
            if not acie_src.endswith("acie-official-logo-transparent.png"):
                defects.append(f"ACIE logo src mismatch: expected acie-official-logo-transparent.png, got {acie_src}")
            elif acie_nat_w == 0 or acie_nat_h == 0:
                defects.append(f"ACIE logo failed to load: naturalWidth={acie_nat_w}, naturalHeight={acie_nat_h}")
            else:
                print(f"  PASS: ACIE transparent logo verified (src={acie_src}, dims={acie_nat_w}x{acie_nat_h})")

            # --- 2. Action Buttons Contract Verification ---
            print("\n[TEST 2] Action Buttons Contract Verification")
            desktop_nav = nav.locator(".hidden.lg\\:flex")
            reg_btn = desktop_nav.locator("button:has-text('REGISTRATION')").first
            # In HashRouter, <Link to="/registration"> renders href="#/registration"
            reg_link = desktop_nav.locator("a[href*='registration']").first
            brochure_btn = desktop_nav.locator("button:has-text('BROCHURE')").first
            brochure_link = desktop_nav.locator("a[href*='ACIE-2027-Brochure.pdf']").first
            
            if reg_link.count() == 0:
                defects.append("REGISTRATION link href pointing to registration not found in desktop nav")
            else:
                print(f"  PASS: REGISTRATION button links to {reg_link.get_attribute('href')}")
                
            if brochure_link.count() == 0:
                defects.append("BROCHURE link href to ACIE-2027-Brochure.pdf not found in desktop nav")
            else:
                print(f"  PASS: BROCHURE button links to {brochure_link.get_attribute('href')}")

            # --- 3. Computed Font Sizes & CSS Specificity ---
            print("\n[TEST 3] Computed Font Sizes & CSS Specificity")
            for w, expected_val in [(1024, 10.5), (1280, 12.0), (1536, 13.0)]:
                page.set_viewport_size({"width": w, "height": 800})
                page.wait_for_timeout(200)
                home_link = desktop_nav.locator("a:has-text('HOME')").first
                computed_fs_str = home_link.evaluate("el => window.getComputedStyle(el).fontSize")
                computed_fs = float(computed_fs_str.replace("px", ""))
                diff = abs(computed_fs - expected_val)
                print(f"  Viewport {w}px: HOME font-size computed as {computed_fs_str} (expected ~{expected_val}px, diff={diff:.3f}px)")
                if diff > 0.3:
                    defects.append(f"Computed font-size at {w}px is {computed_fs_str}, expected ~{expected_val}px")

            # --- 4. Fine-Grained Viewport Boundary & Overflow Scan ---
            print("\n[TEST 4] Fine-Grained Viewport Boundary & Overflow Scan")
            test_widths = [
                1024, 1025, 1030, 1050, 1075, 1100, 1125, 1150, 1177, 1200, 1250, 1279,
                1280, 1300, 1400, 1535,
                1536, 1600, 1920, 2560
            ]
            
            for w in test_widths:
                page.set_viewport_size({"width": w, "height": 800})
                page.wait_for_timeout(200)
                
                b_box = brochure_btn.bounding_box()
                r_box = reg_btn.bounding_box()
                container = nav.locator(".max-w-7xl").first
                c_box = container.bounding_box()
                
                b_right = b_box['x'] + b_box['width']
                c_right = c_box['x'] + c_box['width']
                c_left = c_box['x']
                
                # Check 1: Brochure button off-screen
                if b_right > w + 0.5:
                    diff = b_right - w
                    defects.append(f"Viewport {w}px: BROCHURE clipped off-screen by {diff:.1f}px (right={b_right:.1f}px > viewport={w}px)")
                    print(f"  FAIL @ {w}px: BROCHURE clipped off-screen by {diff:.1f}px")
                # Check 2: Brochure button container overflow
                elif b_right > c_right + 0.5:
                    diff = b_right - c_right
                    defects.append(f"Viewport {w}px: BROCHURE overflows container by {diff:.1f}px (right={b_right:.1f}px > container={c_right:.1f}px)")
                    print(f"  FAIL @ {w}px: BROCHURE overflows container by {diff:.1f}px")
                else:
                    # Margin to container boundary
                    margin = c_right - b_right
                    # Check page horizontal scroll
                    scroll_w = page.evaluate("() => document.documentElement.scrollWidth")
                    client_w = page.evaluate("() => document.documentElement.clientWidth")
                    if scroll_w > client_w + 1:
                        defects.append(f"Viewport {w}px: Page has horizontal scrollbar (scrollWidth={scroll_w} > clientWidth={client_w})")
                        print(f"  FAIL @ {w}px: Horizontal scrollbar detected ({scroll_w} > {client_w})")
                    else:
                        print(f"  PASS @ {w}px: BROCHURE right={b_right:.1f}px <= container right={c_right:.1f}px (margin: {margin:.1f}px)")

            # --- 5. Desktop Dropdown Interaction & Containment Test ---
            print("\n[TEST 5] Desktop Dropdown Interaction & Containment Test")
            page.set_viewport_size({"width": 1024, "height": 800})
            page.wait_for_timeout(200)
            dropdown_configs = [
                ('ABOUT', 'About Conference'),
                ('AUTHORS', 'Call for Papers'),
                ('SPEAKERS', 'Keynote Speakers'),
                ('AWARDS', 'Best Paper Award')
            ]
            for d_name, child_item_text in dropdown_configs:
                parent_group = desktop_nav.locator("div.relative.group").filter(has_text=d_name).first
                parent_group.hover()
                page.wait_for_timeout(250)
                child_el = page.locator(f"text='{child_item_text}'").first
                if not child_el.is_visible():
                    defects.append(f"Dropdown for {d_name} ('{child_item_text}') not visible on hover")
                    print(f"  FAIL: Dropdown {d_name} not visible on hover")
                else:
                    dropdown_box = child_el.evaluate("el => el.closest('.absolute.left-0.top-full').getBoundingClientRect()")
                    d_right = dropdown_box['x'] + dropdown_box['width']
                    if d_right > 1024:
                        defects.append(f"Dropdown {d_name} overflows 1024px screen: right={d_right:.1f}px")
                        print(f"  FAIL: Dropdown {d_name} overflows screen ({d_right:.1f}px > 1024px)")
                    else:
                        print(f"  PASS: Dropdown {d_name} visible and contained (right={d_right:.1f}px <= 1024px)")
                # move mouse away
                page.mouse.move(0, 0)
                page.wait_for_timeout(100)

            # --- 6. Mobile Viewport & Drawer Responsiveness ---
            print("\n[TEST 6] Mobile Viewport & Drawer Responsiveness")
            mobile_widths = [320, 360, 375, 414, 768, 820, 1023]
            for mw in mobile_widths:
                page.set_viewport_size({"width": mw, "height": 700})
                page.wait_for_timeout(150)
                
                # desktop nav must be hidden
                is_desktop_vis = desktop_nav.is_visible()
                if is_desktop_vis:
                    defects.append(f"Desktop nav visible at mobile width {mw}px")
                
                # hamburger must be visible
                hamburger = nav.locator("button[aria-label='Toggle Navigation Menu']")
                if not hamburger.is_visible():
                    defects.append(f"Hamburger button not visible at mobile width {mw}px")
                    
                print(f"  PASS @ {mw}px: Desktop nav hidden, Hamburger button visible.")

            browser.close()
    finally:
        proc.terminate()
        
    print("\n==========================================")
    print("      REVIEWER 2 ADVERSARIAL VERDICT      ")
    print("==========================================")
    if defects:
        print(f"FAIL: {len(defects)} defects found:")
        for d in defects:
            print(f"  - {d}")
        return False
    else:
        print("PASS: ALL ADVERSARIAL STRESS-TESTS PASSED!")
        return True

if __name__ == "__main__":
    success = run_adversarial_suite()
    sys.exit(0 if success else 1)
