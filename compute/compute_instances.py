# 📁 File: actions/instances.py
import os

def do_instances(page):
    print("🟢 Bắt đầu thao tác Instances")
    os.makedirs("step_images/instances", exist_ok=True)

    try:
        print("✅ Đã chuyển đến trang Instances")

        # Click vào "Compute"
        print("👉 Click vào menu Compute")
        page.click("span:has-text('Compute')")
        page.wait_for_timeout(1000)

        # Click vào "Instances"
        print("👉 Click vào menu Instances")
        page.click("span:has-text('Instances')")
        page.wait_for_load_state("networkidle")

        # (Các bước tiếp theo – tạm thời đang comment)
        page.wait_for_selector("span:has-text('Instances')", timeout=15000)
        page.screenshot(path="step_images/instances/01_instances_list.png")

        page.click('button.MuiButton-containedPrimary')
        page.wait_for_selector('input[name="name"]')
        page.screenshot(path="step_images/instances/02_create_form.png")

        page.fill('input[name="name"]', "h1")
        page.screenshot(path="step_images/instances/03_filled_form.png")

        page.click('button:has-text("Next")')
        page.wait_for_timeout(2000)
        page.screenshot(path="step_images/instances/04_done.png")
        page.wait_for_timeout(3000)


    except Exception as e:
        print("❌ Lỗi trong thao tác Instances:", e)
