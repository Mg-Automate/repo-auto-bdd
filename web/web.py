from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Web(object):
    __TIMEOUT = 10

    def __init__(self, web_driver):
        super().__init__()
        self._web_driver_wait = WebDriverWait(web_driver, Web.__TIMEOUT)
        self.__web_driver = web_driver

