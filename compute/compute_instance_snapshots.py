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

        # Điền tên snapshot
        page.fill('input.MuiOutlinedInput-input', "demo-snap")
        page.wait_for_timeout(500)
        page.screenshot(path="step_images/snapshots/03_filled_form.png")

        # Bấm Create
        page.click('div[role="dialog"] button:has-text("Create")', force=True)
        page.wait_for_timeout(2000)
        page.screenshot(path="step_images/snapshots/04_created.png")
        print("✅ Đã thao tác và chụp ảnh xong Instance Snapshots")
        page.click('button[aria-label="close"]')


    except Exception as e:
        print("❌ Lỗi trong thao tác Instance Snapshots:", e)
