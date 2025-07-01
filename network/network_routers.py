# 📁 File: network/network_routers.py
import os

def do_routers(page):
    print("🟠 Thao tác Routers")
    os.makedirs("step_images/routers", exist_ok=True)

    try:
        # Click menu "Network"
        # print("👉 Click vào menu Network")
        # page.click("span:has-text('Network')")
        page.wait_for_timeout(1000)

        # Click menu "Routers"
        print("👉 Click vào menu Routers")
        page.click("span:has-text('Routers')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Routers")

        # Chụp danh sách Routers
        page.screenshot(path="step_images/routers/01_routers_list.png")

        # Mở form tạo Router
        print("📸 Mở form tạo Router")
        page.click('button:has-text("Create Router")')
        page.wait_for_selector('input.MuiOutlinedInput-input', timeout=2000)
        page.screenshot(path="step_images/routers/02_create_form.png")

        # Đóng dialog
        page.wait_for_timeout(1000)
        page.click('div[role="dialog"] button:has-text("Cancel")')

    except Exception as e:
        print("❌ Lỗi trong thao tác Routers:", e)
