from page_obj.baidu import Baidu
import unittest, time
from selenium import webdriver
chrome_capabilities = {
            'platform': 'ANY',
            'browserName': 'chrome',
            'version': '',
            'javascriptEnabled': True
        }


class Test_Baidu(unittest.TestCase, Baidu):

    def setUp(self):

        self.host = "http://192.168.2.128:4444/wd/hub"
        self.driver = webdriver.Remote(command_executor=self.host, desired_capabilities=chrome_capabilities)
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test001(self):
        self.search("selenium")
        time.sleep(1)
        self.assertEqual(self.search_result(), "selenium_百度搜索")

    def test002(self):
        self.click_news()
        time.sleep(1)
        self.assertIn("百度新闻", self.search_result())


if __name__ == "__main__":
    unittest.main()