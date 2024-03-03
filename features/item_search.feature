Feature: this feature will contain only tests related to search
  @Libra_pozitive
  Scenario: I am on the main page and search for a specific item
    Given I am on the main page
    When I click on the search button
    When I enter "Politicieni de tot rasul"
    When I click the magnifier
    Then The item with the title "Politicieni de tot rasul" should be visible
