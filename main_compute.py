# 📁 File: main_compute.py
from playwright.sync_api import sync_playwright
from compute.compute_login import login
from compute.compute_instances import do_instances
from compute.compute_instance_snapshots import do_instance_snapshots
from compute.compute_flavors import do_flavors
from compute.compute_images import do_images
from compute.compute_keypairs import do_keypairs

USERNAME = "customer@x-or.cloud"
PASSWORD = "123zXc_-"
TARGET_URL = "https://portal.stack-dev.x-or.cloud/compute"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()

    try:
        login(page, USERNAME, PASSWORD, TARGET_URL)
        do_instances(page)
        do_instance_snapshots(page)
        do_flavors(page)
        do_images(page)
        do_keypairs(page)
        print("✅ Đã hoàn tất chụp toàn bộ màn hình Compute.")
    except Exception as e:
        print("❌ Lỗi:", e)
    finally:
        browser.close()
