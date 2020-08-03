from common.base import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


# 网易页面
class WangYi(BasePage):

    # 用户名
    username = (By.NAME, 'email')
    # 密码
    pwd = (By.NAME, 'password')
    # 登录按钮
    login_btn = (By.ID, 'dologin')
    # iframe
    iframe = (By.XPATH, '//*[contains(@id, "x-URS-iframe")]')
    # 登录名
    login_name = (By.ID, 'spnUid')
    # 写信按钮
    write_btn = (By.XPATH, "//span[contains(text(),'写 信')]")
    # 收件人
    addressee = (By.XPATH, "//*[contains(@id,'_mail_emailinput')]/input")
    # 主题
    subject = (By.XPATH, "//*[contains(@id,'_subjectInput')]")
    # 内容的iframe
    iframe_content = (By.XPATH, "//*[contains(@class,'APP-editor-iframe')]")
    # 内容
    content = (By.XPATH, "//body")
    # 发送按钮
    send_btn = (By.XPATH, "//*[contains(@class,'jp0')]/div[1]")

    # 发送成功校验

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

    # 点写信按钮
    def click_write_email(self):
        self.click_element(self.write_btn)

    # 输入收件人
    def input_addressee(self, addressee):
        self.input_text(self.addressee, addressee)

    # 输入主题
    def input_subject(self, subject):
        self.input_text(self.subject, subject)

    # 输入内容  富文本框
    def input_content(self, content):
        self.input_text(self.content, content)

    # 点击发送
    def click_send(self):
        self.click_element(self.send_btn)

    # 登录业务流程
    def login_wang_yi(self, username, pwd):
        self.switch_iframe(self.iframe, 5, 0.5)
        self.input_username(username)
        self.input_pwd(pwd)
        self.click_login_btn()

    # 验证是否登录成功
    def check_email_name(self):
        return self.get_element(self.login_name).text

    # 登录后写信并发送
    def send_email(self, username, pwd, addressee, sub, content):
        self.login_wang_yi(username, pwd)
        self.click_write_email()
        self.input_addressee(addressee)
        self.input_subject(sub)
        self.switch_iframe(self.iframe_content)
        self.input_content(content)
        time.sleep(6)
        self.switch_iframe_back_to_default()
        self.click_send()
