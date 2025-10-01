CREATE DATABASE HotelDB;
USE HotelDB;

CREATE TABLE KhachHang (
  maKH INT AUTO_INCREMENT PRIMARY KEY,
  hoTen VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  soDienThoai VARCHAR(15),
  diaChi VARCHAR(200)
);

CREATE TABLE Phong (
  maPhong INT AUTO_INCREMENT PRIMARY KEY,
  loaiPhong VARCHAR(50),
  gia DECIMAL(10,2),
  tinhTrang VARCHAR(20)
);

CREATE TABLE PhieuDatPhong (
  maPhieu INT AUTO_INCREMENT PRIMARY KEY,
  maKH INT,
  maPhong INT,
  ngayDat DATE,
  ngayNhan DATE,
  ngayTra DATE,
  FOREIGN KEY (maKH) REFERENCES KhachHang(maKH),
  FOREIGN KEY (maPhong) REFERENCES Phong(maPhong)
);

CREATE TABLE HoaDon (
  maHoaDon INT AUTO_INCREMENT PRIMARY KEY,
  maPhieu INT,
  ngayLap DATE,
  tongTien DECIMAL(10,2),
  FOREIGN KEY (maPhieu) REFERENCES PhieuDatPhong(maPhieu)
);
