import unittest
from world.obstacles import *

class TestFunctions(unittest.TestCase):
    
    def test_is_position_blocked(self):
        res = is_position_blocked(10, 10)
        self.assertEqual(res, False)

    def test_is_path_blocked(self):
        res = is_path_blocked(10, 10, 12, 12)
        self.assertEqual(res, False)