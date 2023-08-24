packagename = "com.riddlesDev.kidscustomerapp:id /"
nextquestionicon_id = "next"
nextlevelicon_id = "homeIcon"
replayicon_id = "replayIcon"
totalscorecount_id = "scoreCountTextview"
categoryicon_id = "homeimg"
backicon_id = "backicon"
unlocklevel_id = "lockOrUnlockImage"
questioncount_id = "com.riddlesDev.kidscustomerapp:id/questionCount"

from selenium.webdriver.common.by import By

class homepage():

    def __init__(self,driver):
        self.driver = driver

    def clicknxtquesicon(self):
        self.driver.find_element(By.ID,nextquestionicon_id).click()

    def clicknextlevelicon(self):
        self.driver.find_element(By.ID,nextlevelicon_id).click()

    def clickreplayicon(self):
        self.driver.find_element(By.ID,replayicon_id).click()

    def readtotalscorecount(self):
        self.driver.find_element(By.ID,totalscorecount_id)

    def clickcategoryicon(self):
        self.driver.find_element(By.ID,categoryicon_id).click()

    def clickbackicon(self):
        self.driver.find_element(By.ID,backicon_id).click()

    def clickunlocklevel(self):
        self.driver.find_element(By.ID,unlocklevel_id).click()

    def questioncount(self):
        return self.driver.find_element(By.ID,questioncount_id).text


