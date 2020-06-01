"""
test init.py
"""
import unittest
from init import *


class TestInit(unittest.TestCase):
    """test init.py"""

    def test_init_map1(self):
        """test init_map method"""
        if init_map(10, 10) == -1:
            sign = init_map(10, 10)
        else:
            sign = 1
        self.assertEqual(1, sign)

    def test_init_map2(self):
        """test init_map method"""
        if init_map(0, 0) == -1:
            sign = init_map(0, 0)
        else:
            sign = 1
        self.assertEqual(-1, sign)

    def test_init_map3(self):
        """test init_map method"""
        if init_map(-1, -1) == -1:
            sign = init_map(-1, -1)
        else:
            sign = 1
        self.assertEqual(-1, sign)


if __name__ == '__main__':
    unittest.main()
