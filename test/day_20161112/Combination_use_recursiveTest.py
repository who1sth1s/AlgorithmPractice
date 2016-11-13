import unittest
import time

from main.day_20161112.Combination_use_recursive import *


class CombinationUseRecursiveTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_combination(self):
        result = combination_recursive(4)
        self.assertEqual(result, 7)

    if __name__ == '__main__':
        unittest.main()