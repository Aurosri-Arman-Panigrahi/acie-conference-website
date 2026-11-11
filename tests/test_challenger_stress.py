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

def run_stress_suite():
    port = find_free_port()
    print(f"Starting Vite preview on port {port}...")
    
    proc = subprocess.Popen(
        f"npx --no-install vite preview --port {port} --strictPort",
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
            
            # Stress viewports including critical breakpoint transitions
            stress_viewports = [
                1024, # lg breakpoint start
                1025,
                1100,
                1199,
                1279, # just before xl
                1280, # xl breakpoint start
                1366, # common laptop resolution
                1440, # standard desktop
                1535, # just before 2xl
                1536, # 2xl breakpoint start
                1680,
                1920, # standard 1080p desktop
                2560  # 1440p / QHD ultrawide
            ]
            
            expected_links = [
                "HOME", "ABOUT", "AUTHORS", "SPEAKERS", 
                "COMMITTEE", "AWARDS", "ACCOMODATION", 
                "SCHEDULE", "SPONSORSHIP"
            ]
            
            print("\n=======================================================")
            print("  CHALLENGER 2: DEEP EMPIRICAL STRESS TEST SUITE")
            print("=======================================================\n")
            
            for w in stress_viewports:
                page.set_viewport_size({"width": w, "height": 850})
                page.goto(url, wait_until="networkidle")
                page.wait_for_timeout(150)
                
                nav = page.locator("nav")
                desktop_nav = nav.locator(".hidden.lg\\:flex")
                container = nav.locator(".max-w-7xl").first
                c_box = container.bounding_box()
                c_right = c_box['x'] + c_box['width']
                
                # 1. Document scrollWidth vs viewport width (no horizontal page scrollbar)
                doc_scroll_w = page.evaluate("() => document.documentElement.scrollWidth")
                if doc_scroll_w > w:
                    findings.append(f"Viewport {w}px: Document has horizontal scroll! (scrollWidth={doc_scroll_w}px > viewport={w}px)")
                    print(f"[FAIL] Viewport {w}px: document.documentElement.scrollWidth={doc_scroll_w}px > {w}px")
                
                # 2. Collect all 11 items (9 links + 2 buttons)
                items = []
                for link_text in expected_links:
                    el = desktop_nav.locator(f":text-matches('^{link_text}$', 'i')").first
                    if not el.is_visible():
                        findings.append(f"Viewport {w}px: Navigation item '{link_text}' is not visible!")
                        print(f"[FAIL] Viewport {w}px: '{link_text}' not visible")
                    else:
                        box = el.bounding_box()
                        # check text clipping
                        is_clipped = el.evaluate("el => el.scrollWidth > el.clientWidth")
                        items.append((link_text, box, is_clipped))
                
                # Registration & Brochure buttons
                reg_btn = desktop_nav.locator("button:has-text('REGISTRATION')").first
                bro_btn = desktop_nav.locator("button:has-text('BROCHURE')").first
                
                if not reg_btn.is_visible():
                    findings.append(f"Viewport {w}px: REGISTRATION button not visible")
                else:
                    reg_box = reg_btn.bounding_box()
                    reg_clipped = reg_btn.evaluate("el => el.scrollWidth > el.clientWidth")
                    items.append(("REGISTRATION", reg_box, reg_clipped))
                    
                if not bro_btn.is_visible():
                    findings.append(f"Viewport {w}px: BROCHURE button not visible")
                else:
                    bro_box = bro_btn.bounding_box()
                    bro_clipped = bro_btn.evaluate("el => el.scrollWidth > el.clientWidth")
                    items.append(("BROCHURE", bro_box, bro_clipped))
                
                # 3. Check for text truncation inside any item
                for name, box, clipped in items:
                    if clipped:
                        findings.append(f"Viewport {w}px: Item '{name}' has internal text clipping/truncation!")
                        print(f"[FAIL] Viewport {w}px: '{name}' internal text clipped!")
                
                # 4. Check for wrapping / vertical baseline alignment
                y_coords = [b['y'] for _, b, _ in items if b]
                avg_y = sum(y_coords) / len(y_coords) if y_coords else 0
                for name, b, _ in items:
                    if abs(b['y'] - avg_y) > 15:
                        findings.append(f"Viewport {w}px: Item '{name}' wrapped or misaligned vertically (y={b['y']}, avg_y={avg_y})")
                        print(f"[FAIL] Viewport {w}px: '{name}' wrapped vertically!")
                
                # 5. Check for horizontal overlap between adjacent items
                for i in range(len(items) - 1):
                    curr_name, curr_b, _ = items[i]
                    next_name, next_b, _ = items[i+1]
                    curr_right = curr_b['x'] + curr_b['width']
                    if curr_right > next_b['x'] + 0.5:
                        overlap = curr_right - next_b['x']
                        findings.append(f"Viewport {w}px: Items '{curr_name}' and '{next_name}' overlap by {overlap:.1f}px!")
                        print(f"[FAIL] Viewport {w}px: overlap between '{curr_name}' and '{next_name}' by {overlap:.1f}px")
                
                # 6. Check rightmost edge vs container & viewport
                bro_right = bro_box['x'] + bro_box['width'] if bro_box else 0
                if bro_right > w:
                    diff = bro_right - w
                    findings.append(f"Viewport {w}px: BROCHURE button exceeds viewport edge by {diff:.1f}px")
                    print(f"[FAIL] Viewport {w}px: BROCHURE right={bro_right:.1f}px > viewport={w}px")
                elif bro_right > c_right + 0.5:
                    diff = bro_right - c_right
                    findings.append(f"Viewport {w}px: BROCHURE button overflows container by {diff:.1f}px")
                    print(f"[FAIL] Viewport {w}px: BROCHURE right={bro_right:.1f}px > container={c_right:.1f}px")
                else:
                    margin = c_right - bro_right
                    print(f"[PASS] Viewport {w:4d}px: all 11 items aligned in 1 row, 0 overlap, 0 clipping, right margin={margin:.1f}px")

            # --- Dropdown Overflow Test at 1024px ---
            print("\n=== Dropdown Menus Boundary Test at 1024px ===")
            page.set_viewport_size({"width": 1024, "height": 850})
            page.goto(url, wait_until="networkidle")
            
            dropdown_triggers = ["ABOUT", "AUTHORS", "SPEAKERS", "AWARDS"]
            for trig in dropdown_triggers:
                btn = nav.locator(f".hidden.lg\\:flex button:has-text('{trig}')").first
                btn.hover()
                page.wait_for_timeout(200)
                # Find visible dropdown panel
                dropdown_panel = nav.locator(".hidden.lg\\:flex .group .absolute.opacity-100").first
                if dropdown_panel.is_visible():
                    dp_box = dropdown_panel.bounding_box()
                    dp_right = dp_box['x'] + dp_box['width']
                    print(f"Dropdown '{trig}': left={dp_box['x']:.1f}px, width={dp_box['width']:.1f}px, right={dp_right:.1f}px")
                    if dp_right > 1024:
                        findings.append(f"Dropdown '{trig}' overflows right viewport edge by {dp_right - 1024:.1f}px at 1024px viewport!")
                    if dp_box['x'] < 0:
                        findings.append(f"Dropdown '{trig}' overflows left viewport edge by {-dp_box['x']:.1f}px at 1024px viewport!")
                else:
                    findings.append(f"Dropdown '{trig}' failed to open on hover!")
                    
            browser.close()
    finally:
        proc.terminate()
        
    print("\n=======================================================")
    print("           STRESS TEST SUITE VERDICT")
    print("=======================================================")
    if findings:
        print(f"VERDICT: REQUEST_CHANGES ({len(findings)} issues found)")
        for f in findings:
            print(f"  - {f}")
        return False
    else:
        print("VERDICT: APPROVE (100% stress tests passed cleanly)")
        return True

if __name__ == "__main__":
    success = run_stress_suite()
    sys.exit(0 if success else 1)
