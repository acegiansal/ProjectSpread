import pygsheets
import pandas as pd


def open_spreadsheet(page_name):
    # authorization
    gc = pygsheets.authorize(service_file='credentials3.json')
    # open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open(page_name)
    return sh


def print_column(date_range):
    """
    Can only print a column
    :param date_range:
    :return:
    """
    for c in date_range.cells:
        cell = c[0]
        print(f"Cell {cell.label} has value: {cell.value}")
