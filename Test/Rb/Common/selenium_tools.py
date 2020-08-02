"""Selenium 相关封装"""
from HTMLReport import logger, addImage
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import logging



class SeleniumWebDriver(object):
    def __init__(self, driver, base_url):
        self.base_url = base_url
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Firefox()

    def get_browser(self):
        self.driver = webdriver.Firefox()
        logging.info("打开浏览器火狐浏览器")
        self.driver.implicitly_wait(10)
        logging.info("设置隐式等待 10 S")
        self.driver.maximize_window()
        logging.info("浏览器最大化")
        return self.driver

    def addImage(self):
        addImage(self.driver.get_screenshot_as_base64())

    def open(self, baseUrl, url):
        self.driver.get(baseUrl + url)

    def find_element(self, loc):
        return self.driver.find_element(*loc)