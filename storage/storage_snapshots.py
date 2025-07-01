import os

def do_snapshots(page):
    print("🟠 Đang chụp ảnh màn hình Snapshots")
    os.makedirs("step_images/snapshots", exist_ok=True)

    try:
        # Đợi đến khi chữ Snapshots xuất hiện trên trang (không cần h1)
        page.wait_for_selector(":text('Snapshots')", timeout=10000)

        # Chụp ảnh màn hình
        page.screenshot(path="step_images/snapshots/01_snapshots_list.png")
        print("✅ Đã chụp ảnh danh sách Snapshots")

    except Exception as e:
        print("❌ Lỗi thao tác Snapshots:", e)
