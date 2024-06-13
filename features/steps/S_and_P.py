from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_relly_signup(context):
    context.app.main_page.open_main()


@given('Click Sign in')
def click_sign_in(context):
    context.app.main_page.click_sign_in(context)


@then('Input email')
def input_email(context):
    context.app.sign_in_page.input_email(context)


@then('Input password')
def input_password(context):
    context.app.sign_in_page.input_password(context)


@then('Click on Continue button')
def click_continue(context):
    context.app.sign_in_page.click_continue(context)
    sleep(6)

@then('Click on Settings option')
def click_settings_option(context):
    context.app.sign_in_page.click_settings_option(context)
    sleep(6)


@when('Click on Subscription & payments option')
def click_subscription_and_payments(context):
    context.app.sign_in_page.click_subscription_and_payments(context)
    sleep(6)


@then('Verify title Subscription & payments is visible')
def verify_subscription_and_payments_text(context):
    context.app.sign_in_page.verify_subscription_and_payments_text()


@then('Verify Back button is available')
def verify_back_button_available(context):
    context.app.sign_in_page.verify_back_button_available()


@then('Verify  upgrade plan button is available')
def verify_upgrade_plan_available(context):
    context.app.sign_in_page.verify_upgrade_plan_available()
