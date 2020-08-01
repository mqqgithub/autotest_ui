from common.base import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


# 网易页面
class WangYi(BasePage):

    username = (By.NAME, 'email')
    pwd = (By.NAME, 'password')
    login_btn = (By.ID, 'dologin')
    iframe = (By.XPATH, '//*[contains(@id, "x-URS-iframe")]')
    email_name = (By.ID, 'spnUid')

    def __init__(self, dr):
        super().__init__(dr)

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.username, username)

    # 输入密码
    def input_pwd(self, pwd):
        self.input_text(self.pwd, pwd)

    # 点击登录按钮
    def click_login_btn(self):
        self.click_element(self.login_btn)

    # 登录业务流程
    def login_wang_yi(self, username, pwd):
        self.switch_iframe(self.iframe, 5, 0.5)
        self.input_username(username)
        self.input_pwd(pwd)
        self.click_login_btn()

    def check_email_name(self):
        return self.get_element(self.email_name).text
