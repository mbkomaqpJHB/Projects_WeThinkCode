import unittest
import robot 
from robot import *
from unittest.mock import patch
from io import StringIO


class TestFunctions(unittest.TestCase):
    @patch("sys.stdin", StringIO("Mbali\n"))
    def test_get_robot_name(self):
        res_name = get_robot_name()
        self.assertEqual(res_name, "Mbali")


    @patch("sys.stdin", StringIO("bck 10\nforward 10\noff\n"))
    def test_get_command(self):
        res = get_command("mbali")
        self.assertEqual(res, "forward 10")


    def test_split_command_input(self):
        res_forward = split_command_input("forward 10")
        res_right = split_command_input("right")
        self.assertEqual(res_forward, ("forward", "10"))
        self.assertEqual(res_right, ("right", ""))


    def test_is_int(self):
        res_int = is_int(10)
        res_not_int = is_int("silent")
        self.assertEqual(res_int, True)
        self.assertEqual(res_not_int, False)


    def test_valid_command(self):
        res_valid = valid_command("replay silent")
        res_not_valid = valid_command("back reverse")
        self.assertEqual(res_valid, True)
        self.assertEqual(res_not_valid, False)


    def test_do_help(self):
        res_help = do_help()
        self.assertEqual(res_help,(True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""))


    def test_do_forward(self):
        res_forward = do_forward("mbali", 10)
        res_not = do_forward("mbali", 2010)
        self.assertEqual(res_forward, (True, " > mbali moved forward by 10 steps."))
        self.assertEqual(res_not, (True,'mbali: Sorry, I cannot go outside my safe zone.'))

    
    def test_do_back(self):
        res_back = do_back("mbali", 10)
        res_not = do_back("mbali", 1010)
        self.assertEqual(res_back, (True, ' > mbali moved back by 10 steps.'))
        self.assertEqual(res_not, (True, 'mbali: Sorry, I cannot go outside my safe zone.'))


    def test_do_right_turn(self):
        res = do_right_turn("mbali")
        self.assertEqual(res, (True, ' > mbali turned right.'))

    
    def test_do_left_turn(self):
        res = do_left_turn("mbali")
        self.assertEqual(res, (True, ' > mbali turned left.'))


    def test_do_sprint(self):
        res = do_sprint("mbali", 1)
        self.assertEqual(res, (True, """ > mbali moved forward by 1 steps."""))


    def test_get_commands_history(self):
        res = get_commands_history(0, 1, 1)
        self.assertEqual(res, [])
    

    def test_do_replay(self):
        robot.history = ['forward 10']
        res = do_replay("mbali", "silent")
        self.assertEqual(res, (True, ' > mbali replayed 1 commands silently.'))


    def test_handle_command(self):
        res = handle_command("mbali", "forward 10")
        res_off = handle_command("mbali", "off")
        self.assertEqual(res, True)
        self.assertEqual(res_off, False)


if __name__ == "__main__":
    unittest.main()