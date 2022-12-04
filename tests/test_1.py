from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import Login_page
from pages.main_page import Main_page

def test_select_product():
    browser = webdriver.Chrome(ChromeDriverManager().install())

    page = Login_page(browser)
    page.authorization()
    mpage = Main_page(browser)
    mpage.add_product_1()

    browser.quit()