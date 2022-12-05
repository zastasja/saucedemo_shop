from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page


def test_link_about():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.select_menu_about()


    browser.quit()