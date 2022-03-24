import unittest
from External.SpreadSheetCom import *


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        print("HELLO I AM IN HERE")

    def test_SpreadSheetCom(self):
        self.assertEqual(3, testFunction(), "Test function failed!")



if __name__ == '__main__':
    unittest.main()
