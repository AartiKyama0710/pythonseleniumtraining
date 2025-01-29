import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class SalesforceAutomation:
    def __init__(self):
        # Initialize ChromeOptions
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-popup-blocking')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('disable-infobars')
        self.options.add_argument('--whitelisted-ips')
        self.options.add_argument('--remote-debugging-port=9222')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--window-size=1366,2000')
        self.options.add_argument('--start-maximized')
        self.options.add_argument("--incognito")
        self.options.add_argument("--remote-allow-origins=*")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument("--ignore-ssl-errors")
        self.options.add_argument("--allow-running-insecure-content")
        self.options.add_argument('--disable-blink-features=AutomationControlled')

        self.chrome_binary_path = r"C:\Users\aarti.kyama\Downloads\chrome-win64 (1)\chrome-win64\chrome.exe"
        self.options.binary_location = self.chrome_binary_path


        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(driver_version='130').install()),
            options=self.options
        )
        self.driver.implicitly_wait(20)  # Set implicit wait

    def login_and_create_contact(self):

        self.driver.get("https://login.salesforce.com/?locale=in")

        # Log in
        self.driver.find_element(By.NAME, 'username').send_keys('satishkyama-fne0@force.com')
        self.driver.find_element(By.NAME, 'pw').send_keys("Anita@1164")
        self.driver.find_element(By.XPATH, "//input[@class='button r4 wide primary']").click()


        dropdown = self.driver.find_element(By.XPATH, "//one-app-nav-bar-item-root[@data-id='Contact']/one-app-nav-bar-item-dropdown")
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown).click().perform()

        # Hide visual message queue
        self.driver.execute_script("document.querySelector('.forceVisualMessageQueue').style.display='none';")
        time.sleep(5)

        # Interact with "New Contact" option
        arrow = self.driver.find_element(By.XPATH, "//one-app-nav-bar-item-root[@data-id='Contact']/one-app-nav-bar-item-dropdown")
        new = arrow.find_element(By.XPATH, "//span[text()='New Contact']")
        actions.move_to_element(new).click().perform()
        time.sleep(5)

        # Fill in the form
        self.driver.find_element(By.XPATH, "(//input[@class='slds-input'])[3]").send_keys("ABC")
        self.driver.find_element(By.XPATH, "(//input[@class='slds-combobox__input slds-input'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Aarti_K')]").click()

        # Save the new contact
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@class='slds-button slds-button_brand']").click()

    def close_browser(self):
        self.driver.quit()



if __name__ == "__main__":
    automation = SalesforceAutomation()
    automation.login_and_create_contact()
    automation.close_browser()
