Feature: this feature will contain only tests related to search
  @carturesti_pozitive
  Scenario: I am on the main page and search for a specific book
    Given I am on the home page
    When I click on the find button
    When I enter this ISBN code "0602455725868"
    When I click the magnifier_button
    Then The vinyl with the title "Master of Puppets" should be visible

  @caruresti_search
  Scenario: I can navigate directly to page 109 for a specific key-word
    Given  I am the main page with "vinyl" keyword and page parameter "109"
    Then The current page selected is "109"
