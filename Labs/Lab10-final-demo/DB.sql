-- Tạo database
CREATE DATABASE HotelBookingSystem;
USE HotelBookingSystem;

-- Bảng Khách hàng
CREATE TABLE Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Bảng Phòng
CREATE TABLE Room (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(20) UNIQUE NOT NULL,
    type VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    status ENUM('available','booked','maintenance') DEFAULT 'available'
);

-- Bảng Đặt phòng
CREATE TABLE Booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    room_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    total_price DECIMAL(10,2),
    status ENUM('pending','confirmed','cancelled','completed') DEFAULT 'pending',
    CONSTRAINT fk_booking_customer FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    CONSTRAINT fk_booking_room FOREIGN KEY (room_id) REFERENCES Room(room_id)
);

-- Bảng Thanh toán
CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    method ENUM('cash','credit_card','debit_card','online') NOT NULL,
    payment_date DATE NOT NULL,
    status ENUM('pending','paid','failed') DEFAULT 'pending',
    CONSTRAINT fk_payment_booking FOREIGN KEY (booking_id) REFERENCES Booking(booking_id)
);

-- Bảng Nhân viên (quản lý / lễ tân)
CREATE TABLE Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role ENUM('admin','receptionist','manager') NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Thêm vài dữ liệu mẫu
INSERT INTO Customer (name,email,phone,username,password) VALUES
('ChongDangChiThanh','n23dcpt047@student.ptithcm.edu.vn','0912345678','userThanh','123456'),
('Tran Thi B','b@gmail.com','0987654321','userB','abcdef');

INSERT INTO Room (room_number,type,price,status) VALUES
('101','Single',300000,'available'),
('102','Double',500000,'available'),
('201','Suite',1200000,'maintenance');
