from driver import Driver
from pages.login_page import LoginPage
from pages.emag_search_page import EmagSearchPage
from pages.carturesti_search_page import CarturestiSearchPage


def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.emag_search = EmagSearchPage()
    context.carturesti_search = CarturestiSearchPage()




def after_all(context):
    context.browser.close()