import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ItemSearch(BasePage):

    MAIN_URL = "https://www.libris.ro/"
    SEARCH_INPUT_SELECTOR = (By.ID, "autoComplete")
    TITLE_SELECTOR = (By.CSS_SELECTOR, "pr-title-ct")
    MAGNIFIER_SELECTOR = (By.XPATH, "onSearchClick")

    def navigate_to_page(self):
        self.driver.get(self.MAIN_URL)

    def click_on_search_button(self):
        self.click(self.SEARCH_INPUT_SELECTOR)

    def type_anything_on_search(self, text_to_search):
        self.type(self.SEARCH_INPUT_SELECTOR, text_to_search)

    def click_on_magnifier_button(self):
        self.click(self.MAGNIFIER_SELECTOR)

    def get_title_text(self):
       return self.get_element_text(self.TITLE_SELECTOR)
