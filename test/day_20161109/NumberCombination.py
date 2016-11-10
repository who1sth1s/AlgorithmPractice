import unittest
import time

from main.day_20161109.NumberCombination import *


class NumberCombinationTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_combination(self):
        result = get_combination(4)
        self.assertEqual(result, 7)

    if __name__ == '__main__':
        unittest.main()