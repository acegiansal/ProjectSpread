import pygsheets
import pandas as pd
from External import SpreadSheetCom

SPREADSHEET_NAME = "Test Spreadsheet"

if __name__ == '__main__':
    sheet = SpreadSheetCom.openSpreadsheet(SPREADSHEET_NAME)

    # Create empty dataframe
    df = pd.DataFrame()

    # Create a column
    df['name'] = ['John', 'Steve', 'Sarah']

    #select the first sheet
    wks = sheet[0]

    #update the first sheet with df, starting at cell B2.
    # wks.set_dataframe(df,(1,1))

    dateRange = pygsheets.DataRange('A1', 'A4', wks)
    for c in dateRange.cells:
        cell = c[0]
        print(f"Cell {cell.label} has value: {cell.value}")

    for row in wks:
        print(row)
