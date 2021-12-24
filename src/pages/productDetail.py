
import random,time

from src.common import basePage
from src.common import driverConf
from src.common import gestureManipulation
from appium.webdriver.common import mobileby
from src.common import basePage


class ProductDetail(basePage.Basepage):

        by = mobileby.MobileBy()

        def click_save_product(self):
            """ 点击 收藏按钮，收藏商品"""
            save_product = (self.by.IOS_PREDICATE,'name == "icon_not_collected"')
            self.find_element(*save_product)

        def click_add_bag(self):
            """ 点击add to bag 加入商品到购物车 """
            add_bag = (self.by.XPATH,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]')
            self.find_element(*add_bag)

        def share_product(self):
            """ 分享预播 """
            share = (self.by.IOS_PREDICATE,'label == "icon product details share"')
            self.find_element(*share)

        def click_video_close(self):
            """ 关闭商品视频 """
            video_close = (self.by.IOS_PREDICATE,'label == "icon video floating close"')
            self.find_element(*video_close).click()

        def click_product_money(self):
            """ 点击商品价格 """
            product_money = (self.by.IOS_PREDICATE,'label == "$39.50"')
            self.find_element(*product_money).click()

        def click_ratings(self):
            """ 点击rating，跳转到评论页面"""
            ratings = (self.by.XPATH,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]/XCUIElementTypeOther')
            self.find_element(*ratings).click()

        def click_ratings_back(self):
            """ 评论页面点击返回"""
            back = (self.by.IOS_PREDICATE,'label == "icon nav back"')
            self.find_element(*back).click()

        def click_edit_review(self):
            """ 点击修改评论 """
            edit_review = (self.by.XPATH,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther[4]')
            self.find_element(*edit_review).click()

        def click_review_back(self):
            """ 评论页面点击返回 """
            review_back = (self.by.IOS_PREDICATE,'label == "icon nav back"')
            self.find_element(*review_back).click()

        def click_description(self):
            """ 点击商品描述 """
            description = (self.by.XPATH,'(//XCUIElementTypeImage[@name="icon_product_details_disclosure_indicator"])[1]')
            self.find_element(*description).click()

        def product_variant_see_all(self):
            """ 点击商品属性的see all"""
            variant = (self.by.IOS_PREDICATE,'label == "See All" AND name == "See All" AND value == "See All"')
            self.find_element(*variant).click()

        def click_rating_more(self):
            """ 点击评论的more """
            more = (self.by.IOS_PREDICATE,'label == "More" AND name == "More" AND type == "XCUIElementTypeButton"')
            self.find_element(*more).click()

        def scroll_to(self, start, stop, duration):
            """ 滑动评论模块"""
            start = (self.by.IOS_PREDICATE,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[10]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther')
            stop = (self.by.IOS_PREDICATE,'/XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther[10]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther')
            duration = 250
            self.find_element(*start,*stop,duration)





































