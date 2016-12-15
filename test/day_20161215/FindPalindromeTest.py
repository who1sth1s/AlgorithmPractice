import unittest

from main.day_20161215.FindPalindrome import *


class CardGameTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_combination(self):
        result = find_palindrome(195)
        self.assertEqual(result, (195, 4, 9339))

    if __name__ == '__main__':
        unittest.main()
