from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_xpath("//*[contains(text(),'新闻')]").click()
time.sleep(2)
title = driver.title
print(title)

driver.quit()
