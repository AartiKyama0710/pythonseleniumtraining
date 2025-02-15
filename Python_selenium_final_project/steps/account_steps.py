from pytest_bdd import given, when, then
from pages.account_page import AccountPage

@given("the Salesforce home page is open")
def open_home_page(browser):
    browser.get("https://login.salesforce.com/home")  # Adjust the home URL

@when('the user selects "New Account" from the Account dropdown')
def select_new_account(browser):
    account_page = AccountPage(browser)
    account_page.select_new_account()

@when('fills in the account name "<account_name>"')
def fill_account_name(browser, account_name):
    account_page = AccountPage(browser)
    account_page.fill_account_name(account_name)

@when("clicks the save button")
def save_account(browser):
    account_page = AccountPage(browser)
    account_page.save_account()

@then("the account should be created successfully")
def verify_account_creation():
    # Add verification logic
    pass
