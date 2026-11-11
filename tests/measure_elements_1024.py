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
        page.wait_for_timeout(200)
        
        data = page.evaluate("""() => {
            const nav = document.querySelector('nav');
            const container = nav.querySelector('.max-w-7xl');
            const innerFlex = container.firstElementChild;
            const logo = innerFlex.firstElementChild;
            const desktopNav = innerFlex.children[1];
            
            const getMetrics = (el) => {
                const r = el.getBoundingClientRect();
                const style = window.getComputedStyle(el);
                return {
                    text: el.innerText ? el.innerText.trim().replace(/\\n/g, ' ') : el.tagName,
                    width: r.width,
                    x: r.x,
                    paddingLeft: style.paddingLeft,
                    paddingRight: style.paddingRight,
                    marginLeft: style.marginLeft,
                    marginRight: style.marginRight,
                    fontSize: style.fontSize
                };
            };
            
            const navItems = Array.from(desktopNav.children).map(getMetrics);
            
            return {
                container: getMetrics(container),
                innerFlex: {
                    ...getMetrics(innerFlex),
                    gap: window.getComputedStyle(innerFlex).gap
                },
                logo: getMetrics(logo),
                desktopNav: {
                    ...getMetrics(desktopNav),
                    gap: window.getComputedStyle(desktopNav).gap
                },
                navItems: navItems
            };
        }""")
        
        print("=== 1024px Viewport Layout Breakdown ===")
        print(f"Container width: {data['container']['width']:.2f}px (padding: L={data['container']['paddingLeft']}, R={data['container']['paddingRight']})")
        print(f"Inner Flex width: {data['innerFlex']['width']:.2f}px (gap={data['innerFlex']['gap']})")
        print(f"Logo element width: {data['logo']['width']:.2f}px")
        print(f"Desktop Nav width: {data['desktopNav']['width']:.2f}px (x={data['desktopNav']['x']:.2f})")
        print("\nNav Items:")
        total_items_w = 0
        for i, item in enumerate(data['navItems']):
            print(f"  {i+1}. {item['text']:<15} : width={item['width']:>6.2f}px (fontSize={item['fontSize']}, padL={item['paddingLeft']}, padR={item['paddingRight']})")
            total_items_w += item['width']
            
        print(f"\nSum of 11 item widths: {total_items_w:.2f}px")
        print(f"Logo ({data['logo']['width']:.2f}px) + Gap + Nav ({data['desktopNav']['width']:.2f}px) = {data['logo']['width'] + data['desktopNav']['width']:.2f}px")
        print(f"Total needed: > {data['logo']['x'] + data['desktopNav']['width']:.2f}px, but Viewport is only 1024px!")
        
        browser.close()
finally:
    proc.terminate()
