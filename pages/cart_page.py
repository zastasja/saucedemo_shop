from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Cart_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators
    checkout_btn = "//button[@id='checkout']"

    # Getters

    def get_checkout_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_btn)))

    #Actions

    def click_checkout_btn(self):
        self.get_checkout_btn().click()
        print('click checkout btn')

    # Method
    def product_confirm(self):
        self.get_current_url()
        self.click_checkout_btn()

