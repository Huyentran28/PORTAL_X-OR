import os

docs_path = "docs/identity"
os.makedirs(docs_path, exist_ok=True)

# --- Projects ---
with open(f"{docs_path}/projects.md", "w", encoding="utf-8") as f:
    f.write("""
# Quản lý Projects (Dự án)

## Giới thiệu
Chức năng **Projects** trong module **Identity** cho phép tạo các dự án để tổ chức và phân quyền tài nguyên cho người dùng.

## Các bước thao tác

### 1. Truy cập Projects
- Từ menu chính chọn `Identity > Projects`.
- Giao diện hiển thị danh sách các project hiện có.

![Danh sách Projects](../../step_images/projects/01_projects_list.png)

### 2. Tạo Project mới
- Nhấn nút `Create Project`.
- Nhập:
  - **Name**: project-demo
  - **Description**: Demo project for testing
- Bấm `Create`.

![Form tạo Project](../../step_images/projects/02_create_form.png)
![Form đã điền](../../step_images/projects/03_filled_form.png)

### 3. Project được tạo thành công
![Tạo thành công](../../step_images/projects/04_created.png)

## Đường dẫn thao tác
`https://portal.stack-dev.x-or.cloud/identity/projects`
    """.strip())

# --- Users ---
with open(f"{docs_path}/users.md", "w", encoding="utf-8") as f:
    f.write("""
# Quản lý Users (Người dùng)

## Giới thiệu
Chức năng **Users** trong module **Identity** cho phép tạo người dùng mới và phân quyền sử dụng tài nguyên.

## Các bước thao tác

### 1. Truy cập Users
- Từ menu chính chọn `Identity > Users`.
- Giao diện hiển thị danh sách người dùng hiện có.

![Danh sách Users](../../step_images/users/01_users_list.png)

### 2. Tạo User mới
- Nhấn `Create User`.
- Nhập:
  - **Username**: demo-user
  - **Email**: demo@example.com
  - **Password** và xác nhận: `123456`
- Bấm `Create`.

![Form tạo User](../../step_images/users/02_create_form.png)
![Form đã điền](../../step_images/users/03_filled_form.png)

### 3. User được tạo thành công
![Tạo thành công](../../step_images/users/04_created.png)

## Đường dẫn thao tác
`https://portal.stack-dev.x-or.cloud/identity/users`
    """.strip())

# --- Roles ---
with open(f"{docs_path}/roles.md", "w", encoding="utf-8") as f:
    f.write("""
# Quản lý Roles (Vai trò)

## Giới thiệu
Chức năng **Roles** trong module **Identity** cho phép định nghĩa các vai trò và quyền hạn để phân cho người dùng theo từng dự án.

## Các bước thao tác

### 1. Truy cập Roles
- Từ menu chính chọn `Identity > Roles`.
- Giao diện hiển thị danh sách các vai trò.

![Danh sách Roles](../../step_images/roles/01_roles_list.png)

### 2. Tạo Role mới
- Nhấn nút `Create Role`.
- Nhập:
  - **Name**: role-demo
  - **Description**: Demo role for testing
- Bấm `Create`.

![Form tạo Role](../../step_images/roles/02_create_form.png)
![Form đã điền](../../step_images/roles/03_filled_form.png)

### 3. Role được tạo thành công
![Tạo thành công](../../step_images/roles/04_created.png)

## Đường dẫn thao tác
`https://portal.stack-dev.x-or.cloud/identity/roles`
    """.strip())
