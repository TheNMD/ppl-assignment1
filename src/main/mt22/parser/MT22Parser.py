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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'")
        buf.write("\f\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\2\2\4\2\4\2")
        buf.write("\2\2\t\2\6\3\2\2\2\4\t\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2\3")
        buf.write("\b\3\3\2\2\2\t\n\7\3\2\2\n\5\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'none'", "<INVALID>", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
                     "'>'", "'>='", "'<'", "'<='", "'::'", "'.'", "','", 
                     "';'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "ADDOP", "SUBOP", 
                      "MULOP", "DIVOP", "MODOP", "EXC", "ANDOP", "OROP", 
                      "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", 
                      "SEQLOP", "CONCATOP", "DOT", "CM", "SM", "CL", "LB", 
                      "RB", "LSB", "RSB", "LCB", "RCB", "EQL", "INT", "FLOAT", 
                      "DECIMAL", "EXPONENT", "BOOLEAN", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decls = 1

    ruleNames =  [ "program", "decls" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    ADDOP=3
    SUBOP=4
    MULOP=5
    DIVOP=6
    MODOP=7
    EXC=8
    ANDOP=9
    OROP=10
    EQLOP=11
    DIFOP=12
    LARGEOP=13
    LEQLOP=14
    SMALLOP=15
    SEQLOP=16
    CONCATOP=17
    DOT=18
    CM=19
    SM=20
    CL=21
    LB=22
    RB=23
    LSB=24
    RSB=25
    LCB=26
    RCB=27
    EQL=28
    INT=29
    FLOAT=30
    DECIMAL=31
    EXPONENT=32
    BOOLEAN=33
    WS=34
    ERROR_CHAR=35
    UNCLOSE_STRING=36
    ILLEGAL_ESCAPE=37

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

        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


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
            self.state = 4
            self.decls()
            self.state = 5
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(MT22Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





