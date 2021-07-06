from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        self.desire_cap= {
            "platformName": "Android",
            # "deviceName": "127.0.0.1:6555",
            "deviceName": "JJN6R18305004805",
            "platformVersion" : "9.0",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.splash.SplashActivity",
            "noReset": True,
            "automationName": "uiautomator2",
            "autoGrantPermissions": True,
            'chromedriverExecutable': r'D:\tool\chromedriver\78.0\chromedriver.exe'
        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.find_element_by_xpath("//*[@text='交易']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text='期货']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@text='开户' and @index=6]").click()
        print('点击开户之后',self.driver.contexts)
        sleep(2)
        self.driver.switch_to.context(self.driver.contexts[-1])
        print('driver切换后', self.driver.context)
        # self.driver.find_element_by_xpath()
