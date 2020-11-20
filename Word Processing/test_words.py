import unittest
from word_processor import *
from io import StringIO
from unittest.mock import patch

class FunctionTest(unittest.TestCase):
    def test_convert_to_word_list(self):
        res = convert_to_word_list("The are indeed")
        self.assertEqual(res, ['the', 'are', 'indeed'])

    @patch("sys.stdin",StringIO("The are indeed\n"))
    def test_words_longer_than(self):
        res = words_longer_than(3, "The are indeed")
        self.assertEqual(res, ["indeed"])

    @patch("sys.stdin",StringIO("The are indeed\n"))
    def test_words_lengths_map(self):
        res = words_lengths_map("The are indeed")
        self.assertEqual(res, {3: 2, 6: 1})

    @patch("sys.stdin",StringIO("The are indeed\n"))
    def test_letters_count_map(self):
        res = letters_count_map("The are indeed")
        self.assertEqual(res, {'a': 1, 'b': 0, 'c': 0, 'd': 2, 'e': 4, 'f': 0, 'g': 0, 'h': 1, 'i': 1, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 0, 'p': 0, 'q': 0, 'r': 1, 's': 0, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0} )
    
    def test_most_used_character(self):
        res = most_used_character("The are indeed")
        res1 = most_used_character("")
        res2 = most_used_character("123")
        self.assertEqual(res, "e")
        self.assertEqual(res1, None)
        self.assertEqual(res2, None)