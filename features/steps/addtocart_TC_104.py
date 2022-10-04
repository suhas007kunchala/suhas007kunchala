from behave import *

from PageObjects.yourlogo.MyStore_Homepage import Homepage
from PageObjects.yourlogo.MyStore_OrderPage import Orderpage
from PageObjects.yourlogo.MyStore_Womentabpage import Womenpage
from PageObjects.yourlogo.MyStore_Twitter import twitterpage
from PageObjects.yourlogo.yourlogo_login import loginmodule


@given(u'user is on home page')
def step_impl(context):
    context.homepg = Homepage(context.drive)
    context.womenpg = Womenpage(context.drive)
    context.orderpg = Orderpage(context.drive)
    context.twitter = twitterpage(context.drive)
    context.loginmod = loginmodule(context.drive)
    context.execute_steps(u'''
        Given yourlogo website "http://automationpractice.com/index.php" is opened
        When sign in button is clicked
        Then use "gm63@live.com" to enter email
        Then use "lkjh1234" to enter password
        Then click on sign in button
        Then validate login success
    ''')
    context.homepg.clickhomebtn()


@when(u'user clicks on "{tab}" module')
def step_impl(context, tab):
    context.homepg.clickwomentab(tab)


@then(u'user checks tops checkbox')
def step_impl(context):
    context.womenpg.topscheckbox()


@then(u'user selects "{value}" option')
def step_impl(context, value):
    context.womenpg.sort_by(value)


@then(u'user slides low to "{low}" and high to "{high}"')
def step_impl(context, low, high):
    context.womenpg.sliderlow(low)


@when(u'user hovers over product')
def step_impl(context):
    context.womenpg.hoverover()


@then(u'user clicks on quick view')
def step_impl(context):
    context.womenpg.clickquickview()


@then(u'user selects "{val}" size option')
def step_impl(context, val):
    context.womenpg.selectsize(int(val))


@then(u'user clicks on Add to cart')
def step_impl(context):
    context.womenpg.clickaddtocart()


@then(u'user clicks on Proceed to checkout')
def step_impl(context):
    context.womenpg.clickcheckout()


@then(u'user checks "{stage}" and clicks on checkout')
def step_impl(context, stage):
    context.orderpg.clickproceedtocheckout(stage)


@then(u'user checks Delivery "{stage}" and clicks on checkout')
def step_impl(context, stage):
    context.orderpg.clickproceedtocheckout(stage)


@then(u'user checks i agree in "{stage}" details and click on checkout')
def step_impl(context, stage):
    context.orderpg.checktermsandconditions()
    context.orderpg.clickproceedtocheckout(stage)


@then(u'user clicks on Pay by bank wire')
def step_impl(context):
    context.orderpg.clickpaybywire()


@then(u'user clicks on I confirm my order')
def step_impl(context):
    context.orderpg.clickconfirmord()


@then(u'user should see order complete message')
def step_impl(context):
    context.orderpg.validateorder()


@then(u'user clicks on Home button')
def step_impl(context):
    context.homepg.clickhomebtn()


@then(u'user vists yourlogo twitter page')
def step_impl(context):
    context.homepg.clicktwitter()


@then(u'user clicks on follow button')
def step_impl(context):
    context.twitter.clickfollowbtn()


@then(u'user navigates back to yourlogo page')
def step_impl(context):
    context.homepg.yourlogowindow()


@then(u'user logout from yourlogo website')
def step_impl(context):
    context.loginmod.logout()
