import logging
from datetime import date,datetime

from pages.category import categorypage
from base.scrolling import scrollingclass
from pages.homepage import homepage
from utilities import excelutilities, customlogger
import pytest
import time
path = "C:\\Users\\Sivasankar\\Desktop\\pythonProject\\pythonProject\\riddles(27-07-2022)\\testdata\\Riddlesautomationdetails.xlsx"
excelsheet = "randomnavigation"
@pytest.mark.usefixtures("setup")
class Test_loginpage():
      def test_login(self):
          categorypageobject=categorypage(self.driver)
          homepageobject = homepage(self.driver)
          time.sleep(3)
          scrollingobject=scrollingclass(self.driver)
          log = customlogger.custologger.cuslog(logLevel=logging.INFO)
          rownumber = excelutilities. getRouCount(path,excelsheet)
          log.info(f"{rownumber} row numbers in Excel Sheet")
          for i in range(2, rownumber + 1):
              time.sleep(5)
              status = excelutilities.readData(path, excelsheet, i, 11)
              if status != "done":
                  categorylist = excelutilities.readData(path,excelsheet, i, 1)
                  scrollingobject.scrollingto(categorylist)
                  print(categorylist)
                  categorypageobject.customcategory(categorylist)
                  time.sleep(5)
                  navbar = categorypageobject.customnav()
                  print(navbar)
                  time.sleep(2)
                  excelutilities.writeData(path,excelsheet, i, 2, navbar)
                  time.sleep(5)
                  excelutilities.writeData(path,excelsheet,i,3,"Done" )
                  homepageobject.clickcategoryicon()
                  today = date.today()
                  uploaddate = today.strftime("%d/%m/%Y")
                  excelutilities.writeData(path,excelsheet, i, 4, uploaddate)
                  todaytime = datetime.now()
                  uploadedtime = todaytime.strftime("%H:%M:%S")
                  excelutilities.writeData(path,excelsheet, i, 5, uploadedtime)
                  time.sleep(7)