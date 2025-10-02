
import pytest
from hotel_booking import add_booking, bookings

def setup_function():
    bookings.clear()  

def test_add_booking_success():
    result = add_booking("KH001", "P101", "2025-10-10", "2025-10-12")
    assert result["status"] == "success"
    assert len(bookings) == 1

def test_add_booking_missing_info():
    result = add_booking("", "P101", "2025-10-10", "2025-10-12")
    assert result["status"] == "error"
    assert "Thiếu thông tin" in result["message"]

def test_add_booking_invalid_date():
    result = add_booking("KH002", "P102", "2025-10-15", "2025-10-12")
    assert result["status"] == "error"
    assert "không hợp lệ" in result["message"]

def test_add_booking_room_conflict():
    add_booking("KH001", "P103", "2025-10-10", "2025-10-12")  
    result = add_booking("KH002", "P103", "2025-10-11", "2025-10-13")  
    assert result["status"] == "error"
    assert "Phòng đã được đặt" in result["message"]
