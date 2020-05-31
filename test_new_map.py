"""test new_map.py"""
import unittest
from new_map import *


class TestNewMap(unittest.TestCase):
    """test new_map.py"""
    def test_cell_laws(self):
        """test cell_laws method"""
        old_map = [
            [0, 1, 0],
            [0, 1, 1],
            [0, 1, 1],
        ]
        new_map = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.assertEqual(new_map, cell_laws(old_map))


if __name__ == '__main__':
    unittest.main()
