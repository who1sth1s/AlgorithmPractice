import unittest
import time

from main.day_20161201.BracketEffectiveness import *


class CombinationUseRecursiveTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_combination(self):
        result = bracket_effectiveness('(((())(()){}{}[][]')
        self.assertEqual(result, False)

    if __name__ == '__main__':
        unittest.main()
