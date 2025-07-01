# compute/compute_images.py

import os

def do_images(page):
    print("🖼️ Thao tác Images")
    os.makedirs("step_images/images", exist_ok=True)
    print("👉 Click vào menu Images")
    page.click("span:has-text('Images')")
    page.wait_for_load_state("networkidle")
    page.wait_for_selector("h1:has-text('Images')")
    page.screenshot(path="step_images/images/01_images_list.png")

    # Click nút "Create Image"
    page.click('button:has-text("Create Image")')
    page.wait_for_timeout(1000)
    page.screenshot(path="step_images/images/02_create_form.png")

    page.wait_for_timeout(2000)
    page.screenshot(path="step_images/images/03_done.png")
