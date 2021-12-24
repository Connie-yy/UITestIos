'''
description: 测试预播 分享
'''

import unittest, time
from src.pages import ongoingBrand
from src.pages import productDetail
from src.common import driverConf, gestureManipulation


class TestOngoingBrand(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driverConf.DriverConfigure().get_driver()
        cls.GM = gestureManipulation.GestureManipulation()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        # cls.driver.quit()

    def test_brand_(self):
        """ 点击商家头像进入商家主页,进入商品详情页，点击all"""
        self.Brand = ongoingBrand.OngoingBrand()
        self.Brand.click_follow()
        self.Brand.click_brand_photo()
        self.Brand.click_close()
        self.Brand.click_back()
        self.Brand.click_product_detail()
        self.Brand.click_product_back()
        self.Brand.click_all()

    def test_brand_name(self):
        """ 点击商家名进入商家主页"""
        self.Brand = ongoingBrand.OngoingBrand()
        self.Brand.click_follow()
        self.Brand.click_brand_name()
        self.Brand.click_close()
        self.Brand.click_back()

    def test_brand_followers(self):
        """ 点击商家粉丝数量进入商家主页"""
        self.Brand = ongoingBrand.OngoingBrand()
        self.Brand.click_follow()
        self.Brand.click_brand_followers()
        self.Brand.click_close()
        self.Brand.click_back()

    def test_product_detail(self):
        """ 从商家模块进入商品详情页，收藏商品、添加商品进购物车、点击description,variant_see_all,分享"""
        self.Brand = ongoingBrand.OngoingBrand()
        self.Detail = productDetail.ProductDetail()
        self.Brand.click_product_detail()
        self.GM.swipe_value(250,0.5,0.9,0.5,0.1)
        self.Detail.click_video_close()
        self.GM.swipe_up()
        self.Detail.click_description()
        self.Detail.product_variant_see_all()
        self.Detail.click_add_bag()
        self.Detail.click_save_product()
        self.Detail.click_add_bag()
        self.Detail.share_product()
        self.Brand.click_product_back()

    def test_rating(self):
        """ 点击rating文案，跳转至评论页面"""
        self.Brand = ongoingBrand.OngoingBrand()
        self.Detail = productDetail.ProductDetail()
        self.Brand.click_product_detail()
        self.Detail.click_video_close()
        self.GM.swipe_up()
        self.Detail.click_ratings()
        self.Detail.click_ratings_back()
        self.Brand.click_product_back()

    def test_rating_more(self,start=None,stop=None,duration=None):
        """ 点击rating文案，跳转至评论页面"""
        self.Brand = ongoingBrand.OngoingBrand()
        self.Detail = productDetail.ProductDetail()
        self.Brand.click_product_detail()
        self.GM.swipe_value(250, 0.5, 0.9, 0.5, 0.1)
        self.Detail.click_video_close()
        self.GM.swipe_up()
        self.Detail.click_rating_more()
        self.Detail.click_review_back()
        self.Detail.scroll_to(start,stop,duration)
        self.Brand.click_product_back()


















