from playwright.sync_api import sync_playwright
from compute.compute_login import login
from identity.identity_projects import do_projects
from identity.identity_users import do_users
from identity.identity_roles import do_roles

USERNAME = "customer@x-or.cloud"
PASSWORD = "123zXc_-"
TARGET_URL = "https://portal.stack-dev.x-or.cloud/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context()
    page = context.new_page()

    try:
        login(page, USERNAME, PASSWORD, TARGET_URL)
        do_projects(page)
        do_users(page)
        do_roles(page)
        print("✅ Đã hoàn tất chụp toàn bộ màn hình Identity.")
    except Exception as e:
        print("❌ Lỗi:", e)
    finally:
        browser.close()
