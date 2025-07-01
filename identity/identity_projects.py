import os

def do_projects(page):
    print("🟢 Thao tác Projects")
    os.makedirs("step_images/projects", exist_ok=True)

    try:
        # Click menu "Identity"
        print("👉 Click vào menu Identity")
        page.click("span:has-text('Identity')")
        page.wait_for_timeout(1000)

        # Đảm bảo menu Projects hiện ra
        print("👉 Đợi menu Projects hiển thị")
        # project_item = page.locator("span:has-text('Projects')")
        # project_item.wait_for(state="visible", timeout=2000)

        # Click menu "Projects"
        print("👉 Click vào menu Projects")
        page.click("span:has-text('Projects')")
        page.wait_for_timeout(2000)
        print("✅ Đã mở trang Projects")

        # Chụp danh sách projects
        page.screenshot(path="step_images/projects/01_projects_list.png")

        # Mở form tạo Project
        print("📸 Mở form tạo Project")
        page.click('button:has-text("Create Project")')
        page.wait_for_selector('input.MuiOutlinedInput-input', timeout=2000)
        page.screenshot(path="step_images/projects/02_create_form.png")
        page.wait_for_timeout(3000)

        # Đóng dialog
        page.click('div[role="dialog"] button:has-text("Cancel")')

    except Exception as e:
        print("❌ Lỗi trong thao tác Projects:", e)
