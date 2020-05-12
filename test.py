from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.Chrome()
dr.get("https://www.baidu.com")
dr.find_element_by_xpath("//*[contains(text(),'新闻')]").click()
cur_handle = dr.current_window_handle
print(cur_handle)
window_handles = dr.window_handles
print(window_handles)
dr.switch_to.window(window_handles[-1])
print(dr.title)
dr.quit()
