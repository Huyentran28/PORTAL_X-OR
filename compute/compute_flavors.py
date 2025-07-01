# compute/compute_flavors.py
import os

def do_flavors(page):
    print("🔵 Thao tác Flavors")
    os.makedirs("step_images/flavors", exist_ok=True)

    # Truy cập trang Flavors
          # Click vào "Instances"
    print("👉 Click vào menu Flavors")
    page.click("span:has-text('Flavors')")
    page.wait_for_load_state("networkidle")
    page.wait_for_selector("h1:has-text('Flavors')")
    page.screenshot(path="step_images/flavors/01_list.png")

    print("✅ Đã thao tác và chụp ảnh xong Flavors")
