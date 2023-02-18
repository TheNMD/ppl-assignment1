import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" \t """, 'abc,<EOF>', 103))