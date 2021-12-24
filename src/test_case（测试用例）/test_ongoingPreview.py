# coding:utf-8
__author__ = 'connie'
'''
description: 测试绑定商品开直播
'''

import unittest, time
from src.pages import ongoingPreview
from src.common import driverConf, gestureManipulation


class TestOngoingPreview(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driverConf.DriverConfigure().get_driver()
        cls.GM = gestureManipulation.GestureManipulation()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        # cls.driver.quit()

    def test_click_preview(self):
        '''拿手柄,绑定商品开预播'''
        self.OngPreview = ongoingPreview.Ongoing(self.driver)
        self.GM.swipe_value(250,0.5,0.9,0.5,0.1)



















