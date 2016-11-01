import unittest
import time

from main.day_20161031.FibonacciSequence import *

class FibonacciSequenceTestClass(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetFibonacciNumberByIterate(self):
        self.assertEqual(FibonacciSequence().get_fibonacci_number_by_iterate(1), 0)
        self.assertEqual(FibonacciSequence().get_fibonacci_number_by_iterate(2), 1)
        self.assertEqual(FibonacciSequence().get_fibonacci_number_by_iterate(3), 1)
        self.assertEqual(FibonacciSequence().get_fibonacci_number_by_iterate(4), 2)
        self.assertEqual(FibonacciSequence().get_fibonacci_number_by_iterate(5), 3)

    def testGetFibonacciNumberByRecursive(self):
        fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        start = time.time()
        for index in range(1, 6):
            fibonacci_sequence_class = FibonacciSequence()
            fibonacci_sequence_class.get_fibonacci_number_by_recursive(index)
            self.assertEqual(fibonacci_sequence_class.FIBONACCI_LIST[index-1], fibonacci_sequence[index-1])
        end = time.time()
        print(end-start)

    if __name__ == '__main__':
        unittest.main()