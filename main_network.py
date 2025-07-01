from playwright.sync_api import sync_playwright
from compute.compute_login import login
from network.network_networks import do_networks
from network.network_ports import do_ports
from network.network_routers import do_routers
from network.network_floating_ips import do_floating_ips
from network.network_security_groups import do_security_groups


USERNAME = "customer@x-or.cloud"
PASSWORD = "123zXc_-"
TARGET_URL = "https://portal.stack-dev.x-or.cloud/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()

    try:
        login(page, USERNAME, PASSWORD, TARGET_URL)
        do_networks(page)
        do_ports(page)
        do_routers(page)
        do_floating_ips(page)
        do_security_groups(page)
        print("✅ Đã hoàn tất chụp toàn bộ màn hình Network.")
    except Exception as e:
        print("❌ Lỗi:", e)
    finally:
        browser.close()
