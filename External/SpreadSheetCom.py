import pygsheets
from External.DataManagement import DataManagement


def open_spreadsheet(page_name) -> pygsheets.spreadsheet.Spreadsheet:
    # authorization
    # The credentials should be added to the project directory, and will be git ignored
    gc = pygsheets.authorize(service_file='credentials.json')
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


def transpose_range(data_range: pygsheets.DataRange):
    # Get the data as a python list of lists
    print(data_range)
    data_as_list = data_range
    transposed_table = DataManagement.transpose_range(data_as_list)
    return transposed_table


if __name__ == '__main__':
    test_range = [ [1,2,3], [4,5,6] ]
    print("Previous Table:\n---------------")
    for row in test_range:
        for val in row:
            print(val, end=" ")
        print()
    print("----------------\nGoal:\n------------------")
    goal = [ [1,4], [2,5], [3,5] ]
    for row in goal:
        for val in row:
            print(val, end=" ")
        print()
    print("----------------\nGot:\n------------------")
    got = transpose_range(test_range)
    for row in got:
        for val in row:
            print(val, end=" ")
        print()

