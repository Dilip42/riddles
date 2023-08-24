import time
import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import os

path = os.getcwd()


@pytest.fixture(scope="class")
def setup(request):

    desiredcababilities={


        "platformName": "Android",

        "deviceName": "Android Emulator",

        "app": f"{path}\\app\\Riddles(24-09-2022)fixed.apk"

    }
    #appium_service= AppiumService()
    #appium_service.start()
    #print(appium_service.is_running)
    #print(appium_service.is_listening)
    time.sleep(5)
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredcababilities)





    driver.implicitly_wait(150)

    request.cls.driver= driver





    #yield
    #appium_service.stop()
    #print(appium_service.is_running)
    #print(appium_service.is_listening)