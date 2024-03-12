from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from driver import Driver

class BasePage(Driver):

    ACCEPT_COOKIE_BUTTON = (By.XPATH, '//a[@aria-label="allow cookies"]')

    def type(self, locator, text):
        element = self.driver.find_element(*locator)
        element.click()
        #aici am schimbat click cu clear
        element.send_keys(text)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def wait_for_element(self, locator, wait_time) -> WebElement:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))

    def get_element_text(self, locator):
        return self.wait_for_element(locator,  10).text

    def accept_cookie(self):
        self.driver.find_element(*self.ACCEPT_COOKIE_BUTTON).click()

