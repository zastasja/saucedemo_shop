from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Main_page(Base):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # locators
    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    enter_to_cart = "//div[@class='shopping_cart_container']"

    # Getters

    def get_product_1(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_enter_to_cart(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_to_cart)))


    #Actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print('click add product 1 btn')

    def click_enter_to_cart(self):
        self.get_enter_to_cart().click()
        print('click cart icon')
    def add_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_enter_to_cart()

