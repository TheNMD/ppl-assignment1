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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\'")
        buf.write("\u00d1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\3\2\3\2\3\2\3\2\3\2\3\3\3\3\7\3U\n\3\f\3\16\3X")
        buf.write("\13\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\7\36\u0098\n\36\f\36\16\36\u009b")
        buf.write("\13\36\3\36\5\36\u009e\n\36\3\37\3\37\5\37\u00a2\n\37")
        buf.write("\3\37\5\37\u00a5\n\37\3 \3 \7 \u00a9\n \f \16 \u00ac\13")
        buf.write(" \3!\3!\5!\u00b0\n!\3!\6!\u00b3\n!\r!\16!\u00b4\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u00c0\n\"\3#\6#\u00c3")
        buf.write("\n#\r#\16#\u00c4\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\2\2")
        buf.write("\'\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("\3\2\n\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\4\2\62;aa\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2\u00da\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\3M\3\2\2\2\5R\3\2\2\2\7Y\3\2\2\2\t[\3\2\2\2\13")
        buf.write("]\3\2\2\2\r_\3\2\2\2\17a\3\2\2\2\21c\3\2\2\2\23e\3\2\2")
        buf.write("\2\25h\3\2\2\2\27k\3\2\2\2\31n\3\2\2\2\33q\3\2\2\2\35")
        buf.write("s\3\2\2\2\37v\3\2\2\2!x\3\2\2\2#{\3\2\2\2%~\3\2\2\2\'")
        buf.write("\u0080\3\2\2\2)\u0082\3\2\2\2+\u0084\3\2\2\2-\u0086\3")
        buf.write("\2\2\2/\u0088\3\2\2\2\61\u008a\3\2\2\2\63\u008c\3\2\2")
        buf.write("\2\65\u008e\3\2\2\2\67\u0090\3\2\2\29\u0092\3\2\2\2;\u009d")
        buf.write("\3\2\2\2=\u009f\3\2\2\2?\u00a6\3\2\2\2A\u00ad\3\2\2\2")
        buf.write("C\u00bf\3\2\2\2E\u00c2\3\2\2\2G\u00c8\3\2\2\2I\u00cb\3")
        buf.write("\2\2\2K\u00ce\3\2\2\2MN\7p\2\2NO\7q\2\2OP\7p\2\2PQ\7g")
        buf.write("\2\2Q\4\3\2\2\2RV\t\2\2\2SU\t\3\2\2TS\3\2\2\2UX\3\2\2")
        buf.write("\2VT\3\2\2\2VW\3\2\2\2W\6\3\2\2\2XV\3\2\2\2YZ\7-\2\2Z")
        buf.write("\b\3\2\2\2[\\\7/\2\2\\\n\3\2\2\2]^\7,\2\2^\f\3\2\2\2_")
        buf.write("`\7\61\2\2`\16\3\2\2\2ab\7\'\2\2b\20\3\2\2\2cd\7#\2\2")
        buf.write("d\22\3\2\2\2ef\7(\2\2fg\7(\2\2g\24\3\2\2\2hi\7~\2\2ij")
        buf.write("\7~\2\2j\26\3\2\2\2kl\7?\2\2lm\7?\2\2m\30\3\2\2\2no\7")
        buf.write("#\2\2op\7?\2\2p\32\3\2\2\2qr\7@\2\2r\34\3\2\2\2st\7@\2")
        buf.write("\2tu\7?\2\2u\36\3\2\2\2vw\7>\2\2w \3\2\2\2xy\7>\2\2yz")
        buf.write("\7?\2\2z\"\3\2\2\2{|\7<\2\2|}\7<\2\2}$\3\2\2\2~\177\7")
        buf.write("\60\2\2\177&\3\2\2\2\u0080\u0081\7.\2\2\u0081(\3\2\2\2")
        buf.write("\u0082\u0083\7=\2\2\u0083*\3\2\2\2\u0084\u0085\7<\2\2")
        buf.write("\u0085,\3\2\2\2\u0086\u0087\7*\2\2\u0087.\3\2\2\2\u0088")
        buf.write("\u0089\7+\2\2\u0089\60\3\2\2\2\u008a\u008b\7]\2\2\u008b")
        buf.write("\62\3\2\2\2\u008c\u008d\7_\2\2\u008d\64\3\2\2\2\u008e")
        buf.write("\u008f\7}\2\2\u008f\66\3\2\2\2\u0090\u0091\7\177\2\2\u0091")
        buf.write("8\3\2\2\2\u0092\u0093\7?\2\2\u0093:\3\2\2\2\u0094\u009e")
        buf.write("\7\62\2\2\u0095\u0099\t\4\2\2\u0096\u0098\t\5\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099\3")
        buf.write("\2\2\2\u009c\u009e\b\36\2\2\u009d\u0094\3\2\2\2\u009d")
        buf.write("\u0095\3\2\2\2\u009e<\3\2\2\2\u009f\u00a1\5;\36\2\u00a0")
        buf.write("\u00a2\5? \2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a4\3\2\2\2\u00a3\u00a5\5A!\2\u00a4\u00a3\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5>\3\2\2\2\u00a6\u00aa\7\60\2\2\u00a7")
        buf.write("\u00a9\t\6\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2")
        buf.write("\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab@\3\2\2")
        buf.write("\2\u00ac\u00aa\3\2\2\2\u00ad\u00af\t\7\2\2\u00ae\u00b0")
        buf.write("\t\b\2\2\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write("\u00b2\3\2\2\2\u00b1\u00b3\t\6\2\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3")
        buf.write("\2\2\2\u00b5B\3\2\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7")
        buf.write("t\2\2\u00b8\u00b9\7w\2\2\u00b9\u00c0\7g\2\2\u00ba\u00bb")
        buf.write("\7h\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be")
        buf.write("\7u\2\2\u00be\u00c0\7g\2\2\u00bf\u00b6\3\2\2\2\u00bf\u00ba")
        buf.write("\3\2\2\2\u00c0D\3\2\2\2\u00c1\u00c3\t\t\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\b#\3\2")
        buf.write("\u00c7F\3\2\2\2\u00c8\u00c9\13\2\2\2\u00c9\u00ca\b$\4")
        buf.write("\2\u00caH\3\2\2\2\u00cb\u00cc\13\2\2\2\u00cc\u00cd\b%")
        buf.write("\5\2\u00cdJ\3\2\2\2\u00ce\u00cf\13\2\2\2\u00cf\u00d0\b")
        buf.write("&\6\2\u00d0L\3\2\2\2\r\2V\u0099\u009d\u00a1\u00a4\u00aa")
        buf.write("\u00af\u00b4\u00bf\u00c4\7\3\36\2\b\2\2\3$\3\3%\4\3&\5")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2
    ADDOP = 3
    SUBOP = 4
    MULOP = 5
    DIVOP = 6
    MODOP = 7
    EXC = 8
    ANDOP = 9
    OROP = 10
    EQLOP = 11
    DIFOP = 12
    LARGEOP = 13
    LEQLOP = 14
    SMALLOP = 15
    SEQLOP = 16
    CONCATOP = 17
    DOT = 18
    CM = 19
    SM = 20
    CL = 21
    LB = 22
    RB = 23
    LSB = 24
    RSB = 25
    LCB = 26
    RCB = 27
    EQL = 28
    INT = 29
    FLOAT = 30
    DECIMAL = 31
    EXPONENT = 32
    BOOLEAN = 33
    WS = 34
    ERROR_CHAR = 35
    UNCLOSE_STRING = 36
    ILLEGAL_ESCAPE = 37

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'none'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'::'", 
            "'.'", "','", "';'", "':'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EXC", "ANDOP", 
            "OROP", "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", 
            "CONCATOP", "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", 
            "LCB", "RCB", "EQL", "INT", "FLOAT", "DECIMAL", "EXPONENT", 
            "BOOLEAN", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                  "EXC", "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", 
                  "SMALLOP", "SEQLOP", "CONCATOP", "DOT", "CM", "SM", "CL", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "EQL", "INT", 
                  "FLOAT", "DECIMAL", "EXPONENT", "BOOLEAN", "WS", "ERROR_CHAR", 
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
            actions[28] = self.INT_action 
            actions[34] = self.ERROR_CHAR_action 
            actions[35] = self.UNCLOSE_STRING_action 
            actions[36] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


