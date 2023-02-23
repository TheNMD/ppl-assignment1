import unittest
from TestUtils import TestLexer
class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 102))
        self.assertTrue(TestLexer.test("abc", "abck,<EOF>", 103))
