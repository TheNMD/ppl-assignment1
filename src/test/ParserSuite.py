import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input =  """ a : string = "213123213\\'" ;  """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
        input = """x : integer"""
        expect = "Error on line 1 col 11: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 201))
        input = """xyxx : array [2] of string ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
