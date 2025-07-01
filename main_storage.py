# 📁 File: main_storage.py
from playwright.sync_api import sync_playwright
from compute.compute_login import login 
from storage.storage_volumes import do_volumes
from storage.storage_snapshots import do_snapshots

USERNAME = "customer@x-or.cloud"
PASSWORD = "123zXc_-"
TARGET_URL = "https://portal.stack-dev.x-or.cloud/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()

    try:
        login(page, USERNAME, PASSWORD, TARGET_URL)
        do_volumes(page)
        do_snapshots(page)
        print("✅ Đã hoàn tất chụp toàn bộ màn hình Storage.")
    except Exception as e:
        print("❌ Lỗi:", e)
    finally:
        browser.close()
