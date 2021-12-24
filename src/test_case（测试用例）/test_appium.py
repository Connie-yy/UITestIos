# coding:utf-8
__author__ = 'jack'
'''
description: 测试登录和登出功能
'''

import unittest, time
from src.pages import login
from src.common import driverConf, gestureManipulation



class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driverConf.DriverConfigure().get_driver()
        cls.GM = gestureManipulation.gesture_mainpulation()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        # cls.driver.quit()

    def test_index_page(self):
        self.loginPage = login.LoginPage(self.driver)
        self.loginPage.select_profile_page()
        self.loginPage.scroll_value()


    def test_live(self):
        pass














