import random, time

from src.common import basePage
from appium.webdriver.common import mobileby
from src.common import gestureManipulation


class LivePreview(basePage.Basepage):

    by = mobileby.MobileBy()

    def go_live(self):
        """首页点击Go Live"""
        go = (self.by.IOS_PREDICATE,'label == "Go Live"')
        self.find_element(*go).click()

    def access_camera(self):
        """开启相机权限"""
        camera = (self.by.XPATH,'//XCUIElementTypeOther[@name="Vertical scroll bar, 1 page"])[2]')
        self.find_element(*camera).click()

    def access_microphone(self):
        """"开启语音权限"""""
        microphone =(self.by.XPATH,'//XCUIElementTypeOther[@name="Vertical scroll bar, 1 page"])[2]')
        self.find_element(*microphone).click()

    def click_schedule(self):
        """点击预播"""
        schedule = (self.by.IOS_PREDICATE,'label == "Schedule Stream" AND name == "Schedule Stream" AND type == "XCUIElementTypeButton"')
        self.find_element(*schedule).click()

    def add_stream_cover(self):
        """添加照片"""
        cover = (self.by.IOS_PREDICATE,'label == "Add a Stream Cover"')
        self.find_element(*cover).click()

    def select_photo(self):
        """选择照片"""
        select = (self.by.XPATH,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]/XCUIElementTypeOther/XCUIElementTypeButton')
        self.find_element(*select).click()

    def click_done(self):
        """选择照片"""
        done = (self.by.IOS_PREDICATE,'label == "Done" AND name == "Done" AND value == "Done"')
        self.find_element(*done).click()

    def add_preview_video(self):
        """ 添加视频"""
        video = (self.by.IOS_PREDICATE,'label == "Add a Preview Video"')
        self.find_element(*video).click()

    def stream_title(self,title):
        """ 输入标题 """
        send_title = (self.by.IOS_PREDICATE,'value == "Please enter a title for the stream"')
        self.send_keys(*send_title,title)

    def click_blank(self):
        """ dianji """
        blank = (self.by.IOS_PREDICATE,'label == "Stream Title"')
        self.find_element(*blank).click()

    def description(self,description):
        """输入description"""
        dec = (self.by.IOS_PREDICATE,'label == "Some small details you want viewers to see"')
        self.send_keys(description,*dec)

    def hashtag_text(self,hashtag):
        """输入hashtag"""
        has = (self.by.IOS_PREDICATE,'value == "Hastags related to your stream"')
        self.send_keys(hashtag,*has)

    def next_bath(self):
        """点击下一步"""
        next = (self.by.IOS_PREDICATE,'label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"')
        self.find_element(*next).click()

    def add_product(self):
        """添加商品"""
        add = (self.by.IOS_PREDICATE,'label == "Add" AND name == "Add" AND type == "XCUIElementTypeButton"')
        self.find_element(*add).click()

    def skip_product(self):
        """跳过商品选择"""
        skip = (self.by.IOS_PREDICATE, 'label == "Skip" AND name == "Skip" AND type == "XCUIElementTypeButton"')
        self.find_element(*skip).click()

    def search_product(self,search):
        """输入关键词D，搜索商品"""
        sea= (self.by.IOS_PREDICATE, 'label == "Pull down to refresh"')
        self.send_keys(search,*sea)

    def click_product(self):
        """点击商品"""
        click = (self.by.XPATH, '//XCUIElementTypeStaticText[@name="Tinted Brow Gel"])[3]')
        self.find_element(*click).click()

    def click_product_b(self):
        """点击商品"""
        click = (self.by.IOS_PREDICATE, 'label == "Drink Me! Gift"')
        self.find_element(*click).click()

    def click_add(self):
        """点击Add"""
        click_add = (self.by.IOS_PREDICATE, 'label == "Add"')
        self.find_element(*click_add).click()

    def click_next(self):
        """点击下一步"""
        click_next = (self.by.IOS_PREDICATE, 'label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"')
        self.find_element(*click_next).click()
# huadong

    def click_preview_next(self):
        """点击下一步"""
        click_next = (self.by.IOS_PREDICATE, 'label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"')
        self.find_element(*click_next).click()

    def edit_product(self):
        """点击Edit，修改商品"""
        click_edit = (self.by.IOS_PREDICATE,'label == "Edit" AND name == "Edit" AND value == "Edit"')
        self.find_element(*click_edit).click()

    def add_product_c(self):
        """点击商品"""
        click = (self.by.IOS_PREDICATE, 'label == "Luminous Foundation"')
        self.find_element(*click).click()

    def stream_now_scroll_a(self):
        """ 从下网上滑"""
        a = (self.by.XPATH, '//XCUIElementTypeStaticText[@name="Schedule Time"]')
        b = (self.by.XPATH, '//XCUIElementTypeStaticText[@name="Description"]')
        # self.LiveNow = liveNow.LiveNow(self.driver)
        self.scroll_to(a, b, 3000)

    def stream_now_scroll_b(self):
        """ 从下网上滑"""
        a = (self.by.XPATH, '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther')
        b = (self.by.XPATH, '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther')
        # self.LiveNow = liveNow.LiveNow(self.driver)
        self.scroll_to(a, b, 3000)














