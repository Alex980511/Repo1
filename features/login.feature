Feature: Tests for login page
  @Login_pozitive
  Scenario Outline: The user can login with valid credentials
    Given I am on the login page
    When I insert a username "<email>"
    When I insert a password "<password>"
    When I click on the login button
    Then The banner is displayed
    Then The message is "<message>"

  Examples:
    |  email                    | password             |    message  |
    |  alex                     | alex123              |Your username is invalid!       |
    |  minge                    | minge12              |Your username is invalid!       |
    | tomsmith                  | SuperSecretPassword! |You logged into a secure area! |