from common.base import BasePage
from selenium.webdriver.common.by import By


class Baidu(BasePage):

    loc_search_text = (By.ID, "kw")
    loc_search_btn = (By.ID, "su")
    loc_news_link = (By.XPATH, "//*[contains(text(),'新闻')]")

    def __init__(self, driver):
        super().__init__(driver)

    def input_search_text(self, content):
        self.get_element(self.loc_search_text).send_keys(content)

    def click_search_btn(self):
        self.get_element(self.loc_search_btn).click()

    def click_news(self):
        self.get_element(self.loc_news_link).click()
        title = self.switch_window("new")
        return title

    def search_result(self):

        title = self.driver.title
        return title

    def search(self, content):
        self.input_search_text(content)
        self.click_search_btn()
