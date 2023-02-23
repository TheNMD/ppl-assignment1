import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input =  """ a : string = "213123213\\'" ;  """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_simple_program(self):
        """Simple program: int main() {} """
        input =  """ a : string = "213123213\\'" ;  """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
