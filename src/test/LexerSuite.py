import unittest
from TestUtils import TestLexer
class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 100))
        self.assertTrue(TestLexer.test("randotesto\t\f", "randotesto,<EOF>", 101))
        self.assertTrue(TestLexer.test("12312.ee3332szxd3!", "12312.,ee3332szxd3,!,<EOF>", 102))
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """, """He asked me: \\"Where is John?\\",<EOF>""", 103))
        self.assertTrue(TestLexer.test("9983e-3232", "9983e-3232,<EOF>", 104))
        self.assertTrue(TestLexer.test("{sdsadee}", "{,sdsadee,},<EOF>", 105))
        self.assertTrue(TestLexer.test("truefalse false,true}true", "truefalse,false,,,true,},true,<EOF>", 106))
        self.assertTrue(TestLexer.test("a121_232ss 1122_33.4343 _232", "a121_232ss,112233.4343,_232,<EOF>", 107))
        self.assertTrue(TestLexer.test("9abc a9bc", "9,abc,a9bc,<EOF>", 108))
        self.assertTrue(TestLexer.test("\t\b\n\f", "<EOF>", 109))
        self.assertTrue(TestLexer.test("4aaaaxxx__33//randomcomment", "4,aaaaxxx__33,<EOF>", 110))
        self.assertTrue(TestLexer.test("ooppxxew/*randomcomment*/122311123", "ooppxxew,122311123,<EOF>", 111))
        self.assertTrue(TestLexer.test(""" "aasdasdxx""", "Unclosed String: aasdasdxx", 112))
        self.assertTrue(TestLexer.test(""" "aasdasdxx\\nsds" """, "aasdasdxx\\nsds,<EOF>", 113))
        self.assertTrue(TestLexer.test("ab?cd", "ab,Error Token ?", 114))
        self.assertTrue(TestLexer.test("a : integer = ?", "a,:,integer,=,Error Token ?", 115))
        self.assertTrue(TestLexer.test(""" "abc"" """, "", 116))
