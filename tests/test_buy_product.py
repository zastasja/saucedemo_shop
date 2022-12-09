import pytest

from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page
import allure

@pytest.mark.parametrize("login_user, login_password",
                         [('standard_user', 'secret_sauce')])
@allure.description("test full product purchase process")
def test_buy_product(browser, login_user, login_password):
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
    fpage.finish('test_buy_product')