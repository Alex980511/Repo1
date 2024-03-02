from behave import *

@given ('I am on the main page')
def step_impl(context):
    context.item_search.navigate_to_page()

@when ('I click on the search button')
def step_impl(context):
    context.item_search.click_on_search_button()

@when('I enter this ISBN code "{isbn}"')
def step_impl(context, isbn):
    context.item_search.type_anything_on_search(isbn)

@when ('I click the magnifier')
def step_impl(context):
    context.item_search.click_on_magnifier_button()

@then ('The item with the title "{booktitle}" should be visible')
def step_impl(context, booktitle):
    assert booktitle in context.item_search.get_title_text()