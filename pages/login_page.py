import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class Login_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators
    base_url = "https://www.saucedemo.com/"
    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_btn = "//input[@id='login-button']"
    product_word = "//span[@class='title']"

    # Getters

    def get_username(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))

    def get_product_word(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_word)))

    # Actions

    def input_username(self, username):
        self.get_username().send_keys(username)
        print('input username')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('input password')

    def click_lgn_btn(self):
        self.get_login_btn().click()
        print('click login button')


    def authorization(self, login_user, login_password):
        self.browser.get(self.base_url)
        self.browser.maximize_window()
        self.get_current_url()
        self.input_username(login_user)
        self.input_password(login_password)
        self.click_lgn_btn()
        self.assert_word(self.get_product_word(), 'PRODUCTS')
