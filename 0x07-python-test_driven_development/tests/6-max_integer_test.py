#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        # Test for an empty list
        result = max_integer([])
        self.assertIsNone(result)
    
    def test_non_list_input(self):
        # Test for when a list is not passed as the input
        string = [1, 2, "Hello", 4, 5]
        self.assertRaises(TypeError, max_integer, string)

    def test_list_withh_value(self):
        # Test for with float/int values
        self.assertEqual(max_integer([1,2,4,9,3,5]), 9)
        self.assertEqual(max_integer([-1,-2,-4,-9,-3,-5]), -1)
        self.assertEqual(max_integer([1,-2,4,-9,3,-5]), 4)
        self.assertAlmostEqual(max_integer([1.5, 2.2, 4.8, 3.7]), 4.8)
        self.assertAlmostEqual(max_integer([-1.5, -2.2, -4.8, -3.7]), -1.5)
        self.assertAlmostEqual(max_integer([1.5, -2.2, 4.8, -3.7]), 4.8)
