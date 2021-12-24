import random,time

from src.common import basePage
from src.common import driverConf
from src.common import gestureManipulation
from appium.webdriver.common import mobileby
from src.common import basePage


class OngoingBrand(basePage.Basepage):

    by = mobileby.MobileBy()

    def click_follow(self):
        """  follow按钮 关注商家"""
        click_save = (self.by.XPATH,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]')
        self.find_element(*click_save).click()

    def click_brand_photo(self):
        """ 点击商家照片，进入商家页面 """
        brand_photo = (self.by.XPATH,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage')
        self.find_element(*brand_photo).click()

    def click_brand_name(self):
        """ 点击商家名，进入商家页面"""
        brand_name = (self.by.XPATH,'//XCUIElementTypeStaticText[@name="longyi"]')
        self.find_element(*brand_name).click()

    def click_brand_followers(self):
        """ 点击商家粉丝数，进入商家页面 """
        stream_title = (self.by.XPATH,'//XCUIElementTypeStaticText[@name="4 Followers"]')
        self.find_element(*stream_title).click()

    def click_close(self):
        """ 点击商家主页的弹窗关闭按钮 """
        close = (self.by.IOS_PREDICATE,'label == "icon home summary close"')
        self.find_element(*close).click()

    def click_back(self):
        """ 点击商家主页的返回按钮 """
        click_bath = (self.by.IOS_PREDICATE,'label == "icon nav back"')
        self.find_element(*click_bath).click()

    def click_product_detail(self):
        """ 点击图片进入商品详情页"""
        product_detail = (self.by.XPATH,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeImage')
        self.find_element(*product_detail).click()

    def click_product_back(self):
        """ 点击商品页返回按钮"""
        back = (self.by.IOS_PREDICATE,'label == "icon navigation masked back"')
        self.find_element(*back).click()

    def click_all(self):
        """ 点击商家模块的 all"""
        all = (self.by.IOS_PREDICATE,'(//XCUIElementTypeStaticText[@name="All"])[1]')
        self.find_element(*all).click()

