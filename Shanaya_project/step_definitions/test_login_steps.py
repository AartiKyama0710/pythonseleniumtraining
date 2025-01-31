import pytest
from pytest_bdd import given, when, then
from pages.login_page import LoginPage

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@given("the login page is open")
def open_login_page(browser):
    browser.get("https://login.salesforce.com/?locale=in")

@when("the user enters a valid username and password")
def enter_credentials(login_page):
    login_page.enter_username("satishkyama-fne0@force.com")
    login_page.enter_password("Anita@1164")

@when("clicks the login button")
def click_login(login_page):
    login_page.click_login()

@then("the user should be redirected to the homepage")
def verify_homepage(browser):
    assert "home" in browser.current_url  # Adjust based on actual Salesforce URL
