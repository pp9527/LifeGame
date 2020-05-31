# -*- coding: utf-8 -*-

import unittest
from test_init import TestInit
from test_check import TestCheck
from test_new_map import TestNewMap

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestCheck("test_check1"), TestCheck("test_check2"), TestCheck("test_check3"),
             TestInit("test_init_map1"), TestInit("test_init_map2"), TestInit("test_init_map3"),
             TestNewMap("test_cell_laws")]

    suite.addTests(tests)
    with open('UnittestTextReport.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
