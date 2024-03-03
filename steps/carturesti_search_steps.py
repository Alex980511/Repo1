from behave import *

@given('I am on the home page')
def step_impl(context):
    context.carturesti_search.navigate_to_page()

@given('I am the main page with "{keyword}" keyword and page parameter "{page_parameter}"')
def step_impl(context, keyword, page_parameter):
    context.carturesti_search.navigate_to_page_with_key_word(keyword, page_parameter)

@when('I click on the find button')
def step_impl(context):
    context.carturesti_search.click_in_search_button()

@when('I enter this ISBN code "{isbn}"')
def step_impl(context, isbn):
    context.carturesti_search.type_anything_on_search(isbn)

@when('I click the magnifier_button')
def step_impl(context):
    context.carturesti_search.click_on_magnifier_button_1()

@then('The vinyl with the title "{keyword}" should be visible')
def step_impl(context, keyword):
    assert keyword in context.carturesti_search.get_title_text()

@then('The current page selected is "{current_page_number}"')
def step_impl(context, current_page_number):
    assert current_page_number in context.carturesti_search.get_current_page_text()