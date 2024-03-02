from behave import *

@given('I am on the primary page')
def step_impl(context):
    context.emag_search.navigate_to_page()

@when('I click on the icon button')
def step_impl(context):
    context.emag_search.click_on_icon_button()

@when('I enter the keyword "{keyword}"')
def step_impl(context, keyword):
    context.emag_search.type_anything_on_search(keyword)

@when('I click on specific button')
def step_impl(context):
    context.emag_search.click_on_specific_button()

@then('"{keyword}" keyword is in title phrasing element')
def step_impl(context, keyword):
    assert keyword in context.emag_search.get_title_text(), f"{keyword} is note found in title phrasing after search"