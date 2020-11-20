import unittest 
import sys
from unittest.mock import patch
from io import StringIO
from mastermind import *


class TestFunctions(unittest.TestCase):
    #check if it returns 4 digits 
    def test_create_code(self): 
        result = len(create_code([1,2,3,4])) 
        expected = len([1, 2, 3, 4]) 
        self.assertEqual(result, expected)

    #check the range of the list 
    def test_create_code_range(self): 
        for i in create_code([1,2,3,4]): 
            if i < 1 or i > 8:  #check each number if its between 1 & 8 
                return False 
            else:
                return True
                self.assertEqual(create_code([1,2,3,4]), create_code[1,2,3,4])

    @patch("sys.stdin", StringIO("1234\n")) 
    def test_get_user_input(self): 
        result = get_user_input() 
        expected = "1234" 
        self.assertEqual(result, expected)

    def test_check_correctness(self):   
        output = StringIO()
        sys.stdout = output
        result1 = check_correctness(0, False, 4)
        result2 = check_correctness(0, False, 3)
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)
        

    @patch("sys.stdin", StringIO("1234\n4321\n"))
    def test_take_turn(self):
        self.assertEqual(take_turn([1,2,3,4]), (4,0))
        self.assertEqual(take_turn([1,2,3,4]), (0,4))
    
    
    