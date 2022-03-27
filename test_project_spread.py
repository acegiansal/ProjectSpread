import unittest
import pygsheets
from External import SpreadSheetCom


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        print("HELLO I AM IN HERE")




if __name__ == '__main__':
    unittest.main()
