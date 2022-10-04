import pygsheets
import pandas as pd
from External import SpreadSheetCom
from External import DataManagement

SPREADSHEET_NAME = "Test Spreadsheet"

if __name__ == '__main__':
    sheet = SpreadSheetCom.open_spreadsheet(SPREADSHEET_NAME)

    # Create empty dataframe
    df = pd.DataFrame()

    # Create a column
    df['name'] = ['John', 'Steve', 'Sarah']
    df['test'] = [1, 2, 3]
    print(f"df: {type(df)}, value: \n{df}")

    # select the first sheet
    wks = sheet[0]

    # update the first sheet with df,
    wks.set_dataframe(df,(1,1))

    dateRange = pygsheets.DataRange('A1', 'b4', wks)
    print(dateRange)
    SpreadSheetCom.print_range(dateRange)
    print(wks.range('A1:B4', returnas='matrix'))

    print(SpreadSheetCom.transpose_range(dateRange))

    # testDateRange = pygsheets.DataRange('A5', 'd5', wks)
    # SpreadSheetCom.update_row(testDateRange, [5, 6, 7, 8])
    # row_check = SpreadSheetCom.compare_ranges(testDateRange, [[5, 6, 7, 8]])
    # if not row_check:
    #     print("update row did not work!")
    # else:
    #     print("update row worked!")

