# Hệ thống đặt phòng khách sạn – Demo

## 🎯 Mục tiêu
- Hoàn thiện quy trình phần mềm từ **thiết kế** → **lập trình** → **triển khai**.  
- Tích hợp các artifacts: Use Case Diagram, Sequence Diagram, giao diện Front-end (Form Login).  
- Quản lý version bằng Git & GitHub.

---

## 1. Use Case Diagram
**Mô tả:** Hệ thống quản lý đặt phòng khách sạn gồm 3 tác nhân chính:
- **Khách hàng**: tìm kiếm, đặt phòng, thanh toán.  
- **Nhân viên lễ tân**: check-in, check-out, quản lý booking.  
- **Quản lý khách sạn**: quản lý phòng, xem báo cáo.  
- **Hệ thống thanh toán**: tích hợp xử lý giao dịch.

![Use Case Diagram](../Lab02/Use%20Case%20Diagram.jpg)


---

## 2. Sequence Diagram
**Mô tả:** Quy trình “Đặt phòng và Thanh toán trực tuyến”.

![Sequence Diagram](../Lab03/SQ%20Diagram.jpg)



---

## 3. Giao diện Form Login (Front-end)
**File:** `index.html`  
**Ngôn ngữ:** HTML, CSS, JavaScript  
**Tính năng:**
- Nhập `username` (dạng email) và `password`.  
- Nút **Login** (giả lập xác thực) và **Cancel** (reset form).  
- Tùy chọn **Remember me** (lưu username vào `localStorage`).  
- Validation cơ bản bằng JavaScript.  

📂 Source code: [index.html](../Lab04/index.html)

Demo trên GitHub Pages:  
👉 [https://N23DCPT047.github.io/NhapMonCongNghePhanMem/](https://N23DCPT047.github.io/NhapMonCongNghePhanMem/)

---

## 4. Quy trình làm việc
1. **Thiết kế**
   - Vẽ Use Case.  
   - Vẽ Sequence Diagram cho quy trình nghiệp vụ.  

2. **Phát triển**
   - Code Form Login (`index.html`).  
   - Test local bằng trình duyệt.  

3. **Tích hợp**
   - Gom artifacts vào repo GitHub.  
 

4. **Triển khai**
   - Dùng GitHub Pages để chạy demo Form Login.  

---

## 5. Khởi tạo DB


CREATE TABLE KhachHang (
    maKH INT PRIMARY KEY AUTO_INCREMENT,
    hoTen VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    soDT VARCHAR(15)
);

CREATE TABLE KhachSan (
    maKS INT PRIMARY KEY AUTO_INCREMENT,
    tenKS VARCHAR(100),
    diaChi VARCHAR(255)
);

CREATE TABLE Phong (
    maPhong INT PRIMARY KEY AUTO_INCREMENT,
    soPhong VARCHAR(20),
    loaiPhong VARCHAR(50),
    gia DECIMAL(10,2),
    tinhTrang VARCHAR(50),
    maKS INT,
    FOREIGN KEY (maKS) REFERENCES KhachSan(maKS)
);

CREATE TABLE DatPhong (
    maDP INT PRIMARY KEY AUTO_INCREMENT,
    ngayDat DATE,
    ngayNhan DATE,
    ngayTra DATE,
    maKH INT,
    maPhong INT,
    FOREIGN KEY (maKH) REFERENCES KhachHang(maKH),
    FOREIGN KEY (maPhong) REFERENCES Phong(maPhong)
);

CREATE TABLE HoaDon (
    maHD INT PRIMARY KEY AUTO_INCREMENT,
    ngayLap DATE,
    tongTien DECIMAL(10,2),
    maDP INT,
    FOREIGN KEY (maDP) REFERENCES DatPhong(maDP)
);


## 6. Kết quả test và sprint report
![Kết quả test Selenium](../Lab10-final-demo/selenium_pass.jpg)
![Kết quả Unit Test module](../Lab10-final-demo/unit_test.png)
![Backlog report](../Lab09/Evidence/backlog1.jpg)
![Board report](../Lab09/Evidence/board.jpg)
![Burndown report](../Lab09/Evidence/burndown.jpg)

## 7. Kế luận và định hướng mở rộng

### 7.1 Kết luận

Hệ thống đặt phòng khách sạn đã được xây dựng và kiểm thử thành công với các chức năng cơ bản:

Người dùng có thể đặt phòng, và quản lý thông tin đặt phòng trực tuyến.

Quản trị viên có thể quản lý khách sạn, phòng, và khách hàng một cách dễ dàng.

Cấu trúc cơ sở dữ liệu rõ ràng, hỗ trợ mở rộng về lâu dài.

Quy trình phát triển theo sprint đảm bảo tiến độ và chất lượng sản phẩm.

Kết quả cho thấy hệ thống đã đáp ứng đúng yêu cầu đặt ra, giảm thiểu thời gian đặt phòng truyền thống, nâng cao trải nghiệm người dùng và hiệu quả vận hành của khách sạn.

### 7.2 Định hướng mở rộng

Để hoàn thiện và nâng cao giá trị sử dụng, hệ thống có thể được mở rộng theo các hướng sau:

Tìm kiếm phòng theo tên, bộ lọc (vị trí, đánh giá, giá tiền,...)

Ứng dụng di động (Mobile App) trên iOS/Android để đặt phòng mọi lúc mọi nơi.

Hệ thống đánh giá & phản hồi để khách hàng chấm điểm, nhận xét khách sạn/phòng.

Tích hợp AI gợi ý phòng phù hợp theo nhu cầu, lịch sử đặt phòng.

Tích hợp bản đồ & gợi ý du lịch để người dùng xem vị trí khách sạn và các dịch vụ xung quanh.
