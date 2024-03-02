Feature: this feature will contain only tests related to search

  @emag
  Scenario: I am on the main page and search for a specific item
    Given I am on the primary page
    When I click on the icon button
    When I enter this ISBN code "Politicieni de tot rasul"
    When I click the specific button
    Then The item with the title "Politicieni de tot rasul" should be visible
