import pytest
import allure
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page

@pytest.mark.parametrize("login_user, login_password",
                         [('standard_user', 'secret_sauce'), ('problem_user', 'secret_sauce'),
                          ('performance_glitch_user', 'secret_sauce')])
@allure.description("add product 1 to the cart")
@pytest.mark.run(order=2)
def test_buy_product_1(browser, login_user, login_password):
    page = Login_page(browser)
    page.authorization(login_user, login_password)
    mpage = Main_page(browser)
    mpage.add_product_1()
    cpage = Cart_page(browser)
    cpage.product_confirm()
    cipage = Client_info_page(browser)
    cipage.input_client_info()
    ppage = Payment_page(browser)
    ppage.payment()
    fpage = Finish_page(browser)
    fpage.finish('test_buy_product 1')

@allure.description("add product 2 to the cart")
@pytest.mark.run(order=1)
def test_buy_product_2(browser, login_user, login_password):
    page = Login_page(browser)
    page.authorization(login_user, login_password)
    mpage = Main_page(browser)
    mpage.add_product_2()
    cpage = Cart_page(browser)
    cpage.product_confirm()
    cipage = Client_info_page(browser)
    cipage.input_client_info()
    ppage = Payment_page(browser)
    ppage.payment()
    fpage = Finish_page(browser)
    fpage.finish('test_buy_product 1')


@allure.description("add product 3 to the cart")
@pytest.mark.run(order=3)
def test_buy_product_3(browser, login_user, login_password):
    page = Login_page(browser)
    page.authorization(login_user, login_password)
    mpage = Main_page(browser)
    mpage.add_product_3()
    cpage = Cart_page(browser)
    cpage.product_confirm()
    cipage = Client_info_page(browser)
    cipage.input_client_info()
    ppage = Payment_page(browser)
    ppage.payment()
    fpage = Finish_page(browser)
    fpage.finish('test_buy_product 3')


@allure.description("add product 4 to the cart")
@pytest.mark.run(order=5)
def test_buy_product_4(browser, login_user, login_password):
    page = Login_page(browser)
    page.authorization(login_user, login_password)
    mpage = Main_page(browser)
    mpage.add_product_4()
    cpage = Cart_page(browser)
    cpage.product_confirm()
    cipage = Client_info_page(browser)
    cipage.input_client_info()
    ppage = Payment_page(browser)
    ppage.payment()
    fpage = Finish_page(browser)
    fpage.finish('test_buy_product 4')


@allure.description("add product 5 to the cart")
@pytest.mark.run(order=4)
def test_buy_product_5(browser, login_user, login_password):
    page = Login_page(browser)
    page.authorization(login_user, login_password)
    mpage = Main_page(browser)
    mpage.add_product_5()
    cpage = Cart_page(browser)
    cpage.product_confirm()
    cipage = Client_info_page(browser)
    cipage.input_client_info()
    ppage = Payment_page(browser)
    ppage.payment()
    fpage = Finish_page(browser)
    fpage.finish('test_buy_product 5')


@allure.description("add product 6 to the cart")
@pytest.mark.run(order=6)
def test_buy_product_6(browser, login_user, login_password):
    page = Login_page(browser)
    page.authorization(login_user, login_password)
    mpage = Main_page(browser)
    mpage.add_product_6()
    cpage = Cart_page(browser)
    cpage.product_confirm()
    cipage = Client_info_page(browser)
    cipage.input_client_info()
    ppage = Payment_page(browser)
    ppage.payment()
    fpage = Finish_page(browser)
    fpage.finish('test_buy_product 6')
