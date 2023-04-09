import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    
    driver = webdriver.Chrome("/Users/naufalazhar/Documents/ChromeDriver/chromedriver", options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

# ==================================================================================================

def test_valid_login(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(by=By.ID, value='user-name')
    password = browser.find_element(by=By.ID, value='password')
    login_button = browser.find_element(by=By.ID, value='login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)

    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html'

# ==================================================================================================

def test_invalid_login(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(by=By.ID, value='user-name')
    password = browser.find_element(by=By.ID, value='password')
    login_button = browser.find_element(by=By.ID, value='login-button')
    username.send_keys("invalid_user")
    password.send_keys("invalid_password")
    login_button.click()
    sleep(2)

    assert browser.find_element(by=By.CSS_SELECTOR, value='.error-button').is_displayed()
    assert "Epic sadface: Username and password do not match any user in this service" in browser.page_source

# ==================================================================================================

def test_logout(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(by=By.ID, value='user-name')
    password = browser.find_element(by=By.ID, value='password')
    login_button = browser.find_element(by=By.ID, value='login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

    menu_button = browser.find_element(by=By.ID, value='react-burger-menu-btn')
    menu_button.click()
    logout_button = browser.find_element(by=By.ID, value='logout_sidebar_link')
    logout_button.click()
    sleep(2)
    assert "Swag Labs" in browser.title
    assert "Username" in browser.find_element(by=By.ID, value='user-name').get_attribute("placeholder")

# ==================================================================================================

def test_checkout(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(by=By.ID, value='user-name')
    password = browser.find_element(by=By.ID, value='password')
    login_button = browser.find_element(by=By.ID, value='login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

    # Add item to cart
    item = browser.find_element(by=By.ID, value='add-to-cart-sauce-labs-bike-light')
    item.click()
    assert "Remove" in browser.find_element(by=By.XPATH, value="//button[@name='remove-sauce-labs-bike-light']").text
    assert "1" in browser.find_element(by=By.CLASS_NAME, value="shopping_cart_badge").text
    sleep(2)

    # Go to cart
    cart_button = browser.find_element(by=By.CSS_SELECTOR, value='.shopping_cart_badge')
    cart_button.click()
    sleep(2)

    assert "Your Cart" in browser.page_source
    assert "$9.99" in browser.find_element(by=By.CLASS_NAME, value="inventory_item_price").text

    # Proceed to checkout
    checkout_button = browser.find_element(by=By.ID, value='checkout')
    checkout_button.click()
    sleep(2)

    # Fill in checkout form
    assert "Checkout: Your Information" in browser.page_source
    assert browser.find_element(by=By.CLASS_NAME, value="checkout_info").is_displayed()

    firstname = browser.find_element(by=By.ID, value='first-name')
    lastname = browser.find_element(by=By.ID, value='last-name')
    postalcode = browser.find_element(by=By.ID, value='postal-code')
    continue_button = browser.find_element(by=By.ID, value='continue')
    firstname.send_keys("Naufal")
    lastname.send_keys("Azhar")
    postalcode.send_keys("123")
    continue_button.click()

    # Ensure the purchase is successful
    assert "Checkout: Overview" in browser.page_source
    assert "Payment Information" in browser.find_element(by=By.CLASS_NAME, value="summary_info_label").text

    confirm_purchase_button = browser.find_element(by=By.ID, value='finish')
    confirm_purchase_button.click()

    # Complete Checkout
    assert browser.find_element(by=By.XPATH, value="//div[@class='checkout_complete_container']").is_displayed()
    assert 'Thank you for your order!' in browser.find_element(by=By.CSS_SELECTOR, value='h2').text
    sleep(4)

# ==================================================================================================

def test_invalid_checkout(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(by=By.ID, value='user-name')
    password = browser.find_element(by=By.ID, value='password')
    login_button = browser.find_element(by=By.ID, value='login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

    item = browser.find_element(by=By.ID, value='add-to-cart-sauce-labs-bike-light')
    item.click()
    assert "Remove" in browser.find_element(by=By.XPATH, value="//button[@name='remove-sauce-labs-bike-light']").text
    assert "1" in browser.find_element(by=By.CLASS_NAME, value="shopping_cart_badge").text
    sleep(2)

    cart_button = browser.find_element(by=By.CSS_SELECTOR, value='.shopping_cart_badge')
    cart_button.click()
    sleep(2)
    assert "Your Cart" in browser.page_source
    assert "$9.99" in browser.find_element(by=By.CLASS_NAME, value="inventory_item_price").text

    checkout_button = browser.find_element(by=By.ID, value='checkout')
    checkout_button.click()
    sleep(2)

    assert "Checkout: Your Information" in browser.page_source
    assert browser.find_element(by=By.CLASS_NAME, value="checkout_info").is_displayed()
    firstname = browser.find_element(by=By.ID, value='first-name')
    lastname = browser.find_element(by=By.ID, value='last-name')
    postalcode = browser.find_element(by=By.ID, value='postal-code')
    continue_button = browser.find_element(by=By.ID, value='continue')
    firstname.send_keys("Naufal")
    lastname.send_keys("Azhar")
    # postal code is left empty intentionally
    postalcode.send_keys("")
    continue_button.click()

    # check if error message is displayed
    assert browser.find_element(by=By.XPATH, value="//h3").is_displayed()
    assert "Error: Postal Code is required" in browser.page_source
    sleep(2)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_script.py'])
