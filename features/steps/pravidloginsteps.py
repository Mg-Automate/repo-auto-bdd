import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@given(u'user is on the login page of pravid')
def On_Login(context):
    Service()
    context.driver = webdriver.Chrome()
    context.driver.get("https://pravid.io/login")

@when(u'user enters valid username "{username}" and valid password "{password}"')
def Enter_Credentials(context,username,password):
    context.driver.find_element("xpath", "//*[@type='email']").send_keys(username)
    context.driver.find_element("xpath", "//*[@type='password']").send_keys(password)
    #context.driver.find_element_by_xpath("//*[@type='email']").send_keys(username)
    #context.driver.find_element_by_xpath("//*[@type='password']").send_keys(password)


@when(u'click on login button')
def Login_btn(context):
    context.driver.find_element("xpath", "//*[@value='Login']").click()
    #context.driver.find_element_by_xpath("//*[@value='Login']").click()


@then(u'the user is logged in')
def LoggedIn(context):
    time.sleep(5)
    try:
        text = context.driver.find_element("xpath", "//*[@id='welcome_saarthi']").text
   # text = context.driver.find_element_by_xpath("//*[@id='welcome_saarthi']").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text=="Welcome!":
        context.driver.close()
        assert True, "Test Passed"

    #assert text=="Welcome!"
    #context.driver.close()

