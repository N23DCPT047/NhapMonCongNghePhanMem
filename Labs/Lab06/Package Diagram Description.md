## 📑 Mô tả Package Diagram – Hệ thống đặt phòng khách sạn
1. Package Người dùng

- Chứa các lớp đại diện cho tác nhân trực tiếp sử dụng hệ thống:

- Khách hàng (KhachHang): tạo tài khoản, đặt phòng, thanh toán.

- Nhân viên lễ tân (NhanVienLeTan): xử lý check-in/check-out, quản lý phiếu đặt.

- Quản lý khách sạn (QuanLyKhachSan): quản trị phòng, theo dõi báo cáo kinh doanh.

👉 Đây là nhóm lớp thuộc tầng sử dụng, tương tác trực tiếp với hệ thống.

2. Package Quản lý đặt phòng

- Xử lý logic cốt lõi liên quan đến booking:

- Phiếu đặt phòng (PhieuDatPhong): lưu thông tin đặt chỗ, ngày đến, ngày đi, tình trạng phiếu.

- Phòng (Phong): chứa thông tin phòng khách sạn (loại phòng, giá, tình trạng).

👉 Đây là trái tim của hệ thống, nơi mọi giao dịch và quản lý xoay quanh.

3. Package Thanh toán & Hóa đơn

Đảm nhận phần tài chính:

- Hóa đơn (HoaDon): phát hành cho khách khi hoàn tất thanh toán.

- Hệ thống thanh toán (HeThongThanhToan): trung gian xử lý giao dịch với ngân hàng, ví điện tử.

👉 Package này đảm bảo dòng tiền minh bạch và kết nối an toàn với hệ thống bên ngoài.

🔗 Quan hệ giữa các package

- Khách hàng tạo → Phiếu đặt phòng → gắn với Phòng.

- Sau khi hoàn tất, Khách hàng nhận Hóa đơn.

- Hóa đơn kết nối với Hệ thống thanh toán để xử lý giao dịch.

- Nhân viên lễ tân quản lý phiếu đặt phòng.

- Quản lý khách sạn quản trị thông tin phòng và trích xuất báo cáo từ hóa đơn.

👉 Nói ngắn gọn:

- Người dùng = đầu vào/ra của hệ thống.

- Quản lý đặt phòng = business logic.

- Thanh toán & Hóa đơn = xử lý nghiệp vụ tài chính.
