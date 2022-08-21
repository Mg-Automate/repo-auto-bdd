from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@given('lauch chrome')
def launchBrowser(context):
    Service()
    context.driver=webdriver.Chrome()


@when('open pravid home page')
def openHomePage(context):
    context.driver.get("https://pravid.io/")

@then('verify logo present on page')
def verifyLogo(context):
    word="LOGO ILLA"
    print(context)
    print(word)

@then('close browser')
def closeBrowser(context):
    context.driver.close()
