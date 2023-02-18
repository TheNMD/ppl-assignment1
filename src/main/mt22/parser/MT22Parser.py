# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'void'", "'auto'", 
                     "'integer'", "'float'", "'boolean'", "'string'", "'array'", 
                     "'inherit'", "'function'", "'true'", "'false'", "'for'", 
                     "'while'", "'do'", "'break'", "'continue'", "'return'", 
                     "'if'", "'else'", "'of'", "'out'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'::'", 
                     "'.'", "','", "';'", "':'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", 
                      "KWINT", "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", 
                      "KWFUNC", "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", 
                      "KWDO", "KWBRK", "KWCONT", "KWRTN", "KWIF", "KWELSE", 
                      "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", "MULOP", 
                      "DIVOP", "MODOP", "EXC", "ANDOP", "OROP", "EQLOP", 
                      "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", 
                      "CONCATOP", "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", 
                      "RSB", "LCB", "RCB", "EQL", "LITINT", "LITFLOAT", 
                      "LITDEC", "LITEXP", "LITBOO", "LITSTR", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    CCOMMENT=1
    CPPCOMMENT=2
    KWVOID=3
    KWAUTO=4
    KWINT=5
    KWFLOAT=6
    KWBOO=7
    KWSTR=8
    KWARR=9
    KWINHERIT=10
    KWFUNC=11
    KWTRUE=12
    KWFALSE=13
    KWFOR=14
    KWWHILE=15
    KWDO=16
    KWBRK=17
    KWCONT=18
    KWRTN=19
    KWIF=20
    KWELSE=21
    KWOF=22
    KWOUT=23
    ID=24
    ADDOP=25
    SUBOP=26
    MULOP=27
    DIVOP=28
    MODOP=29
    EXC=30
    ANDOP=31
    OROP=32
    EQLOP=33
    DIFOP=34
    LARGEOP=35
    LEQLOP=36
    SMALLOP=37
    SEQLOP=38
    CONCATOP=39
    DOT=40
    CM=41
    SM=42
    CL=43
    LB=44
    RB=45
    LSB=46
    RSB=47
    LCB=48
    RCB=49
    EQL=50
    LITINT=51
    LITFLOAT=52
    LITDEC=53
    LITEXP=54
    LITBOO=55
    LITSTR=56
    WS=57
    ERROR_CHAR=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





