# coding:utf-8
__author__ = 'connie'
'''
description: 测试绑定商品开直播
'''

import unittest, time
from src.pages import livePreview
from src.common import driverConf, gestureManipulation


class TestScheduleLive(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driverConf.DriverConfigure().get_driver()
        cls.GM = gestureManipulation.GestureManipulation()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        # cls.driver.quit()

    def test_binding_product_preview(self,title=None,description=None,hashtag=None,search=None):
        '''拿手柄,绑定商品开预播'''
        self.Preview = livePreview.LivePreview(self.driver)
        self.Preview.go_live()
        # self.ScheduleLive.access_camera()
        # self.ScheduleLive.access_microphone()
        self.Preview.click_schedule()

        self.Preview.add_stream_cover()
        self.Preview.select_photo()
        self.Preview.click_done()
        self.Preview.add_preview_video()
        self.Preview.stream_title(title)
        self.Preview.stream_now_scroll_a()
        self.Preview.description(description)
        self.Preview.hashtag_text(hashtag)
        self.Preview.next_bath()
        self.Preview.add_product()
        self.Preview.search_product(search)
        self.Preview.click_product()
        self.Preview.click_add()
        self.Preview.click_next()
        self.GM.swipe_up()
        self.Preview.click_preview_next()

    def test_skip_product_preview(self,title=None,description=None,hashtag=None,search=None):
        '''拿手柄,skip商品开预播'''
        self.Preview = livePreview.LivePreview(self.driver)
        self.Preview.go_live()
        self.Preview.access_camera()
        self.Preview.access_microphone()
        self.Preview.click_schedule()
        self.Preview.add_stream_cover()
        self.Preview.select_photo()
        self.Preview.click_done()
        self.Preview.add_preview_video()
        self.Preview.stream_title(title)
        self.GM.swipe_up()
        self.Preview.description(description)
        self.Preview.hashtag_text(hashtag)
        self.Preview.next_bath()
        self.Preview.skip_product()
        self.GM.swipe_up()
        self.Preview.click_preview_next()

    # def test_edit_product_preview(self,title=None,description=None,hashtag=None,search=None):
    #     '''拿手柄,修改商品开预播'''
    #     self.Preview = livePreview.LivePreview(self.driver)
    #     self.ScheduleLive.go_live()
    #     self.ScheduleLive.access_camera()
    #     self.ScheduleLive.access_microphone()
    #     self.ScheduleLive.click_schedule()
    #     self.ScheduleLive.add_stream_cover()
    #     self.ScheduleLive.select_photo()
    #     self.ScheduleLive.click_done()
    #     self.ScheduleLive.add_preview_video()
    #     self.ScheduleLive.stream_title(title)
    #     self.GM.swipe_up()
    #     self.ScheduleLive.description(description)
    #     self.ScheduleLive.hashtag_text(hashtag)
    #     self.ScheduleLive.next_bath()
    #     self.ScheduleLive.add_product()
    #     self.ScheduleLive.search_product(search)
    #     self.ScheduleLive.click_product()
    #     self.ScheduleLive.click_product_b()
    #     self.ScheduleLive.click_add()
    #     self.ScheduleLive.edit_product()
    #     self.ScheduleLive.add_product_c()
    #     self.ScheduleLive.click_add()
    #     self.ScheduleLive.click_next()
    #     self.GM.swipe_up()
    #     self.ScheduleLive.click_preview_next()
    #

A = TestScheduleLive()




























