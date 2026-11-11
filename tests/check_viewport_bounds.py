import os
import subprocess
import time
import socket
from playwright.sync_api import sync_playwright

with socket.socket() as s:
    s.bind(('127.0.0.1', 0))
    port = s.getsockname()[1]

proc = subprocess.Popen(
    f'npx --no-install vite preview --port {port} --strictPort',
    shell=True,
    cwd=os.path.abspath('.')
)

time.sleep(2)

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f'http://127.0.0.1:{port}')
        
        viewports = [1024, 1080, 1100, 1180, 1200, 1240, 1280, 1440, 1920]
        for w in viewports:
            page.set_viewport_size({'width': w, 'height': 800})
            page.wait_for_timeout(200)
            
            # Find the desktop container and buttons
            desktop_nav = page.locator("nav .hidden.lg\\:flex")
            brochure = desktop_nav.locator("button:has-text('BROCHURE')").first
            reg = desktop_nav.locator("button:has-text('REGISTRATION')").first
            
            b_box = brochure.bounding_box()
            r_box = reg.bounding_box()
            
            b_right = b_box['x'] + b_box['width']
            r_right = r_box['x'] + r_box['width']
            
            container = page.locator("nav .max-w-7xl").first
            c_box = container.bounding_box()
            c_right = c_box['x'] + c_box['width']
            
            print(f"Viewport {w}px:")
            print(f"  Container: left={c_box['x']:.1f}px, width={c_box['width']:.1f}px, right={c_right:.1f}px")
            print(f"  REGISTRATION right edge: {r_right:.1f}px (fits in {w}px? {r_right <= w})")
            print(f"  BROCHURE right edge:     {b_right:.1f}px (fits in {w}px? {b_right <= w})")
            if b_right > w:
                print(f"  ==> CRITICAL DEFECT: BROCHURE IS CUT OFF / OFF-SCREEN BY {b_right - w:.1f}px!")
            elif b_right > c_right:
                print(f"  ==> OVERFLOW: BROCHURE overflows container by {b_right - c_right:.1f}px!")
            else:
                print(f"  PASS: Completely fits within viewport and container.")
            print()
            
        browser.close()
finally:
    proc.terminate()
