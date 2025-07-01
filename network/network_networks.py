# 📁 File: network/network_networks.py
import os

def do_networks(page):
    print("🟠 Thao tác Network")
    os.makedirs("step_images/network", exist_ok=True)

    try:
        # Click menu "Network"
        print("👉 Click vào menu Network")
        page.click("span:has-text('Network')")
        page.wait_for_timeout(1000)

        # Click menu "Networks"
        print("👉 Click vào menu Networks")
        page.click("span:has-text('Networks')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Networks")

        # Chụp danh sách networks
        page.screenshot(path="step_images/networks/01_networks_list.png")

        # Mở form tạo network
        print("📸 Mở form tạo Network")
        page.click('button:has-text("Create Network")')
        page.wait_for_selector('input.MuiOutlinedInput-input', timeout=2000)
        page.screenshot(path="step_images/networks/02_create_form.png")
        page.wait_for_timeout(3000)
        page.click('div[role="dialog"] button:has-text("Cancel")')


    except Exception as e:
        print("❌ Lỗi trong thao tác Networks:", e)
