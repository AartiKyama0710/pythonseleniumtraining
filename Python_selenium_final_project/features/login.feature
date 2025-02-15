Feature: Salesforce Login

  Scenario: User logs in to Salesforce
    Given the Salesforce login page is open
    When the user enters username "satishkyama-fne0@force.com" and password "Anita@1164"
    And clicks the login button
    Then the user should be logged in successfully
