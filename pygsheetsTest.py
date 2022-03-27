import pygsheets
import pandas as pd
from External import SpreadSheetCom

SPREADSHEET_NAME = "Test Spreadsheet"

if __name__ == '__main__':
    sheet = SpreadSheetCom.open_spreadsheet(SPREADSHEET_NAME)

    # Create empty dataframe
    df = pd.DataFrame()

    # Create a column
    df['name'] = ['John', 'Steve', 'Sarah']

    # select the first sheet
    wks = sheet[0]

    # update the first sheet with df,
    # wks.set_dataframe(df,(1,1))

    dateRange = pygsheets.DataRange('A1', 'b4', wks)
    print(dateRange)
    SpreadSheetCom.print_range(dateRange)

    testDateRange = pygsheets.DataRange('A5', 'd5', wks)

    SpreadSheetCom.update_row(testDateRange, [5,6,7,8])
