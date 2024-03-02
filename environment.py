from driver import Driver
from pages.login_page import LoginPage
from pages.item_search import ItemSearch
from pages.emag_search_page import EmagSearchPage


def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.item_search = (ItemSearch())
    context.emag_search = EmagSearchPage()

def after_all(context):
    context.browser.close()