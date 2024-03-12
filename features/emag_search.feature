Feature: this test suite tests search feature on Emag.ro website
 @emag_pozitive
  Scenario: This scenario will test the search feature for a specific keyword
    Given I am on the primary page
    When I click on the icon button
    When I enter the keyword "iphone15"
    When I click on specific button
    Then "iphone15" keyword is in title phrasing element

@emag_negative
  Scenario: This scenario will test a negative case for a non existing product
    Given I am on the primary page
    When I click on the icon button
    When I enter the keyword "bvdfvasdfafdsc"
    When I click on specific button
    Then ""bvdfvasdfafdsc" 200 rezultate." is in title phrasing number element