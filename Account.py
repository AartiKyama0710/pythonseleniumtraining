from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class SalesforceAutomation:
    def __init__(self, chrome_binary_path):
        self.chrome_binary_path = chrome_binary_path
        self.driver = self._setup_driver()
        self.driver.implicitly_wait(20)  # Set implicit wait globally

    def _setup_driver(self):
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

        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(driver_version='130').install()),
            options=options
        )

    def login(self, username, password):

        self.driver.get("https://login.salesforce.com/?locale=in")
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'pw').send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@class='button r4 wide primary']").click()

    def click_dropdown_and_select(self, dropdown_xpath, option_text):

        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown).click().perform()

        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{option_text}']"))
        )
        actions.move_to_element(option).click().perform()

    def fill_form(self, last_name=None, company=None, account_name=None):

        if last_name and company:
            self.driver.find_element(By.XPATH, "(//input[@class='slds-input'])[3]").send_keys(last_name)
            self.driver.find_element(By.XPATH, "(//input[@class='slds-input'])[4]").send_keys(company)
        if account_name:
            self.driver.find_element(By.XPATH, "(//input[@class='slds-input'])[2]").send_keys(account_name)

    def save_form(self):

        self.driver.find_element(By.XPATH, "//button[@class='slds-button slds-button_brand']").click()

    def close_browser(self):
        """Closes the browser."""
        self.driver.quit()


# Usage Example
if __name__ == "__main__":
    chrome_binary_path = r"C:\Users\aarti.kyama\Downloads\chrome-win64 (1)\chrome-win64\chrome.exe"
    username = "satishkyama-fne0@force.com"
    password = "Anita@1164"

    automation = SalesforceAutomation(chrome_binary_path)

    try:
        automation.login(username, password)

        # Create a new account
        automation.click_dropdown_and_select(
            "//one-app-nav-bar-item-root[@data-id='Account']/one-app-nav-bar-item-dropdown", "New Account"
        )
        automation.fill_form(account_name="Aarti_1")
        automation.save_form()
    finally:
        automation.close_browser()
