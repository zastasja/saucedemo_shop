from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Client_info_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_btn = "//input[@id='continue']"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))

    #Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('input first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('input last name')

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print('input postal code')

    def click_continue_btn(self):
        self.get_continue_btn().click()
        print('click continue button')

    #Method

    def input_client_info(self):
        self.get_current_url()
        self.input_first_name('Jane')
        self.input_last_name('Doe')
        self.input_postal_code('123456')
        self.click_continue_btn()
