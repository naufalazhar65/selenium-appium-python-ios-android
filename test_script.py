import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--headless')
    browser = webdriver.Chrome(options, service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    browser.implicitly_wait(15)
    yield browser
    browser.quit()

# ==================================================================================================

def test_valid_login(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
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

    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys("invalid_user")
    password.send_keys("invalid_password")
    login_button.click()
    sleep(2)
    assert browser.find_element(By.CSS_SELECTOR, '.error-button').is_displayed()
    assert "Epic sadface: Username and password do not match any user in this service" in browser.page_source

# ==================================================================================================

def test_logout(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

    menu_button = browser.find_element(By.ID, 'react-burger-menu-btn')
    menu_button.click()
    logout_button = browser.find_element(By.ID, 'logout_sidebar_link')
    logout_button.click()
    sleep(2)
    assert "Swag Labs" in browser.title
    assert "Username" in browser.find_element(By.ID, 'user-name').get_attribute("placeholder")

# ==================================================================================================

def test_add_remove_item_from_cart(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)

    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html'

    # Add product to cart
    product_name = browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    product_name.click()
    sleep(2)
    
    # Verify that the product is added to the cart
    assert "1" in browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').get_attribute('innerHTML')
    assert "Remove" in browser.find_element(By.ID, 'remove-sauce-labs-backpack').get_attribute('innerHTML')

    # Remove product from cart
    cart_button = browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()
    sleep(2)
    remove_button = browser.find_element(By.ID, 'remove-sauce-labs-backpack')
    remove_button.click()

    # Verify that the product is removed from the cart
    assert "" in browser.find_element(By.CLASS_NAME, 'shopping_cart_link').get_attribute('innerHTML')
    elements = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert len(elements) == 0

# ==================================================================================================

def test_product_sort(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    sort_button = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(By.XPATH, "//option[@value='za']")
    sort_name.click()
    product_names = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert product_names[0].text == 'Test.allTheThings() T-Shirt (Red)'
    assert product_names[-1].text == 'Sauce Labs Backpack'
    sleep(2)
    sort_button = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(By.XPATH, "//option[@value='lohi']")
    sort_name.click()
    product_names = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert product_names[0].text == 'Sauce Labs Onesie'
    assert product_names[-1].text == 'Sauce Labs Fleece Jacket'
    sleep(2)
    sort_button = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(By.XPATH, "//option[@value='hilo']")
    sort_name.click()
    product_names = browser.find_elements(by=By.CLASS_NAME, value='inventory_item_name')
    assert product_names[0].text == 'Sauce Labs Fleece Jacket'
    assert product_names[-1].text == 'Sauce Labs Onesie'
    sleep(2)
    sort_button = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_button.click()
    sort_name = browser.find_element(By.XPATH, "//option[@value='az']")
    sort_name.click()
    product_names = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert product_names[0].text == 'Sauce Labs Backpack'
    assert product_names[-1].text == 'Test.allTheThings() T-Shirt (Red)'
    sleep(2)

# ==================================================================================================

def test_checkout(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

    # Add item to cart
    item = browser.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
    item.click()
    assert "Remove" in browser.find_element(By.XPATH, "//button[@name='remove-sauce-labs-bike-light']").text
    assert "1" in browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    sleep(2)

    # Go to cart
    cart_button = browser.find_element(By.CSS_SELECTOR, '.shopping_cart_badge')
    cart_button.click()
    sleep(2)
    assert "Your Cart" in browser.page_source
    assert "$9.99" in browser.find_element(By.CLASS_NAME, "inventory_item_price").text

    # Proceed to checkout
    checkout_button = browser.find_element(By.ID, 'checkout')
    checkout_button.click()
    sleep(2)

    # Fill in checkout form
    assert "Checkout: Your Information" in browser.page_source
    assert browser.find_element(By.CLASS_NAME, "checkout_info").is_displayed()
    firstname = browser.find_element(By.ID, 'first-name')
    lastname = browser.find_element(By.ID, 'last-name')
    postalcode = browser.find_element(By.ID, 'postal-code')
    continue_button = browser.find_element(By.ID, 'continue')
    firstname.send_keys("Naufal")
    lastname.send_keys("Azhar")
    postalcode.send_keys("123")
    continue_button.click()

    # Ensure the purchase is successful
    assert "Checkout: Overview" in browser.page_source
    assert "Payment Information" in browser.find_element(By.CLASS_NAME, "summary_info_label").text
    confirm_purchase_button = browser.find_element(By.ID, 'finish')
    confirm_purchase_button.click()

    # Complete Checkout
    assert browser.find_element(By.XPATH, "//div[@class='checkout_complete_container']").is_displayed()
    assert 'Thank you for your order!' in browser.find_element(By.CSS_SELECTOR, 'h2').text
    sleep(4)

# ==================================================================================================

def test_invalid_checkout(browser):
    browser.get('https://www.saucedemo.com/')
    assert 'Swag Labs' in browser.title

    username = browser.find_element(By.ID, 'user-name')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)
    assert "Products" in browser.page_source and "Swag Labs" in browser.page_source

    item = browser.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
    item.click()
    assert "Remove" in browser.find_element(By.XPATH, "//button[@name='remove-sauce-labs-bike-light']").text
    assert "1" in browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    sleep(2)

    cart_button = browser.find_element(By.CSS_SELECTOR, '.shopping_cart_badge')
    cart_button.click()
    sleep(2)
    assert "Your Cart" in browser.page_source
    assert "$9.99" in browser.find_element(By.CLASS_NAME, "inventory_item_price").text

    checkout_button = browser.find_element(By.ID, 'checkout')
    checkout_button.click()
    sleep(2)

    assert "Checkout: Your Information" in browser.page_source
    assert browser.find_element(By.CLASS_NAME, "checkout_info").is_displayed()
    firstname = browser.find_element(By.ID, 'first-name')
    lastname = browser.find_element(By.ID, 'last-name')
    postalcode = browser.find_element(By.ID, 'postal-code')
    continue_button = browser.find_element(By.ID, 'continue')
    firstname.send_keys("Naufal")
    lastname.send_keys("Azhar")
    # postal code is left empty intentionally
    postalcode.send_keys("")
    continue_button.click()

    # check if error message is displayed
    assert browser.find_element(By.XPATH, "//h3").is_displayed()
    assert "Error: Postal Code is required" in browser.page_source
    sleep(2)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_script.py'])