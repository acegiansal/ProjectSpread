import unittest
import pygsheets
from External import SpreadSheetCom


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        print("HELLO I AM IN HERE")

    def test_transpose(self):
        test_range = [[1, 2, 3], [4, 5, 6]]
        print("Previous Table:\n---------------")
        for row in test_range:
            for val in row:
                print(val, end=" ")
            print()
        print("----------------\nGoal:\n------------------")
        goal = [[1, 4], [2, 5], [3, 5]]
        for row in goal:
            for val in row:
                print(val, end=" ")
            print()
        print("----------------\nGot:\n------------------")
        got = SpreadSheetCom.transpose_range(test_range)
        for row in got:
            for val in row:
                print(val, end=" ")
            print()



if __name__ == '__main__':
    unittest.main()
