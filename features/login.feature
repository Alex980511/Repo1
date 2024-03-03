Feature: Tests for login page
  @Login_negaitve
  Scenario: The user cannot login with invalid credentials
    Given I am on the login page
    When I insert a username "alex@yahoo.com"
    When I insert a password "masina123"
    When I click on the login button
    Then The banner is displayed
    Then The message is "Your username is invalid"

  @Login_pozitive
  Scenario Outline: The user can login with valid credentials
    Given I am on the login page
    When I insert a username "<email>"
    When I insert a password "<password>"
    When I click on the login button
    Then The banner is displayed
    Then The message is "You logged into a secure area"

  Examples:
    |  email   | password             |
    |  alex    | alex123              |
    |  minge   | minge12              |
    | tomsmith | SuperSecretPassword! |