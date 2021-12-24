import random, time

from src.common import basePage
from appium.webdriver.common import mobileby
from src.common import gestureManipulation

class Live(basePage.Basepage):


    by = mobileby.MobileBy()

    def get_into_room(self):
        '''点击直播画面，进入直播间'''
        xpath = '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther'
        into_the_room = (self.by.XPATH,xpath)
        self.find_element(*into_the_room).click()

    def follow_anthor(self):
        '''关注主播'''
        follow = (self.by.IOS_PREDICATE,'label == "icon audience follow normal"')
        self.find_element(*follow).click()

    def send_great_product(self):
        '''发送Great product！'''
        great_product = (self.by.IOS_PREDICATE,'label == "Great product!"')
        self.find_element(*great_product).click()

    def send_awesome(self):
        '''发送Awesome！'''
        Awesome = (self.by.IOS_PREDICATE,'label == "Awesome!"')
        self.find_element(*Awesome).click()

    def send_smiling_face(self):
        '''发送😀'''
        smiling = (self.by.IOS_PREDICATE, 'label == "😀"')
        self.find_element(*smiling).click()

    def scroll(self,start, stop, duration):
        '''滑动到左边'''
        self.scroll_to(start, stop, duration,)

    def send_face(self):
        '''发送☺️'''
        face = (self.by.IOS_PREDICATE, 'label == "☺️"')
        self.find_element(*face).click()

    def send_good(self):
        '''发送👍'''
        good = (self.by.IOS_PREDICATE, 'label == "👍"')
        self.find_element(*good).click()

    def send_like(self):
        '''发送 喷射爱心💗'''
        like = (self.by.IOS_PREDICATE, 'label == "icon now like normal"')
        self.find_element(*like).click()

    def say_something(self,value):
        '''输入文字'''
        say = (self.by.IOS_PREDICATE, 'label == "Say something ..."')
        self.send_keys(*say).send_keys(value)

    def send_say_something(self):
        '''发送文字'''
        send = (self.by.IOS_PREDICATE,'label == "icon now send message normal"')
        self.find_element(*send).click()

    def remote_audio(self):
        '''关闭听筒'''
        remote = (self.by.IOS_PREDICATE, 'label == "icon now vocal remote audio st"')
        self.find_element(*remote).click()

    def co_stream(self):
        '''发送连麦邀请'''
        stream = (self.by.IOS_PREDICATE, 'label == "icon now co stream"')
        self.find_element(*stream).click()
        
    def close_stream(self):
        '''关闭直播间'''
        close = (self.by.IOS_PREDICATE, '(//XCUIElementTypeButton[@name="icon navigation masked close"])[1]')
        self.find_element(*close).click()

    def shopping(self):
        '''点击直播间展示的商品'''
        shopping = (self.by.IOS_PREDICATE, '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[5]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage')
        self.find_element(*shopping).click()

    def shopping_bag(self):
        '''点击购物包'''
        bag = (self.by.IOS_PREDICATE, 'label == "icon now shopping bag normal"')
        self.find_element(*bag).click()

    def shopping_product(self):
        '''购物包弹出后，点击商品'''
        shoppingproduct = (self.by.IOS_PREDICATE,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage')
        self.find_element(*shoppingproduct).click()


    def click_anthor_photo(self):
        '''点击主播头像，进入主播个人页面'''
        photo = (self.by.IOS_PREDICATE, '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage')
        self.find_element(*photo).click()

    def click_follow(self):
        '''在主播个人页面，点击follow按钮'''
        follow = (self.by.XPATH,'(//XCUIElementTypeStaticText[@name="Following"])[1]')
        self.find_element(*follow).click()

    def click_remind_me(self):
        '''在主播个人页面，收藏预播'''
        remind = (self.by.IOS_PREDICATE, 'label == "Remind Me" AND name == "Remind Me" AND value == "Remind Me"')
        self.find_element(*remind).click()

    def close(self):
        '''在主播个人页面，关闭pip画面'''
        close = (self.by.IOS_PREDICATE, '(label == "icon live close canvas')
        if self.is_element:
            self.find_element(*close).click()

    def get_replay_photo(self):
        '''在主播个人页面，点击回放视频'''
        replay_photo = (self.by.XPATH, '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[4]/XCUIElementTypeImage')
        self.find_element(*replay_photo).click()

    def get_black_stream(self):
        '''返回直播间'''
        black_stream = (self.by.IOS_PREDICATE,'label == "icon nav back"')
        self.find_element(*black_stream).click()


    def is_element(self, *loc):  # 判断元素是否存在
        e = self.driver.find_elements(*loc) == []
        if e:
            return False  # 元素不存在返回False
        else:
            return True  # 元素存在返回True
















































