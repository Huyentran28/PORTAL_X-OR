# 📁 File: network/network_ports.py
import os

def do_ports(page):
    print("🟠 Thao tác Ports")
    os.makedirs("step_images/ports", exist_ok=True)

    try:
        # Mở menu cha "Network" nếu chưa mở
        # print("👉 Click vào menu Network")
        # page.click("span:has-text('Network')")
        page.wait_for_timeout(1000)

        # Click menu con "Ports"
        print("👉 Click vào menu Ports")
        page.click("span:has-text('Ports')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Ports")

        # Chụp danh sách Ports
        page.screenshot(path="step_images/ports/01_ports_list.png")

        # Mở form tạo Port
        print("📸 Mở form tạo Port")
        page.click('button:has-text("Create Port")')
        page.wait_for_selector('input.MuiOutlinedInput-input', timeout=5000)
        page.screenshot(path="step_images/ports/02_create_form.png")
        page.click('div[role="dialog"] button:has-text("Cancel")')
    except Exception as e:
        print("❌ Lỗi trong thao tác Ports:", e)
