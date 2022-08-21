import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@then(u'username should be displayed as "Admin User" for prod credentials')
def step_impl(context):
    print(context.driver.find_element("xpath","//span[contains(text(),'Admin')]").text)
    assert True,"Logged In using Admin Credentials"

@then(u'click on the logger button')
def step_impl(context):
    context.driver.find_element("xpath", " //h6[.=' Logger ']").click()
    Actual_url = context.driver.current_url.text
    Expected_url = "https://pravid.io/calllogger"
    assert Actual_url==Expected_url


@then(u'logger page should be displayed')
def step_impl(context):
    Actual_url = context.driver.current_url.text
    Expected_url = "https://pravid.io/calllogger"
    assert Actual_url == Expected_url

@then(u'click on the analytics button')
def step_impl(context):
    context.driver.find_element("xpath", "//h6[.=' Analytics ']").click()


@then(u'analytics page should be displayed')
def step_impl(context):
    Actual_url = context.driver.current_url.text
    Expected_url = "https://pravid.io/dashboard"
    assert Actual_url == Expected_url


@then(u'click on Campaign button')
def step_impl(context):
    context.driver.find_element("xpath", "//h6[.='Campaign']").click()


@then(u'select campaign manager')
def step_impl(context):
    context.driver.find_element("xpath", " //p[.='campaign manager']").click()


@then(u'Campaign page should be displayed')
def step_impl(context):
    Actual_url = context.driver.current_url.text
    Expected_url = "https://pravid.io/campaignmanager"
    assert Actual_url == Expected_url

