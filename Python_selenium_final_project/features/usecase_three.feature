Feature: Use Case Three - Create and Validate Event

  Background:
    Given the user logs into Salesforce

  Scenario: Create an event and validate it
    When the user creates an event with subject: "ICC_Champions", date: "25-Mar-2025", time: "10:00 pm", and account: "Acc_Meeting"
    Then the event should be created and validated with subject: "ICC_Champions", date: "25-Mar-2025", time: "10:00 pm", and account: "Acc_Meeting"
