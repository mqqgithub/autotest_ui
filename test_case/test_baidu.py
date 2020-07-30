from page_obj.baidu import Baidu
import unittest, time
# from selenium import webdriver
from common.browser_type import BrowserType
import logging as log


class Test_Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = BrowserType().get_url()
        print(self.driver)
        self.p = Baidu(self.driver)

    def tearDown(self):
        self.driver.quit()

    @unittest.skip('skip')
    def test001(self):
        log.info("测试搜索功能开始")
        self.p.search("selenium")
        time.sleep(1)
        self.assertEqual(self.p.search_result(), "selenium_百度搜索")
        log.info("测试搜索功能结束")

    @unittest.skip('skip')
    def test002(self):
        log.info("测试单击新闻开始")
        self.p.click_news()
        time.sleep(1)
        s = self.p.search_result()
        self.assertIn("百度新闻", s)
        log.info("测试单击新闻结束")

    def test003(self):
        log.info("测试未来7天天气")
        self.p.move_loc_config()
        time.sleep(1)
        self.p.click_search_config()
        time.sleep(0.5)
        self.p.click_save()
        time.sleep(0.5)
        self.driver.switch_to.alert.accept()
        print('ok!!!')


if __name__ == "__main__":
    unittest.main(verbosity=2)
