import os

def do_roles(page):
    print("🟢 Thao tác Roles")
    os.makedirs("step_images/roles", exist_ok=True)

    try:
        # Click menu "Identity"
        # print("👉 Click vào menu Identity")
        # page.click("span:has-text('Identity')")
        page.wait_for_timeout(1000)

        # Click menu "Roles"
        print("👉 Click vào menu Roles")
        page.click("span:has-text('Roles')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Roles")

        # Chụp danh sách roles
        page.screenshot(path="step_images/roles/01_roles_list.png")

    except Exception as e:
        print("❌ Lỗi trong thao tác Roles:", e)
