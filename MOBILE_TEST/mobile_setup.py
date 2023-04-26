import pytest
from appium import webdriver
import ios_test as ios
import android_test as android


@pytest.fixture(autouse=True)
def teardown_method():
    yield
    driver.quit()

# Choose platform for test, android or ios
platform = "ios"

# Set capabilities for Android or iOS
if platform.lower() == "android":
    caps = {
        "deviceName": "Google Pixel 4",
        "udid": "emulator-5554",
        "noReset": False,
        "platformName": "Android",
        "platformVersion": "12",    
        "appPackage": "com.saucelabs.mydemoapp.rn",
        "appActivity": "com.saucelabs.mydemoapp.rn.MainActivity",
    }
elif platform.lower() == "ios":
    caps = {
        "platformName": "iOS",
        "platformVersion": "16.4",
        "deviceName": "iPhone 14 pro",
        "udid": "5D083F20-766C-45E3-9FBF-C65BBCC779E7",
        "noReset": False,
        "app": "/Users/naufalazhar/Documents/Demo App/MyRNDemoApp.app",
    }
else:
    raise ValueError("Unsupported platforms")

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# Run test cases based on platform
def run_test_cases(test_cases):
    for test_case in test_cases:
        test_case(driver)

def test_main():
    # Run Android tests
    if platform.lower() == "android":
        print("----- Android tests started! -----")
        test_cases = [android.test_Add_to_cart, android.test_checkout]
        run_test_cases(test_cases)
        print("----- Android tests passed successfully! -----")


    # Run iOS tests
    elif platform.lower() == "ios":
        print("----- iOS tests started! -----")
        test_cases = [ios.test_login, ios.test_sort_button, ios.test_Add_to_cart, ios.test_checkout]
        run_test_cases(test_cases)
        print("----- iOS tests passed successfully! -----")

    # Unsupported platforms
    else:
        raise ValueError("Unsupported platforms")