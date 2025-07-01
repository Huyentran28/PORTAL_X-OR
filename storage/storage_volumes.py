# 📁 File: actions/volumes.py
import os

def do_volumes(page):
    print("🟠 Thao tác Volumes")
    os.makedirs("step_images/volumes", exist_ok=True)

    try:
        # Click menu "Storage"
        print("👉 Click vào menu Storage")
        page.click("span:has-text('Storage')")
        page.wait_for_timeout(1000)

        # Click menu "Volumes"
        print("👉 Click vào menu Volumes")
        page.click("span:has-text('Volumes')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Volumes")

        # Chụp danh sách volumes
        page.screenshot(path="step_images/volumes/01_volumes_list.png")

        # Mở form tạo volume
        print("📸 Mở form tạo volume")
        page.click('button:has-text("Create Volume")')
        page.wait_for_selector('input.MuiOutlinedInput-input', timeout=2000)
        page.screenshot(path="step_images/volumes/02_create_form.png")
        
    except Exception as e:
        print("❌ Lỗi trong thao tác Volumes:", e)
