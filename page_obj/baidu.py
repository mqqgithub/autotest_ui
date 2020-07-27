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
    loc_save = (By.XPATH, "//*[text()='保存设置']")

    def __init__(self, driver):
        super().__init__(driver)

    # 输入输入框
    def input_search_text(self, content):
        self.get_element(self.loc_search_text).send_keys(content)

    # 单击查询按钮
    def click_search_btn(self):
        self.get_element(self.loc_search_btn).click()

    # 单击新闻链接
    def click_news(self):
        self.get_element(self.loc_news_link).click()
        self.switch_window("new")

    # 鼠标移动到设置
    def move_loc_config(self):
        self.move_to(self.loc_config)

    # 单击搜索设置
    def click_search_config(self):
        # self.click_element(self.loc_config)
        self.get_element(self.loc_search_config).click()

    # 选择显示复选框
    def click_display(self):
        self.click_element(self.loc_display)

    # 单击保存
    def click_save(self):
        self.click_element(self.loc_save)

    # 返回搜索结果
    def search_result(self):
        title = self.driver.title
        return title

    # 搜索查询
    def search(self, content):
        self.input_search_text(content)
        self.click_search_btn()
