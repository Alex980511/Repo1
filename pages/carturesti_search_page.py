from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CarturestiSearchPage(BasePage):

    MAIN_URL = "https://carturesti.ro/"
    SEARCH_WITH_PAGE_URL = "https://carturesti.ro/product/search/"

    SEARCH_INPUT_SELECTOR = (By.ID, "search-input")
    TITLE_SELECTOR = (By.CSS_SELECTOR, "md-title ng-binding")
    MAGNIFIER_SELECTOR = (By.CSS_SELECTOR, "div.search-container > i")
    # when you are on the page 10, rest of the elements for page number have @class='ng-scope'
    # this is why, the current page element is the ONLY one in DOM that has @class='ng-scope active'
    CURRENT_PAGE_SELECTOR = (By.XPATH, "//li[@data-ng-repeat='page in pager.pages' and @class='ng-scope active']")


    def navigate_to_page(self):
        self.driver.get(self.MAIN_URL)
    # when you try to search a specific keyword on the maine page
    # the URL looks like this: https://carturesti.ro/product/search/razboi?page=109
    # this is why when you try to navigate directly to a specific page
    # you can "hack" the steps and go directly to the URL

    def navigate_to_page_with_key_word(self, keyword, page):
        URL = self.SEARCH_WITH_PAGE_URL + keyword + "?page=" + page
        self.driver.get(URL)

    def click_in_search_button(self):
        self.click(self.SEARCH_INPUT_SELECTOR)

    def click_on_magnifier_button_1(self):
        self.click(self.MAGNIFIER_SELECTOR)

    def type_anything_on_search(self, text_to_search):
        self.type(self.SEARCH_INPUT_SELECTOR, text_to_search)

    def get_title_text(self):
        return self.get_element_text(self.TITLE_SELECTOR)

    def get_current_page_text(self):
        return self.get_element_text(self.CURRENT_PAGE_SELECTOR)
