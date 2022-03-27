import pygsheets
import DataManagement


def open_spreadsheet(page_name) -> pygsheets.spreadsheet.Spreadsheet:
    # authorization
    gc = pygsheets.authorize(service_file='credentials3.json')
    # open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
    sh = gc.open(page_name)
    return sh


def print_range(data_range) -> None:
    """
    Prints any range cell by cell
    :param data_range: The range to print
    :return: None
    """
    for c in data_range.cells:
        for cell in c:
            print(f"Cell {cell.label} has value: {cell.value}")


def update_row(data_range: pygsheets.DataRange, values: list) -> None:
    to_add = [values]
    data_range.update_values(to_add)


def compare_ranges(r1, values):
    for i in range(len(r1.cells)):
        row_to_check = DataManagement.convert_to_str(values[i])
        counter = 0
        for cell in r1.cells[i]:
            if cell.value != row_to_check[counter]:
                return False
            counter += 1
    return True


