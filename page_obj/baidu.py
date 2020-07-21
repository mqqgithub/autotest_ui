from common.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Baidu(BasePage):

    loc_search_text = (By.ID, "kw")
    loc_search_btn = (By.ID, "su")
    loc_news_link = (By.XPATH, "//*[contains(text(),'新闻')]")
    loc_config = (By.XPATH, '//*[@id="s-usersetting-top"]')
    loc_search_config = (By.XPATH, "//a[text()='搜索设置']")
    loc_display = (By.XPATH, "//*[@id='s1_1']")
    loc_safe = (By.XPATH, "//*[text()='保存设置']")

    def __init__(self, driver):
        super().__init__(driver)

    def input_search_text(self, content):
        self.get_element(self.loc_search_text).send_keys(content)

    def click_search_btn(self):
        self.get_element(self.loc_search_btn).click()

    def click_news(self):
        self.get_element(self.loc_news_link).click()
        self.switch_window("new")

    def move_loc_config(self):
        self.move_to(self.loc_config)

    def click_search_config(self):
        # self.click_element(self.loc_config)
        self.get_element(self.loc_search_config).click()

    def click_display(self):
        self.click_element(self.loc_display)

    def click_safe(self):
        self.click_element(self.loc_safe)

    def search_result(self):
        title = self.driver.title
        return title

    def search(self, content):
        self.input_search_text(content)
        self.click_search_btn()
