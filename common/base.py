
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log import Log
log = Log()


class BasePage(object):

    img_name = r"d:\autotest_ui\report\img_name.png"

    def __init__(self, driver):
        self.driver = driver

    def get_screen(self):
        self.driver.save_screenshot(self.img_name)

    def wait_element_to_visible(self, loc):
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            self.get_screen()
            log.info(e)

    def wait_element_to_invisible(self, loc):
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            self.get_screen()
            log.info(e)

    def get_element(self, loc):
        self.wait_element_to_invisible(loc)
        return self.driver.find_element(*loc)

    def get_elements(self, loc):
        self.wait_element_to_visible(loc)
        return self.driver.find_elements(*loc)




if __name__ == "__main__":
    pass