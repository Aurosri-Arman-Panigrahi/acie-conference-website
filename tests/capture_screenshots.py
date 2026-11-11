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
        
        os.makedirs(".agents/teamwork/challenger_m2_1/screenshots", exist_ok=True)
        
        for w in [1024, 1100, 1280]:
            page.set_viewport_size({'width': w, 'height': 600})
            page.wait_for_timeout(300)
            page.screenshot(path=f".agents/teamwork/challenger_m2_1/screenshots/nav_{w}px.png")
            print(f"Captured screenshot at {w}px")
            
        browser.close()
finally:
    proc.terminate()
