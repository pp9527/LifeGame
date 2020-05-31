"""test check.py"""
import unittest
from check import *


class TestCheck(unittest.TestCase):
    """test check.py"""
    def test_check1(self):
        """test check method"""
        self.assertEqual(50, check_int('50'))

    def test_check2(self):
        """test check method"""
        self.assertEqual(-1, check_int('s'))

    def test_check3(self):
        """test check method"""
        self.assertEqual(-1, check_int('-1'))


if __name__ == '__main__':
    unittest.main()
