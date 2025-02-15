Feature: Create a New Account

  Scenario: User creates a new account
    Given the Salesforce home page is open
    When the user selects "New Account" from the Account dropdown
    And fills in the account name "Aarti_1"
    And clicks the save button
    Then the account should be created successfully
