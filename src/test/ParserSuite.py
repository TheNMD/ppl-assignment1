import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input =  """ str1 : string = "He asked me: \tWhere is John?\t" ; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
