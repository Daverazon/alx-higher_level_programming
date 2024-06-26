#!/usr/bin/python3
"""Defines a unittest for the function `def max_integer(list=[])`"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test the max_integer function
    """
    def test_listContents(self):
        """
        Test the results from various list contents
        """
        self.assertEqual(max_integer([5, 30, 833]), 833)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-434, -9.4, -1024]), -9.4)
        self.assertEqual(max_integer(
            [float('inf'), float('nan')]), float('inf'))
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([4, 4, 4]), 4)


if __name__ == '__main__':
    unittest.main()
