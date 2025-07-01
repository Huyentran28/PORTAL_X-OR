# 📁 File: network/network_floating_ips.py
import os

def do_floating_ips(page):
    print("🟠 Thao tác Floating IPs")
    os.makedirs("step_images/floating_ips", exist_ok=True)

    try:
        # Click menu "Network"
        # print("👉 Click vào menu Network")
        # page.click("span:has-text('Network')")
        page.wait_for_timeout(1000)

        # Click menu "Floating IPs"
        print("👉 Click vào menu Floating IPs")
        page.click("span:has-text('Floating IPs')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Floating IPs")

        # Chụp danh sách Floating IPs
        page.screenshot(path="step_images/floating_ips/01_floating_ips_list.png")

        # Mở form tạo Floating IP
        print("📸 Mở form tạo Floating IP")
        page.click('button:has-text("Allocate Floating IP")')
        page.wait_for_selector('input.MuiOutlinedInput-input', timeout=2000)
        page.screenshot(path="step_images/floating_ips/02_create_form.png")
        page.wait_for_timeout(3000)

        # Đóng dialog
        page.click('div[role="dialog"] button:has-text("Cancel")')

    except Exception as e:
        print("❌ Lỗi trong thao tác Floating IPs:", e)
