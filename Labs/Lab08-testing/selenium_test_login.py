
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://n23dcpt047.github.io/NhapMonCongNghePhanMem/"  

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(1)
    
    assert "Thành công" in driver.page_source.lower()

def test_login_fail(driver):
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(1)
    assert "Sai" in driver.page_source.lower()

def test_login_empty(driver):
    driver.get(URL)
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(1)
    assert "Không được để trống" in driver.page_source.lower()
