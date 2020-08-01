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


if __name__ == "__main__":
    unittest.main(verbosity=2)
