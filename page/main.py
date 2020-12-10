

from page.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class Main(BasePage):
    def search(self):
        # self.find('com.android.chrome:id/home_button').click()
        self.steps("../page/main.yaml")
        time.sleep(10)






