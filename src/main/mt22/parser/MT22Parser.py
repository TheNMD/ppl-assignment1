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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u00eb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\3\2\7\2?\n\2\f\2\16\2B\13\2\3\3\3\3\7\3F\n\3\f\3")
        buf.write("\16\3I\13\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5T\n")
        buf.write("\5\3\6\3\6\3\6\3\6\5\6Z\n\6\3\7\3\7\3\7\3\7\3\7\5\7a\n")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\5\bh\n\b\3\t\3\t\3\t\3\t\5\tn\n")
        buf.write("\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f~\n\f\3\r\3\r\3\r\3\r\5\r\u0084\n\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u008b\n\16\3\17\5\17\u008e\n\17")
        buf.write("\3\17\5\17\u0091\n\17\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00a1\n\22")
        buf.write("\3\23\3\23\5\23\u00a5\n\23\3\24\3\24\3\24\5\24\u00aa\n")
        buf.write("\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\5\27\u00bb\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\5\30\u00c2\n\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u00cc\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u00d3\n\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34")
        buf.write("\u00db\n\34\f\34\16\34\u00de\13\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u00e5\n\35\3\36\3\36\3\36\3\36\3\36\3G\3\66")
        buf.write("\37\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:\2\6\3\2\4\4\3\2\t\16\3\2\b\r\3\2 !\2\u00e8")
        buf.write("\2<\3\2\2\2\4C\3\2\2\2\6L\3\2\2\2\bS\3\2\2\2\nY\3\2\2")
        buf.write("\2\f[\3\2\2\2\16g\3\2\2\2\20m\3\2\2\2\22o\3\2\2\2\24q")
        buf.write("\3\2\2\2\26t\3\2\2\2\30\u0083\3\2\2\2\32\u008a\3\2\2\2")
        buf.write("\34\u008d\3\2\2\2\36\u0096\3\2\2\2 \u0098\3\2\2\2\"\u00a0")
        buf.write("\3\2\2\2$\u00a4\3\2\2\2&\u00a9\3\2\2\2(\u00ad\3\2\2\2")
        buf.write("*\u00b1\3\2\2\2,\u00ba\3\2\2\2.\u00c1\3\2\2\2\60\u00c3")
        buf.write("\3\2\2\2\62\u00cb\3\2\2\2\64\u00d2\3\2\2\2\66\u00d4\3")
        buf.write("\2\2\28\u00e4\3\2\2\2:\u00e6\3\2\2\2<@\7\3\2\2=?\n\2\2")
        buf.write("\2>=\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\3\3\2\2\2")
        buf.write("B@\3\2\2\2CG\7\5\2\2DF\13\2\2\2ED\3\2\2\2FI\3\2\2\2GH")
        buf.write("\3\2\2\2GE\3\2\2\2HJ\3\2\2\2IG\3\2\2\2JK\7\6\2\2K\5\3")
        buf.write("\2\2\2LM\5\b\5\2MN\7\2\2\3N\7\3\2\2\2OP\5\n\6\2PQ\5\b")
        buf.write("\5\2QT\3\2\2\2RT\5\n\6\2SO\3\2\2\2SR\3\2\2\2T\t\3\2\2")
        buf.write("\2UZ\5\f\7\2VZ\5\24\13\2WZ\5\2\2\2XZ\5\4\3\2YU\3\2\2\2")
        buf.write("YV\3\2\2\2YW\3\2\2\2YX\3\2\2\2Z\13\3\2\2\2[\\\5\16\b\2")
        buf.write("\\]\7\60\2\2]`\5\22\n\2^_\7\67\2\2_a\5,\27\2`^\3\2\2\2")
        buf.write("`a\3\2\2\2ab\3\2\2\2bc\7/\2\2c\r\3\2\2\2de\7\35\2\2eh")
        buf.write("\5\20\t\2fh\7\35\2\2gd\3\2\2\2gf\3\2\2\2h\17\3\2\2\2i")
        buf.write("j\7.\2\2jk\7\35\2\2kn\5\20\t\2ln\3\2\2\2mi\3\2\2\2ml\3")
        buf.write("\2\2\2n\21\3\2\2\2op\t\3\2\2p\23\3\2\2\2qr\5\26\f\2rs")
        buf.write("\5 \21\2s\25\3\2\2\2tu\7\35\2\2uv\7\60\2\2vw\7\20\2\2")
        buf.write("wx\5\36\20\2xy\7\61\2\2yz\5\30\r\2z}\7\62\2\2{|\7\17\2")
        buf.write("\2|~\7\35\2\2}{\3\2\2\2}~\3\2\2\2~\27\3\2\2\2\177\u0080")
        buf.write("\5\34\17\2\u0080\u0081\5\32\16\2\u0081\u0084\3\2\2\2\u0082")
        buf.write("\u0084\3\2\2\2\u0083\177\3\2\2\2\u0083\u0082\3\2\2\2\u0084")
        buf.write("\31\3\2\2\2\u0085\u0086\7.\2\2\u0086\u0087\5\34\17\2\u0087")
        buf.write("\u0088\5\32\16\2\u0088\u008b\3\2\2\2\u0089\u008b\3\2\2")
        buf.write("\2\u008a\u0085\3\2\2\2\u008a\u0089\3\2\2\2\u008b\33\3")
        buf.write("\2\2\2\u008c\u008e\7\17\2\2\u008d\u008c\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u0091\7\34\2")
        buf.write("\2\u0090\u008f\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0093\7\35\2\2\u0093\u0094\7\60\2\2\u0094")
        buf.write("\u0095\5\22\n\2\u0095\35\3\2\2\2\u0096\u0097\t\4\2\2\u0097")
        buf.write("\37\3\2\2\2\u0098\u0099\7\65\2\2\u0099\u009a\5\"\22\2")
        buf.write("\u009a\u009b\7\66\2\2\u009b!\3\2\2\2\u009c\u009d\5$\23")
        buf.write("\2\u009d\u009e\5\"\22\2\u009e\u00a1\3\2\2\2\u009f\u00a1")
        buf.write("\3\2\2\2\u00a0\u009c\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1")
        buf.write("#\3\2\2\2\u00a2\u00a5\5\f\7\2\u00a3\u00a5\5&\24\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5%\3\2\2\2\u00a6")
        buf.write("\u00aa\5(\25\2\u00a7\u00aa\5*\26\2\u00a8\u00aa\5\60\31")
        buf.write("\2\u00a9\u00a6\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8")
        buf.write("\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\7/\2\2\u00ac")
        buf.write("\'\3\2\2\2\u00ad\u00ae\7\35\2\2\u00ae\u00af\7\67\2\2\u00af")
        buf.write("\u00b0\5\62\32\2\u00b0)\3\2\2\2\u00b1\u00b2\7\35\2\2\u00b2")
        buf.write("\u00b3\7\61\2\2\u00b3\u00b4\5,\27\2\u00b4\u00b5\7\62\2")
        buf.write("\2\u00b5+\3\2\2\2\u00b6\u00b7\5\62\32\2\u00b7\u00b8\5")
        buf.write(".\30\2\u00b8\u00bb\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b6")
        buf.write("\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb-\3\2\2\2\u00bc\u00bd")
        buf.write("\7.\2\2\u00bd\u00be\5\62\32\2\u00be\u00bf\5.\30\2\u00bf")
        buf.write("\u00c2\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00bc\3\2\2\2")
        buf.write("\u00c1\u00c0\3\2\2\2\u00c2/\3\2\2\2\u00c3\u00c4\7\30\2")
        buf.write("\2\u00c4\u00c5\5\62\32\2\u00c5\61\3\2\2\2\u00c6\u00c7")
        buf.write("\5\64\33\2\u00c7\u00c8\7\36\2\2\u00c8\u00c9\5\62\32\2")
        buf.write("\u00c9\u00cc\3\2\2\2\u00ca\u00cc\5\64\33\2\u00cb\u00c6")
        buf.write("\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\63\3\2\2\2\u00cd\u00ce")
        buf.write("\5\66\34\2\u00ce\u00cf\7\37\2\2\u00cf\u00d0\5\66\34\2")
        buf.write("\u00d0\u00d3\3\2\2\2\u00d1\u00d3\5\66\34\2\u00d2\u00cd")
        buf.write("\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\65\3\2\2\2\u00d4\u00d5")
        buf.write("\b\34\1\2\u00d5\u00d6\58\35\2\u00d6\u00dc\3\2\2\2\u00d7")
        buf.write("\u00d8\f\4\2\2\u00d8\u00d9\t\5\2\2\u00d9\u00db\58\35\2")
        buf.write("\u00da\u00d7\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3")
        buf.write("\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\67\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00df\u00e5\78\2\2\u00e0\u00e5\79\2\2\u00e1\u00e5")
        buf.write("\7\35\2\2\u00e2\u00e5\5*\26\2\u00e3\u00e5\5:\36\2\u00e4")
        buf.write("\u00df\3\2\2\2\u00e4\u00e0\3\2\2\2\u00e4\u00e1\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e59\3\2\2")
        buf.write("\2\u00e6\u00e7\7\61\2\2\u00e7\u00e8\5\62\32\2\u00e8\u00e9")
        buf.write("\7\62\2\2\u00e9;\3\2\2\2\27@GSY`gm}\u0083\u008a\u008d")
        buf.write("\u0090\u00a0\u00a4\u00a9\u00ba\u00c1\u00cb\u00d2\u00dc")
        buf.write("\u00e4")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'//'", "'\n'", "'/*'", "'*/'", "<INVALID>", 
                     "'void'", "'auto'", "'integer'", "'float'", "'boolean'", 
                     "'string'", "'array'", "'inherit'", "'function'", "'true'", 
                     "'false'", "'for'", "'while'", "'do'", "'break'", "'continue'", 
                     "'return'", "'if'", "'else'", "'of'", "'out'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'::'", 
                     "'.'", "','", "';'", "':'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "KWVOID", "KWAUTO", "KWINT", "KWFLOAT", 
                      "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
                      "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", 
                      "KWCONT", "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", 
                      "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                      "EXC", "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", 
                      "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", "DOT", 
                      "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", 
                      "RCB", "EQL", "LITINT", "LITFLOAT", "LITBOO", "LITSTR", 
                      "LITARR", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_ccomment = 0
    RULE_cppcomment = 1
    RULE_program = 2
    RULE_declist = 3
    RULE_decl = 4
    RULE_vardecl = 5
    RULE_idlist = 6
    RULE_ids = 7
    RULE_vartyp = 8
    RULE_funcdecl = 9
    RULE_funcproto = 10
    RULE_paralist = 11
    RULE_paras = 12
    RULE_para = 13
    RULE_functyp = 14
    RULE_funcbody = 15
    RULE_bodylist = 16
    RULE_bodydecl = 17
    RULE_stmt = 18
    RULE_assignstmt = 19
    RULE_callstmt = 20
    RULE_exprlist = 21
    RULE_exprs = 22
    RULE_returnstmt = 23
    RULE_expr = 24
    RULE_expr1 = 25
    RULE_expr2 = 26
    RULE_operand = 27
    RULE_subexpr = 28

    ruleNames =  [ "ccomment", "cppcomment", "program", "declist", "decl", 
                   "vardecl", "idlist", "ids", "vartyp", "funcdecl", "funcproto", 
                   "paralist", "paras", "para", "functyp", "funcbody", "bodylist", 
                   "bodydecl", "stmt", "assignstmt", "callstmt", "exprlist", 
                   "exprs", "returnstmt", "expr", "expr1", "expr2", "operand", 
                   "subexpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WS=5
    KWVOID=6
    KWAUTO=7
    KWINT=8
    KWFLOAT=9
    KWBOO=10
    KWSTR=11
    KWARR=12
    KWINHERIT=13
    KWFUNC=14
    KWTRUE=15
    KWFALSE=16
    KWFOR=17
    KWWHILE=18
    KWDO=19
    KWBRK=20
    KWCONT=21
    KWRTN=22
    KWIF=23
    KWELSE=24
    KWOF=25
    KWOUT=26
    ID=27
    ADDOP=28
    SUBOP=29
    MULOP=30
    DIVOP=31
    MODOP=32
    EXC=33
    ANDOP=34
    OROP=35
    EQLOP=36
    DIFOP=37
    LARGEOP=38
    LEQLOP=39
    SMALLOP=40
    SEQLOP=41
    CONCATOP=42
    DOT=43
    CM=44
    SM=45
    CL=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    LCB=51
    RCB=52
    EQL=53
    LITINT=54
    LITFLOAT=55
    LITBOO=56
    LITSTR=57
    LITARR=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CcommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_ccomment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCcomment" ):
                return visitor.visitCcomment(self)
            else:
                return visitor.visitChildren(self)




    def ccomment(self):

        localctx = MT22Parser.CcommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ccomment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MT22Parser.T__0)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==MT22Parser.T__1:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CppcommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_cppcomment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCppcomment" ):
                return visitor.visitCppcomment(self)
            else:
                return visitor.visitChildren(self)




    def cppcomment(self):

        localctx = MT22Parser.CppcommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cppcomment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(MT22Parser.T__2)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 66
                    self.matchWildcard() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 72
            self.match(MT22Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declist(self):
            return self.getTypedRuleContext(MT22Parser.DeclistContext,0)


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
        self.enterRule(localctx, 4, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.declist()
            self.state = 75
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def declist(self):
            return self.getTypedRuleContext(MT22Parser.DeclistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_declist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclist" ):
                return visitor.visitDeclist(self)
            else:
                return visitor.visitChildren(self)




    def declist(self):

        localctx = MT22Parser.DeclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declist)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.decl()
                self.state = 78
                self.declist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def ccomment(self):
            return self.getTypedRuleContext(MT22Parser.CcommentContext,0)


        def cppcomment(self):
            return self.getTypedRuleContext(MT22Parser.CppcommentContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.funcdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.ccomment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.cppcomment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def CL(self):
            return self.getToken(MT22Parser.CL, 0)

        def vartyp(self):
            return self.getTypedRuleContext(MT22Parser.VartypContext,0)


        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def EQL(self):
            return self.getToken(MT22Parser.EQL, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.idlist()
            self.state = 90
            self.match(MT22Parser.CL)
            self.state = 91
            self.vartyp()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.EQL:
                self.state = 92
                self.match(MT22Parser.EQL)
                self.state = 93
                self.exprlist()


            self.state = 96
            self.match(MT22Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def ids(self):
            return self.getTypedRuleContext(MT22Parser.IdsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_idlist)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(MT22Parser.ID)
                self.state = 99
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MT22Parser.CM, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def ids(self):
            return self.getTypedRuleContext(MT22Parser.IdsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = MT22Parser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ids)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(MT22Parser.CM)
                self.state = 104
                self.match(MT22Parser.ID)
                self.state = 105
                self.ids()
                pass
            elif token in [MT22Parser.CL]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWAUTO(self):
            return self.getToken(MT22Parser.KWAUTO, 0)

        def KWINT(self):
            return self.getToken(MT22Parser.KWINT, 0)

        def KWFLOAT(self):
            return self.getToken(MT22Parser.KWFLOAT, 0)

        def KWBOO(self):
            return self.getToken(MT22Parser.KWBOO, 0)

        def KWSTR(self):
            return self.getToken(MT22Parser.KWSTR, 0)

        def KWARR(self):
            return self.getToken(MT22Parser.KWARR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_vartyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartyp" ):
                return visitor.visitVartyp(self)
            else:
                return visitor.visitChildren(self)




    def vartyp(self):

        localctx = MT22Parser.VartypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vartyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.KWAUTO) | (1 << MT22Parser.KWINT) | (1 << MT22Parser.KWFLOAT) | (1 << MT22Parser.KWBOO) | (1 << MT22Parser.KWSTR) | (1 << MT22Parser.KWARR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcproto(self):
            return self.getTypedRuleContext(MT22Parser.FuncprotoContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(MT22Parser.FuncbodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.funcproto()
            self.state = 112
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncprotoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def CL(self):
            return self.getToken(MT22Parser.CL, 0)

        def KWFUNC(self):
            return self.getToken(MT22Parser.KWFUNC, 0)

        def functyp(self):
            return self.getTypedRuleContext(MT22Parser.FunctypContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def paralist(self):
            return self.getTypedRuleContext(MT22Parser.ParalistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def KWINHERIT(self):
            return self.getToken(MT22Parser.KWINHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcproto

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncproto" ):
                return visitor.visitFuncproto(self)
            else:
                return visitor.visitChildren(self)




    def funcproto(self):

        localctx = MT22Parser.FuncprotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcproto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MT22Parser.ID)
            self.state = 115
            self.match(MT22Parser.CL)
            self.state = 116
            self.match(MT22Parser.KWFUNC)
            self.state = 117
            self.functyp()
            self.state = 118
            self.match(MT22Parser.LB)
            self.state = 119
            self.paralist()
            self.state = 120
            self.match(MT22Parser.RB)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWINHERIT:
                self.state = 121
                self.match(MT22Parser.KWINHERIT)
                self.state = 122
                self.match(MT22Parser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(MT22Parser.ParaContext,0)


        def paras(self):
            return self.getTypedRuleContext(MT22Parser.ParasContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = MT22Parser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paralist)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.KWINHERIT, MT22Parser.KWOUT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.para()
                self.state = 126
                self.paras()
                pass
            elif token in [MT22Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MT22Parser.CM, 0)

        def para(self):
            return self.getTypedRuleContext(MT22Parser.ParaContext,0)


        def paras(self):
            return self.getTypedRuleContext(MT22Parser.ParasContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paras

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParas" ):
                return visitor.visitParas(self)
            else:
                return visitor.visitChildren(self)




    def paras(self):

        localctx = MT22Parser.ParasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paras)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(MT22Parser.CM)
                self.state = 132
                self.para()
                self.state = 133
                self.paras()
                pass
            elif token in [MT22Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def CL(self):
            return self.getToken(MT22Parser.CL, 0)

        def vartyp(self):
            return self.getTypedRuleContext(MT22Parser.VartypContext,0)


        def KWINHERIT(self):
            return self.getToken(MT22Parser.KWINHERIT, 0)

        def KWOUT(self):
            return self.getToken(MT22Parser.KWOUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MT22Parser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWINHERIT:
                self.state = 138
                self.match(MT22Parser.KWINHERIT)


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWOUT:
                self.state = 141
                self.match(MT22Parser.KWOUT)


            self.state = 144
            self.match(MT22Parser.ID)
            self.state = 145
            self.match(MT22Parser.CL)
            self.state = 146
            self.vartyp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWAUTO(self):
            return self.getToken(MT22Parser.KWAUTO, 0)

        def KWINT(self):
            return self.getToken(MT22Parser.KWINT, 0)

        def KWFLOAT(self):
            return self.getToken(MT22Parser.KWFLOAT, 0)

        def KWBOO(self):
            return self.getToken(MT22Parser.KWBOO, 0)

        def KWSTR(self):
            return self.getToken(MT22Parser.KWSTR, 0)

        def KWVOID(self):
            return self.getToken(MT22Parser.KWVOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctyp" ):
                return visitor.visitFunctyp(self)
            else:
                return visitor.visitChildren(self)




    def functyp(self):

        localctx = MT22Parser.FunctypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_functyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.KWVOID) | (1 << MT22Parser.KWAUTO) | (1 << MT22Parser.KWINT) | (1 << MT22Parser.KWFLOAT) | (1 << MT22Parser.KWBOO) | (1 << MT22Parser.KWSTR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def bodylist(self):
            return self.getTypedRuleContext(MT22Parser.BodylistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcbody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncbody" ):
                return visitor.visitFuncbody(self)
            else:
                return visitor.visitChildren(self)




    def funcbody(self):

        localctx = MT22Parser.FuncbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(MT22Parser.LCB)
            self.state = 151
            self.bodylist()
            self.state = 152
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodylistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bodydecl(self):
            return self.getTypedRuleContext(MT22Parser.BodydeclContext,0)


        def bodylist(self):
            return self.getTypedRuleContext(MT22Parser.BodylistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_bodylist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodylist" ):
                return visitor.visitBodylist(self)
            else:
                return visitor.visitChildren(self)




    def bodylist(self):

        localctx = MT22Parser.BodylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_bodylist)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.KWRTN, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.bodydecl()
                self.state = 155
                self.bodylist()
                pass
            elif token in [MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_bodydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodydecl" ):
                return visitor.visitBodydecl(self)
            else:
                return visitor.visitChildren(self)




    def bodydecl(self):

        localctx = MT22Parser.BodydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_bodydecl)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 164
                self.assignstmt()
                pass

            elif la_ == 2:
                self.state = 165
                self.callstmt()
                pass

            elif la_ == 3:
                self.state = 166
                self.returnstmt()
                pass


            self.state = 169
            self.match(MT22Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def EQL(self):
            return self.getToken(MT22Parser.EQL, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MT22Parser.ID)
            self.state = 172
            self.match(MT22Parser.EQL)
            self.state = 173
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(MT22Parser.ID)
            self.state = 176
            self.match(MT22Parser.LB)
            self.state = 177
            self.exprlist()
            self.state = 178
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def exprs(self):
            return self.getTypedRuleContext(MT22Parser.ExprsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exprlist)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ID, MT22Parser.LB, MT22Parser.LITINT, MT22Parser.LITFLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.expr()
                self.state = 181
                self.exprs()
                pass
            elif token in [MT22Parser.SM, MT22Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MT22Parser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def exprs(self):
            return self.getTypedRuleContext(MT22Parser.ExprsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = MT22Parser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exprs)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(MT22Parser.CM)
                self.state = 187
                self.expr()
                self.state = 188
                self.exprs()
                pass
            elif token in [MT22Parser.SM, MT22Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWRTN(self):
            return self.getToken(MT22Parser.KWRTN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MT22Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MT22Parser.KWRTN)
            self.state = 194
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MT22Parser.Expr1Context,0)


        def ADDOP(self):
            return self.getToken(MT22Parser.ADDOP, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.expr1()
                self.state = 197
                self.match(MT22Parser.ADDOP)
                self.state = 198
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def SUBOP(self):
            return self.getToken(MT22Parser.SUBOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr1)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.expr2(0)
                self.state = 204
                self.match(MT22Parser.SUBOP)
                self.state = 205
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def MULOP(self):
            return self.getToken(MT22Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(MT22Parser.DIVOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 213
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 214
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.MULOP or _la==MT22Parser.DIVOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 215
                    self.operand() 
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITINT(self):
            return self.getToken(MT22Parser.LITINT, 0)

        def LITFLOAT(self):
            return self.getToken(MT22Parser.LITFLOAT, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(MT22Parser.SubexprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_operand)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(MT22Parser.LITINT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(MT22Parser.LITFLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.match(MT22Parser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.callstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 225
                self.subexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = MT22Parser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MT22Parser.LB)
            self.state = 229
            self.expr()
            self.state = 230
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




