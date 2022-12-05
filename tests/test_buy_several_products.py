import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page


@pytest.mark.run(order=2)
def test_buy_product_1():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_1()
    cpage = Cart_page(browser)
    cpage.product_confirm()

    browser.quit()


@pytest.mark.run(order=1)
def test_buy_product_2():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_2()
    cpage = Cart_page(browser)
    cpage.product_confirm()

    browser.quit()


@pytest.mark.run(order=3)
def test_buy_product_3():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_3()
    cpage = Cart_page(browser)
    cpage.product_confirm()

    browser.quit()

@pytest.mark.run(order=5)
def test_buy_product_4():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_4()
    cpage = Cart_page(browser)
    cpage.product_confirm()

    browser.quit()

@pytest.mark.run(order=4)
def test_buy_product_5():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_5()
    cpage = Cart_page(browser)
    cpage.product_confirm()

    browser.quit()

@pytest.mark.run(order=6)
def test_buy_product_6():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_6()
    cpage = Cart_page(browser)
    cpage.product_confirm()

    browser.quit()