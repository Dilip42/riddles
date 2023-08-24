import logging
from datetime import date,datetime

from pages.category import categorypage
from base.scrolling import scrollingclass
from pages.homepage import homepage
from utilities import excelutilities, customlogger
from sheetutilities import sheets
import pytest
import time
from base.screenshot import screenshotclass

#path = "./testdata/Riddlesautomationdetails.xlsx"
#excelsheet = "testsheet"

@pytest.mark.usefixtures("setup")
class Test_loginpage():

      def test_login(self):

          categorypageobject=categorypage(self.driver)
          homepageobject = homepage(self.driver)
          scrollingobject=scrollingclass(self.driver)
          #max_row = excelutilities.getRouCount(path,excelsheet)
          log = customlogger.custologger.cuslog(logLevel=logging.INFO)
          screenshotobject = screenshotclass(self.driver)


          sheets.selectsheet('sample_flow')

          row_count = int(sheets.row_count())
          print(row_count)
          log.info(f"{row_count} row numbers in Excel Sheet")
          time.sleep(10)

          ## To Read the Category Names ###
          cate_list = categorypageobject.categorynames()
          time.sleep(5)

          len_of = (len(cate_list))
          count = int(len_of)
          print(count)

          a_list = []

          for val in cate_list:
              ele_name = val.get_attribute("text")
              log.info(ele_name)
              a_list.append(ele_name)
              time.sleep(3)

          print(a_list)

          col_count = 3
          question_write = 2
          initial = 2

          for category in range(1, len_of):
              cat_name = a_list[category]
              print(cat_name)


              if cat_name in a_list:
                  categorypageobject.customcategory(cat_name)
                  print(category)
                  #excelutilities.writeData(path,excelsheet,1,categorycount,cat_name)
                  time.sleep(5)


                ### To Read the Level Count in the Category Page ###
                  read_levels = categorypageobject.readlevelcount()
                  level_len = len(read_levels)
                  level_count = int(level_len)
                  print(f"levelcount is {level_count}")

                  b_list = []
                  for value in read_levels:
                      element_name = value.get_attribute("text")
                      print(element_name)
                      b_list.append(element_name)
                  print(b_list)
                  time.sleep(5)



                  for levels in range(1, level_count):
                      levelcount = (b_list[levels])
                      print(f"The level is {levels}")
                      time.sleep(5)

                      if levelcount in b_list:
                          categorypageobject.clicklevel1(levelcount)
                          time.sleep(5)

                          questioncunt = int(homepageobject.questioncount())
                          log.info(questioncunt)



                          for question_count in range(1, questioncunt + 1):
                              time.sleep(3)
                              question_in_app = categorypageobject.customques()
                              #log.info(question_in_app)
                              #sheets.writedata(question_write,col_count,question_in_app)

                              for init in range(initial,row_count+1):

                                  time.sleep(3)
                                  question_name = sheets.readdata(f'A{init}')
                                  answer_option = sheets.readdata(f'B{init}')

                                  print(f'The Sheet Question is {question_name}')
                                  #print(f'The App Question is {question_in_app}')

                                  if question_name == question_in_app:

                                      time.sleep(3)

                                      categorypageobject.customanswer(answer_option)
                                      time.sleep(2)

                                      screenshotobject.takephoto('Riddle_')

                                      homepageobject.clicknxtquesicon()
                                      time.sleep(2)
                                      break

                                  else:
                                      init = initial
                                      #print(init)
                                      #return init

                          initial = initial + questioncunt
                          print(f'initiaal is {initial}')

                          homepageobject.clicknextlevelicon()
                          time.sleep(5)















                          




































                  '''for levels in range(1,level_count):
                      levelcount = (b_list[levels])
                      print(f"The level is {levels}")
                      time.sleep(5)

                      if levelcount in b_list:

                          categorypageobject.clicklevel1(levelcount)
                          time.sleep(5)

                          questioncunt = int(homepageobject.questioncount())
                          log.info(questioncunt)

                          categorycount = categorycount+questioncunt
                          log.info(categorycount)

                          question_count =1

                          for question_count in range(1,questioncunt+1):

                              question = categorypageobject.customques()
                              log.info(question)

                              excelutilities.writeData(path,excelsheet,question_count,2,question)
                              time.sleep(2)

                              categorypageobject.clickfirstchoice()
                              time.sleep(2)

                              homepageobject.clicknxtquesicon()
                              time.sleep(2)

                          #return question_count


                          questioncunt = question_count + questioncunt
                          print(questioncunt)

                      homepageobject.clicknextlevelicon()
                      time.sleep(5)
                  self.driver.press_keycode(4)
                  time.sleep(5)'''
































