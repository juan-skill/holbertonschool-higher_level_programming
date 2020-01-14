#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    test cases for max integer function
    """

    def test_numbers(self):
        self.assertEqual(max_integer([2, 3, 4, 8, 10]), 10)
        self.assertEqual(max_integer([-2, -1, -4, -5, 1]), 1)
        self.assertEqual(max_integer([2.5, -1.2, 6.6, 9.9, 10.5]), 10.5)
        self.assertEqual(max_integer([98, 98, 98, 98]), 98)
        self.assertEqual(max_integer([10000]), 10000)

    def test_character(self):
        self.assertEqual(max_integer(["Hello", "World"]), "World")
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_bool(self):
        self.assertEqual(max_integer([98, True, False, -9, 39, 1337]), 1337)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_error(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "Holberton"])


if __name__ == '__main__':
    unittest.main()
