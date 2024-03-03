import time
from selenium.webdriver.common.by import By
from pages.base_page import (BasePage)


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://the-internet.herokuapp.com/login"
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    FLASH_CONTAINER = (By.ID, "flash-messages")

    def navigate_to_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        #se mai putea scrie si self.driver.find_element(*self.EMAIL_iNPUT).send_keys(email)
        self.type(self.EMAIL_INPUT, email)

    def set_password(self, password):
        # se mai putea scrie si self.driver.find_element(*self.PASSWORD_iNPUT).send_keys(email)
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def is_message_displayed(self):
        assert self.wait_for_element(self.FLASH_CONTAINER, 50).is_displayed() == True, "Banner is not displayed"

    def get_message_text(self):
        return self.get_element_text(self.FLASH_CONTAINER).replace("×","")


