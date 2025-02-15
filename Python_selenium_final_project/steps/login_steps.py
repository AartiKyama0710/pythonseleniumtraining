from pytest_bdd import given, when, then
from pages.login_page import LoginPage

@given("the Salesforce login page is open")
def open_login_page(browser):
    browser.get("https://login.salesforce.com/?locale=in")

@when("the user enters username '<username>' and password '<password>'")
def enter_credentials(browser, username, password):
    login_page = LoginPage(browser)
    login_page.login(username, password)

@then("the user should be logged in successfully")
def verify_login():
    # Add verification logic
    pass
