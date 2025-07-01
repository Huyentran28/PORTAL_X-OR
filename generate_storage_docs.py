import os

storage_dir = "docs/storage"
os.makedirs(storage_dir, exist_ok=True)

with open(f"{storage_dir}/volumes.md", "w", encoding="utf-8") as f:
    f.write("""
# Quản lý Volumes (Ổ đĩa lưu trữ)

## Giới thiệu
Chức năng **Volumes** trong module **Storage** cho phép người dùng tạo, chỉnh sửa, gắn kết và xóa các ổ đĩa lưu trữ (volume) cho các máy ảo (instance).

## Các bước thao tác

### 1. Truy cập Volumes
- Từ menu chính chọn `Storage > Volumes`.
- Giao diện sẽ hiển thị danh sách các volumes đang có.

![Volumes List](../../step_images/volumes/01_volumes_list.png)

### 2. Tạo mới Volume
- Bấm nút `Create Volume`.
- Nhập thông tin:
  - **Name**: Tên volume
  - **Size (GB)**: Dung lượng ổ đĩa
  - **Description** (tuỳ chọn)
  - **Availability Zone**: Vùng khả dụng
- Bấm `Create` để hoàn tất.

![Form tạo Volume](../../step_images/volumes/02_create_form.png)

## Lưu ý
- Volume đang được gắn vào Instance thì không thể xóa.
- Có thể tạo snapshot từ volume để sao lưu.

## Đường dẫn thao tác
`https://portal.stack-dev.x-or.cloud/storage/volumes`
    """.strip())


import os

storage_dir = "docs/storage"
os.makedirs(storage_dir, exist_ok=True)

with open(f"{storage_dir}/snapshots.md", "w", encoding="utf-8") as f:
    f.write("""
# Quản lý Snapshots (Sao lưu Volume)

## Giới thiệu
Chức năng **Snapshots** trong module **Storage** cho phép người dùng tạo bản sao lưu (snapshot) của các ổ đĩa (volume) để khôi phục khi cần.

## Các bước thao tác

### 1. Truy cập Snapshots
- Từ menu chính chọn `Storage > Snapshots`.
- Giao diện sẽ hiển thị danh sách snapshot đang có.

![Danh sách Snapshots](../../step_images/snapshots/01_snapshots_list.png)

## Lưu ý
- Snapshot chỉ tạo được khi volume không bị lock hoặc đang ở trạng thái phù hợp.
- Có thể dùng snapshot để tạo volume mới.

## Đường dẫn thao tác
`https://portal.stack-dev.x-or.cloud/storage/snapshots`
    """.strip())
