# 启动app
from appium import webdriver
from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    package = 'com.android.chrome'
    activity = 'com.google.android.apps.chrome.Main'
    def start(self):
        desired_caps = {}
        desired_caps['deviceName'] = 'emulator-5554'  # adb devices查到的设备名
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11.0.1'
        desired_caps['appPackage'] = self.package  # 被测App的包名
        desired_caps['appActivity'] = self.activity  # 启动时的Activity
        desired_caps['noReset'] = True  # 不重置（记住登入信息）-fullReset重置
        # desired_caps['avd'] = "Pixel_2_API_30"#启动模拟器
        # desired_caps['udid'] = "Pixel_2_API_30"#设备管理
        # desired_caps['autoGrantPermissions'] = True#关闭系统及弹框（获取定位等）
        # desired_caps['dontStopAppOnReset'] = True#不关闭app
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
        return self
    def main(self)->Main:
        return Main(self.driver)



