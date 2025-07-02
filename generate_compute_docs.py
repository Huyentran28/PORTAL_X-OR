import os
import logging

# Thiết lập logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Đường dẫn thư mục ảnh và thư mục lưu tài liệu Markdown
base_dir = "step_images"
output_dir = "doc"

# Danh sách các chức năng thuộc Compute
sections = {
    "instances": {
        "title": "Instances",
        "description": "Instances là các máy ảo (Virtual Machines - VMs) dùng để chạy ứng dụng hoặc dịch vụ trên nền tảng đám mây."
    },
    "snapshots": {
        "title": "Snapshots",
        "description": "Snapshots là bản sao lưu của instance tại một thời điểm cụ thể. Dùng để khôi phục hoặc tạo image mới khi cần."
    },
    "flavors": {
        "title": "Flavors",
        "description": "Flavors định nghĩa cấu hình phần cứng (CPU, RAM, ổ cứng) cho instance. Bạn cần chọn flavor phù hợp khi tạo máy ảo."
    },
    "images": {
        "title": "Images",
        "description": "Images là các bản cài đặt hệ điều hành (như Ubuntu, CentOS, Windows) hoặc template phần mềm dùng để tạo instance."
    },
    "keypairs": {
        "title": "Key Pairs",
        "description": "Key Pairs là cặp khóa bảo mật (public/private key) dùng để đăng nhập vào instance qua SSH. Bạn cần tạo và tải về khóa cá nhân."
    }
}

# Tạo thư mục đầu ra nếu chưa tồn tại
try:
    os.makedirs(output_dir, exist_ok=True)
    logging.info(f"✅ Thư mục đầu ra `{output_dir}` đã được tạo hoặc đã tồn tại.")
except Exception as e:
    logging.error(f"❌ Lỗi khi tạo thư mục {output_dir}: {e}")
    raise

# Tạo file tài liệu tổng quan (trang chính)
try:
    with open(os.path.join(output_dir, "compute-doc.md"), "w", encoding="utf-8") as main_file:
        main_file.write("# 🧭 Hướng dẫn sử dụng Compute\n\n")
        main_file.write("Chào mừng bạn đến với tài liệu hướng dẫn sử dụng Compute của hệ thống X-OR Stack.\n")
        main_file.write("Tài liệu này giúp bạn từng bước quản lý tài nguyên tính toán như: tạo máy ảo, sao lưu, cấu hình phần cứng, v.v...\n\n")

        main_file.write("## 📋 Danh sách chức năng\n\n")
        for key, info in sections.items():
            main_file.write(f"- [🔹 {info['title']}]({key}.md): {info['description']}\n")

        main_file.write("\n---\n")
        main_file.write("_Hãy chọn chức năng bạn muốn tìm hiểu từ danh sách trên._\n")
    logging.info("✅ Tạo file `compute-doc.md` thành công.")
except Exception as e:
    logging.error(f"❌ Lỗi khi tạo file compute-doc.md: {e}")
    raise

# Tạo tài liệu chi tiết cho từng chức năng
for key, info in sections.items():
    try:
        filename = os.path.join(output_dir, f"{key}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# 🔹 {info['title']}\n\n")
            f.write(f"## 📝 Giới thiệu\n{info['description']}\n\n")

            img_dir = os.path.join(base_dir, key)
            if os.path.isdir(img_dir):
                imgs = sorted([img for img in os.listdir(img_dir) if img.endswith(".png")])

                if imgs:
                    f.write("## 📸 Hướng dẫn từng bước\n")
                    for idx, img in enumerate(imgs, 1):
                        step_title = img.replace(".png", "").replace("_", " ").capitalize()
                        img_path = f"../{base_dir}/{key}/{img}"

                        f.write(f"\n### 🔸 Bước {idx}: {step_title}\n")
                        f.write(f"![{step_title}]({img_path})\n")
                        f.write(f"_👉 Mô tả: Đây là bước \"{step_title.lower()}\". Hãy đối chiếu hình ảnh và thực hiện đúng thao tác._\n")
                else:
                    f.write("> ⚠️ Không tìm thấy hình ảnh hướng dẫn trong thư mục.\n")
                    logging.warning(f"Không tìm thấy file PNG trong {img_dir}")
            else:
                f.write("> ⚠️ Thư mục hình ảnh chưa được tạo.\n")
                logging.warning(f"Thư mục {img_dir} không tồn tại.")

            # Thêm liên kết quay lại trang chính
            f.write("\n---\n[⬅️ Quay lại trang chính](compute-doc.md)\n")

        logging.info(f"✅ Tạo file {key}.md thành công với {len(imgs) if 'imgs' in locals() else 0} ảnh.")
    except Exception as e:
        logging.error(f"❌ Lỗi khi tạo file {key}.md: {e}")
        raise

logging.info("🎉 Hoàn tất quá trình tạo tài liệu hướng dẫn Compute.")
