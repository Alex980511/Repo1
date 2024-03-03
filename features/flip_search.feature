Feature: this test suite tests search feature on Flip.ro website
  @Flip_pozitive
  Scenario: This scenario will test the search feature for a specific keyword
    Given I am on the base page
    When I click on the search
    When I enter the word "husa S20"
    When I click on the magnifier
    Then "husa S20" keyword is in title phrasing element
