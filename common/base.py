# 封装webdriver方法

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time, os
import logging as log


class BasePage(object):

    img_path = os.path.dirname(os.path.dirname(os.path.realpath("__file__")))
    img_name = os.path.join(img_path, 'report') + r'\\'+time.strftime("%Y_%m_%d_%H_%M_%S_")+'_img_err.png'

    def __init__(self, driver):
        self.driver = driver

    def get_screen(self):
        log.info("截取屏幕")
        self.driver.save_screenshot(self.img_name)

    def input_url(self, url):
        log.info(f"输入要访问的网址{url}")
        self.driver.get(url)

    def close_br(self):
        self.driver.quit()

    def refresh(self):
        log.info("刷新")
        self.driver.refresh()

    def go(self):
        log.info("向前一页")
        self.driver.forward()

    def back(self):
        log.info("向后一页")
        self.driver.back()

    def set_size(self, x, y):
        log.info(f"设置浏览器尺寸{x}*{y}")
        self.driver.set_window_size(x, y)

    def max_window(self):
        log.info("浏览器最大化")
        self.driver.maximize_window()

    # loc = (By.ID, "su")
    def wait_element_to_visible(self, loc):
        try:
            ele = WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return ele

        except Exception as e:
            self.get_screen()
            log.info(e)

    def wait_element_to_invisible(self, loc):
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.invisibility_of_element_located(loc))
        except Exception as e:
            self.get_screen()
            log.info(e)

    def get_element(self, loc):

        '''
            loc= (By.ID, 'id')
            By.ID = "id"
            By.XPATH = "xpath"
            By.LINK_TEXT = "link text"
            By.PARTIAL_LINK_TEXT = "partial link text"
            By.NAME = "name"
            By.TAG_NAME = "tag name"
            By.CLASS_NAME = "class name"
            By.CSS_SELECTOR = "css selector"

            (By.XPATH,"//*[@id='kw']")
            (By.XPATH,"//*[@name='wd']")
            (By.XPATH,"//*[@class='s_ipt']")
            (By.XPATH,"//*[@autocomplete='off']")
            (By.XPATH,"//*[@id='kw']/input")
            (By.XPATH,"//*[@id='kw']/input[1]")
            (By.XPATH,"//*[@id='kw' and @class='s_ipt']”)
            (By.XPATH,"//*[@id='kw' or @class='s_ipt']")
            (By.XPATH,"//input[contains(@id,'kw')]")
            (By.XPATH,"//*[contains(text(),'新闻')]")
            (By.XPATH,'//*[text()="新闻"]')
            (By.XPATH,"//*[contains(.,'新闻')]")
            (By.XPATH,"//input[starts-with(@id,'nice')")
            (By.XPATH,"//input[ends-with(@id,'很漂亮')")
            (By.XPATH,"//input[contains(@id,'那么美')]")
            (By.XPATH,"//*[contains(text(),'hao123')]/preceding-sibling::a")
            (By.XPATH,"//*[contains(text(),'hao123')]/following-sibling::a")
            (By.XPATH,"//*[contains(text(),'hao123')]/parent::div")
        '''

        log.info(f"查找单个页面元素{loc}")
        return self.wait_element_to_visible(loc)

    def get_elements(self, loc):
        log.info(f"查找多个页面元素{loc}")
        self.wait_element_to_visible(loc)
        return self.driver.find_elements(*loc)

    def input_text(self, loc, text):
        log.info(f"{loc}中输入文本{text}")
        self.get_element(loc).send_keys(text)

    def clean_input_text(self, loc, text):
        log.info(f"{loc}先清空，在输入文本{text}")
        self.get_element(loc).clear()
        self.get_element(loc).send_keys(text)

    def click_element(self, loc):
        log.info(f"单击{loc}")
        self.get_element(loc).click()

    # 下拉框的value值定位
    def select_list_value(self, loc, value):
        log.info(f"选择下拉列表{value}")
        ele = self.get_element(loc)
        Select(ele).select_by_value(value)

    # 取消所有选择
    def deselect_all(self, loc, value):
        log.info(f"选择下拉列表{value}")
        ele = self.get_element(loc)
        Select(ele).deselect_all()

    # loc=("id","xxx"),t="2016-12-25"
    def input_time_readonly(self, loc, t):
        ele = self.get_element(loc)
        log.info("去掉{}只读属性输入时间".format(loc))
        # js = 'document.getElementById("train_date").removeAttribute("readonly");'
        # js_value = 'document.getElementById("train_date").value="2016-12-25"'

        js1 = "document.getElementBy" + loc[0].title() + "('"
        js2 = "').removeAttribute('readonly')"
        js3 = "').value=" + "'" + t + "'"
        js = js1 + loc[1] + js2
        js_value = js1 + loc[1] + js3
        log.info(js_value)
        try:
            self.driver.execute_script(js)
            ele.clear()
            self.driver.execute_script(js_value)
        except Exception as e:
            log.info(e)
            log.info("时间控件输入失败")

    def get_element_text(self, loc):
        log.info(f"获取元素{loc}文本")
        return self.get_element(loc).text

    def get_element_attribute(self, loc, attr):
        log.info(f"获取元素{loc}属性{attr}")
        return self.get_element(loc).get_attribute(attr)

    # iframe 切换
    def switch_iframe(self, frame_refer, timeout=20, poll_frequency=0.5):
        # 等待 iframe 存在
        log.info('iframe 切换操作:')
        ele_iframe = self.driver.find_element(*frame_refer)
        try:
            # 判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
            # 注意这里并没有一个frame可以切换进去
            # if WebDriverWait(self.driver, timeout, poll_frequency).
            # until(EC.frame_to_be_available_and_switch_to_it(ele_iframe)):
            # 切换frame_refer == index\name\id\WebElement
            self.driver.switch_to.frame(ele_iframe)
            time.sleep(0.5)
            log.info('切换成功')

        except Exception as e:
            log.exception(e)
            # 截图
            self.get_screen()

    def switch_iframe_back_to_default(self):
        # 切回默认主页面
        log.info("iframe返回主页面")
        try:
            self.driver.switch_to.default_content()

        except Exception as e:
            log.info(e)
            log.info("iframe返回主页面失败")

    def switch_iframe_to_parent(self):
        # iframe返回上一级iframe
        log.info("iframe返回上一级iframe")
        try:
            self.driver.switch_to.parent_frame()

        except Exception as e:
            log.info(e)
            log.info("iframe返回上一级iframe失败")

    # 窗口切换 = 如果是切换到新窗口,new. 如果是回到默认的窗口,default
    def switch_window(self, handle):

        try:
            if handle == 'new':

                handles = self.driver.window_handles
                self.driver.switch_to.window(handles[-1])
                time.sleep(5)

            elif handle == 'default':
                log.info('切换到默认页面')
                self.driver.switch_to.default_content()

        except Exception as e:
            log.info('切换窗口失败!!!', e)

    # 执行js脚本
    def execute_js(self, js, *args):
        log.info('执行js脚本')
        try:
            self.driver.execute_script(js, *args)
        except Exception as e:
            log.info(e)

    # 移动到指定元素
    def move_to(self, loc):
        log.info(f'鼠标移动到元素{loc}上')
        try:
            ele = self.get_element(loc)
            ActionChains(self.driver).move_to_element(ele).perform()

        except Exception as e:
            log.info(e)

    def context_click(self, loc):
        log.info(f'右击元素{loc}上')
        try:
            ele = self.get_element(loc)
            ActionChains(self.driver).context_click(ele).perform()

        except Exception as e:
            log.info(e)

    def double_click(self, loc):
        log.info(f'双击元素{loc}上')
        try:
            ele = self.get_element(loc)
            ActionChains(self.driver).double_click(ele).perform()

        except Exception as e:
            log.info(e)

    def drag_and_drop(self, loc1, loc2):
        log.info(f'拖拽{loc1}移动到元素{loc2}上')
        try:
            ele1 = self.get_element(loc1)
            ele2 = self.get_element(loc2)
            ActionChains(self.driver).drag_and_drop(ele1, ele2).perform()

        except Exception as e:
            log.info(e)

    def input_keys(self, loc, x):
        log.info(f"元素{loc}输入x")
        if x == 'C':
            self.get_element(loc).send_keys(Keys.CONTROL, 'c')
        elif x == 'V':
            self.get_element(loc).send_keys(Keys.CONTROL, 'v')
        elif x == 'A':
            self.get_element(loc).send_keys(Keys.CONTROL, 'a')
        elif x == 'X':
            self.get_element(loc).send_keys(Keys.CONTROL, 'x')
        elif x == 'F1':
            self.get_element(loc).send_keys(Keys.F1)
        elif x == 'TAB':
            self.get_element(loc).send_keys(Keys.TAB)
        elif x == 'ENTER':
            self.get_element(loc).send_keys(Keys.ENTER)

    def accept_alert(self):
        log.info("alert点确定")
        al = self.driver.switch_to_alert()
        al.accept()

    def dismiss_alert(self):
        log.info("alert点取消")
        al = self.driver.switch_to_alert()
        al.dismiss()


if __name__ == "__main__":
    dr = webdriver.Chrome()
    p = BasePage(dr)
    p.input_url("https://www.baidu.com")
    p.get_screen()
    p.close_br()
