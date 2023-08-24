import pygsheets
import os

path = os.getcwd()

print(f'the path is {path}')

client = pygsheets.authorize(service_account_file=f"{path}\\sheetutilities\\testingteamworksheet-30dce50f0c9f.json")

spreadsheet = client.open("testing")

def selectsheet(sheetname):
    global worksheet
    worksheet = spreadsheet.worksheet("title",f"{sheetname}")

def row_count():

    a = worksheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False,returnas="matrix")
    row_count = (len(a))
    return row_count

def col_count():
    b = worksheet.get_col(1,returnas='matrix', include_tailing_empty=False)
    col_count = len(b)
    return col_count

def readdata(row):
    readdata = worksheet.get_value(f"{row}")
    return readdata

def writedata(row,column,data):
    writedata = worksheet.cell((row,column)).value = f"{data}"
    return writedata


'''selectsheet('sample_flow')

col = row_count()
print(col)'''