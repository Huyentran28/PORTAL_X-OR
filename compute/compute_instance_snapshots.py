# 📁 File: actions/snapshots.py
import os

def do_instance_snapshots(page):
    print("🟠 Thao tác Instance Snapshots")
    os.makedirs("step_images/snapshots", exist_ok=True)

    try:
        # Click menu "Compute"
        # print("👉 Click vào menu Compute")
        # page.click("span:has-text('Compute')")
        # page.wait_for_timeout(1000)

        # Click menu "Instance Snapshots"
        print("👉 Click vào menu Instance Snapshots")
        page.click("span:has-text('Instance Snapshots')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Instance Snapshots")

        # Chụp danh sách snapshots
        page.screenshot(path="step_images/snapshots/01_snapshots_list.png")

        # Mở form tạo snapshot
        print("📸 Mở form tạo snapshot")
        page.click('button:has-text("Create Instance Snapshot")')
        page.wait_for_selector('input.MuiOutlinedInput-input', timeout=5000)
        page.screenshot(path="step_images/snapshots/02_create_form.png")

        page.click('button[aria-label="close"]')


    except Exception as e:
        print("❌ Lỗi trong thao tác Instance Snapshots:", e)
