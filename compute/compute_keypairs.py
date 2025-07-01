import os

def do_keypairs(page):
    print("🔑 Thao tác Key Pairs")
    os.makedirs("step_images/keypairs", exist_ok=True)

    # Truy cập trang
    print("👉 Click vào menu Keypairs")
    page.click("span:has-text('Key Pairs')")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)  # Đợi thêm cho chắc
    page.screenshot(path="step_images/keypairs/01_list.png")

    # Nhấn nút "Create Key Pair"
    page.click('button:has-text("Create Key Pair")')
    page.wait_for_timeout(1000)  # Đợi form hiển thị

    # Chờ form hiển thị
    try:
        page.wait_for_selector('input[name="name"]', timeout=5000)
    except:
        print("❌ Không tìm thấy input name!")
        return

    page.screenshot(path="step_images/keypairs/02_form.png")

    # Nhấn nút Create
    try:
        page.click('button:has-text("Create")')
    except:
        page.click('button:has-text("Tạo")')

    page.wait_for_timeout(2000)
    page.screenshot(path="step_images/keypairs/03_done.png")

    print("✅ Đã thao tác và chụp ảnh xong Key Pairs")
