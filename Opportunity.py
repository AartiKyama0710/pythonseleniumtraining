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

        # Open Chrome browser
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager(driver_version='130').install()),
            options=self.options
        )
        self.driver.implicitly_wait(20)  # Set implicit wait

    def login(self):

        self.driver.get("https://login.salesforce.com/?locale=in")

        # Log in
        self.driver.find_element(By.NAME, 'username').send_keys('satishkyama-fne0@force.com')
        self.driver.find_element(By.NAME, 'pw').send_keys("Anita@1164")
        self.driver.find_element(By.XPATH, "//input[@class='button r4 wide primary']").click()

    def create_opportunity(self):
        # Wait for the dropdown to be clickable
        dropdown = self.driver.find_element(By.XPATH, "//one-app-nav-bar-item-root[@data-id='Opportunity']/one-app-nav-bar-item-dropdown")
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown).click().perform()


        arrow = self.driver.find_element(By.XPATH, "//one-app-nav-bar-item-root[@data-id='Opportunity']/one-app-nav-bar-item-dropdown")
        new = arrow.find_element(By.XPATH, "//span[text()='New Opportunity']")
        actions.move_to_element(new).click().perform()
        time.sleep(5)

        # Fill in the form
        self.driver.find_element(By.XPATH, "(//input[@class='slds-input'])[2]").send_keys("Shanu")
        self.driver.find_element(By.XPATH, "//input[@class='slds-combobox__input slds-input']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Aarti_1')]").click()

        # Save the new opportunity
        self.driver.find_element(By.XPATH, '(//input[@class="slds-input"])[3]').click()
        self.driver.find_element(By.XPATH, "//td[@aria-label='2025-01-30']//span[@role='button'][normalize-space()='30']").click()
        time.sleep(5)

        # Scroll down to make all elements visible
        self.driver.execute_script("window.scrollBy(0,500);")
        time.sleep(5)

        # Select "Stage" option
        self.driver.find_element(By.XPATH, "(//button[@class='slds-combobox__input slds-input_faux fix-slds-input_faux slds-combobox__input-value'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Qualify')]").click()

        # Select "Forecast Category" option
        self.driver.find_element(By.XPATH, '(//button[@class="slds-combobox__input slds-input_faux fix-slds-input_faux slds-combobox__input-value"])[2]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Pipeline')]").click()

        # Submit the form
        self.driver.find_element(By.XPATH, "//button[@class='slds-button slds-button_brand']").click()
        time.sleep(1)

    def close_browser(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    automation = SalesforceAutomation()
    automation.login()
    automation.create_opportunity()
    automation.close_browser()
