# 📁 File: network/network_security_groups.py
import os

def do_security_groups(page):
    print("🟠 Thao tác Security Groups")
    os.makedirs("step_images/security_groups", exist_ok=True)

    try:
        # Click menu "Network"
        # print("👉 Click vào menu Network")
        # page.click("span:has-text('Network')")
        page.wait_for_timeout(1000)

        # Click menu "Security Groups"
        print("👉 Click vào menu Security Groups")
        page.click("span:has-text('Security Groups')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Security Groups")

        # Chụp danh sách Security Groups
        page.screenshot(path="step_images/security_groups/01_security_groups_list.png")

        # Mở form tạo Security Group
        print("📸 Mở form tạo Security Group")
        page.click('button:has-text("Create Security Group")')
        page.wait_for_selector('input.MuiOutlinedInput-input', timeout=2000)
        page.screenshot(path="step_images/security_groups/02_create_form.png")
        page.wait_for_timeout(3000)

        # Đóng dialog
        page.click('div[role="dialog"] button:has-text("Cancel")')

    except Exception as e:
        print("❌ Lỗi trong thao tác Security Groups:", e)
