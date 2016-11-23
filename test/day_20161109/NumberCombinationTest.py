import unittest

from main.day_20161109.NumberCombination import *


class NumberCombinationTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_combination(self):
        result = get_combination(6)
        print(result)

    if __name__ == '__main__':
        unittest.main()