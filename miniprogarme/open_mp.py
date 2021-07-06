from time import sleep

from appium import webdriver


class TestDemo:
    def setup(self):
        self.desire_cap= {
            "platformName": "Android",
            # "deviceName": "Q5S5T19620005961",
            "deviceName": "127.0.0.1:7555",
            "platformVersion" : "6.0",
            "appPackage": "com.tencent.mm",
            "appActivity": ".ui.LauncherUI",
            "noReset": "true",
            "autoLaunch": "false",
            'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
            'autoGrantPermissions':"true",
            'chromedriverExecutable': r'D:\tool\chromedriver\2.22\chromedriver.exe'

        }
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
        self.driver.implicitly_wait(10)

    # def setup(self):
    #     self.desire_cap= {
    #         "platformName": "android",
    #         "deviceName": "JJN6R18305004805",
    #         "platformVersion" : "9.0",
    #         "browserName": "Chrome",
    #         "noReset": "true",
    #         # 'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},
    #         'chromedriverExecutable':r'D:\tool\chromedriver\78.0\chromedriver.exe'
    #
    #     }
    #     self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desire_cap)
    #     # self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
    # def test_browser(self):
    #     self.driver.get("https://m.baidu.com")
    #     sleep(5)
    def test_demo(self):
        self.driver.find_element_by_xpath("//*[@text='微信']").click()
        # self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/dtx']/../../../../*[@class='android.widget.RelativeLayout' and @index=0]").click()
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        print(width,height)
        self.driver.swipe((width / 2), int((height * 0.1)), (width / 2), (height * 0.9), 2000)
        # self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/ipm' and contains(@text,'珍爱优恋空间')]").click()
        # self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/gam' and contains(@text,'珍爱优恋空间')]").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/gam' and contains(@text,'雪球')]")
        sleep(5)
        print(self.driver.contexts,'第一次打印')
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/h8a' and contains(@text,'热门')]").click()
        self.driver.find_element_by_xpath('//*[@text="请输入股票名称/代码"]').send_keys("阿里巴巴")
        text = self.driver.find_element_by_xpath('//*[@content-desc="阿里巴巴"]')
        assert text