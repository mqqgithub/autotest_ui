from selenium import webdriver
from common.base import BasePage
from selenium.webdriver.common.by import By
dr = webdriver.Chrome()
dr.get("http://www.baidu.com")
bp = BasePage(dr)
ele = bp.wait_element_to_visible((By.ID, 'su'))
