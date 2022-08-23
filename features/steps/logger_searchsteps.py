import time
import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from Pages.LoginPage import Login

@given(u'user is on the login page of chathistory')
def On_Login(context):
    Service()
    context.driver = webdriver.Chrome()
    context.driver.get("https://chathistory.saarthi.ai/login")


@when(u'select Logger tab')
def logger_tab(context):
    time.sleep(5)
    context.driver.find_element("xpath", "//h6[.=' Logger ']").click()
    time.sleep(3)


@when(u'Select Date Range')
def logger_dateRange(context):
    pass


@when(u'click on search button and search by phone number "{phone}"')
def step_impl(context,phone):
    global search_feild
    search_feild = context.driver.find_element("xpath","//input[@placeholder='Phone Number or Loan Id']")
    search_feild.Send_keys(phone)
    time.sleep(5)
    return search_feild

@then(u'Logger data should be for provided number')
def step_impl(context):
    htmltable = context.driver.findElement("xpath","//*[@id='main']/table[1]/tbody");
    rows = htmltable.findElements("tagName","tr");
"""
    for (int rnum=0;rnum < rows.size();rnum++):
    for 
    {
    columns = rows.get(rnum).findElements(By.tagName("th"));
    System.out.println("Number of columns:" + columns.size());

    for (int cnum=0;cnum < columns.size();cnum++)
    {
    System.out.println(columns.get(cnum).getText());
    }
    }

    pass

@when(u'click on search button and search by loan ID "{loan_id}"')
def step_impl(context,loan_id):
    search_feild.Send_keys(loan_id)


@then(u'Logger data should be for provided loan ID')
def step_impl(context):
   pass