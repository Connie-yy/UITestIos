import random,time

from src.common import basePage
from src.common import driverConf
from src.common import gestureManipulation
from appium.webdriver.common import mobileby
from src.common import basePage


class Ongoing(basePage.Basepage):

    by = mobileby.MobileBy()

    def click_save_preview(self):
        """ 点击收藏按钮，收藏预播 """
        click_save = (self.by.XPATH,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther')
        self.find_element(*click_save).click()

    def click_time_preview(self):
        """ 点击预播时间，进入预播 """
        click_time =(self.by.IOS_PREDICATE,'label == "12/24 | 12:45 PM GMT+8"')
        self.find_element(*click_time)

    def click_preview_bath(self):
        """ 点击预播按钮，进入预播 """
        click_bath =(self.by.XPATH,'xpath(//XCUIElementTypeStaticText[@name="Preview"])[1]')
        self.find_element(*click_bath)

    def click_enlarge_bath(self):
        """ 点击放大按钮，进入预播 """
        enlarge_preview = (self.by.XPATH,'(//XCUIElementTypeButton[@name="icon banner video card full"])[1]')
        self.find_element(*enlarge_preview).click()

    def click_streamer_name(self):
        """ 点击主播displayName，进入预播 """
        streamer_name = (self.by.XPATH,'(//XCUIElementTypeStaticText[@name="You"])[1]')
        self.find_element(*streamer_name).click()

    def click_stream_title(self):
        """ 点击预播标题，进入预播 """
        stream_title = (self.by.XPATH,'//XCUIElementTypeStaticText[@name="zzz"]')
        self.find_element(*stream_title).click()

    def click_preview_sound(self):
        """ 点击播放声音按钮 """
        preview_sound = (self.by.XPATH, '(//XCUIElementTypeButton[@name="icon banner video card full"])[1]')
        self.find_element(*preview_sound).click()

    def click_close_bath(self):
        """ 点击关闭弹窗"""
        close = (self.by.XPATH,'//XCUIElementTypeButton[@name="icon home summary close"]')
        self.find_element(*close)

    def click_back(self):
        """ 点击播放声音按钮 """
        back = (self.by.IOS_PREDICATE,'label == "icon navigation masked back"')
        self.find_element(*back).click()

    def click_remind_me(self):
        """ 点击 Remind Me 按钮，收藏预播"""
        remind_me = (self.by.XPATH,'//XCUIElementTypeStaticText[@name="Remind Me"]')
        self.find_element(*remind_me)

    def click_streamer_photo(self):
        """ 点击主播头像，进入主播首页 """
        streamer_photo = (self.by.XPATH,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage')
        self.find_element(*streamer_photo)

    def share_preview(self):
        """ 分享预播 """
        share = (self.by.IOS_PREDICATE,'label == "icon schedule share"')
        self.find_element(*share)

    def click_product_name(self):
        """ 点击商品名 """
        product_name = (self.by.IOS_PREDICATE,'label == "CC+ Cream with SPF 50+"')
        self.find_element(*product_name).click()

    def click_product_money(self):
        """ 点击商品价格 """
        product_money = (self.by.IOS_PREDICATE,'label == "$39.50"')
        self.find_element(*product_money).click()










