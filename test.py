from selenium import webdriver
from common.base import BasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome()
dr.get("https://www.tdft.cn/news.html")
bp = BasePage(dr)
bp.max_window()
x = dr.find_element_by_xpath("//*[@id='app']/div[1]/div/ul/li[6]/a")
ActionChains(dr).move_to_element(x).perform()
y = dr.find_element_by_xpath("//*[@id='app']/div[1]/div/ul/li[6]/ul/li/a")
y.click()
time.sleep(5)
dr.quit()


driver = webdriver.Chrome()
handle = driver.current_window_handle
