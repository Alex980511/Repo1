from behave import *

@given('I am on the base page')
def step_impl(context):
    context.flip_search.navigate_to_page()

@when('I click on the search')
def step_impl(context):
    context.flip_search.click_on_the_search()

@when('I enter the word "{write}"')
def step_impl(context, write):
    context.flip_search.type_anything_on_search(write)

@when('I click on the magnifier')
def step_impl(context):
    context.flip_search.click_on_the_magnifier()

@then('"{write}" word is in title phrasing element')
def step_impl(context, write):
    assert write in context.flip_search.get_titile_text(), f"{write} is not found in title phrasing element"
