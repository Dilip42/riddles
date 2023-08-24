from appium.webdriver.common.appiumby import AppiumBy

class scrollingclass:
    def __init__(self,driver):
        self.driver = driver

    def scrollingto(self,scroolto):

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{scroolto}").instance(0));')

