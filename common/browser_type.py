# 浏览器类型选择


from selenium import webdriver


class BrowserType(object):

    def __init__(self, browser="chrome"):
        self.chrome_capabilities = {
            'platform': 'ANY',
            'browserName': browser,
            'version': '',
            'javascriptEnabled': True
        }
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('--disable-infobars')  # 禁止策略化
        # self.options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        # self.options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        # self.options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        # self.options.add_argument('--incognito')  # 隐身模式（无痕模式）
        # self.options.add_argument('--disable-javascript')  # 禁用javascript
        # self.options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
        self.options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
        # self.options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        # self.options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        # self.options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        # self.options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # 手动指定使用的浏览器位置

        self.host = 'http://localhost:4444/wd/hub'
        self.driver = webdriver.Remote(command_executor=self.host, desired_capabilities=self.chrome_capabilities
                                       , options=self.options)
        self.driver.maximize_window()

    def get_url(self, url="https://www.baidu.com"):
        self.driver.get(url)
        return self.driver


if __name__ == '__main__':
    b = BrowserType().get_url()
    b.quit()
