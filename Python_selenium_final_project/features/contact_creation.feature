Feature: Create a New Contact

  Scenario: User creates a new contact
    Given the Salesforce home page is open
    When the user selects "New Contact" from the Contact dropdown
    And fills in the contact details with last name "ABC" and account "Aarti_K"
    And clicks the save button
    Then the contact should be created successfully
