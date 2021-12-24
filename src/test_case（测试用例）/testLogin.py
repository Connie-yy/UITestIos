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
        cls.GM = gestureManipulation.GestureManipulation()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        # cls.driver.quit()

    def test_index_page(self):
        self.loginPage = login.LoginPage(self.driver)

        # self.loginPage.select_profile_page()
        time.sleep(10)
        # self.GM.swipe_up(self.driver, 3000)
        #
        # time.sleep(3)
        self.GM.swipe_down(self.driver, 3000)
        #
        self.loginPage.email_login_action()
        self.loginPage.login_email_account("connie")
        self.loginPage.login_account_next_action()
        self.loginPage.login_input_account_password("123456789")
        self.loginPage.login_select_secret()
        self.loginPage.login_select_secret()
        self.loginPage.login_account_login_action()



