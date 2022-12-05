from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Finish_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators
    # Getters
    # Actions

    def finish(self, test_name):
        self.get_current_url()
        self.get_screenshot(test_name)
        print('take screenshot')

    # Method
    def payment(self):
        self.get_current_url()
        self.click_finish_btn()
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()

