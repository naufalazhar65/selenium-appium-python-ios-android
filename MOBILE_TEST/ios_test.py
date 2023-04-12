from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

def test_login(driver):
    print("======== Login Functionality =========")
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="tab bar option menu")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="menu item log in")
    el2.click()
    assert driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Login"]').is_displayed()
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Username input field")
    el3.send_keys("bob@example.com")
    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Password input field")
    el5.send_keys("10203040")
    el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Return")
    el10.click()
    el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login button")
    el11.click()
    assert driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Products"]').is_displayed()



def test_sort_button(driver):
    print("======== Sort By Button Functionality =========")
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="sort button")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@name=\"Name - Descending\"]")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="sort button")
    el3.click()
    el4 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@name=\"Price - Ascending\"]")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="sort button")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@name=\"Price - Descending\"]")
    el6.click()
    el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="sort button")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@name=\"Name - Ascending\"]")
    el8.click()
    sleep(2)

def test_Add_to_cart(driver):
    print("======== Add To Cart Functionality =========")
    assert driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Products"]').is_displayed()
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sauce Labs Bike Light")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="counter plus button")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add To Cart button")
    el3.click()
    assert driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sauce Labs Bike Light").is_displayed()
    sleep(2)


def test_checkout(driver):
    print("========= Checkout Functionality =========")
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="tab bar option cart")
    el1.click()
    assert driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="My Cart").is_displayed()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Proceed To Checkout button")
    el2.click()
    assert driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Checkout"]').is_displayed()
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Full Name* input field")
    el3.send_keys("Naufal Azhar")
    el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Address Line 1* input field")
    el4.send_keys("Jakarta")
    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Address Line 2 input field")
    el5.send_keys("Indonesia")
    el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="City* input field")
    el6.send_keys("Pamulang")
    el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="State/Region input field")
    el7.send_keys("Indonesia")
    el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Return")
    el8.click()
    el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Zip Code* input field")
    el9.send_keys("1234")
    el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Return")
    el10.click()
    el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Country* input field")
    el11.send_keys("Indonesia")
    el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Return")
    el12.click()
    el13 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="To Payment button")
    el13.click()
    el14 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Full Name* input field")
    el14.send_keys("Naufal Azhar")
    el15 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Card Number* input field")
    el15.send_keys("3258 1265 7568 789")
    el16 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Expiration Date* input field")
    el16.send_keys("03/25")
    el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Return")
    el17.click()
    el18 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Security Code* input field")
    el18.send_keys("123")
    el19 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Review Order button")
    el19.click()
    sleep(2)

