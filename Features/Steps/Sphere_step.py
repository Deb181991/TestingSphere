# import argparse
import time

from behave import *

from Pages.Sphere_Page import LoginPage
from Utilities.GenericMethod import genericmethod
from Utilities.customLogger import LogGen

global lPage


# baseURL = ReadConfig.getURL()
myLogger = LogGen.loggeen()


# ********************* Login *********************************************
@given(u'launch the "{Sphere_Url}"')
def LandingPage(context, Sphere_Url):
    # global lPage
    lPage = LoginPage(context.driver)
    context.gMethod = genericmethod(context.driver)
    myLogger.info("****** Url Launched ******")
    time.sleep(2)
    lPage.LaunchBrowser(Sphere_Url)


@then(u'Enter the "{username}" in the username field')
def step_impl(context, username):
    myLogger.info('******Entering Username **********')
    lPage.enterUserName(username)


@then(u'Enter the "{password}" in the Password field')
def step_impl(context, password):
    lPage.enterPassword(password)


@then('click on login button')
def step_impl(context):
    lPage.clickOnLogin()


@then('click on dashboard page')
def step_impl(context):
    lPage.Dashboard_Menu()


@then('click on target portal')
def step_impl(context):
    lPage.Target_Portal()


@then('click on truck information')
def step_impl(context):
    lPage.Truck_Information()


@then('click on truck schedule')
def step_impl(context):
    lPage.Truck_Schedule()


@then('click on new request')
def step_impl(context):
    lPage.New_Request()


@then('select Type from the "{SelectType}" dropdown')
def step_impl(context, SelectType):
    lPage.Enter_Request(SelectType)


@then('select "{ServiceProvider}" from the dropdown')
def step_impl(context, ServiceProvider):
    lPage.Service_Provider(ServiceProvider)


@then('select In Store Date from the calander')
def step_impl(context):
    lPage.InStore_Date()


@then('select "{Origin}" from the Origin dropdown')
def step_impl(context, Origin):
    lPage.TargetOrigin(Origin)


@then('select "{Destination}" from the Destination dropdown')
def step_impl(context, Destination):
    lPage.TargetDestination(Destination)


@then('select Requested Pickup Date from the calander')
def step_impl(context):
    lPage.RequestedPickUpDate()


@then('select Requested Delivery Date from the calander')
def step_impl(context):
    lPage.RequestedDeliveryDate()


@then('enter request "{time}" in Pickup field')
def step_impl(context, time):
    lPage.PickUptime(time)


@then('enter request "{time}" in Delivery field')
def step_impl(context, time):
    lPage.Deliverytime(time)


@then('click on submit')
def step_impl(context):
    lPage.submit()
    
@then('confirm the details')
def step_impl(context):
    lPage.ConfirmDetails()

# @then('Please enter the intent with "{customerName}"')
# def step_impl(context, customerName):
#     lPage.CustName(customerName)

@then('click on Allocation Menu')
def step_impl(context):
    lPage.Aloction()

@then('click on Pick Submenu')
def step_impl(context):
    lPage.PickButton()

@then('choose "{location}" from location dropdown box')
def step_impl(context,location):
    lPage.locationDropDown(location)

@then('click on getNextPick button')
def step_impl(context):
    lPage.getNextPickButton()    
@then('enter "{Lp}" in Scan License Plate field')
def step_impl(context,Lp):
    lPage.EnterLP(Lp)    
