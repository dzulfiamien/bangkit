
from hello import filter_only_word
import unittest

class TestFilterOnlyWord(unittest.TestCase):
    def test_success(self):
        testcase = "bangkit"
        expected = "bangkit"
        self.assertEqual(filter_only_word(testcase), expected)

    def test_fail_numeric(self):
        testcase = "b4ngkit"
        expected = None
        self.assertEqual(filter_only_word(testcase), expected)

    def test_fail_symbol(self):
        testcase = "bangkit!!"
        expected = None
        self.assertEqual(filter_only_word(testcase), expected)

    def test_fail_empty(self):
        testcase = ""
        expected = None
        self.assertEqual(filter_only_word(testcase), expected)

    def test_fail_single_char(self):
        testcase = "x"
        expected = None
        self.assertEqual(filter_only_word(testcase), expected)

unittest.main()