class toasting:
    def __init__(self,driver):
        self.driver = driver

    def toastmess(self):
        return self.driver.find_element_by_xpath("//android.widget.Toast[1]").text