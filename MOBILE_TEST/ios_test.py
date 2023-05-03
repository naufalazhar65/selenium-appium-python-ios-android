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
    el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Return")
    el6.click()
    el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Login button")
    el7.click()
    assert driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Products"]').is_displayed()

# ======================================================================================================================================

def test_sort_button(driver):
    print("======== Sort By Button Functionality =========")
    
    # Click the sort button and select "Name - Descending"
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="sort button")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@name=\"Name - Descending\"]")
    el2.click()
    
    # Check that the first item is "Test.allTheThings() T-Shirt"
    el2 = driver.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value="Test.allTheThings() T-Shirt")
    assert el2[0].text == 'Test.allTheThings() T-Shirt'
    
    # Click the sort button and select "Price - Ascending"
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="sort button")
    el3.click()
    el4 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@name=\"Price - Ascending\"]")
    el4.click()
    
    # Check that the first item has a price of $7.99
    el4 = driver.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText[`label == "$7.99"`]')
    assert el4[0].text == '$7.99'
    
    # Click the sort button and select "Price - Descending"
    el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="sort button")
    el5.click()
    el6 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@name=\"Price - Descending\"]")
    el6.click()
    
    # Check that the first item has a price of $49.99
    el6 = driver.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText[`label == "$49.99"`]')
    assert el6[0].text == '$49.99'
    
    # Click the sort button and select "Name - Ascending"
    el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="sort button")
    el7.click()
    el8 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@name=\"Name - Ascending\"]")
    el8.click()
    
    # Check that the first item is "Sauce Labs Backpack"
    el8 = driver.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText[`label == "Sauce Labs Backpack"`]')
    assert el8[0].text == 'Sauce Labs Backpack'
    sleep(2)

# ======================================================================================================================================

def test_add_to_cart(driver):
    print("======== Add To Cart Functionality =========")

    # Check if the Products page is displayed
    assert driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Products"]').is_displayed()

    # Click on a product
    product_name = "Sauce Labs Bike Light"
    product_element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=product_name)
    product_element.click()

    # Add the product to the cart
    add_to_cart_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add To Cart button")
    add_to_cart_button.click()

    # Check if the product was added to the cart
    assert driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=product_name).is_displayed()
    sleep(2)

# ======================================================================================================================================

def test_checkout(driver):
    print("========= Checkout Functionality =========")

    # Step 1: Click on Cart Tab
    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="tab bar option cart")
    el1.click()
    assert driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="My Cart").is_displayed()

    # Step 2: Proceed to Checkout
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Proceed To Checkout button")
    el2.click()
    assert driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Checkout"]').is_displayed()

    # Step 3: Fill in Shipping Address Details
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

    # Step 4: Proceed to Payment
    el13 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="To Payment button")
    el13.click()
    el13 = driver.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText[`label == "Enter a payment method"`]')
    assert el13[0].text == 'Enter a payment method'

    # Step 5: Fill in Payment Details
    el14 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Full Name* input field")
    el14.send_keys("Naufal")
    el15 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Card Number* input field")
    el15.send_keys("222222222222222")
    el16 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Expiration Date* input field")
    el16.send_keys("11/2")
    el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Return")
    el17.click()
    el18 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Security Code* input field")
    el18.send_keys("222")
    el18 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText[`label == "My billing address is the same as my shipping address."`]')
    el18.click()
    sleep(2)
    el20 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeOther[`label == "Review Order"`][2]')
    el20.click()
    el20.click()

    # Step 6: Verify Complete Order
    el23 = driver.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText[`label == "Review your order"`]')
    assert el23[0].text == 'Review your order'
    el24 = driver.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText[`label == "Review your order"`]')
    assert el24[0].text == 'Review your order'
    el25 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Place Order button")
    el25.click()
    el26 = driver.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value="Checkout Complete")
    assert el26[0].text == 'Checkout Complete'
    el26 = driver.find_elements(by=AppiumBy.ACCESSIBILITY_ID, value="Thank you for your order")
    assert el26[0].text == 'Thank you for your order'
    sleep(2)

# ======================================================================================================================================

def test_invalid_checkout(driver):
    print("========= Invalid Checkout Functionality =========")

    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="tab bar option cart")
    el1.click()
    assert driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="My Cart").is_displayed()
    el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Proceed To Checkout button")
    el2.click()
    assert driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Checkout"]').is_displayed()
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Full Name* input field")
    el3.send_keys("")
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
    el14 = driver.find_elements(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeStaticText[`label == "Please provide your full name."`]')
    assert el14[0].text == 'Please provide your full name.'
    sleep(2)
