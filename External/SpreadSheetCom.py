import pygsheets
import pandas as pd


def open_spreadsheet(page_name):
    # authorization
    gc = pygsheets.authorize(service_file='credentials3.json')
    # open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open(page_name)
    return sh


def print_range(date_range):
    """
    Can only print a column
    :param date_range:
    :return:
    """
    for c in date_range.cells:
        for cell in c:
            print(f"Cell {cell.label} has value: {cell.value}")


def update_row(date_range, values: list):
    to_add = [values]
    date_range.update_values(to_add)
