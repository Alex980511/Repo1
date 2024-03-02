Feature: this test suite tests search feature on Emag.ro website

  @emag
  Scenario: This scenario will test the search feature for a specific keyword
    Given I am on the primary page
    When I click on the icon button
    When I enter the keyword "iphone15"
    When I click on specific button
    Then "iphone15" keyword is in title phrasing element
