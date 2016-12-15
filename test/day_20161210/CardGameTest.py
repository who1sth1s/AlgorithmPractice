import unittest

from main.day_20161210.CardGame import *


class CardGameTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_combination(self):
        result = card_game()
        self.assertEqual('Winner' in result, True)

    if __name__ == '__main__':
        unittest.main()
