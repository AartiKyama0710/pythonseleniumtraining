from pytest_bdd import given, when, then
from pages.contact_page import ContactPage

@given("the Salesforce home page is open")
def open_home_page(browser):
    browser.get("https://login.salesforce.com/home")

@when('the user selects "New Contact" from the Contact dropdown')
def select_new_contact(browser):
    contact_page = ContactPage(browser)
    contact_page.select_new_contact()

@when('fills in the contact details with last name "<last_name>" and account "<account_name>"')
def fill_contact_details(browser, last_name, account_name):
    contact_page = ContactPage(browser)
    contact_page.fill_contact_details(last_name, account_name)

@when("clicks the save button")
def save_contact(browser):
    contact_page = ContactPage(browser)
    contact_page.save_contact()

@then("the contact should be created successfully")
def verify_contact_creation():
    # Add verification logic
    pass
