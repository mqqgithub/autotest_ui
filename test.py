from selenium import webdriver
chrome_capabilities = {
            'platform': 'ANY',
            'browserName': 'chrome',
            'version': '',
            'javascriptEnabled': True
        }
host = 'http://localhost:4444/wd/hub'
dr = webdriver.Remote(command_executor=host, desired_capabilities=chrome_capabilities)
dr.maximize_window()
dr.get('http://www.baidu.com')
print(dr.current_window_handle)
dr.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()
print(dr.current_window_handle)
handles = dr.window_handles
dr.switch_to.window(handles[-1])
title = dr.title
print(dr.current_window_handle)
print(title)
dr.quit()

