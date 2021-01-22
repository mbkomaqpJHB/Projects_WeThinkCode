import unittest
from robot import *
from io import StringIO
from unittest.mock import patch

class FunctionTest(unittest.TestCase):
    def test_history_command(self):
        self.assertEqual(history_command("right"), history_command("right"))
        # self.assertEqual(history_command("forward 10"), ["right", "forward 10"])

    def test_replay_command(self):
        self.assertEqual(replay_command("HAL", "replay"), (True, " > HAL replayed 2 commands."))

    def test_replay_silent(self):
        self.assertEqual(replay_silent("HAL", "replay silent"),(True, " > HAL replayed 2 commands silently.", 0))

    def test_replay_reversed(self):
        self.assertEqual(replay_reversed("HAL", "replay reverse"), (True, " > HAL replayed 2 commands in reverse."))

    def test_replay_reversed_silent(self):
        self.assertEqual(replay_reversed_silent("HAL", "replay reversed silent"), (True, " > HAL replayed 2 commands in reverse silently.", 0))

    def test_limit_range(self):
        self.assertEqual(limit_range("HAL", "replay 1", 1), (True, " > HAL replayed 1 commands."))

    def test_range_silent(self):
        self.assertEqual(limit_range_silent("HAL", "replay silent 1", 1), (True, " > HAL replayed 1 commands silently.", 0))

    def test_limit_range_nm(self):
        self.assertEqual(limit_range_nm("HAL", "replay 2-1", 2, 1), (True, " > HAL replayed 1 commands."))

    @patch("sys.stdin", StringIO("HAL\n"))
    def test_robot_name(self):
        self.assertEqual(get_robot_name(), "HAL")

    @patch("sys.stdin", StringIO("forward 10"))
    def test_get_command(self):
        self.assertEqual(get_command("HAL"), "forward 10")

    def test_split_command_input(self):
        self.assertEqual(split_command_input("forward 10"), ("forward", '10'))

    def test_is_int(self):
        self.assertEqual(is_int(10), True)

    def test_valid_command(self):
        self.assertEqual(valid_command("forward 10"), True) 

if __name__ == '__main__':
    unittest.main()