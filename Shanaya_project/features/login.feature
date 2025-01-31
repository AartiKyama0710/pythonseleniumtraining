Feature: Login Functionality

  Scenario: Successful Login with Valid Credentials
    Given the login page is open
    When the user enters a valid username and password
    And clicks the login button
    Then the user should be redirected to the homepage
