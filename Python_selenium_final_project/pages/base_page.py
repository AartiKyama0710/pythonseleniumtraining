from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))

    def click_element(self, by_locator):
        self.wait_for_element(by_locator).click()

    def enter_text(self, by_locator, text):
        self.wait_for_element(by_locator).send_keys(text)
