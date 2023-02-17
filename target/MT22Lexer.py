# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *;
studentID = "2052932";



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\32")
        buf.write("\u0090\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\3\2\3\2\7\2\66\n\2\f\2\16\29\13\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\21\7\21Z\n\21\f\21\16\21]\13\21\3\21\5")
        buf.write("\21`\n\21\3\22\3\22\5\22d\n\22\3\22\5\22g\n\22\3\23\3")
        buf.write("\23\7\23k\n\23\f\23\16\23n\13\23\3\24\3\24\5\24r\n\24")
        buf.write("\3\24\6\24u\n\24\r\24\16\24v\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0082\n\25\3\26\6\26\u0085\n")
        buf.write("\26\r\26\16\26\u0086\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\2\2\32\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\3\2\n\5\2C\\aac|\6\2\62;C\\aac|\3\2")
        buf.write("\63;\4\2\62;aa\3\2\62;\4\2GGgg\4\2--//\5\2\13\f\17\17")
        buf.write("\"\"\2\u0099\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\3\63\3\2\2\2\5:\3")
        buf.write("\2\2\2\7<\3\2\2\2\t>\3\2\2\2\13@\3\2\2\2\rB\3\2\2\2\17")
        buf.write("D\3\2\2\2\21F\3\2\2\2\23H\3\2\2\2\25J\3\2\2\2\27L\3\2")
        buf.write("\2\2\31N\3\2\2\2\33P\3\2\2\2\35R\3\2\2\2\37T\3\2\2\2!")
        buf.write("_\3\2\2\2#a\3\2\2\2%h\3\2\2\2\'o\3\2\2\2)\u0081\3\2\2")
        buf.write("\2+\u0084\3\2\2\2-\u008a\3\2\2\2/\u008c\3\2\2\2\61\u008e")
        buf.write("\3\2\2\2\63\67\t\2\2\2\64\66\t\3\2\2\65\64\3\2\2\2\66")
        buf.write("9\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\4\3\2\2\29\67\3\2")
        buf.write("\2\2:;\7-\2\2;\6\3\2\2\2<=\7/\2\2=\b\3\2\2\2>?\7,\2\2")
        buf.write("?\n\3\2\2\2@A\7\61\2\2A\f\3\2\2\2BC\7\60\2\2C\16\3\2\2")
        buf.write("\2DE\7.\2\2E\20\3\2\2\2FG\7=\2\2G\22\3\2\2\2HI\7<\2\2")
        buf.write("I\24\3\2\2\2JK\7*\2\2K\26\3\2\2\2LM\7+\2\2M\30\3\2\2\2")
        buf.write("NO\7]\2\2O\32\3\2\2\2PQ\7_\2\2Q\34\3\2\2\2RS\7}\2\2S\36")
        buf.write("\3\2\2\2TU\7\177\2\2U \3\2\2\2V`\7\62\2\2W[\t\4\2\2XZ")
        buf.write("\t\5\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3")
        buf.write("\2\2\2][\3\2\2\2^`\b\21\2\2_V\3\2\2\2_W\3\2\2\2`\"\3\2")
        buf.write("\2\2ac\5!\21\2bd\5%\23\2cb\3\2\2\2cd\3\2\2\2df\3\2\2\2")
        buf.write("eg\5\'\24\2fe\3\2\2\2fg\3\2\2\2g$\3\2\2\2hl\7\60\2\2i")
        buf.write("k\t\6\2\2ji\3\2\2\2kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2m&\3")
        buf.write("\2\2\2nl\3\2\2\2oq\t\7\2\2pr\t\b\2\2qp\3\2\2\2qr\3\2\2")
        buf.write("\2rt\3\2\2\2su\t\6\2\2ts\3\2\2\2uv\3\2\2\2vt\3\2\2\2v")
        buf.write("w\3\2\2\2w(\3\2\2\2xy\7v\2\2yz\7t\2\2z{\7w\2\2{\u0082")
        buf.write("\7g\2\2|}\7h\2\2}~\7c\2\2~\177\7n\2\2\177\u0080\7u\2\2")
        buf.write("\u0080\u0082\7g\2\2\u0081x\3\2\2\2\u0081|\3\2\2\2\u0082")
        buf.write("*\3\2\2\2\u0083\u0085\t\t\2\2\u0084\u0083\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u0089\b\26\3\2\u0089,\3\2\2")
        buf.write("\2\u008a\u008b\13\2\2\2\u008b.\3\2\2\2\u008c\u008d\13")
        buf.write("\2\2\2\u008d\60\3\2\2\2\u008e\u008f\13\2\2\2\u008f\62")
        buf.write("\3\2\2\2\r\2\67[_cflqv\u0081\u0086\4\3\21\2\b\2\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    ADDOP = 2
    SUBOP = 3
    MULOP = 4
    DIVOP = 5
    DOT = 6
    CM = 7
    SM = 8
    CL = 9
    LB = 10
    RB = 11
    LSB = 12
    RSB = 13
    LCB = 14
    RCB = 15
    INTLIT = 16
    FLOATLIT = 17
    DECIMAL = 18
    EXPONENT = 19
    BOOLIT = 20
    WS = 21
    ERROR_CHAR = 22
    UNCLOSE_STRING = 23
    ILLEGAL_ESCAPE = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'.'", "','", "';'", "':'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "DOT", "CM", "SM", 
            "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "INTLIT", "FLOATLIT", 
            "DECIMAL", "EXPONENT", "BOOLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "DOT", "CM", 
                  "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "INTLIT", 
                  "FLOATLIT", "DECIMAL", "EXPONENT", "BOOLIT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[15] = self.INTLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     


