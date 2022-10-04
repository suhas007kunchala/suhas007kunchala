from behave import *
from PageObjects.imgbb.Imgbb_Homepage import homepage


@given(u'user is on "{website}"')
def step_impl(context, website):
    context.imgbbhome = homepage(context.drive)
    context.imgbbhome.imgbbsite(website)


@then(u'user clicks on browse from computer')
def step_impl(context):
    context.imgbbhome.clickstartuploadbtn()


@then(u'user navigates to "{path}" and opens file')
def step_impl(context, path):
    context.imgbbhome.fileupload(path)


@then(u'user clicks on uplode button')
def step_impl(context):
    context.imgbbhome.clickstartuploadbtn()


@then(u'validate upload complete')
def step_impl(context):
    context.imgbbhome.validateuploadstatus()
