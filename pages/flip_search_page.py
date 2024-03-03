from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FlipSearchPage(BasePage):

    MAIN_URL = "https://flip.ro/magazin/"

    SEARCH_INPUT_SELECTOR = (By.ID, "__BVID__188")
    MAGNIFIER_SELECTOR = (By.XPATH, "//span[@xmlns='http://www.w3.org/2000/svg']")
    TITLE_PHRASING_SELECTOR = (By.XPATH, "//span[@class='md-title ng-binding']")


    def navigate_to_page(self):
        self.driver.get(self.MAIN_URL)


    def click_on_the_search(self):
        self.click(self.SEARCH_INPUT_SELECTOR)

    def click_on_the_magnifier(self):
        self.click(self.MAGNIFIER_SELECTOR)

    def type_anything_on_search(self, text_to_search):
        self.type((self.SEARCH_INPUT_SELECTOR, text_to_search))

    def get_title_text(self):
        return self.get_element_text(self.TITLE_PHRASING_SELECTOR)



