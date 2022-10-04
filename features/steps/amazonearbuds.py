from behave import *
from helpers.helper_base import Helperbase

hbls = Helperbase()


@given(u'user is on "{site}"')
def step_impl(context, site):
    hbls.visturl(site)


@then(u'user search for "{x}"')
def step_impl(context, x):
    hbls.filltext_xpath(x)


@then(u'user checks with microphone and wireless box')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user checks with microphone and wireless box')


@then(u'open each earbud link')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then open each earbud link')


@then(u'get required data')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then get required data')


@then(u'connect to database')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then connect to database')


@then(u'update data in table')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then update data in table')
