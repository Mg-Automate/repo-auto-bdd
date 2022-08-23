from selenium import webdriver
from web.web import Web

def browser_chrome(context, timeout=30, **kwargs):
    browser = webdriver.Chrome()
    web = Web(browser)
    context.web = web
    yield context.web
    browser.quit()