from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'pw')
    LOGIN_BUTTON = (By.XPATH, "//input[@class='button r4 wide primary']")

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)
