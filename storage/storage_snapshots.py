import os

def do_snapshots(page):
    print("🟢 Thao tác Snapshots")
    os.makedirs("step_images/snapshots", exist_ok=True)

    try:
        # Click menu "Storage"
        # print("👉 Click vào menu Storage")
        # page.click("span:has-text('Storage')")
        page.wait_for_timeout(1000)

        # Click menu "Snapshots"
        print("👉 Click vào menu Snapshots")
        page.click("span:has-text('Snapshots')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Snapshots")

        # Chụp ảnh danh sách Snapshots
        page.screenshot(path="step_images/snapshots/01_snapshots_list.png")

    except Exception as e:
        print("❌ Lỗi trong thao tác Snapshots:", e)
