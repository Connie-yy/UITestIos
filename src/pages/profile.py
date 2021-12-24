
''' edit Profile page'''

import random,time
from src.common import basePage
from appium.webdriver.common import mobileby


class EditProfile(basePage.Basepage):


    by = mobileby.MobileBy()

    def scroll_value(self):
        start = (self.by.IOS_PREDICATE, 'label == "Livestreams"')
        stop = (self.by.IOS_PREDICATE, 'label == "Coins"')
        self.scroll_to(3000, start, stop)

    def go_profile(self):
        """ 去主页"""
        profile = (self.by.XPATH,'(//XCUIElementTypeOther[@name="TabBarItem_AccessibilityLabel"])[4]')
        self.find_element(*profile).click()

    def edit_profile(self):
        """点击修改个人信息的按钮"""
        click_Edit = (self.by.IOS_PREDICATE, 'label == "Edit Profile"')
        self.find_element(*click_Edit).click()

    def edit_displayname(self,name):
        """点击输入displayname"""
        input_name = (self.by.XPATH, '//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField')
        self.send_keys(name,*input_name)


    def eit_description(self,description_text):
        """输入修改描述"""
        description = (self.by.IOS_PREDICATE, 'type == "XCUIElementTypeTextView"')
        self.send_keys(description_text,*description)

    def click_blank(self):
        """点击空白页"""
        blank = (self.by.IOS_PREDICATE,'label == "Display Name *"')
        self.find_element(*blank).click()

    def click_save(self):
        """点击保存"""
        save = (self.by.IOS_PREDICATE,'label == "Save" AND name == "Save" AND type == "XCUIElementTypeButton"')
        self.find_element(*save).click()

    def click_photo(self):
        """点击摄像头"""
        photo = (self.by.CLASS_NAME, '**/XCUIElementTypeButton[`label == "icon profile edit camera"`]')
        self.find_element(*photo).click()

    def select_photo(self):
        """选择照片"""
        select = (self.by.XPATH,'//XCUIElementTypeApplication[@name="LIT Live"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[4]/XCUIElementTypeOther')
        self.find_element(*select).click()

    def click_done(self):
        """点击done"""
        done = (self.by.IOS_PREDICATE, 'label == "Done" AND name == "Done" AND type == "XCUIElementTypeButton"')
        self.find_element(*done).click()

    def click_back(self):
        """ 点击返回"""
        back = (self.by.IOS_PREDICATE, 'label == "icon nav back"')
        self.find_element(*back).click()

    def click_coins(self):
        """点击coins按钮"""
        coins = (self.by.IOS_PREDICATE,'label == "Earn coins for savings"')
        self.find_element(*coins).click()

    def click_shopnow(self):
        """点击ShopNow进行搜索"""
        shopnow = (self.by.IOS_PREDICATE,'label == "Shop Now" AND name == "Shop Now" AND type == "XCUIElementTypeButton"')
        self.find_element(*shopnow).click()

    def click_shopnow_backs(self):
        """搜索后点击返回"""
        backs = (self.by.IOS_PREDICATE, 'label == "icon nav back"')
        self.find_element(*backs).click()

    def click_collect(self):
        """ 点击签到领取积分"""
        collect = (self.by.IOS_PREDICATE,'label == "Collect" AND name == "Collect" AND value == "1"')
        self.find_element(*collect).click()

    def promo(self,code):
        """输入兑换积分券code"""
        promo = (self.by.IOS_PREDICATE, 'value == "Promo code"')
        self.send_keys(code,*promo)

    def click_apply(self):
        """点击兑换"""
        apply = (self.by.IOS_PREDICATE, 'label == "Apply" AND name == "Apply" AND type == "XCUIElementTypeButton"')
        self.find_element(*apply).click()

    def click_livestreams(self):
        """点击历史视频"""
        livestreams = (self.by.XPATH, '(//XCUIElementTypeImage[@name="icon_search_all_arrow"])[1]')
        self.find_element(*livestreams).click()

    def scroll_to_a(self):
        """滑动历史视频"""
        re = (self.by.XPATH, '(//XCUIElementTypeImage[@name="icon_search_all_replay"])[3]')
        replay = (self.by.XPATH, '(//XCUIElementTypeImage[@name="icon_search_all_replay"])[1]')
        self.scroll_to(re,replay,3000)

    def livestreams_back(self):
        """历史视频页点击返回"""
        back = (self.by.XPATH, '//XCUIElementTypeButton[@name="icon nav back"]')
        self.find_element(*back).click()

    def click_orders(self):
        """点击历史订单"""
        orders = (self.by.XPATH, '(//XCUIElementTypeImage[@name="icon_search_all_arrow"])[2]')
        self.find_element(*orders).click()

    def orders_back(self):
        """点击历史订单页的返回按钮"""
        back = (self.by.IOS_PREDICATE, 'label == "icon nav back"')
        self.find_element(*back).click()

    def replay_back_scroll(self):
        """点击历史视频返回按钮"""
        replay_back = (self.by.XPATH, '//XCUIElementTypeButton[@name="icon nav back"]')
        self.find_element(*replay_back).click()

    def order_click(self):
        """点击订单按钮"""
        order = (self.by.XPATH, '(//XCUIElementTypeImage[@name="icon_search_all_arrow"])[2]')
        self.find_element(*order).click()

    def order_detail_click(self):
        """点击订单详情按钮"""
        replay_back = (self.by.XPATH, '(//XCUIElementTypeImage[@name="icon_my_orders_disclosure_indicator"])[1]')
        self.find_element(*replay_back).click()

    def order_back(self):
        """点击订单返回按钮"""
        order = (self.by.IOS_PREDICATE, 'label == "icon navigation back"')
        self.find_element(*order).click()




    # def collect_back(self):
    #
    #     back = (self.by.IOS_PREDICATE,'label == "icon nav back"')
    #     self.find_element(*back).click()










# class EditProfileError(basePage.Basepage):
#
#
#     by = mobileby.MobileBy()
#
#     def edit_Profile_error(self):
#         '''清除displayname'''
#         clear = (self.by.IOS_PREDICATE,'value == "User Display Name"')
#         self.send_keys(*clear).clear()
#
#     def edit_description(self,description_text):
#         '''输入用户描述'''
#         description = (self.by.IOS_PREDICATE, 'type == "XCUIElementTypeTextView"')
#         self.send_keys(*description).send_keys(description_text)
#
#         '''点击保存'''
#         save = (self.by.IOS_PREDICATE, 'label == "Save" AND name == "Save" AND type == "XCUIElementTypeButton"')
#         self.find_element(*save).click()
#
#         '''点击保存后，定位页面上的文字'''
#         SaveError = (self.by.XPATH,'(//XCUIElementTypeStaticText[@name="Description"])[1]')
#         Save =self.find_element(*SaveError).text
#
#         '''断言点击保存后，页面上还有Description，则修改用户资料失败'''
#         assert Save == "Edit Profile"
#         print("修改资料失败，缺少displayname")
































