import random, time

from src.common import basePage
from appium.webdriver.common import mobileby
from src.common import gestureManipulation


class LiveNow(basePage.Basepage):

    by = mobileby.MobileBy()

    def go_profile(self):
        profile = (self.by.XPATH,'(//XCUIElementTypeOther[@name="TabBarItem_AccessibilityLabel"])[4]')
        self.find_element(*profile).click()

    def go_live(self):
        '''首页点击Go Live'''
        go = (self.by.IOS_PREDICATE,'label == "Go Live"')
        self.find_element(*go).click()

    def access_camera(self):
        ''' 开启相机权限'''
        camera = (self.by.XPATH,'//XCUIElementTypeOther[@name="Vertical scroll bar, 1 page"])[2]')
        self.find_element(*camera).click()

    def access_microphone(self):
        ''' 开启语音权限'''
        microphone =(self.by.XPATH,'//XCUIElementTypeOther[@name="Vertical scroll bar, 1 page"])[2]')
        self.find_element(*microphone).click()

    def stream_now(self):
        ''' 点击now'''
        stream = (self.by.IOS_PREDICATE,'label == "Stream Now" AND name == "Stream Now" AND type == "XCUIElementTypeButton"')
        self.find_element(*stream).click()

    def click_blank(self):
        """ dianji """
        blank = (self.by.IOS_PREDICATE,'label == "Stream Title"')
        self.find_element(*blank).click()

    def stream_now_scroll_a(self):
        """ 从下网上滑"""
        a = (self.by.IOS_PREDICATE, 'label == "Stream Title"')
        b = (self.by.IOS_PREDICATE, 'name == "icon_streaming_picture_placeholder"')
        # self.LiveNow = liveNow.LiveNow(self.driver)
        self.scroll_to(a, b, 3000)

    def stream_now_scroll(self):
        """ 从上往下"""
        a = (self.by.IOS_PREDICATE, 'label == "Stream Title"')
        b = (self.by.IOS_PREDICATE, 'label == "Hashtag"')
        # self.LiveNow = liveNow.LiveNow(self.driver)
        self.scroll_to(a, b, 3000)

    def add_cover(self):
        '''点击Add a stream cover'''
        cover = (self.by.IOS_PREDICATE,'name == "icon_streaming_picture_placeholder"')
        self.find_element(*cover).click()

    def add_photo(self):
        '''选择照片'''
        photo = (self.by.XPATH, '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]/XCUIElementTypeOther/XCUIElementTypeButton')
        self.find_element(*photo).click()

    def edit_delete_photo(self):
        ''' 修改照片'''
        delete = (self.by.IOS_PREDICATE,'label == "icon streaming delete"')
        self.find_element(*delete).click()

    def add_photo_b(self):
        '''重新添加照片'''
        photo = (self.by.XPATH, '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeButton')
        self.find_element(*photo).click()

    def click_done(self):
        '''点击Done'''
        done = (self.by.IOS_PREDICATE,'label == "Done" AND name == "Done" AND type == "XCUIElementTypeButton"')
        self.find_element(*done).click()

    def stream_title(self,title):
        '''输入title'''
        title_text = (self.by.IOS_PREDICATE,'value == "Please enter a title for the stream"')
        self.send_keys(title,*title_text)

    # huadong

    def description(self,description):
        '''输入description'''
        dec = (self.by.IOS_PREDICATE,'label == "Some small details you want viewers to see"')
        self.send_keys(description,*dec)

    def hashtag_text(self,hashtag):
        '''输入hashtag'''
        has = (self.by.IOS_PREDICATE,'value == "Hastags related to your stream"')
        self.send_keys(hashtag,*has)

    def next_bath(self):
        '''点击下一步'''
        next = (self.by.IOS_PREDICATE,'label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"')
        self.find_element(*next).click()

    def add_product(self):
        '''添加商品'''
        add = (self.by.IOS_PREDICATE,'label == "Add" AND name == "Add" AND type == "XCUIElementTypeButton"')
        self.find_element(*add).click()

    def skip_product(self):
        '''跳过商品选择'''
        skip = (self.by.IOS_PREDICATE, 'label == "Skip" AND name == "Skip" AND type == "XCUIElementTypeButton"')
        self.find_element(*skip).click()

    def search_product(self,search):
        '''输入关键词D，搜索商品'''
        sea= (self.by.IOS_PREDICATE, 'label == "Search"')
        self.send_keys(search,*sea)

    def click_select_prod(self):

        select = (self.by.IOS_PREDICATE,'label == "Select Products"')
        self.find_element(*select).click()

    def click_product(self):
        '''点击商品'''
        click = (self.by.IOS_PREDICATE, 'label == "Drink Me! Gift"')
        self.find_element(*click).click()

    def click_product_b(self):
        '''点击商品'''
        click = (self.by.IOS_PREDICATE, 'label == "Drink Me! Gift Box"')
        self.find_element(*click).click()

    def click_add(self):
        '''点击Add'''
        click_add = (self.by.XPATH, '//XCUIElementTypeButton[@name="Add"]')
        self.find_element(*click_add).click()

    def click_next(self):
        '''点击下一步'''
        click_next = (self.by.IOS_PREDICATE, 'label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"')
        self.find_element(*click_next).click()
# huadong

    def click_preview_next(self):
        '''点击下一步'''
        click_next = (self.by.IOS_PREDICATE, 'label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"')
        self.find_element(*click_next).click()

    def edit_product(self):
        '''点击Edit，修改商品'''
        click_edit = (self.by.IOS_PREDICATE,'label == "Edit" AND name == "Edit" AND type == "XCUIElementTypeButton"')
        self.find_element(*click_edit).click()

    def add_product_b(self):
        '''点击商品'''
        click = (self.by.IOS_PREDICATE, 'label == "Cookie and red cookie and yellow cookie and good cookie and big cookie "')
        self.find_element(*click).click()

    def start_live(self):
        '''点击Start Live，开启视频'''
        start = (self.by.IOS_PREDICATE,'label == "Start Live" AND name == "Start Live" AND type == "XCUIElementTypeButton"')
        self.find_element(*start).click()

    def change_camera(self):
        '''点击相机反符号'''
        change = (self.by.IOS_PREDICATE,'label == "icon toggle camera"')
        self.find_element(*change).click()

    def stream_now_scroll_b(self):
        """ 从下网上滑"""
        a = (self.by.XPATH, '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther')
        b = (self.by.XPATH, '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther')
        # self.LiveNow = liveNow.LiveNow(self.driver)
        self.scroll_to(a, b, 3000)