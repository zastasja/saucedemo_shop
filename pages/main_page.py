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
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    select_product_4 = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    select_product_5 = "//button[@id='add-to-cart-sauce-labs-onesie']"
    select_product_6 = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"

    enter_to_cart = "//div[@class='shopping_cart_container']"
    burger_menu_btn = "//button[@id='react-burger-menu-btn']"
    link_about = "//a[@id='about_sidebar_link']"
    link_products = "//a[@id='inventory_sidebar_link']"
    link_logout = "//a[@id='logout_sidebar_link']"
    link_reset_app = "//a[@id='reset_sidebar_link']"

    shopping_cart_badge = "//span[@class='shopping_cart_badge']"

    # Getters

    def get_product_1(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))
    def get_product_2(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))
    def get_product_3(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))
    def get_product_4(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_4)))
    def get_product_5(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_5)))
    def get_product_6(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_6)))

    def get_enter_to_cart(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_to_cart)))
    def get_burger_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu_btn)))

    def get_link_about(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))

    def get_link_products(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_products)))

    def get_link_logout(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_logout)))

    def get_link_reset_app(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_reset_app)))

    def get_shop_cart_badge(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.shopping_cart_badge)))


    #Actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print('click add product 1 btn')

    def click_select_product_2(self):
        self.get_product_2().click()
        print('click add product 2 btn')

    def click_select_product_3(self):
        self.get_product_3().click()
        print('click add product 3 btn')

    def click_select_product_4(self):
        self.get_product_4().click()
        print('click add product 4 btn')

    def click_select_product_5(self):
        self.get_product_5().click()
        print('click add product 5 btn')

    def click_select_product_6(self):
        self.get_product_6().click()
        print('click add product 6 btn')


    def click_enter_to_cart(self):
        self.get_enter_to_cart().click()
        print('click cart icon')

    def click_menu(self):
        self.get_burger_menu().click()
        print('click menu icon')

    def click_about(self):
        self.get_link_about().click()
        print('click about link')

    def click_products(self):
        self.get_link_products().click()
        print('click all products link')

    def click_logout(self):
        self.get_link_logout().click()
        print('click logout link')

    def click_reset_app(self):
        self.get_link_reset_app().click()
        print('click reset link')

    def text_of_shop_cart_badge(self):
        word = self.get_shop_cart_badge().text
        return word
        print('get shopping cart badge text')
    # Method
    def add_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_enter_to_cart()

    def add_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_enter_to_cart()

    def add_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_enter_to_cart()

    def add_product_4(self):
        self.get_current_url()
        self.click_select_product_4()
        self.click_enter_to_cart()

    def add_product_5(self):
        self.get_current_url()
        self.click_select_product_5()
        self.click_enter_to_cart()

    def add_product_6(self):
        self.get_current_url()
        self.click_select_product_6()
        self.click_enter_to_cart()
    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_about()
        self.assert_url("https://saucelabs.com/")

    def select_products_sidebar_menu(self):
        self.get_current_url()
        self.click_menu()
        self.click_products()
        self.assert_url("https://www.saucedemo.com/inventory.html")

    def select_logout_sidebar_menu(self):
        self.get_current_url()
        self.click_menu()
        self.click_logout()
        self.assert_url("https://www.saucedemo.com/")

    def select_reset_app_sidebar_menu(self):
        self.get_current_url()
        self.click_menu()
        self.click_reset_app()
        self.assert_url("https://www.saucedemo.com/inventory.html")
