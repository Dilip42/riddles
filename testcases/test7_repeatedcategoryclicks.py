import logging
from datetime import date,datetime

from pages.category import categorypage
from base.scrolling import scrollingclass
from pages.homepage import homepage
from utilities import excelutilities, customlogger
import pytest
import time
from sheetutilities import sheets



@pytest.mark.usefixtures("setup")
class Test_loginpage():

      def test_login(self):

          categorypageobject=categorypage(self.driver)
          homepageobject = homepage(self.driver)
          scrollingobject=scrollingclass(self.driver)
          #max_row = excelutilities.getRouCount(path,excelsheet)
          log = customlogger.custologger.cuslog(logLevel=logging.INFO)
          time.sleep(10)

          sheets.selectsheet("test5_repeatedclickcategories")

          row_cou = 2
          levels = 2

          cate_list = categorypageobject.categorynames()
          time.sleep(5)

          len_of = (len(cate_list))
          count = int(len_of)
          print(count)

          a_list = []

          for val in cate_list:
              ele_name = val.get_attribute("text")
              log.info(ele_name)
              # excelutilities.writeData(path,excelsheet,val,1,ele_name)
              a_list.append(ele_name)
              time.sleep(3)

          print(a_list)



          for category in range(1, len_of):
              cat_name = a_list[category]
              print(cat_name)


              if cat_name in a_list:
                  cat_name=sheets.readdata(f"A{levels}")
                  categorypageobject.customcategory(cat_name)
                  print(f"category is {cat_name}")
                  time.sleep(1)

                  status = sheets.readdata(f"L{row_cou}")
                  print(status)

                  if status != f"{cat_name} Completed":

                      #sheets.writedata(row_cou, 1, cat_name)
                      navbar = categorypageobject.customnav()
                      sheets.writedata(row_cou,2,navbar)


                      read_levels = categorypageobject.readlevelcount()
                      level_len = len(read_levels)
                      level_count = int(level_len)
                      print(f"levelcount is {level_count}")

                      b_list = []

                      for value in read_levels:
                          time.sleep(1)
                          element_name = value.get_attribute("text")
                          print(element_name)
                          b_list.append(element_name)
                      print(b_list)
                      time.sleep(5)


                      for level in range(1, level_count):
                          levelcount = (b_list[level])
                          print(f"The level is {levelcount}")
                          time.sleep(5)
                          sheets.writedata(row_cou,3,levelcount)

                          if levelcount in b_list:

                              categorypageobject.clicklevel1(levelcount)
                              time.sleep(5)

                              que_count = int(homepageobject.questioncount())
                              print(f"question count is {que_count}")

                              for question in range(1, que_count + 1):

                                question = categorypageobject.customques()
                                log.info(f"Question is  {question}")

                                sheets.writedata(levels, 4, question)

                                answerlist = sheets.readdata(f"E{levels}")
                                print(f"{answerlist}answer is")
                                categorypageobject.customanswer(answerlist)

                                readcorrectanswerstatus = categorypageobject.readcorrectanswertext()
                                print(readcorrectanswerstatus)
                                sheets.writedata(levels, 6, readcorrectanswerstatus)
                                time.sleep(5)

                                readmonsterscore = categorypageobject.readmonster()
                                print(readmonsterscore)
                                sheets.writedata(levels, 7, readmonsterscore)

                                readrubyscore = categorypageobject.readruby()
                                print(readrubyscore)
                                sheets.writedata(levels, 8, readrubyscore)

                                readdiamondscore = categorypageobject.readdiamond()
                                print(readdiamondscore)
                                sheets.writedata(levels, 9, readdiamondscore)

                                sheets.writedata(levels,12,f"{cat_name} Completed")

                                homepageobject.clicknxtquesicon()
                                time.sleep(2)

                                levels = levels + 1

                              categorycount1 = levels - 1
                              print(levels)
                              sheets.writedata(categorycount1, 10, categorypageobject.compltedscore())

                              readlevelcompletedstatus = categorypageobject.readlevelcompleted()
                              sheets.writedata(categorycount1, 11, readlevelcompletedstatus)
                              time.sleep(5)

                              row_cou = row_cou + que_count
                              print(f"count is{row_cou}")

                          homepageobject.clicknextlevelicon()
                          time.sleep(5)



                      time.sleep(5)
                      categorypageobject.clickcategoryicon()
                      time.sleep(5)