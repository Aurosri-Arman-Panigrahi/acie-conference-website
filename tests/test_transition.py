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

def test():
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
        
        # 1. Fresh at 1024
        page.set_viewport_size({"width": 1024, "height": 800})
        page.wait_for_timeout(200)
        brochure = page.locator("nav .hidden.lg\\:flex button:has-text('BROCHURE')").first
        b1 = brochure.bounding_box()
        fs1 = page.locator("nav .hidden.lg\\:flex a:has-text('HOME')").first.evaluate("el => window.getComputedStyle(el).fontSize")
        print(f"1. Fresh 1024 b_right: {b1['x'] + b1['width']:.2f}px, HOME fs: {fs1}")
        
        # 2. Resize to 1920
        page.set_viewport_size({"width": 1920, "height": 800})
        page.wait_for_timeout(200)
        b2 = brochure.bounding_box()
        fs2 = page.locator("nav .hidden.lg\\:flex a:has-text('HOME')").first.evaluate("el => window.getComputedStyle(el).fontSize")
        print(f"2. 1920 b_right: {b2['x'] + b2['width']:.2f}px, HOME fs: {fs2}")
        
        # 3. Resize back to 1024 with 100ms
        page.set_viewport_size({"width": 1024, "height": 800})
        page.wait_for_timeout(100)
        b3 = brochure.bounding_box()
        fs3 = page.locator("nav .hidden.lg\\:flex a:has-text('HOME')").first.evaluate("el => window.getComputedStyle(el).fontSize")
        print(f"3. Resize to 1024 (100ms) b_right: {b3['x'] + b3['width']:.2f}px, HOME fs: {fs3}")
        
        # 4. Wait another 300ms
        page.wait_for_timeout(300)
        b4 = brochure.bounding_box()
        fs4 = page.locator("nav .hidden.lg\\:flex a:has-text('HOME')").first.evaluate("el => window.getComputedStyle(el).fontSize")
        print(f"4. Resize to 1024 (+300ms) b_right: {b4['x'] + b4['width']:.2f}px, HOME fs: {fs4}")

        browser.close()
    proc.terminate()

if __name__ == "__main__":
    test()
