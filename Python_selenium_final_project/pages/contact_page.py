import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage

class ContactPage(BasePage):
    CONTACT_DROPDOWN = (By.XPATH, "//one-app-nav-bar-item-root[@data-id='Contact']/one-app-nav-bar-item-dropdown")
    NEW_CONTACT_OPTION = (By.XPATH, "//span[text()='New Contact']")
    LAST_NAME_FIELD = (By.XPATH, "(//input[@class='slds-input'])[3]")
    ACCOUNT_NAME_FIELD = (By.XPATH, "(//input[@class='slds-combobox__input slds-input'])[1]")
    SELECT_ACCOUNT = (By.XPATH, "//span[contains(text(),'Aarti_K')]")
    SAVE_BUTTON = (By.XPATH, "//button[@class='slds-button slds-button_brand']")

    def select_new_contact(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.wait_for_element(self.CONTACT_DROPDOWN)).click().perform()
        self.driver.execute_script("document.querySelector('.forceVisualMessageQueue').style.display='none';")
        time.sleep(2)
        actions.move_to_element(self.wait_for_element(self.NEW_CONTACT_OPTION)).click().perform()

    def fill_contact_details(self, last_name, account_name):
        self.enter_text(self.LAST_NAME_FIELD, last_name)
        self.click_element(self.ACCOUNT_NAME_FIELD)
        time.sleep(2)
        self.click_element(self.SELECT_ACCOUNT)

    def save_contact(self):
        time.sleep(2)
        self.click_element(self.SAVE_BUTTON)
