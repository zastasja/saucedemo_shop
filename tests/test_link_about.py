import allure
from pages.login_page import Login_page
from pages.main_page import Main_page

@allure.description("test link about")
def test_link_about(browser):
    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.select_menu_about()
