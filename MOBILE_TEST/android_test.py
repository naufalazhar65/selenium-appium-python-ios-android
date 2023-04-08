from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

def test_android(driver):
    el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"cart badge\"]")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@content-desc=\"Go Shopping button\"]")
    el2.click()
    sleep(2)