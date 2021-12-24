# coding:utf-8
__author__ = 'jack'
'''
description: 手势操作
'''

import time

from src.common import basePage
from appium.webdriver.common import mobileby


class LoginPage(basePage.BasePage):
    def __init__(self):
        self.by = mobileby.MobileBy()

    def indexProfilePage(self):
        index_loc = (self.by.XPATH, '//XCUIElementTypeNavigationBar[@name="Lit_Live.HomeView"]/XCUIElementTypeOther/XCUIElementTypeOther[1]')
        self.find_element(*index_loc).click()
        time.sleep(10)










        