from page_obj.baidu import Baidu
import unittest, time
from selenium import webdriver
import logging as log
chrome_capabilities = {
            'platform': 'ANY',
            'browserName': 'chrome',
            'version': '',
            'javascriptEnabled': True
        }


class Test_Baidu(unittest.TestCase, Baidu):

    def setUp(self):

        # self.host = "http://2.0.1.54:4444/wd/hub"
        self.host = 'http://192.168.170.26:4444/wd/hub'
        self.driver = webdriver.Remote(command_executor=self.host, desired_capabilities=chrome_capabilities)
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test001(self):
        log.info("测试搜索功能开始")
        self.search("selenium")
        time.sleep(1)
        self.assertEqual(self.search_result(), "selenium_百度搜索")
        log.info("测试搜索功能结束")

    def test002(self):
        log.info("测试单击新闻开始")
        # self.click_news()
        time.sleep(2)
        self.assertIn("百度新闻", self.click_news())
        log.info("测试单击新闻结束")


if __name__ == "__main__":
    unittest.main(verbosity=2)
