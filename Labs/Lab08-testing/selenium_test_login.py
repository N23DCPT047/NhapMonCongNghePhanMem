import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://n23dcpt047.github.io/NhapMonCongNghePhanMem"

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

     WebDriverWait(driver, 3).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    assert "đăng nhập thành công" in alert.text.lower()
    alert.accept()


def test_login_empty_fields(driver):
    driver.get(URL)
    driver.find_element(By.ID, "btnLogin").click()
    error_text = driver.find_element(By.ID, "errorMsg").text
    assert "không được để trống" in error_text.lower()


def test_login_invalid_email(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("wrongformat")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "btnLogin").click()
    error_text = driver.find_element(By.ID, "errorMsg").text
    assert "email hợp lệ" in error_text.lower()


def test_login_short_password(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("admin@example.com")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.ID, "btnLogin").click()
    error_text = driver.find_element(By.ID, "errorMsg").text
    assert "ít nhất 6 ký tự" in error_text.lower()


def test_login_cancel_clears_fields(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("admin@example.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "btnCancel").click()

    assert driver.find_element(By.ID, "username").get_attribute("value") == ""
    assert driver.find_element(By.ID, "password").get_attribute("value") == ""
    
    assert driver.find_element(By.ID, "errorMsg").text.strip() == ""


def test_login_forgot_password_alert(driver):
    driver.get(URL)
    driver.find_element(By.ID, "forgotLink").click()

    alert = driver.switch_to.alert
    assert "đặt lại mật khẩu" in alert.text.lower()
    alert.accept()
