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
        page.set_viewport_size({'width': 1024, 'height': 800})
        
        info = page.evaluate("""() => {
            const home = document.querySelector('nav .hidden.lg\\\\:flex a');
            const style = window.getComputedStyle(home);
            return {
                fontSize: style.fontSize,
                fontWeight: style.fontWeight,
                className: home.className
            };
        }""")
        print("HOME link style at 1024px:", info)
        browser.close()
finally:
    proc.terminate()
