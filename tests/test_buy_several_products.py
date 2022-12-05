import pytest
import allure
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page


@allure.description("add product 1 to the cart")
@pytest.mark.run(order=2)
def test_buy_product_1(browser):
    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_1()
    cpage = Cart_page(browser)
    cpage.product_confirm()


@allure.description("add product 2 to the cart")
@pytest.mark.run(order=1)
def test_buy_product_2(browser):
    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_2()
    cpage = Cart_page(browser)
    cpage.product_confirm()


@allure.description("add product 3 to the cart")
@pytest.mark.run(order=3)
def test_buy_product_3(browser):
    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_3()
    cpage = Cart_page(browser)
    cpage.product_confirm()


@allure.description("add product 4 to the cart")
@pytest.mark.run(order=5)
def test_buy_product_4(browser):
    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_4()
    cpage = Cart_page(browser)
    cpage.product_confirm()


@allure.description("add product 5 to the cart")
@pytest.mark.run(order=4)
def test_buy_product_5(browser):
    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_5()
    cpage = Cart_page(browser)
    cpage.product_confirm()


@allure.description("add product 6 to the cart")
@pytest.mark.run(order=6)
def test_buy_product_6(browser):
    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_6()
    cpage = Cart_page(browser)
    cpage.product_confirm()
