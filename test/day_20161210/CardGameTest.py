import unittest

from main.day_20161210.CardGame import *


class CardGameTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_combination(self):
        result = random_card_game(4)
        print(result)

    if __name__ == '__main__':
        unittest.main()
