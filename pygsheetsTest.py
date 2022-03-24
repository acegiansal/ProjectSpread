import pygsheets
import pandas as pd
import argparse

SPREADSHEET_NAME = "Test Spreadsheet"

if __name__ == '__main__':
    #authorization
    gc = pygsheets.authorize(service_file='credentialsPart2.json')

    # Create empty dataframe
    df = pd.DataFrame()

    # Create a column
    df['name'] = ['John', 'Steve', 'Sarah']

    #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open(SPREADSHEET_NAME)

    #select the first sheet
    wks = sh[0]

    #update the first sheet with df, starting at cell B2.
    # wks.set_dataframe(df,(1,1))

    dateRange = pygsheets.DataRange('A1', 'A4', wks)
    for c in dateRange.cells:
        cell = c[0]
        print(f"Cell {cell.label} has value: {cell.value}")

    for row in wks:
        print(row)
