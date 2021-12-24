# coding:utf-8
__author__ = 'connie'
'''
description: 测试修改个人信息
'''

import unittest, time
from src.pages import profile
from src.common import driverConf, gestureManipulation



class TestEditProfile(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driverConf.DriverConfigure().get_driver()
        cls.GM = gestureManipulation.GestureManipulation()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        # cls.driver.quit()

    def test_edit_name(self,name="connie"):
        """ 修改用户名"""
        self.Profile = profile.EditProfile(self.driver)
        self.Profile.go_profile()
        self.Profile.edit_profile()
        self.Profile.edit_displayname(name)
        self.Profile.click_blank()
        self.Profile.click_save()
        self.Profile.click_back()

    def test_edit_description(self,description_text="my name is connie，hahahaha👌"):
        """ 修改个人简介"""
        self.Profile = profile.EditProfile(self.driver)
        self.Profile.go_profile()
        self.Profile.edit_profile()
        self.Profile.eit_description(description_text)
        self.Profile.click_blank()
        self.Profile.click_save()
        self.Profile.click_back()

    # def test_edit_photo(self):
    #     """ 修改头像"""
    #     self.Profile = editProfile.EditProfile(self.driver)
    #     self.Profile.go_profile()
    #     self.Profile.edit_profile()
    #     self.Profile.click_photo()
    #     self.Profile.select_photo()
    #     self.Profile.click_done()
    #     self.Profile.click_save()
    #     self.Profile.click_back()

    def test_conis(self,code="happyeaster76"):
        """ 积分"""
        self.Profile = profile.EditProfile(self.driver)
        self.Profile.go_profile()
        self.Profile.click_coins()
        # self.Profile.click_collect()
        self.Profile.promo(code)
        self.Profile.click_apply()
        time.sleep(8)
        self.Profile.click_shopnow()
        self.Profile.click_shopnow_backs()

    def test_history_stream(self):
        """ 查看历史回放"""
        self.Profile = profile.EditProfile(self.driver)
        self.Profile.go_profile()
        self.Profile.click_livestreams()
        self.Profile.scroll_to_a()
        self.Profile.replay_back_scroll()

    def test_order(self):
        """查看历史订单"""
        self.Profile = profile.EditProfile(self.driver)
        self.Profile.go_profile()
        self.Profile.order_click()
        self.Profile.order_detail_click()
        self.Profile.order_back()
        self.Profile.order_back()

































