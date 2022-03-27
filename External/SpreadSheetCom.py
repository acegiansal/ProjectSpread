import pygsheets
import pandas as pd

def testFunction():
    print("THIS IS A TEST")
    return 3

def openSpreadsheet(pageName):
    # authorization
    gc = pygsheets.authorize(service_file='D:/Documents/Creds/credentials3.json')
    # open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open(pageName)
    return sh
