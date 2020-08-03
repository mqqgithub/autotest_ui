from page_obj.wangyi import WangYi
import unittest, time
# from selenium import webdriver
from common.browser_type import BrowserType
import logging as log


class Test_Wangyi(unittest.TestCase):

    def setUp(self):
        self.driver = BrowserType().get_url("https://mail.163.com")
        self.p = WangYi(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.p.login_wang_yi("mqq508@163.com", "mqq@123")
        self.assertEqual(self.p.check_email_name(), 'mqq508@163.com')

    def test_send_email(self):
        log.info('发送邮件')
        self.p.send_email('mqq508@163.com', 'mqq@123', '756738633@qq.com', 'test', ' 这是一个测试')

    def send_email_with_file(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)

