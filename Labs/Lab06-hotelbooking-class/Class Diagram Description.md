## 📑 Mô tả Class Diagram – Hệ thống đặt phòng khách sạn
1. Khách hàng (KhachHang)

*Thuộc tính:

  - maKH: Mã khách hàng (định danh duy nhất).

  - hoTen: Họ và tên khách hàng.

  - email: Địa chỉ email để đăng nhập, nhận thông tin đặt phòng.

  - soDienThoai: Liên lạc khi cần xác nhận booking.

  - diaChi: Địa chỉ liên hệ.

*Phương thức:

  - dangKyTaiKhoan(): Tạo tài khoản mới.

  - dangNhap(): Đăng nhập hệ thống.

  - datPhong(): Thực hiện đặt phòng, tạo phiếu đặt.

  - thanhToan(): Thanh toán và nhận hóa đơn.

2. Phòng (Phong)

*Thuộc tính:

  - maPhong: Số phòng hoặc ID phòng.

  - loaiPhong: Loại phòng (Standard, Deluxe, VIP...).

  - gia: Giá theo đêm.

  - tinhTrang: Trạng thái phòng (còn trống, đã đặt, đang sửa...).

*Phương thức:

  - capNhatTinhTrang(): Thay đổi trạng thái khi đặt/cancel/checkout.

3. Phiếu đặt phòng (PhieuDatPhong)

*Thuộc tính:

  - maPhieu: Mã phiếu đặt phòng.

  - ngayDat: Ngày khách hàng thực hiện đặt.

  - ngayNhan: Ngày khách check-in.

  - ngayTra: Ngày khách check-out.

*Phương thức:

  - taoPhieu(): Khởi tạo phiếu mới khi khách đặt phòng.

  - huyPhieu(): Hủy phiếu khi khách không sử dụng.

4. Hóa đơn (HoaDon)

*Thuộc tính:

  - maHoaDon: Mã hóa đơn.

  - ngayLap: Ngày phát hành hóa đơn.

  - tongTien: Tổng chi phí khách phải trả.

*Phương thức:

  - inHoaDon(): Xuất hóa đơn thanh toán.

5. Nhân viên lễ tân (NhanVienLeTan)

*Thuộc tính:

  - maNV: Mã nhân viên.

  - hoTen: Tên nhân viên.

  - caLamViec: Ca trực (sáng/chiều/tối).

*Phương thức:

  - checkIn(): Xác nhận khách đến nhận phòng.

  - checkOut(): Xác nhận khách trả phòng.

  - quanLyPhieuDat(): Theo dõi, chỉnh sửa, cập nhật phiếu đặt phòng.

6. Quản lý khách sạn (QuanLyKhachSan)

*Thuộc tính:

  - maQL: Mã quản lý.

  - hoTen: Tên quản lý.

*Phương thức:

  - quanLyPhong(): Thêm/xóa/cập nhật thông tin phòng.

  - xemBaoCao(): Trích xuất báo cáo tình hình kinh doanh.

7. Hệ thống thanh toán (HeThongThanhToan)

*Thuộc tính:

  - tenNganHang: Ngân hàng xử lý giao dịch.

  - soTaiKhoan: Tài khoản nhận tiền.

*Phương thức:

  - xuLyThanhToan(): Thực hiện giao dịch thanh toán online.
