from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Payment_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators

    finish_btn = "//button[@id='finish']"

    # Getters

    def get_finish_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_btn)))

    # Actions

    def click_finish_btn(self):
        self.get_finish_btn().click()
        print('click finish button')

    # Method
    def payment(self):
        self.get_current_url()
        self.click_finish_btn()
