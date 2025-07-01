import os

docs_path = "docs/network"
os.makedirs(docs_path, exist_ok=True)

# Nội dung tài liệu Networks
with open(f"{docs_path}/networks.md", "w", encoding="utf-8") as f:
    f.write("""
# Quản lý Networks (Mạng nội bộ)

## Giới thiệu
Chức năng **Networks** trong module **Network** cho phép người dùng tạo và quản lý các mạng nội bộ (private networks) dùng để kết nối giữa các máy ảo.

## Các bước thao tác

### 1. Truy cập Networks
- Từ menu chính chọn `Network > Networks`.
- Giao diện hiển thị danh sách các mạng hiện có.

![Danh sách Networks](../../step_images/networks/01_networks_list.png)

### 2. Tạo Network mới
- Nhấn nút `Create Network`.
- Nhập thông tin:
  - **Name**: Tên mạng (ví dụ: `network-demo`)
  - **CIDR**: Dải mạng, ví dụ `192.168.100.0/24`
  - **Gateway IP**: IP cổng, ví dụ `192.168.100.1`
- Bấm `Create`.

![Form tạo Network](../../step_images/networks/02_create_form.png)
![Form đã điền](../../step_images/networks/03_filled_form.png)

### 3. Network đã được tạo thành công
![Tạo thành công](../../step_images/networks/04_created.png)

## Ghi chú
- CIDR và Gateway IP cần không trùng với các mạng đang có.
- Sau khi tạo có thể dùng để gán cho Instance hoặc Router.

## Đường dẫn thao tác
`https://portal.stack-dev.x-or.cloud/network/networks`
    """.strip())

# Nội dung tài liệu Ports
with open(f"{docs_path}/ports.md", "w", encoding="utf-8") as f:
    f.write("""
# Quản lý Ports (Cổng mạng)

## Giới thiệu
Chức năng **Ports** trong module **Network** cho phép tạo và quản lý các cổng mạng (port) kết nối giữa instance và network.

## Các bước thao tác

### 1. Truy cập Ports
- Từ menu chính chọn `Network > Ports`.
- Giao diện hiển thị danh sách các port hiện có.

![Danh sách Ports](../../step_images/ports/01_ports_list.png)

### 2. Tạo Port mới
- Nhấn nút `Create Port`.
- Nhập thông tin:
  - **Name**: Tên port (ví dụ: `port-demo`)
  - **Network**: Chọn mạng kết nối (ví dụ: `network-demo`)
- Bấm `Create`.

![Form tạo Port](../../step_images/ports/02_create_form.png)
![Form đã điền](../../step_images/ports/03_filled_form.png)

### 3. Port đã được tạo thành công
![Tạo thành công](../../step_images/ports/04_created.png)

## Ghi chú
- Mỗi port đại diện cho một interface mạng.
- Có thể gắn port này vào instance hoặc router.

## Đường dẫn thao tác
`https://portal.stack-dev.x-or.cloud/network/ports`
    """.strip())
# Nội dung tài liệu Routers
with open(f"{docs_path}/routers.md", "w", encoding="utf-8") as f:
    f.write("""
# Quản lý Routers (Bộ định tuyến)

## Giới thiệu
Chức năng **Routers** trong module **Network** cho phép định tuyến lưu lượng giữa các mạng nội bộ và internet/public network.

## Các bước thao tác

### 1. Truy cập Routers
- Từ menu chính chọn `Network > Routers`.
- Giao diện hiển thị danh sách các router hiện có.

![Danh sách Routers](../../step_images/routers/01_routers_list.png)

### 2. Tạo Router mới
- Nhấn nút `Create Router`.
- Nhập:
  - **Name**: Tên router (ví dụ: `router-demo`)
  - **External Gateway**: Chọn mạng ngoài (nếu có)
- Bấm `Create`.

![Form tạo Router](../../step_images/routers/02_create_form.png)
![Form đã điền](../../step_images/routers/03_filled_form.png)

### 3. Router đã được tạo thành công
![Tạo thành công](../../step_images/routers/04_created.png)

## Ghi chú
- Có thể gán router cho một network để kết nối Internet.
- Phải có mạng ngoài để gán Gateway.

## Đường dẫn thao tác
`https://portal.stack-dev.x-or.cloud/network/routers`
    """.strip())

# Nội dung tài liệu Floating IPs
with open(f"{docs_path}/floating_ips.md", "w", encoding="utf-8") as f:
    f.write("""
# Quản lý Floating IPs (IP công cộng)

## Giới thiệu
**Floating IP** là địa chỉ IP công cộng dùng để ánh xạ vào máy ảo (instance) đang chạy trong private network.

## Các bước thao tác

### 1. Truy cập Floating IPs
- Từ menu chính chọn `Network > Floating IPs`.
- Giao diện hiển thị danh sách IP hiện có.

![Danh sách Floating IPs](../../step_images/floating_ips/01_floating_ips_list.png)

### 2. Cấp phát Floating IP
- Nhấn `Allocate Floating IP`.
- Chọn:
  - **Pool**: Mạng public
            
- Bấm `Allocate`.

![Form cấp IP](../../step_images/floating_ips/02_allocate_form.png)


### 3. Gán Floating IP vào Instance
- Chọn Floating IP vừa tạo → `Associate`.
- Chọn instance/port cần gán.


## Ghi chú
- Mỗi IP chỉ gán được cho 1 port tại 1 thời điểm.
- Gán IP giúp instance truy cập Internet hoặc được SSH từ ngoài.

## Đường dẫn thao tác
`https://portal.stack-dev.x-or.cloud/network/floating_ips`
    """.strip())

# Nội dung tài liệu Security Groups
with open(f"{docs_path}/security_groups.md", "w", encoding="utf-8") as f:
    f.write("""
# Quản lý Security Groups (Nhóm bảo mật)

## Giới thiệu
**Security Groups** là tập hợp các luật firewall dùng để giới hạn truy cập vào instance (VD: cho phép SSH, HTTP...).

## Các bước thao tác

### 1. Truy cập Security Groups
- Từ menu chính chọn `Network > Security Groups`.
- Giao diện hiển thị danh sách các nhóm bảo mật.

![Danh sách Security Groups](../../step_images/security_groups/01_security_groups_list.png)

### 2. Tạo Security Group mới
- Nhấn `Create Security Group`.
- Nhập tên, mô tả → Bấm `Create`.

![Tạo nhóm bảo mật](../../step_images/security_groups/02_create_group.png)

### 3. Thêm luật cho Security Group
- Click vào Security Group → Tab `Rules`.
- Nhấn `Add Rule` → Chọn loại:
  - Ví dụ: **Ingress - TCP - 22 - 0.0.0.0/0** (cho phép SSH)
- Bấm `Add`.

![Thêm rule](../../step_images/security_groups/03_add_rule.png)

## Ghi chú
- Cần mở đúng cổng để máy ảo có thể SSH, HTTP hoặc HTTPS.
- Có thể tạo nhiều Security Group và gán cho từng Instance.

## Đường dẫn thao tác
`https://portal.stack-dev.x-or.cloud/network/security_groups`
    """.strip())
