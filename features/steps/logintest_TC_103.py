from behave import *
from PageObjects.yourlogo.yourlogo_login import loginmodule


@given(u'yourlogo website "{site}" is opened')
def step_impl(context, site):
    context.login = loginmodule(context.drive)
    context.login.yourlogosite(site)


@when(u'sign in button is clicked')
def step_impl(context):
    context.login.clicksingin()


@then(u'use "{email}" to enter email')
def step_impl(context, email):
    context.login.enteremail(email)


@then(u'use "{password}" to enter password')
def step_impl(context, password):
    context.login.enterpassword(password)


@then(u'click on sign in button')
def step_impl(context):
    context.login.clicklogin()


@then(u'user clicks sign out')
def step_impl(context):
    context.login.logout()


@then(u'validate login success')
def step_impl(context):
    assert context.login.loginsuccessmsg.__eq__(
        "Welcome to your account. Here you can manage all of your personal "
        "information and orders.")
