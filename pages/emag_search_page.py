from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class EmagSearchPage(BasePage):

    MAIN_URL = "https://www.emag.ro/"

    SEARCH_INPUT_SELECTOR = (By.ID, "searchboxTrigger")
    MAGNIFIER_SELECTOR = (By.CSS_SELECTOR, "button.searchbox-submit-button")
    # after you seearch anything on emag, the result page will display the following info
    # total number of products + your keyword
    # the total number of products is hold by this element: span @class='title-phrasing title-phrasing-sm'
    # the keyword that you just entered is hold by this element: span @class='title-phrasing title-phrasing-xl'
    TITLE_PHRASING_SELECTOR_POZITIVE = (By.XPATH, "//span[@class='title-phrasing title-phrasing-xl']")
    # for the negative cases when the keyword is not found on emag, title and number of products elements
    # have different selectors, you can find them bellow
    TITLE_PHRASING_SELECTOR_NEGATIVE = (By.XPATH, "//span[@class='title-phrasing title-phrasing-md']")
    TITLE_PHRASING_NUMBER_NEGATIVE = (By.XPATH, "//span[@class='title-phrasing title-phrasing-sm text-danger']")

    def navigate_to_page(self):
        self.driver.get(self.MAIN_URL)

    def click_on_icon_button(self):
        self.click(self.SEARCH_INPUT_SELECTOR)

    def click_on_specific_button(self):
        self.click(self.MAGNIFIER_SELECTOR)

    def type_anything_on_search(self, text_to_search):
        self.type(self.SEARCH_INPUT_SELECTOR, text_to_search)

    def get_title_text(self):
        return self.get_element_text(self.TITLE_PHRASING_SELECTOR_POZITIVE)

    def get_title_negative_text(self):
        return self.get_element_text(self.TITLE_PHRASING_SELECTOR_NEGATIVE)

    def get_nr_of_products_negative_text(self):
        return self.get_element_text(self.TITLE_PHRASING_NUMBER_NEGATIVE)


