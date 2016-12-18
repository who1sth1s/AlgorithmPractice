import unittest

from main.day_20161218.InterestingParty import *


class CardGameTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_combination(self):
        test1_first = ['fishing', 'gardening', 'swimming', 'fishing']
        test1_second = ['hunting', 'fishing', 'fishing', 'biting']

        test2_first = ['variety', 'diversity', 'loquacity', 'courtesy']
        test2_second = ['talking', 'speaking', 'discussion', 'meeting']

        test3_first = ['snakes', 'programming', 'cobra', 'monty']
        test3_second = ['python', 'python', 'anaconda', 'python']

        test4_first = ['t', 'o', 'p', 'c', 'o', 'd', 'e', 'r', 's', 'i', 'n', 'g', 'l', 'e', 'r', 'o', 'u', 'n', 'd', 'm', 'a', 't', 'c', 'h', 'f', 'o', 'u', 'r', 'n', 'i']
        test4_second = ['n', 'e', 'f', 'o', 'u', 'r', 'j', 'a', 'n', 'u', 'a', 'r', 'y', 't', 'w', 'e', 'n', 't', 'y', 't', 'w', 'o', 's', 'a', 't', 'u', 'r', 'd', 'a', 'y']

        interesting_party1 = InterestingParty(test1_first, test1_second)
        interesting_party2 = InterestingParty(test2_first, test2_second)
        interesting_party3 = InterestingParty(test3_first, test3_second)
        interesting_party4 = InterestingParty(test4_first, test4_second)

        result1 = interesting_party1.best_invitation()
        result2 = interesting_party2.best_invitation()
        result3 = interesting_party3.best_invitation()
        result4 = interesting_party4.best_invitation()

        self.assertEqual('4' in result1, True)
        self.assertEqual('1' in result2, True)
        self.assertEqual('3' in result3, True)
        self.assertEqual('6' in result4, True)

    if __name__ == '__main__':
        unittest.main()
