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

## 5. Quản lý source code (Git/GitHub)

### Khởi tạo & push repo
```bash
# clone repo hoặc tạo repo mới
git init
git add .
git commit -m "Initial commit: add UML + login form"

# kết nối với GitHub
git remote add origin https://github.com/N23DCPT047/hotel-login-demo.git](https://n23dcpt047.github.io/NhapMonCongNghePhanMem/
git branch -M main
git push -u origin main
