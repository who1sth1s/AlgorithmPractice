import unittest
import time

from main.day_20161031.FibonacciSequence import *


FIBONACCI_LIST = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]  # 21


class FibonacciSequenceTestClass(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetFibonacciNumberByIterate(self):
        for index in range(5):
            self.assertEqual(get_fibonacci_number_by_iterate(index+1), FIBONACCI_LIST[index])

    def testGetFibonacciNumberByRecursive(self):
        self.assertEqual(get_fibonacci_number_by_recursive(21), FIBONACCI_LIST[20])

    if __name__ == '__main__':
        unittest.main()