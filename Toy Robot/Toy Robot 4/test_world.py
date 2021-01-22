import unittest
from world.text.world import *

class TestFunctions(unittest.TestCase):
    def test_is_position_allowed(self):
        res_min = is_position_allowed(10, 30)
        res_max = is_position_allowed(110, 20)
        self.assertEqual(res_min, True)
        self.assertEqual(res_max, False)

    def test_update_position(self):
        res_forward = update_position(10)
        res_right = update_position(0)
        self.assertEqual(res_forward, True)
        self.assertEqual(res_right, True)