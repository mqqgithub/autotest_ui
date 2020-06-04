from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
chrome_capabilities = {
            'platform': 'ANY',
            'browserName': 'chrome',
            'version': '',
            'javascriptEnabled': True
        }
host = 'http://localhost:4444/wd/hub'
dr = webdriver.Remote(command_executor=host, desired_capabilities=chrome_capabilities)
dr.maximize_window()
dr.get('https://www.baidu.com')

ele = dr.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(dr).move_to_element(ele).perform()
time.sleep(2)
dr.find_element_by_xpath("//a[text()='搜索设置']").click()
time.sleep(3)
dr.find_element_by_xpath("//*[text()='保存设置']").click()
time.sleep(2)
dr.switch_to.alert.accept()
print('123')
dr.quit()

