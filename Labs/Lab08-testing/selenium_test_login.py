import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "file:///C:/Users/Thanh/NhapMonCongNghePhanMem/Labs/Lab08-testing/index.html"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

def test_login_success(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("admin@example.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "btnLogin").click()

    # Check alert
    alert = driver.switch_to.alert
    assert "Đăng nhập thành công" in alert.text
    alert.accept()

def test_login_fail_invalid_email(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "btnLogin").click()

    error_text = driver.find_element(By.ID, "errorMsg").text
    assert "email hợp lệ" in error_text.lower()

def test_login_empty(driver):
    driver.get(URL)
    driver.find_element(By.ID, "btnLogin").click()

    error_text = driver.find_element(By.ID, "errorMsg").text
    assert "không được để trống" in error_text.lower()
