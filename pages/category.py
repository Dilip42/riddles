from selenium.webdriver.common.by import By

packagename = "com.riddlesDev.kidscustomerapp:id/"
#unlocklevel_id = "lockOrUnlockImage"
customnav_id = "categoryName"
customques_id = "riddleQuestion"
firstchoice_id = "firstChoice"
firstchoicetext_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.AdapterViewFlipper/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.TextView"
correctanswertext_id = "correctAnswerTxtview"
readlevelname_id = "levelName"
clickreadlevels_id = "lockOrUnlockImage"
monster_id = "monsterchip"
ruby_id = "rubychip"
diamond_id = "diamondchip"
completedscore_id = "scoreCountTextview"
nextlevelicon_id = "homeIcon"
categoryicon_id = "homeimg"
levelcompleted_id = "levelCompletedTextview"
subcat_count_id = "com.riddlesDev.kidscustomerapp:id/subcategorycount"


class categorypage():
    def __init__(self,driver):
        self.driver = driver

    def customnav(self):
         return self.driver.find_element(By.ID,customnav_id).text

    def customcategory(self, clickcategory):
        self.driver.find_element(By.XPATH,f"//android.widget.TextView[@text='{clickcategory}']").click()

    def customanswer(self,clickanswer):
        self.driver.find_element(By.XPATH,f"//android.widget.TextView[@text='{clickanswer}']").click()

    def customques(self):
        return self.driver.find_element(By.ID,customques_id).text

    def clickfirstchoice(self):
        self.driver.find_element(By.ID,firstchoice_id).click()

    def readfirstchoice(self):
        return self.driver.find_element(By.XPATH,firstchoicetext_xpath).text

    def readcorrectanswertext(self):
        return self.driver.find_element(By.ID,correctanswertext_id).text

    def readlevelsname(self):
        return self.driver.find_element(By.ID,readlevelname_id).text

    def clickreadlevels(self):
        self.driver.find_element(By.ID,clickreadlevels_id).click()

    def clicklevel1(self,levelstage):
        self.driver.find_element(By.XPATH,f"//android.widget.TextView[@text='{levelstage}']").click()

    def readmonster(self):
        return self.driver.find_element(By.ID,monster_id).text

    def readruby(self):
        return self.driver.find_element(By.ID,ruby_id).text

    def readdiamond(self):
        return self.driver.find_element(By.ID,diamond_id).text

    def compltedscore(self):
        return self.driver.find_element(By.ID,completedscore_id).text

    def clicknextlevelicon(self):
        self.driver.find_element(By.ID,nextlevelicon_id).click()

    def clickcategoryicon(self):
        self.driver.find_element(By.ID,categoryicon_id).click()

    def readlevelcompleted(self):
        return self.driver.find_element(By.ID,levelcompleted_id).text

    def readlevels(self):
        self.driver.find_elements(By.ID,"//com.riddlesDev.kidscustomerapp:id/levelName")

    def options(self):
        self.driver.find_elements(By.XPATH,"//android.widget.TextView")

    def clicklevel(self,level):
        self.driver.find_element(By.XPATH,f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[{level}]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()


    def categorynames(self):
        return self.driver.find_elements(By.XPATH,f"//android.widget.TextView")

    def readlevelcount(self):
        return self.driver.find_elements(By.XPATH,f"//android.widget.TextView")

    def subcatcount(self):
        return self.driver.find_element(By.ID,subcat_count_id).text




