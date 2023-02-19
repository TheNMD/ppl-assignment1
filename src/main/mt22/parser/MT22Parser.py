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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\u00d5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\5\3@\n\3\3\4\3\4\5\4D\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5K\n\5\3\5\3\5\3\6\3\6\3\6\5\6R\n\6\3\7\3\7\3\7\3")
        buf.write("\7\5\7X\n\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\nh\n\n\3\13\3\13\3\13\3\13\5\13n\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\fu\n\f\3\r\5\rx\n\r\3\r\5\r{\n")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u008b\n\20\3\21\3\21\5\21\u008f\n")
        buf.write("\21\3\22\3\22\3\22\5\22\u0094\n\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u00a5\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00ac\n")
        buf.write("\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30\u00b6")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u00bd\n\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\7\32\u00c5\n\32\f\32\16\32\u00c8")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\5\33\u00cf\n\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\2\3\62\35\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\66\2\5\3\2\7\f\3\2\6\13")
        buf.write("\3\2\36\37\2\u00d0\28\3\2\2\2\4?\3\2\2\2\6C\3\2\2\2\b")
        buf.write("E\3\2\2\2\nQ\3\2\2\2\fW\3\2\2\2\16Y\3\2\2\2\20[\3\2\2")
        buf.write("\2\22^\3\2\2\2\24m\3\2\2\2\26t\3\2\2\2\30w\3\2\2\2\32")
        buf.write("\u0080\3\2\2\2\34\u0082\3\2\2\2\36\u008a\3\2\2\2 \u008e")
        buf.write("\3\2\2\2\"\u0093\3\2\2\2$\u0097\3\2\2\2&\u009b\3\2\2\2")
        buf.write("(\u00a4\3\2\2\2*\u00ab\3\2\2\2,\u00ad\3\2\2\2.\u00b5\3")
        buf.write("\2\2\2\60\u00bc\3\2\2\2\62\u00be\3\2\2\2\64\u00ce\3\2")
        buf.write("\2\2\66\u00d0\3\2\2\289\5\4\3\29:\7\2\2\3:\3\3\2\2\2;")
        buf.write("<\5\6\4\2<=\5\4\3\2=@\3\2\2\2>@\5\6\4\2?;\3\2\2\2?>\3")
        buf.write("\2\2\2@\5\3\2\2\2AD\5\b\5\2BD\5\20\t\2CA\3\2\2\2CB\3\2")
        buf.write("\2\2D\7\3\2\2\2EF\5\n\6\2FG\7.\2\2GJ\5\16\b\2HI\7\65\2")
        buf.write("\2IK\5(\25\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\7-\2\2M\t")
        buf.write("\3\2\2\2NO\7\33\2\2OR\5\f\7\2PR\7\33\2\2QN\3\2\2\2QP\3")
        buf.write("\2\2\2R\13\3\2\2\2ST\7,\2\2TU\7\33\2\2UX\5\f\7\2VX\3\2")
        buf.write("\2\2WS\3\2\2\2WV\3\2\2\2X\r\3\2\2\2YZ\t\2\2\2Z\17\3\2")
        buf.write("\2\2[\\\5\22\n\2\\]\5\34\17\2]\21\3\2\2\2^_\7\33\2\2_")
        buf.write("`\7.\2\2`a\7\16\2\2ab\5\32\16\2bc\7/\2\2cd\5\24\13\2d")
        buf.write("g\7\60\2\2ef\7\r\2\2fh\7\33\2\2ge\3\2\2\2gh\3\2\2\2h\23")
        buf.write("\3\2\2\2ij\5\30\r\2jk\5\26\f\2kn\3\2\2\2ln\3\2\2\2mi\3")
        buf.write("\2\2\2ml\3\2\2\2n\25\3\2\2\2op\7,\2\2pq\5\30\r\2qr\5\26")
        buf.write("\f\2ru\3\2\2\2su\3\2\2\2to\3\2\2\2ts\3\2\2\2u\27\3\2\2")
        buf.write("\2vx\7\r\2\2wv\3\2\2\2wx\3\2\2\2xz\3\2\2\2y{\7\32\2\2")
        buf.write("zy\3\2\2\2z{\3\2\2\2{|\3\2\2\2|}\7\33\2\2}~\7.\2\2~\177")
        buf.write("\5\16\b\2\177\31\3\2\2\2\u0080\u0081\t\3\2\2\u0081\33")
        buf.write("\3\2\2\2\u0082\u0083\7\63\2\2\u0083\u0084\5\36\20\2\u0084")
        buf.write("\u0085\7\64\2\2\u0085\35\3\2\2\2\u0086\u0087\5 \21\2\u0087")
        buf.write("\u0088\5\36\20\2\u0088\u008b\3\2\2\2\u0089\u008b\3\2\2")
        buf.write("\2\u008a\u0086\3\2\2\2\u008a\u0089\3\2\2\2\u008b\37\3")
        buf.write("\2\2\2\u008c\u008f\5\b\5\2\u008d\u008f\5\"\22\2\u008e")
        buf.write("\u008c\3\2\2\2\u008e\u008d\3\2\2\2\u008f!\3\2\2\2\u0090")
        buf.write("\u0094\5$\23\2\u0091\u0094\5&\24\2\u0092\u0094\5,\27\2")
        buf.write("\u0093\u0090\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0092\3")
        buf.write("\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\7-\2\2\u0096#\3")
        buf.write("\2\2\2\u0097\u0098\7\33\2\2\u0098\u0099\7\65\2\2\u0099")
        buf.write("\u009a\5.\30\2\u009a%\3\2\2\2\u009b\u009c\7\33\2\2\u009c")
        buf.write("\u009d\7/\2\2\u009d\u009e\5(\25\2\u009e\u009f\7\60\2\2")
        buf.write("\u009f\'\3\2\2\2\u00a0\u00a1\5.\30\2\u00a1\u00a2\5*\26")
        buf.write("\2\u00a2\u00a5\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a0")
        buf.write("\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5)\3\2\2\2\u00a6\u00a7")
        buf.write("\7,\2\2\u00a7\u00a8\5.\30\2\u00a8\u00a9\5*\26\2\u00a9")
        buf.write("\u00ac\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a6\3\2\2\2")
        buf.write("\u00ab\u00aa\3\2\2\2\u00ac+\3\2\2\2\u00ad\u00ae\7\26\2")
        buf.write("\2\u00ae\u00af\5.\30\2\u00af-\3\2\2\2\u00b0\u00b1\5\60")
        buf.write("\31\2\u00b1\u00b2\7\34\2\2\u00b2\u00b3\5.\30\2\u00b3\u00b6")
        buf.write("\3\2\2\2\u00b4\u00b6\5\60\31\2\u00b5\u00b0\3\2\2\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b6/\3\2\2\2\u00b7\u00b8\5\62\32\2\u00b8")
        buf.write("\u00b9\7\35\2\2\u00b9\u00ba\5\62\32\2\u00ba\u00bd\3\2")
        buf.write("\2\2\u00bb\u00bd\5\62\32\2\u00bc\u00b7\3\2\2\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bd\61\3\2\2\2\u00be\u00bf\b\32\1\2\u00bf\u00c0")
        buf.write("\5\64\33\2\u00c0\u00c6\3\2\2\2\u00c1\u00c2\f\4\2\2\u00c2")
        buf.write("\u00c3\t\4\2\2\u00c3\u00c5\5\64\33\2\u00c4\u00c1\3\2\2")
        buf.write("\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\63\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00cf")
        buf.write("\7\66\2\2\u00ca\u00cf\7\67\2\2\u00cb\u00cf\7\33\2\2\u00cc")
        buf.write("\u00cf\5&\24\2\u00cd\u00cf\5\66\34\2\u00ce\u00c9\3\2\2")
        buf.write("\2\u00ce\u00ca\3\2\2\2\u00ce\u00cb\3\2\2\2\u00ce\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\65\3\2\2\2\u00d0\u00d1")
        buf.write("\7/\2\2\u00d1\u00d2\5.\30\2\u00d2\u00d3\7\60\2\2\u00d3")
        buf.write("\67\3\2\2\2\25?CJQWgmtwz\u008a\u008e\u0093\u00a4\u00ab")
        buf.write("\u00b5\u00bc\u00c6\u00ce")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'void'", "'auto'", "'integer'", "'float'", "'boolean'", 
                     "'string'", "'array'", "'inherit'", "'function'", "'true'", 
                     "'false'", "'for'", "'while'", "'do'", "'break'", "'continue'", 
                     "'return'", "'if'", "'else'", "'of'", "'out'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'::'", 
                     "'.'", "','", "';'", "':'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", 
                      "KWAUTO", "KWINT", "KWFLOAT", "KWBOO", "KWSTR", "KWARR", 
                      "KWINHERIT", "KWFUNC", "KWTRUE", "KWFALSE", "KWFOR", 
                      "KWWHILE", "KWDO", "KWBRK", "KWCONT", "KWRTN", "KWIF", 
                      "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", 
                      "MULOP", "DIVOP", "MODOP", "EXC", "ANDOP", "OROP", 
                      "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", 
                      "SEQLOP", "CONCATOP", "DOT", "CM", "SM", "CL", "LB", 
                      "RB", "LSB", "RSB", "LCB", "RCB", "EQL", "LITINT", 
                      "LITFLOAT", "LITBOO", "LITSTR", "LITARR", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_idlist = 4
    RULE_ids = 5
    RULE_vartyp = 6
    RULE_funcdecl = 7
    RULE_funcproto = 8
    RULE_paralist = 9
    RULE_paras = 10
    RULE_para = 11
    RULE_functyp = 12
    RULE_funcbody = 13
    RULE_bodylist = 14
    RULE_bodydecl = 15
    RULE_stmt = 16
    RULE_assignstmt = 17
    RULE_callstmt = 18
    RULE_exprlist = 19
    RULE_exprs = 20
    RULE_returnstmt = 21
    RULE_expr = 22
    RULE_expr1 = 23
    RULE_expr2 = 24
    RULE_operand = 25
    RULE_subexpr = 26

    ruleNames =  [ "program", "declist", "decl", "vardecl", "idlist", "ids", 
                   "vartyp", "funcdecl", "funcproto", "paralist", "paras", 
                   "para", "functyp", "funcbody", "bodylist", "bodydecl", 
                   "stmt", "assignstmt", "callstmt", "exprlist", "exprs", 
                   "returnstmt", "expr", "expr1", "expr2", "operand", "subexpr" ]

    EOF = Token.EOF
    WS=1
    CCOMMENT=2
    CPPCOMMENT=3
    KWVOID=4
    KWAUTO=5
    KWINT=6
    KWFLOAT=7
    KWBOO=8
    KWSTR=9
    KWARR=10
    KWINHERIT=11
    KWFUNC=12
    KWTRUE=13
    KWFALSE=14
    KWFOR=15
    KWWHILE=16
    KWDO=17
    KWBRK=18
    KWCONT=19
    KWRTN=20
    KWIF=21
    KWELSE=22
    KWOF=23
    KWOUT=24
    ID=25
    ADDOP=26
    SUBOP=27
    MULOP=28
    DIVOP=29
    MODOP=30
    EXC=31
    ANDOP=32
    OROP=33
    EQLOP=34
    DIFOP=35
    LARGEOP=36
    LEQLOP=37
    SMALLOP=38
    SEQLOP=39
    CONCATOP=40
    DOT=41
    CM=42
    SM=43
    CL=44
    LB=45
    RB=46
    LSB=47
    RSB=48
    LCB=49
    RCB=50
    EQL=51
    LITINT=52
    LITFLOAT=53
    LITBOO=54
    LITSTR=55
    LITARR=56
    ERROR_CHAR=57
    UNCLOSE_STRING=58
    ILLEGAL_ESCAPE=59

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
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.declist()
            self.state = 55
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
        self.enterRule(localctx, 2, self.RULE_declist)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.decl()
                self.state = 58
                self.declist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
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


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.funcdecl()
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
        self.enterRule(localctx, 6, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.idlist()
            self.state = 68
            self.match(MT22Parser.CL)
            self.state = 69
            self.vartyp()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.EQL:
                self.state = 70
                self.match(MT22Parser.EQL)
                self.state = 71
                self.exprlist()


            self.state = 74
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
        self.enterRule(localctx, 8, self.RULE_idlist)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(MT22Parser.ID)
                self.state = 77
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
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
        self.enterRule(localctx, 10, self.RULE_ids)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(MT22Parser.CM)
                self.state = 82
                self.match(MT22Parser.ID)
                self.state = 83
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
        self.enterRule(localctx, 12, self.RULE_vartyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
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
        self.enterRule(localctx, 14, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.funcproto()
            self.state = 90
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
        self.enterRule(localctx, 16, self.RULE_funcproto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MT22Parser.ID)
            self.state = 93
            self.match(MT22Parser.CL)
            self.state = 94
            self.match(MT22Parser.KWFUNC)
            self.state = 95
            self.functyp()
            self.state = 96
            self.match(MT22Parser.LB)
            self.state = 97
            self.paralist()
            self.state = 98
            self.match(MT22Parser.RB)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWINHERIT:
                self.state = 99
                self.match(MT22Parser.KWINHERIT)
                self.state = 100
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
        self.enterRule(localctx, 18, self.RULE_paralist)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.KWINHERIT, MT22Parser.KWOUT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.para()
                self.state = 104
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
        self.enterRule(localctx, 20, self.RULE_paras)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(MT22Parser.CM)
                self.state = 110
                self.para()
                self.state = 111
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
        self.enterRule(localctx, 22, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWINHERIT:
                self.state = 116
                self.match(MT22Parser.KWINHERIT)


            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWOUT:
                self.state = 119
                self.match(MT22Parser.KWOUT)


            self.state = 122
            self.match(MT22Parser.ID)
            self.state = 123
            self.match(MT22Parser.CL)
            self.state = 124
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
        self.enterRule(localctx, 24, self.RULE_functyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
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
        self.enterRule(localctx, 26, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(MT22Parser.LCB)
            self.state = 129
            self.bodylist()
            self.state = 130
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
        self.enterRule(localctx, 28, self.RULE_bodylist)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.KWRTN, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.bodydecl()
                self.state = 133
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
        self.enterRule(localctx, 30, self.RULE_bodydecl)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
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
        self.enterRule(localctx, 32, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 142
                self.assignstmt()
                pass

            elif la_ == 2:
                self.state = 143
                self.callstmt()
                pass

            elif la_ == 3:
                self.state = 144
                self.returnstmt()
                pass


            self.state = 147
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
        self.enterRule(localctx, 34, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MT22Parser.ID)
            self.state = 150
            self.match(MT22Parser.EQL)
            self.state = 151
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
        self.enterRule(localctx, 36, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MT22Parser.ID)
            self.state = 154
            self.match(MT22Parser.LB)
            self.state = 155
            self.exprlist()
            self.state = 156
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
        self.enterRule(localctx, 38, self.RULE_exprlist)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ID, MT22Parser.LB, MT22Parser.LITINT, MT22Parser.LITFLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.expr()
                self.state = 159
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
        self.enterRule(localctx, 40, self.RULE_exprs)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(MT22Parser.CM)
                self.state = 165
                self.expr()
                self.state = 166
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
        self.enterRule(localctx, 42, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MT22Parser.KWRTN)
            self.state = 172
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
        self.enterRule(localctx, 44, self.RULE_expr)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.expr1()
                self.state = 175
                self.match(MT22Parser.ADDOP)
                self.state = 176
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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
        self.enterRule(localctx, 46, self.RULE_expr1)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.expr2(0)
                self.state = 182
                self.match(MT22Parser.SUBOP)
                self.state = 183
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 191
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 192
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.MULOP or _la==MT22Parser.DIVOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 193
                    self.operand() 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 50, self.RULE_operand)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(MT22Parser.LITINT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(MT22Parser.LITFLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                self.match(MT22Parser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 202
                self.callstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 203
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
        self.enterRule(localctx, 52, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MT22Parser.LB)
            self.state = 207
            self.expr()
            self.state = 208
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
        self._predicates[24] = self.expr2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




