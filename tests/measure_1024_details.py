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

def measure():
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
        
        # Test 1024px
        page.set_viewport_size({"width": 1024, "height": 800})
        page.wait_for_timeout(500)
        
        container = page.locator("nav .max-w-7xl").first
        c_box = container.bounding_box()
        print(f"Container at 1024px: x={c_box['x']:.2f}, width={c_box['width']:.2f}, right={c_box['x']+c_box['width']:.2f}")
        
        logo = page.locator("nav img[src*='acie']").first
        l_box = logo.bounding_box()
        print(f"Logo: x={l_box['x']:.2f}, width={l_box['width']:.2f}, right={l_box['x']+l_box['width']:.2f}")
        
        desktop_nav = page.locator("nav .hidden.lg\\:flex").first
        n_box = desktop_nav.bounding_box()
        print(f"Desktop nav container: x={n_box['x']:.2f}, width={n_box['width']:.2f}, right={n_box['x']+n_box['width']:.2f}")
        
        items = desktop_nav.locator("> *").all()
        for idx, it in enumerate(items):
            box = it.bounding_box()
            text = it.inner_text().strip().replace('\n', ' ')
            tag = it.evaluate("el => el.tagName")
            computed_fs = it.evaluate("el => window.getComputedStyle(el).fontSize")
            print(f"[{idx:02d}] {text:18s} tag={tag:5s} x={box['x']:6.2f} w={box['width']:6.2f} right={box['x']+box['width']:6.2f} fs={computed_fs}")
            
        brochure = desktop_nav.locator("button:has-text('BROCHURE')").first
        b_box = brochure.bounding_box()
        b_right = b_box['x'] + b_box['width']
        print(f"\nFinal BROCHURE button right edge: {b_right:.2f}px (Viewport: 1024px)")
        print(f"Difference (b_right - 1024): {b_right - 1024:.2f}px")
        
        browser.close()
    proc.terminate()

if __name__ == "__main__":
    measure()
