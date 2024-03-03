from driver import Driver
from pages.login_page import LoginPage
from pages.item_search import ItemSearch
from pages.emag_search_page import EmagSearchPage
from pages.flip_search_page import FlipSearchPage
from pages.carturesti_search_page import CarturestiSearchPage


def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    context.item_search = ItemSearch()
    context.emag_search = EmagSearchPage()
    context.flip_search = FlipSearchPage()
    context.carturesti_search = CarturestiSearchPage()




def after_all(context):
    context.browser.close()