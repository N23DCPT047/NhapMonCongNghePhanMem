import mysql.connector
from datetime import date

# ===== CONFIG DB =====
config = {
    "host": "localhost",
    "user": "root",        # đổi user nếu khác
    "password": "",        # đổi password nếu có
    "database": "HotelDB"
}

# ===== KẾT NỐI DB =====
def get_conn():
    return mysql.connector.connect(**config)

# ===== CRUD DEMO =====
def them_khachhang(hoTen, email, soDienThoai, diaChi):
    conn = get_conn()
    cur = conn.cursor()
    sql = "INSERT INTO KhachHang (hoTen, email, soDienThoai, diaChi) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (hoTen, email, soDienThoai, diaChi))
    conn.commit()
    conn.close()
    print("✅ Đã thêm khách hàng:", hoTen)

def xem_khachhang():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM KhachHang")
    for row in cur.fetchall():
        print(row)
    conn.close()

def them_phong(loaiPhong, gia, tinhTrang="Trống"):
    conn = get_conn()
    cur = conn.cursor()
    sql = "INSERT INTO Phong (loaiPhong, gia, tinhTrang) VALUES (%s, %s, %s)"
    cur.execute(sql, (loaiPhong, gia, tinhTrang))
    conn.commit()
    conn.close()
    print("✅ Đã thêm phòng:", loaiPhong)

def dat_phong(maKH, maPhong, ngayNhan, ngayTra):
    conn = get_conn()
    cur = conn.cursor()
    sql = """INSERT INTO PhieuDatPhong (maKH, maPhong, ngayDat, ngayNhan, ngayTra)
             VALUES (%s, %s, %s, %s, %s)"""
    cur.execute(sql, (maKH, maPhong, date.today(), ngayNhan, ngayTra))
    conn.commit()
    conn.close()
    print("✅ Đã đặt phòng cho khách:", maKH)

def lap_hoadon(maPhieu, tongTien):
    conn = get_conn()
    cur = conn.cursor()
    sql = "INSERT INTO HoaDon (maPhieu, ngayLap, tongTien) VALUES (%s, %s, %s)"
    cur.execute(sql, (maPhieu, date.today(), tongTien))
    conn.commit()
    conn.close()
    print("✅ Đã lập hóa đơn cho phiếu:", maPhieu)

# ===== DEMO =====
if __name__ == "__main__":
    # Thêm dữ liệu mẫu
    them_khachhang("Nguyen Van A", "a@gmail.com", "0901234567", "Ha Noi")
    xem_khachhang()
    them_phong("Deluxe", 500000)
    dat_phong(1, 1, "2025-10-05", "2025-10-07")
    lap_hoadon(1, 1000000)
