import os

base_dir = "step_images"
output_dir = "doc"

sections = {
    "instances": "Instances",
    "snapshots": "Snapshots",
    "flavors": "Flavors",
    "images": "Images",
    "keypairs": "Key Pairs"
}

os.makedirs(output_dir, exist_ok=True)

# Tạo file trang chính
with open(f"{output_dir}/compute-doc.md", "w", encoding="utf-8") as main:
    main.write("# 🧭 Tài liệu Hướng dẫn sử dụng Compute\n\n")
    main.write("## 📌 Danh sách chức năng:\n\n")
    for key, title in sections.items():
        main.write(f"- [🔹 {title}]({key}.md)\n")
    main.write("\n---\n")

# Tạo file riêng cho từng chức năng
for key, title in sections.items():
    with open(f"{output_dir}/{key}.md", "w", encoding="utf-8") as f:
        f.write(f"# 🔹 {title}\n\n")
        img_dir = os.path.join(base_dir, key)

        if os.path.isdir(img_dir):
            imgs = sorted(os.listdir(img_dir))
            for img in imgs:
                if img.endswith(".png"):
                    step = img.replace(".png", "").replace("_", " ").capitalize()
                    img_path = f"../{base_dir}/{key}/{img}"
                    f.write(f"## {step}\n")
                    f.write(f"![{step}]({img_path})\n\n")
        else:
            f.write("_Không tìm thấy hình ảnh._\n\n")

        f.write("---\n")
        f.write("[⬅️ Quay lại trang chính](compute-doc.md)\n")
