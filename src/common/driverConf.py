# coding:utf-8
__author__ = 'Helen'

from lib2to3.pgen2 import driver

'''
description:driver配置
'''
from appium import webdriver


class DriverConfigure():
    def get_driver(self):
        '''获取driver'''
        try:
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'ios'  # 平台
            self.desired_caps['platformVersion'] = '15.0'  # 系统版本
            self.desired_caps['automationName'] = 'XCUITest'
            self.desired_caps['bundleId'] = 'live.lit.lit-live'
            self.desired_caps['xcodeOrgId'] = 'ZW458Z7F9U'
            self.desired_caps["appium:deviceName"] = "iPhone 13 Pro"
            self.desired_caps['xcodeSigningId'] = 'Apple Development'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)
            return self.driver

        except Exception as e:
            raise e
