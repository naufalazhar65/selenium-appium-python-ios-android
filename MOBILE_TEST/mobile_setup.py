import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import ios_test as ios
import android_test as android


@pytest.fixture(autouse=True)
def teardown_method():
    yield
    driver.quit()

# Choose platform for test, android or ios
platform = "ios"

# Set capabilities for Android
if platform.lower() == "android":
    caps = {
        "deviceName": "Gphone",
        "udid": "emulator-5554",
        "noReset": False,
        "platformName": "Android",
        "platformVersion": "12",    
        # "app": "/Users/naufalazhar/Documents/Demo App/MyRNDemoApp.apk",
        "appPackage": "com.saucelabs.mydemoapp.rn",
        "appActivity": "com.saucelabs.mydemoapp.rn.MainActivity",
    }

# Set capabilities for iOS
elif platform.lower() == "ios":
    caps = {
        "platformName": "iOS",
        "platformVersion": "16.4",
        "deviceName": "iPhone 14 pro",
        "udid": "5D083F20-766C-45E3-9FBF-C65BBCC779E7",
        "noReset": False,
        "app": "/Users/naufalazhar/Documents/Demo App/MyRNDemoApp.app",
        # "browserName": "Safari"
    }

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

def test_main():
        if platform.lower() == "android":
            test_cases = [android.test_Add_to_cart,
                            android.test_checkout]
            for test_case in test_cases:
                test_case(driver)

        elif platform.lower() == "ios":
            test_cases = [ios.test_login,
                            ios.test_sort_button,
                            ios.test_Add_to_cart,
                            ios.test_checkout]
            for test_case in test_cases:
                test_case(driver)
        else:
            raise ValueError("Unsupported platforms")