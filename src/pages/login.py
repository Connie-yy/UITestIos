
import random, time

from src.common import basePage
from appium.webdriver.common import mobileby


class LoginPage(basePage.Basepage):
    by = mobileby.MobileBy()

    def scroll_value(self):
        start = (self.by.IOS_PREDICATE, 'label == "Livestreams"')
        stop = (self.by.IOS_PREDICATE, 'label == "Coins"')
        self.scroll_to(3000, start, stop)

    def select_profile_page(self):
        "选择tabbar profile"
        index_loc = (self.by.XPATH, '//XCUIElementTypeOther[@name="TabBarItem_AccessibilityLabel"][4]')
        self.find_element(*index_loc).click()

    def email_login_action(self):
        "选择email登录"
        email_login_btn = (self.by.IOS_PREDICATE,
                           'label == "Continue with Email" AND name == "Continue with Email" AND type == "XCUIElementTypeButton"')
        self.find_element(*email_login_btn).click()

    def login_email_account(self, username):
        "输入account用户名"
        user_email_textfield = (self.by.IOS_PREDICATE, 'value == "Enter your email or username here"')
        self.send_keys(username, *user_email_textfield)

    def login_account_next_action(self):
        "点击登录next"
        next_btn = (self.by.IOS_PREDICATE, 'label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"')
        self.find_element(*next_btn).click()

    def login_input_account_password(self, pwd):
        "输入account密码"
        pwd_textfield = (self.by.IOS_PREDICATE, 'value == "Enter your password here"')
        self.send_keys(pwd, *pwd_textfield)

    def login_select_secret(self):
        "点击显示或隐藏密码"
        secret_btn = (self.by.IOS_PREDICATE, 'label == "icon login secret"')
        self.find_element(*secret_btn).click()

    def login_account_login_action(self):
        "点击登录按钮"
        login_btn = (self.by.IOS_PREDICATE, 'label == "Login" AND name == "Login" AND type == "XCUIElementTypeButton"')
        self.find_element(*login_btn).click()

    def forget_pwd_action(self):
        "点击忘记密码按钮"
        forget_pwd_btn = (self.by.IOS_PREDICATE, 'label == "Forget Password?"')
        self.find_element(*forget_pwd_btn).click()

    def forget_send_email(self, email):
        "输入找回密码email"
        email_textfield = (self.by.IOS_PREDICATE, 'value == "Enter your email here"')
        self.send_keys(email, *email_textfield)

    def forget_send_action(self):
        "发送找回密码按钮"
        send_btn = (self.by.IOS_PREDICATE, 'label == "Send" AND name == "Send" AND type == "XCUIElementTypeButton"')
        self.find_element(*send_btn).click()

    def reg_email(self, username_email):
        "注册用户名和email"
        email_textfield = (self.by.IOS_PREDICATE, 'value == "Enter your email here"')
        self.send_keys(username_email, *email_textfield)

    def reg_pwd(self, pwd):
        "输入注册密码"
        pwd_textfield = (self.by.IOS_PREDICATE, 'value == "At least 8 characters"')
        self.send_keys(pwd, *pwd_textfield)

    def reg_conf_pwd(self, conf_pwd):
        "输入注册确认密码"
        conf_pwd_textfield = (self.by.IOS_PREDICATE, 'value == "Re-type your password"')
        self.send_keys(conf_pwd, *conf_pwd_textfield)

    def reg_nex_action(self):
        "点击注册next按钮"
        next_btn = (self.by.IOS_PREDICATE, 'label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"')
        self.find_element(*next_btn).click()

    def reg_profile_avator_action(self):
        "点击用户选择投降按钮"
        avator_btn = (self.by.IOS_PREDICATE, 'label == "icon edit profile picture"')
        self.find_element(*avator_btn).click()

    def reg_profile_avator_select_all(self):
        "用户授权选择全部照片"
        path = '//XCUIElementTypeAlert[@name="“LIT Live”想访问您的照片"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[1]'
        all_btn = (self.by.XPATH, path)
        self.find_element(*all_btn).click()

    def reg_profile_avator_select_part(self):
        "用户授权选择部分照片"
        path = '//XCUIElementTypeAlert[@name="“LIT Live”想访问您的照片"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]'
        all_btn = (self.by.XPATH, path)
        self.find_element(*all_btn).click()

    def reg_profile_display_name(self, name):
        "输入display name"
        display_textfield = (self.by.IOS_PREDICATE, 'value == "This is how you’ll appear on Lit Live"')
        self.send_keys(name, *display_textfield)

    def reg_profile_description(self, text):
        "输入description"
        descrption_textfield = (self.by.IOS_PREDICATE, 'type == "XCUIElementTypeTextView"')
        self.send_keys(text, *descrption_textfield)

    def reg_register_action(self):
        "点击注册按钮"
        register_btn = (
            self.by.IOS_PREDICATE, 'label == "Register" AND name == "Register" AND type == "XCUIElementTypeButton"')
        self.find_element(*register_btn).click()

    def gender_female_action(self):
        "选择female性别"
        famale_btn = (self.by.IOS_PREDICATE, 'name == "icon_demographic_gender_female_normal"')
        self.find_element(*famale_btn).click()

    def gender_male_action(self):
        "选择male性别"
        male_btn = (self.by.IOS_PREDICATE, 'name == "icon_demographic_gender_male_normal"')
        self.find_element(*male_btn).click()

    def gender_neither_action(self):
        "选择neigher性别"
        neither_btn = (self.by.IOS_PREDICATE, 'name == "icon_demographic_gender_neither_normal"')
        self.find_element(*neither_btn).click()

    def gender_next_action(self):
        next_btn = (self.by.IOS_PREDICATE, 'label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"')
        self.find_element(*next_btn).click()

    def birth_next_action(self):
        "选择默认日期"
        next_btn = (self.by.IOS_PREDICATE, 'label == "Next" AND name == "Next" AND type == "XCUIElementTypeButton"')
        self.find_element(*next_btn).clikc()

    def interest_select_action(self):
        "选择interest词"
        interest_content = ['under $100', 'under $50', 'giveaways', 'deals', 'exclusives', 'new products', 'home',
                            'cosmetics', 'skincare', 'hair & body', 'apparel', 'accessories', 'jewelry']
        count = random.randint(0, 12)
        while count >= 0:
            value = interest_content[random.randint(0, count)]
            interest_content.remove(value)
            select_path = (self.by.IOS_PREDICATE, 'label == ' + "\"" + value + "\"")
            self.find_element(*select_path).click()
            count -= 1

    def welcome_select_maybe(self):
        "点击welcome maybe按钮"
        maybe_btn = (self.by.IOS_PREDICATE, 'label == "Maybe Later"')
        self.find_element(*maybe_btn).clikc()

    def welcome_select_yes(self):
        "点击welcome yes 按钮"
        yes_btn = (self.by.IOS_PREDICATE, 'label == "Yes!"')
        self.find_element(*yes_btn).clikc()

    def write_a_review(self):
        "点击write a review"
        review_btn = (self.by.XPATH, '//XCUIElementTypeOther[@name="`"]')
        self.find_element(*review_btn).clikc()

