import allure
import pytest

from pages.login_page import Login_page
from pages.main_page import Main_page

@pytest.mark.parametrize("login_user, login_password",
                         [('standard_user', 'secret_sauce')])
@allure.description("test link about")
def test_link_about(browser, login_user, login_password):
    page = Login_page(browser)
    page.authorization(login_user, login_password)
    mpage = Main_page(browser)
    mpage.select_menu_about()
