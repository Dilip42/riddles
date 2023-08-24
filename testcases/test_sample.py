import logging
from datetime import date, datetime

from pages.category import categorypage
from base.scrolling import scrollingclass
from pages.homepage import homepage
from utilities import excelutilities, customlogger
from sheetutilities import sheets
import pytest
import time
from base.screenshot import screenshotclass


# path = "./testdata/Riddlesautomationdetails.xlsx"
# excelsheet = "testsheet"

@pytest.mark.usefixtures("setup")
class Test_loginpage():

    def test_login(self):

        categorypageobject = categorypage(self.driver)
        homepageobject = homepage(self.driver)
        scrollingobject = scrollingclass(self.driver)
        # max_row = excelutilities.getRouCount(path,excelsheet)
        log = customlogger.custologger.cuslog(logLevel=logging.INFO)
        screenshotobject = screenshotclass(self.driver)

        sheets.selectsheet('Animals_flow')

        row_count = int(sheets.row_count())

        row = 2
        back_to_row = 2
        question_write = 2
        col_count = 3

        categoryname = 'Animals'
        categorypageobject.customcategory(categoryname)
        time.sleep(3)

        subcategorylist = [0,1,2,3,4,5,6,7,8,9,10]
        subcategorylistlen = len(subcategorylist)

        subcategory = int(subcategorylistlen)


        for i in range(1,subcategory+1):

            categorypageobject.clicklevel1(i)
            time.sleep(3)

            question_count = int(homepageobject.questioncount())
            print(question_count)

            for question_count in range(1, question_count + 1):
                time.sleep(3)
                question_in_app = categorypageobject.customques()
                log.info(question_in_app)
                sheets.writedata(question_write,col_count,question_in_app)

                for init in range(back_to_row, row_count + 1):

                    time.sleep(3)
                    question_name = sheets.readdata(f'A{init}')
                    answer_option = sheets.readdata(f'B{init}')

                    print(f'The Sheet Question is {question_name}')
                    # print(f'The App Question is {question_in_app}')

                    if question_name == question_in_app:

                        time.sleep(3)

                        categorypageobject.customanswer(answer_option)
                        time.sleep(2)

                        screenshotobject.takephoto('Riddle_')

                        homepageobject.clicknxtquesicon()
                        time.sleep(2)

                        question_write = question_write +1
                        col_count = col_count + 1

                        break

                    else:
                        init = back_to_row

            back_to_row = back_to_row + question_count
            print(back_to_row)

            homepageobject.clicknextlevelicon()
            time.sleep(5)























































