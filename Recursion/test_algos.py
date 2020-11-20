import unittest
from super_algos import *
from unittest.mock import patch
from io import StringIO


class TestFunctions(unittest.TestCase):
    def test_find_min(self):
        result = find_min([3,2,1,5])
        result1 = find_min([])
        result2 = find_min(["a"])
        self.assertEqual(result, 1)
        self.assertEqual(result1, -1)
        self.assertEqual(result2, -1)

    def test_sum_all(self):
        result = sum_all([1,2,3,4])
        result1 = sum_all([])
        result2 = find_min(["b"])
        self.assertEqual(result, 10)
        self.assertEqual(result1, -1)
        self.assertEqual(result2, -1)
        
    def test_find_possible_strings(self):
        l = ['x','y']
        res = find_possible_strings(l, 3)
        self.assertEqual(res, ['xxx', 'xxy', 'xyx', 'xyy', 'yxx', 'yxy', 'yyx', 'yyy'])