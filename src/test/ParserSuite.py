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
        input = """arrstrcv : float = 11_32_.3_232 ;"""
        expect = "Error on line 1 col 27: _232"
        self.assertTrue(TestParser.test(input, expect, 203))
        input = """arr : array [3_,2] of float = {{1,2},{3,4},{5,8}} ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
        input = """func1 : function auto (out a : integer, b : float) {
            randfloat : float = 1_332.33e-23 ;
            randarr : array [1,3,5] of string ;
            randstring : string = "hololo\\txxewaazh\\f\\b" ;
            return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
        input = """int1, int2, int3 : float = 1.22e332, 1_332_443_.e-1223, 0.3322e0 ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
        input = """a, b, c, d: integer = 3, 4, 6 ;"""
        expect = "Error on line 1 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 207))
        input = """a, b, c: integer = 3, 4, 5, 6 ;"""
        expect = "Error on line 1 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 208))
        input = """arr1, arr2 : array [3_,2] of float = {{1,2},{3,4},{5,8}}, {{0,0},{2,3},{9,9}} ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 210))