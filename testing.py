import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep

@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_product_sort(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(by=By.ID, value='user-name')
    password = browser.find_element(by=By.ID, value='password')
    login_button = browser.find_element(by=By.ID, value='login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    # product_sort = browser.find_element(by=By.CLASS_NAME, value='product_sort_container')
    # product_sort.click()
    # sleep(3)
    # select = Select(product_sort)
    # select.select_by_value('za')
    # sleep(2)
    # select.select_by_value('lohi')
    # sleep(2)
    # select.select_by_value('hilo')
    # sleep(2)
    # select.select_by_value('az')
    # sleep(3)

    sort_button = browser.find_element(by=By.CLASS_NAME, value='product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(by=By.XPATH, value="//option[@value='za']")
    sort_name.click()
    product_names = browser.find_elements(by=By.CLASS_NAME, value='inventory_item_name')
    assert product_names[0].text == 'Test.allTheThings() T-Shirt (Red)'
    assert product_names[-1].text == 'Sauce Labs Backpack'
    sleep(2)
    sort_button = browser.find_element(by=By.CLASS_NAME, value='product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(by=By.XPATH, value="//option[@value='lohi']")
    sort_name.click()
    product_names = browser.find_elements(by=By.CLASS_NAME, value='inventory_item_name')
    assert product_names[0].text == 'Sauce Labs Onesie'
    assert product_names[-1].text == 'Sauce Labs Fleece Jacket'
    sleep(2)
    sort_button = browser.find_element(by=By.CLASS_NAME, value='product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(by=By.XPATH, value="//option[@value='hilo']")
    sort_name.click()
    product_names = browser.find_elements(by=By.CLASS_NAME, value='inventory_item_name')
    assert product_names[0].text == 'Sauce Labs Fleece Jacket'
    assert product_names[-1].text == 'Sauce Labs Onesie'
    sleep(2)
    sort_button = browser.find_element(by=By.CLASS_NAME, value='product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(by=By.XPATH, value="//option[@value='az']")
    sort_name.click()
    product_names = browser.find_elements(by=By.CLASS_NAME, value='inventory_item_name')
    assert product_names[0].text == 'Sauce Labs Backpack'
    assert product_names[-1].text == 'Test.allTheThings() T-Shirt (Red)'
    sleep(2)


    # # Get the list of prices before and after sorting
    # unsorted_prices = browser.find_elements(By.CSS_SELECTOR, '.inventory_item_price')
    # sorted_prices = browser.find_elements(By.CSS_SELECTOR, '.inventory_item_price')

    # # Convert the prices from strings to floats for comparison
    # unsorted_prices = [float(price.text.replace('$', '')) for price in unsorted_prices]
    # sorted_prices = [float(price.text.replace('$', '')) for price in sorted_prices]
    # sorted_prices.sort()

    # # Check that the prices are now sorted correctly
    # assert unsorted_prices == sorted_prices
