from page_obj.baidu import Baidu
import unittest, time
# from selenium import webdriver
from ..common.browser_type import BrowserType
import logging as log


class Test_Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = BrowserType().get_url()
        print(self.driver)
        self.p = Baidu(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test001(self):
        log.info("测试搜索功能开始")
        self.p.search("selenium")
        time.sleep(1)
        self.assertEqual(self.p.search_result(), "selenium_百度搜索")
        log.info("测试搜索功能结束")

    # @unittest.skip('skip')
    def test002(self):
        log.info("测试单击新闻开始")
        s = self.p.click_news()
        print(s)
        time.sleep(2)
        # self.assertIn("百度新闻", s)
        log.info("测试单击新闻结束")


if __name__ == "__main__":
    unittest.main(verbosity=2)
