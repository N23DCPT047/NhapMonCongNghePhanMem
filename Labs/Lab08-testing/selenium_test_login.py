
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://n23dcpt047.github.io/NhapMonCongNghePhanMem/"  

@pytest.fixture
def test_login_success(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("admin@example.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "btnLogin").click()

    alert = driver.switch_to.alert
    assert "Đăng nhập thành công" in alert.text
    alert.accept()


def test_login_empty(driver):
    driver.get(URL)
    driver.find_element(By.ID, "btnLogin").click()
    error_text = driver.find_element(By.ID, "errorMsg").text
    assert "không được để trống" in error_text.lower()
