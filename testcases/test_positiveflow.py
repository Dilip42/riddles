import logging
from datetime import date,datetime

from pages.category import categorypage
from base.scrolling import scrollingclass
from pages.homepage import homepage
from utilities import excelutilities, customlogger
import pytest
import time
path = "C:\\Users\\Sivasankar\\Desktop\\pythonProject\\riddles(27-07-2022)\\testdata\\Riddlesautomationdetails.xlsx"
excelsheet = "positveflow"
@pytest.mark.usefixtures("setup")
class Test_loginpage():
      def test_login(self):
          categorypageobject=categorypage(self.driver)
          homepageobject = homepage(self.driver)
          time.sleep(3)
          scrollingobject=scrollingclass(self.driver)
          log = customlogger.custologger.cuslog(logLevel=logging.INFO)
          rownumber = excelutilities.getRouCount(path,excelsheet)
          log.info(f"{rownumber} row numbers in Excel Sheet")
          for i in range(3, rownumber + 1):

              status = excelutilities.readData(path,excelsheet,i,11)
              if status != "done":
                  try:
                      time.sleep(5)
                      categorylist = excelutilities.readData(path, excelsheet, i, 1)
                      time.sleep(8)
                      scrollingobject.scrollingto(categorylist)

                      print(categorylist)
                      categorypageobject.customcategory(categorylist)
                      time.sleep(3)
                      #levelslist = excelutilities.readData(path,excelsheet,i,2)
                      #print(levelslist)
                      #categorypageobject.clicklevel1(levelslist)
                      navbar = categorypageobject.customnav()
                      print(navbar)
                      time.sleep(2)
                      excelutilities.writeData(path, excelsheet, i, 2, navbar)
                      time.sleep(8)

                      nextlevelsname = categorypageobject.readlevelsname()
                      excelutilities.writeData(path,excelsheet,i,3,nextlevelsname)
                      time.sleep(3)
                      levelcompletedstatus = excelutilities.readData(path,excelsheet,i,12)
                      if levelcompletedstatus != "None":
                        categorypageobject.clickreadlevels()
                        time.sleep(1)

                        time.sleep(1)

                  except:
                      pass

                  questions = categorypageobject.customques()
                  print(questions)
                  excelutilities.writeData(path,excelsheet,i,4,questions)
                  time.sleep(2)
                  categorypageobject.clickfirstchoice()

                  readfirstchoicetext = categorypageobject.readfirstchoice()
                  print(readfirstchoicetext)
                  excelutilities.writeData(path,excelsheet,i,5,readfirstchoicetext)

                  readcorrectanswerstatus = categorypageobject.readcorrectanswertext()
                  print(readcorrectanswerstatus)
                  excelutilities.writeData(path,excelsheet,i,6,readcorrectanswerstatus)
                  time.sleep(3)

                  readmonsterscore =categorypageobject.readmonster()
                  print(readmonsterscore)
                  excelutilities.writeData(path,excelsheet,i,7,readmonsterscore)

                  readrubyscore = categorypageobject.readruby()
                  print(readrubyscore)
                  excelutilities.writeData(path,excelsheet,i,8,readrubyscore)

                  readdiamondscore = categorypageobject.readdiamond()
                  print(readdiamondscore)
                  excelutilities.writeData(path,excelsheet,i,9,readdiamondscore)

                  homepageobject.clicknxtquesicon()

                  time.sleep(5)

                  try:
                      excelutilities.writeData(path,excelsheet,i,10,categorypageobject.compltedscore())
                      readlevelcompletedstatus=categorypageobject.readlevelcompleted()
                      excelutilities.writeData(path,excelsheet,i,12,readlevelcompletedstatus)
                      time.sleep(3)




                      categorypageobject.clicknextlevelicon()
                      categorypageobject.clickcategoryicon()
                      time.sleep(4)
                  except:

                      pass

                  excelutilities.writeData(path, excelsheet, i, 11, "done")













