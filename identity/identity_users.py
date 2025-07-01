import os

def do_users(page):
    print("🟢 Thao tác Users")
    os.makedirs("step_images/users", exist_ok=True)

    try:
        # Click menu "Identity"
        # print("👉 Click vào menu Identity")
        # page.click("span:has-text('Identity')")
        page.wait_for_timeout(1000)

        # Click menu "Users"
        print("👉 Click vào menu Users")
        page.click("span:has-text('Users')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Users")

        # Chụp danh sách users
        page.screenshot(path="step_images/users/01_users_list.png")

        # Mở form tạo User
        print("📸 Mở form tạo User")
        page.click('button:has-text("Create User")')
        page.wait_for_selector('input.MuiOutlinedInput-input', timeout=2000)
        page.screenshot(path="step_images/users/02_create_form.png")
        page.wait_for_timeout(3000)

        # Đóng dialog
        page.click('div[role="dialog"] button:has-text("Cancel")')

    except Exception as e:
        print("❌ Lỗi trong thao tác Users:", e)
