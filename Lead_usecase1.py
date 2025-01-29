import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class SalesforceAutomation:
    def __init__(self, username, password, chrome_binary_path):
        self.username = username
        self.password = password
        self.chrome_binary_path = chrome_binary_path
        self.driver = self.setup_driver()
        self.driver.implicitly_wait(40)

    def setup_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-gpu')
        options.add_argument('disable-infobars')
        options.add_argument('--whitelisted-ips')
        options.add_argument('--remote-debugging-port=9222')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1366,2000')
        options.add_argument('--start-maximized')
        options.add_argument("--incognito")
        options.add_argument("--remote-allow-origins=*")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.binary_location = self.chrome_binary_path

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(driver_version='130').install()),
            options=options
        )
        return driver

    def login(self):
        self.driver.get("https://login.salesforce.com/?locale=in")
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'pw').send_keys(self.password)
        self.driver.find_element(By.XPATH, "//input[@class='button r4 wide primary']").click()

    def click_dropdown_and_select_option(self, dropdown_xpath, option_text):
        dropdown = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown).click().perform()
        option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{option_text}']"))
        )
        actions.move_to_element(option).click().perform()

    def create_lead(self, last_name, company_name):
        self.click_dropdown_and_select_option(
            "//one-app-nav-bar-item-root[@data-id='Lead']/one-app-nav-bar-item-dropdown",
            "New Lead"
        )
        self.driver.find_element(By.XPATH, "(//input[@class='slds-input'])[3]").send_keys(last_name)
        self.driver.find_element(By.XPATH, "(//input[@class='slds-input'])[4]").send_keys(company_name)
        self.driver.find_element(By.XPATH, "//button[@class='slds-button slds-button_brand']").click()

    def create_account(self, account_name):
        self.click_dropdown_and_select_option(
            "//one-app-nav-bar-item-root[@data-id='Account']/one-app-nav-bar-item-dropdown",
            "New Account"
        )
        self.driver.find_element(By.XPATH, "(//input[@class='slds-input'])[2]").send_keys(account_name)
        self.driver.find_element(By.XPATH, "//button[@class='slds-button slds-button_brand']").click()
        time.sleep(5)

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    automation = SalesforceAutomation(
        username="satishkyama-fne0@force.com",
        password="Anita@1164",
        chrome_binary_path=r"C:\Users\aarti.kyama\Downloads\chrome-win64 (1)\chrome-win64\chrome.exe"
    )

    try:
        automation.login()
        automation.create_lead("Kyama", "Tiger")
    finally:
        automation.close()


