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

def test_overflow_and_resize():
    port = find_free_port()
    proc = subprocess.Popen(
        f"npx --no-install vite preview --port {port} --strictPort",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=os.path.abspath(".")
    )
    time.sleep(2)
    url = f"http://127.0.0.1:{port}"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        
        # Test fresh at 1024px
        page.set_viewport_size({"width": 1024, "height": 800})
        page.wait_for_timeout(400) # allow any layout to settle
        
        scroll_w = page.evaluate("() => document.documentElement.scrollWidth")
        client_w = page.evaluate("() => document.documentElement.clientWidth")
        has_h_scroll = page.evaluate("() => window.innerWidth < document.documentElement.scrollWidth")
        
        print(f"At 1024px settled: scrollWidth={scroll_w}, clientWidth={client_w}, has_h_scroll={has_h_scroll}")
        
        b = page.locator("nav .hidden.lg\\:flex button:has-text('BROCHURE')").first.bounding_box()
        b_right = b['x'] + b['width']
        print(f"BROCHURE right: {b_right:.2f}px, viewport: 1024px, margin: {1024 - b_right:.2f}px")
        
        # Now test sudden resize from 1920 down to 1024
        page.set_viewport_size({"width": 1920, "height": 800})
        page.wait_for_timeout(400)
        
        # Now resize to 1024 and measure at 50ms, 150ms, 300ms, 450ms
        page.set_viewport_size({"width": 1024, "height": 800})
        for delay in [50, 100, 150, 200, 300, 450]:
            page.wait_for_timeout(50)
            b_cur = page.locator("nav .hidden.lg\\:flex button:has-text('BROCHURE')").first.bounding_box()
            b_r = b_cur['x'] + b_cur['width']
            s_w = page.evaluate("() => document.documentElement.scrollWidth")
            c_w = page.evaluate("() => document.documentElement.clientWidth")
            print(f"T+{delay:3d}ms after resize: BROCHURE right={b_r:6.2f}px, scrollWidth={s_w}, clientWidth={c_w}")
            
        browser.close()
    proc.terminate()

if __name__ == "__main__":
    test_overflow_and_resize()
