from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time

options = Options()
options.add_argument("start-maximized")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def test_setup():
    global driver
    driver = webdriver.Chrome("/Users/naufalazhar/Documents/ChromeDriver/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(15)
    print("Setup Completed")

def test_get():
    driver.get("https://myjobstreet.jobstreet.co.id/home/login.php?site=id")
    assert driver.title == "Mendaftar atau masuk untuk melamar lowongan @ JobStreet.com"

def test_login():
    username = driver.find_element(by=By.ID, value='login_id')
    password = driver.find_element(by=By.XPATH, value="//input[@type='password']")
    submit_button = driver.find_element(by=By.NAME, value='btn_login')
    username.send_keys('naufalazhar@gmail.com')
    password.send_keys('********')
    time.sleep(2)
    submit_button.click()

def test_findjob():
    assert 'Selamat Datang Naufal' in driver.find_element(by=By.CSS_SELECTOR, value='h3').text
    search_field = driver.find_element(by=By.ID, value='searchKeywordsField')
    location_field = driver.find_element(by=By.ID, value='locationAutoSuggest')
    search_field.send_keys("Quality Assurance")
    location_field.send_keys("Jakarta" + Keys.ENTER)
    time.sleep(2)
    assert "Quality Assurance" in driver.page_source and "Jakarta" in driver.page_source
    print("Test Completed")

def test_profil():
    driver.get("https://myjobstreet.jobstreet.co.id/resume/preview-resume.php")
    assert driver.title == "MyJobStreet - Lihat Profil Saya"
    assert 'Azhar' in driver.find_element(by=By.CSS_SELECTOR, value='div').text
    time.sleep(3)

def test_teardown():
    driver.close()
    driver.quit()

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_script.py'])
