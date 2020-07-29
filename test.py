from selenium import webdriver
from common.base import BasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
dr = webdriver.Chrome()
dr.get("https://mail.163.com/")
iframe = dr.find_element_by_xpath("//*[contains(@id, 'x-URS-iframe')]")
dr.switch_to.frame(iframe)
dr.find_element_by_name("email").send_keys("mqq508@163.com")
dr.find_element_by_name("password").send_keys("mqq@123")
dr.find_element_by_id("dologin").click()
time.sleep(5)
dr.quit()


