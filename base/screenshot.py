import os
import time
path = os.getcwd()

class screenshotclass():

    def __init__(self,driver):
        self.driver = driver

    def takephoto(self,file):
        ts = time.strftime("%Y_%m_%d_%H_%M_%S")
        print(ts)
        #activity_name = self.driver.current_activity
        file_name = file+ts
        #print(file_name)
        self.driver.save_screenshot(f"{path}\\screenshots\\" + file_name + ".png")

