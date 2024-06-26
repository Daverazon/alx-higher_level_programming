#!/usr/bin/python3
"""Defines a unittest for the function `def max_integer(list=[])`"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test the max_integer function
    """
    def test_max_in_last_position(self):
        self.assertEqual(max_integer([5, 30, 833]), 833)

    def test_max_in_middle_position(self):
        self.assertEqual(max_integer([4, 54, 2]), 54)

    def test_max_in_first_position(self):
        self.assertEqual(max_integer(
            [float('inf'), float('nan')]), float('inf'))

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_all_negative_numbers(self):
        self.assertEqual(max_integer([-434, -9.4, -1024]), -9.4)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-4, 84, 2]), 84)

    def test_one_number(self):
        self.assertEqual(max_integer([-379]), -379)

    def test_all_numbers_same(self):
        self.assertEqual(max_integer([4, 4, 4]), 4)


if __name__ == '__main__':
    unittest.main()
