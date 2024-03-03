from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate_to_page()

@when('I insert a username "{username}"')
def step_impl(context, username):
    context.login_page.set_email(username)

@when('I insert a password "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)

@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login()

@then('The banner is displayed')
def step_impl(context):
    context.login_page.is_message_displayed()

@then('The message is "{message}"')
def step_impl(context, message):
    try:
        text = context.login_page.get_message_text("{message}").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text== "You logged into a secure are":
        context.driver.close()
        assert True, "Test Passed"
    #assert message in context.login_page.get_message_text(), f"Message is not the same.Expected:{message},Actual message:{context.login_page.get_message_text()}"

