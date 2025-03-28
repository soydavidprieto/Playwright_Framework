Feature: Login validation for known and unknown users

  Scenario Outline: Login with different user types
    Given the user is on the login page
    When they log in as "<user_type>"
    Then the system should respond appropriately for "<user_type>"

  Examples:
    | user_type |
    | default   |
    | manager   |
    | readonly  |
    | invalid   |
