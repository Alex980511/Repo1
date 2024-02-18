Feature: Tests for login page
  @FailLogin
  Scenario: This is a negative scenario
    Given I am on the login page
    When I insert a username "alex@yahoo.com"
    When I insert a password "masina123"
    When I click on the login button
    Then The banner is displayed
    Then The message is "Your username is invalid"

  @PozitiveLogin
  Scenario: This is a pozitive scenario
    Given I am on the login page
    When I insert a username "tomsmith"
    When I insert a password "SuperSecretPassword!"
    When I click on the login button
    Then The banner is displayed
    Then The message is "You logged into a secure area"

