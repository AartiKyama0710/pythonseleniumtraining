from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountPage(BasePage):
    ACCOUNT_DROPDOWN = (By.XPATH, "//one-app-nav-bar-item-root[@data-id='Account']/one-app-nav-bar-item-dropdown")
    ACCOUNT_OPTION = (By.XPATH, "//span[text()='New Account']")
    ACCOUNT_NAME_FIELD = (By.XPATH, "(//input[@class='slds-input'])[2]")
    SAVE_BUTTON = (By.XPATH, "//button[@class='slds-button slds-button_brand']")

    def select_new_account(self):
        self.click_element(self.ACCOUNT_DROPDOWN)
        self.click_element(self.ACCOUNT_OPTION)

    def fill_account_name(self, account_name):
        self.enter_text(self.ACCOUNT_NAME_FIELD, account_name)

    def save_account(self):
        self.click_element(self.SAVE_BUTTON)
