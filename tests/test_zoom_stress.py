import os
import sys
import subprocess
import socket
from playwright.sync_api import sync_playwright

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]

port = find_free_port()
proc = subprocess.Popen(
    f"npx --no-install vite preview --port {port} --strictPort",
    shell=True,
    cwd=os.path.abspath(".")
)

import time
time.sleep(2)

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Test standard desktop with 1.25x and 1.5x device scale factor (simulating high-DPI / Windows 125% display scaling)
        for dsf in [1.0, 1.25, 1.5]:
            page = browser.new_page(device_scale_factor=dsf, viewport={"width": 1280, "height": 800})
            page.goto(f"http://127.0.0.1:{port}")
            nav = page.locator("nav .hidden.lg\\:flex")
            bro_btn = nav.locator("button:has-text('BROCHURE')").first
            b_box = bro_btn.bounding_box()
            b_right = b_box['x'] + b_box['width']
            container = page.locator("nav .max-w-7xl").first
            c_box = container.bounding_box()
            c_right = c_box['x'] + c_box['width']
            print(f"DeviceScaleFactor={dsf} at 1280px viewport: BROCHURE right={b_right:.1f}px, container right={c_right:.1f}px, fits={b_right <= c_right}")
            assert b_right <= c_right + 0.5, f"Overflow at dsf={dsf}"
        browser.close()
    print("ALL ZOOM/HIGH-DPI TESTS PASSED")
finally:
    proc.terminate()
