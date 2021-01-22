import unittest
from robot import *
from io import StringIO
from unittest.mock import patch


class FunctionTests(unittest.TestCase):

    @patch("sys.stdin", StringIO("Hal\n"))
    def test_robot_name(self):
        result = robot_name()
        self.assertEqual(result, "HAL")


    @patch("sys.stdin", StringIO("forward 10\n"))
    def test_direction_input(self):
        res1 = direction_input("HAL")
        self.assertEqual(res1, ("forward ", "10", "forward 10"))


    def test_off_help_command(self):
        off_c = off_help_command("HAL", "off")
        help_c = off_help_command("HAL", "help")
        self.assertEqual(off_c, "HAL: Shutting down..")
        self.assertEqual(help_c, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move me forward
BACK - move me back
RIGHT - turn right
LEFT - turn left
SPRINT - make a player sprint""")


    def test_update(self):
        update = update_position("HAL", "10", "20")
        self.assertEqual(update, " > HAL now at position (10,20).")


    @patch("sys.stdin", StringIO("off\n"))
    def test_forward_command(self):
        forward = forward_command("HAL", "10", 0, 10, 0)
        self.assertEqual(forward, (" > HAL moved forward by 10 steps."))
        

    @patch("sys.stdin", StringIO("off\n"))
    def test_back_command(self):
        back = back_command("HAL", "10", 0, 0, 0)
        self.assertEqual(back, (" > HAL moved back by 10 steps."))
        

    @patch("sys.stdin", StringIO("off\n"))
    def test_right_command(self):
        right = right_command("HAL", 0, 0, 0)
        self.assertEqual(right, ' > HAL turned right.')


    @patch("sys.stdin", StringIO("off\n"))
    def test_left_command(self):
        left1 = left_command("HAL", 0, 0, 0)
        self.assertEqual(left1, ' > HAL turned left.')
        

    @patch("sys.stdin", StringIO("off\n"))
    def test_sprint_command(self):
        sp = sprint_command("HAL", "5", 0, 0, 0)
        self.assertEqual(sp, ' > HAL now at position (0,15).')


if __name__ == "__main__":
    unittest.main()