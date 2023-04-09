- The given code is a Python code that uses Pytest and Selenium framework to perform testing on the Saucedemo website. There are four testing functions defined in the code: test_valid_login, test_invalid_login, test_logout, and test_checkout. Each testing function performs a series of actions, such as opening the website page, filling in the login form, clicking the logout button, or processing the payment, and checking whether the obtained results match the expected ones. The testing functions are performed using a browser fixture that loads the Selenium driver to perform testing on the Google Chrome browser.

# RUN
- pytest test_script.py -v -s
- pytest test_script.py -v --html=report.html
- pytest -p no:warnings -s -v test_script.py