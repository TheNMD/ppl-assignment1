import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
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
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 211))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 212))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 213))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 214))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 215))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 216))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 217))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 218))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 219))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 220))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 221))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 222))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 223))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 224))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 225))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 226))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 227))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 228))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 229))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 230))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 231))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 232))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 233))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 234))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 235))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 236))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 237))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 238))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 239))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 240))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 241))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 242))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 243))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 244))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 245))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 246))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 247))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 248))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 249))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 250))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 251))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 252))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 253))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 254))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 255))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 256))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 257))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 258))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 259))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 260))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 261))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 262))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 263))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 264))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 265))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 266))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 267))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 268))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 269))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 270))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 271))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 272))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 273))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 274))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 275))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 276))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 277))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 278))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 279))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 280))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 281))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 282))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 283))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 284))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 285))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 286))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 287))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 288))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 289))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 290))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 291))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 292))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 293))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 294))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 295))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 296))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 297))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 298))
        input = """auto : integer ;"""
        expect = "Error on line 1 col 0: auto"
        self.assertTrue(TestParser.test(input, expect, 299))
        input =  """ a : string = "213123213\\'" ;  """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))


