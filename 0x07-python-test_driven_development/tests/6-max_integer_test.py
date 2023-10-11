#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3, 43, -2]), 43)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer((3, 87, 9)), 87)
        self.assertEqual(max_integer('4, 683, -8'), '8')
