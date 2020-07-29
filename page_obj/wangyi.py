from common.base import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


# 网易页面
class WangYi(BasePage):

    username = (By.NAME, 'email')
    pwd = (By.NAME, 'password')
    login_btn = (By.ID, 'dologin')

    def __init__(self, dr):
        super().__init__(dr)

    # 输入用户名
    def input_username(self):
        self.input_text(self.username, 'mqq508@163.com')

    # 输入密码
    def input_pwd(self):
        self.input_text(self.pwd, 'mqq@123')

    # 点击登录按钮
    def click_login_btn(self):
        self.click_element(self.login_btn)

    # 登录业务流程
    def login_wang_yi(self):
        self.input_username()
        self.input_pwd()
        self.click_login_btn()

