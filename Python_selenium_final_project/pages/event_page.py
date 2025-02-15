import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class EventPage(BasePage):
    CALENDAR = (By.XPATH, "//div[@id='calendar']")
    NEW_EVENT = (By.XPATH, "//button[@id='new_event']")
    EVENT_SUBJECT = (By.XPATH, "//input[@id='event_subject']")
    START_DATE = (By.XPATH, "//input[@id='start_date']")
    START_TIME = (By.XPATH, "//input[@id='start_time']")
    ACCOUNT_SEARCH = (By.XPATH, "//input[@id='account_search']")
    EVENT_SAVE_BUTTON = (By.XPATH, "//button[@id='save_event']")
    EVENT_DETAILS = (By.XPATH, "//div[@class='event_details']")

    def create_event(self, subject, date, time, account):
        self.click_element(self.CALENDAR)
        self.click_element(self.NEW_EVENT)
        self.enter_text(self.EVENT_SUBJECT, subject)
        self.enter_text(self.START_DATE, date)
        self.enter_text(self.START_TIME, time)
        self.enter_text(self.ACCOUNT_SEARCH, account)
        time.sleep(2)  # Wait for account suggestions
        self.click_element((By.XPATH, f"//span[contains(text(),'{account}')]"))
        self.click_element(self.EVENT_SAVE_BUTTON)

    def validate_event(self, subject, date, time, account):
        time.sleep(2)
        date_obj = datetime.strptime(date, "%d-%b-%Y")
        year = Select(self.driver.find_element(By.XPATH, "//select[@id='year_selector']"))
        year.select_by_visible_text(str(date_obj.year))
        while date_obj.strftime("%B").upper() != self.driver.find_element(By.XPATH, "//div[@id='month_display']").text:
            self.click_element((By.XPATH, "//button[@id='next_month']"))

        self.click_element((By.XPATH, f"//div[@data-date='{date_obj.strftime('%Y-%m-%d')}']"))
        self.click_element((By.XPATH, f"//div[text()='{subject}']"))
        event_details = self.wait_for_element(self.EVENT_DETAILS).text

        return (subject in event_details and
                date in event_details and
                time in event_details and
                account in event_details)
