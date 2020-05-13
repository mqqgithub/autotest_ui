
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
import logging as log


class BasePage(object):

    img_name = r"d:\autotest_ui\report\img_name.png"

    def __init__(self, driver):
        self.driver = driver

    def get_screen(self):
        log.info("截取屏幕")
        self.driver.save_screenshot(self.img_name)

    def wait_element_to_visible(self, loc):
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
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
        log.info("查找单个页面元素")
        self.wait_element_to_visible(loc)
        return self.driver.find_element(*loc)

    def get_elements(self, loc):
        log.info("查找多个页面元素")
        self.wait_element_to_visible(loc)
        return self.driver.find_elements(*loc)

    def input_text(self, loc, text):
        log.info("输入文本")
        self.get_element(loc).send_keys(text)

    def clean_input_text(self, loc, text):
        log.info("先清空，在输入文本")
        self.get_element(loc).clear()
        self.get_element(loc).send_keys(text)

    def click_element(self, loc):
        log.info("单击")
        self.get_element(loc).click()

    def select_list_element(self, loc, value):
        log.info("选择下拉列表value")
        ele = self.get_element(loc)
        Select(ele).select_by_value(value)

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
        log.info("获取元素文本")
        return self.get_element(loc).text

    def get_element_attribute(self, loc, attr):
        log.info("获取元素属性")
        return self.get_element(loc).get_attribute(attr)

    # iframe 切换
    def switch_iframe(self, frame_refer, timeout=20, poll_frequency=0.5, img_name="iframe定位错误"):
        # 等待 iframe 存在
        log.info('iframe 切换操作:')
        try:
            # 切换 == index\name\id\WebElement
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.frame_to_be_available_and_switch_to_it(frame_refer))
            time.sleep(0.5)
            log.info('切换成功')
        except:
            log.exception('iframe 切换失败!!!')
            # 截图
            self.save_img(img_name)

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
        """
        调用之前要获取window_handles
        :param name: new 代表最新打开的一个窗口. default 代表第一个窗口. 其他的值表示为窗口的 handles
        :param cur_handles:
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param img_name:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:
        """
        try:
            if handle == 'new':

                window_handles = self.driver.window_handles
                print(window_handles)
                print(window_handles[-1])
                self.driver.swich_to.window(window_handles[-1])
                title = self.driver.title
                print('title', title)
                return title

            elif handle == 'default':
                log.info('切换到默认页面')
                self.driver.switch_to.default()
            else:
                log.info('切换到为 handles 的窗口')
                self.driver.swich_to.window(handle)
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
        log.info('鼠标移动到元素上')
        try:
           ActionChains(self.driver).move_to_element(loc).perform()
        except Exception as e:
            log.info(e)


if __name__ == "__main__":
    pass
