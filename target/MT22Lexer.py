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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01a8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\6\2\u0083\n\2")
        buf.write("\r\2\16\2\u0084\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u008d\n\3")
        buf.write("\f\3\16\3\u0090\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\7\4\u009b\n\4\f\4\16\4\u009e\13\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\7\32\u011f\n\32\f\32\16\32\u0122\13\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\65\7\65\u0162\n\65\f\65\16\65\u0165")
        buf.write("\13\65\3\65\5\65\u0168\n\65\3\66\3\66\5\66\u016c\n\66")
        buf.write("\3\66\5\66\u016f\n\66\3\66\3\66\3\67\3\67\7\67\u0175\n")
        buf.write("\67\f\67\16\67\u0178\13\67\38\38\58\u017c\n8\38\68\u017f")
        buf.write("\n8\r8\168\u0180\39\39\59\u0185\n9\3:\3:\3;\3;\3<\3<\3")
        buf.write("<\3<\7<\u018f\n<\f<\16<\u0192\13<\3<\3<\3<\3<\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3\u008e\2")
        buf.write("A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q8")
        buf.write("s\2u\2w9y:{;}<\177=\3\2\f\5\2\n\f\16\17\"\"\4\2\f\f\17")
        buf.write("\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\4\2\62;aa\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\3\2$$\2\u01b1\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2q\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\3\u0082\3\2\2\2\5\u0088\3\2\2")
        buf.write("\2\7\u0096\3\2\2\2\t\u00a1\3\2\2\2\13\u00a6\3\2\2\2\r")
        buf.write("\u00ab\3\2\2\2\17\u00b3\3\2\2\2\21\u00b9\3\2\2\2\23\u00c1")
        buf.write("\3\2\2\2\25\u00c8\3\2\2\2\27\u00ce\3\2\2\2\31\u00d6\3")
        buf.write("\2\2\2\33\u00df\3\2\2\2\35\u00e4\3\2\2\2\37\u00ea\3\2")
        buf.write("\2\2!\u00ee\3\2\2\2#\u00f4\3\2\2\2%\u00f7\3\2\2\2\'\u00fd")
        buf.write("\3\2\2\2)\u0106\3\2\2\2+\u010d\3\2\2\2-\u0110\3\2\2\2")
        buf.write("/\u0115\3\2\2\2\61\u0118\3\2\2\2\63\u011c\3\2\2\2\65\u0123")
        buf.write("\3\2\2\2\67\u0125\3\2\2\29\u0127\3\2\2\2;\u0129\3\2\2")
        buf.write("\2=\u012b\3\2\2\2?\u012d\3\2\2\2A\u012f\3\2\2\2C\u0132")
        buf.write("\3\2\2\2E\u0135\3\2\2\2G\u0138\3\2\2\2I\u013b\3\2\2\2")
        buf.write("K\u013d\3\2\2\2M\u0140\3\2\2\2O\u0142\3\2\2\2Q\u0145\3")
        buf.write("\2\2\2S\u0148\3\2\2\2U\u014a\3\2\2\2W\u014c\3\2\2\2Y\u014e")
        buf.write("\3\2\2\2[\u0150\3\2\2\2]\u0152\3\2\2\2_\u0154\3\2\2\2")
        buf.write("a\u0156\3\2\2\2c\u0158\3\2\2\2e\u015a\3\2\2\2g\u015c\3")
        buf.write("\2\2\2i\u0167\3\2\2\2k\u0169\3\2\2\2m\u0172\3\2\2\2o\u0179")
        buf.write("\3\2\2\2q\u0184\3\2\2\2s\u0186\3\2\2\2u\u0188\3\2\2\2")
        buf.write("w\u018a\3\2\2\2y\u0197\3\2\2\2{\u019f\3\2\2\2}\u01a2\3")
        buf.write("\2\2\2\177\u01a5\3\2\2\2\u0081\u0083\t\2\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\b\2\2\2")
        buf.write("\u0087\4\3\2\2\2\u0088\u0089\7\61\2\2\u0089\u008a\7,\2")
        buf.write("\2\u008a\u008e\3\2\2\2\u008b\u008d\13\2\2\2\u008c\u008b")
        buf.write("\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008f\3\2\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0091\u0092\7,\2\2\u0092\u0093\7\61\2\2\u0093\u0094\3")
        buf.write("\2\2\2\u0094\u0095\b\3\2\2\u0095\6\3\2\2\2\u0096\u0097")
        buf.write("\7\61\2\2\u0097\u0098\7\61\2\2\u0098\u009c\3\2\2\2\u0099")
        buf.write("\u009b\n\3\2\2\u009a\u0099\3\2\2\2\u009b\u009e\3\2\2\2")
        buf.write("\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f\3")
        buf.write("\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\b\4\2\2\u00a0\b")
        buf.write("\3\2\2\2\u00a1\u00a2\7x\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4")
        buf.write("\7k\2\2\u00a4\u00a5\7f\2\2\u00a5\n\3\2\2\2\u00a6\u00a7")
        buf.write("\7c\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa")
        buf.write("\7q\2\2\u00aa\f\3\2\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7g\2\2\u00af\u00b0")
        buf.write("\7i\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7t\2\2\u00b2\16")
        buf.write("\3\2\2\2\u00b3\u00b4\7h\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6")
        buf.write("\7q\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7v\2\2\u00b8\20")
        buf.write("\3\2\2\2\u00b9\u00ba\7d\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7g\2\2\u00be\u00bf")
        buf.write("\7c\2\2\u00bf\u00c0\7p\2\2\u00c0\22\3\2\2\2\u00c1\u00c2")
        buf.write("\7u\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7i\2\2\u00c7\24")
        buf.write("\3\2\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb")
        buf.write("\7t\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7{\2\2\u00cd\26")
        buf.write("\3\2\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1")
        buf.write("\7j\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7v\2\2\u00d5\30\3\2\2\2\u00d6\u00d7")
        buf.write("\7h\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da")
        buf.write("\7e\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7p\2\2\u00de\32\3\2\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\34\3\2\2\2\u00e4\u00e5\7h\2\2\u00e5\u00e6")
        buf.write("\7c\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9")
        buf.write("\7g\2\2\u00e9\36\3\2\2\2\u00ea\u00eb\7h\2\2\u00eb\u00ec")
        buf.write("\7q\2\2\u00ec\u00ed\7t\2\2\u00ed \3\2\2\2\u00ee\u00ef")
        buf.write("\7y\2\2\u00ef\u00f0\7j\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2")
        buf.write("\7n\2\2\u00f2\u00f3\7g\2\2\u00f3\"\3\2\2\2\u00f4\u00f5")
        buf.write("\7f\2\2\u00f5\u00f6\7q\2\2\u00f6$\3\2\2\2\u00f7\u00f8")
        buf.write("\7d\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb")
        buf.write("\7c\2\2\u00fb\u00fc\7m\2\2\u00fc&\3\2\2\2\u00fd\u00fe")
        buf.write("\7e\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100\7p\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\u0102\7k\2\2\u0102\u0103\7p\2\2\u0103\u0104")
        buf.write("\7w\2\2\u0104\u0105\7g\2\2\u0105(\3\2\2\2\u0106\u0107")
        buf.write("\7t\2\2\u0107\u0108\7g\2\2\u0108\u0109\7v\2\2\u0109\u010a")
        buf.write("\7w\2\2\u010a\u010b\7t\2\2\u010b\u010c\7p\2\2\u010c*\3")
        buf.write("\2\2\2\u010d\u010e\7k\2\2\u010e\u010f\7h\2\2\u010f,\3")
        buf.write("\2\2\2\u0110\u0111\7g\2\2\u0111\u0112\7n\2\2\u0112\u0113")
        buf.write("\7u\2\2\u0113\u0114\7g\2\2\u0114.\3\2\2\2\u0115\u0116")
        buf.write("\7q\2\2\u0116\u0117\7h\2\2\u0117\60\3\2\2\2\u0118\u0119")
        buf.write("\7q\2\2\u0119\u011a\7w\2\2\u011a\u011b\7v\2\2\u011b\62")
        buf.write("\3\2\2\2\u011c\u0120\t\4\2\2\u011d\u011f\t\5\2\2\u011e")
        buf.write("\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121\64\3\2\2\2\u0122\u0120\3\2")
        buf.write("\2\2\u0123\u0124\7-\2\2\u0124\66\3\2\2\2\u0125\u0126\7")
        buf.write("/\2\2\u01268\3\2\2\2\u0127\u0128\7,\2\2\u0128:\3\2\2\2")
        buf.write("\u0129\u012a\7\61\2\2\u012a<\3\2\2\2\u012b\u012c\7\'\2")
        buf.write("\2\u012c>\3\2\2\2\u012d\u012e\7#\2\2\u012e@\3\2\2\2\u012f")
        buf.write("\u0130\7(\2\2\u0130\u0131\7(\2\2\u0131B\3\2\2\2\u0132")
        buf.write("\u0133\7~\2\2\u0133\u0134\7~\2\2\u0134D\3\2\2\2\u0135")
        buf.write("\u0136\7?\2\2\u0136\u0137\7?\2\2\u0137F\3\2\2\2\u0138")
        buf.write("\u0139\7#\2\2\u0139\u013a\7?\2\2\u013aH\3\2\2\2\u013b")
        buf.write("\u013c\7@\2\2\u013cJ\3\2\2\2\u013d\u013e\7@\2\2\u013e")
        buf.write("\u013f\7?\2\2\u013fL\3\2\2\2\u0140\u0141\7>\2\2\u0141")
        buf.write("N\3\2\2\2\u0142\u0143\7>\2\2\u0143\u0144\7?\2\2\u0144")
        buf.write("P\3\2\2\2\u0145\u0146\7<\2\2\u0146\u0147\7<\2\2\u0147")
        buf.write("R\3\2\2\2\u0148\u0149\7\60\2\2\u0149T\3\2\2\2\u014a\u014b")
        buf.write("\7.\2\2\u014bV\3\2\2\2\u014c\u014d\7=\2\2\u014dX\3\2\2")
        buf.write("\2\u014e\u014f\7<\2\2\u014fZ\3\2\2\2\u0150\u0151\7*\2")
        buf.write("\2\u0151\\\3\2\2\2\u0152\u0153\7+\2\2\u0153^\3\2\2\2\u0154")
        buf.write("\u0155\7]\2\2\u0155`\3\2\2\2\u0156\u0157\7_\2\2\u0157")
        buf.write("b\3\2\2\2\u0158\u0159\7}\2\2\u0159d\3\2\2\2\u015a\u015b")
        buf.write("\7\177\2\2\u015bf\3\2\2\2\u015c\u015d\7?\2\2\u015dh\3")
        buf.write("\2\2\2\u015e\u0168\7\62\2\2\u015f\u0163\t\6\2\2\u0160")
        buf.write("\u0162\t\7\2\2\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2")
        buf.write("\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0166\3")
        buf.write("\2\2\2\u0165\u0163\3\2\2\2\u0166\u0168\b\65\3\2\u0167")
        buf.write("\u015e\3\2\2\2\u0167\u015f\3\2\2\2\u0168j\3\2\2\2\u0169")
        buf.write("\u016b\5i\65\2\u016a\u016c\5m\67\2\u016b\u016a\3\2\2\2")
        buf.write("\u016b\u016c\3\2\2\2\u016c\u016e\3\2\2\2\u016d\u016f\5")
        buf.write("o8\2\u016e\u016d\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170")
        buf.write("\3\2\2\2\u0170\u0171\b\66\4\2\u0171l\3\2\2\2\u0172\u0176")
        buf.write("\7\60\2\2\u0173\u0175\t\b\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2")
        buf.write("\u0177n\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017b\t\t\2")
        buf.write("\2\u017a\u017c\t\n\2\2\u017b\u017a\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017c\u017e\3\2\2\2\u017d\u017f\t\b\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181p\3\2\2\2\u0182\u0185\5\33\16")
        buf.write("\2\u0183\u0185\5\35\17\2\u0184\u0182\3\2\2\2\u0184\u0183")
        buf.write("\3\2\2\2\u0185r\3\2\2\2\u0186\u0187\7$\2\2\u0187t\3\2")
        buf.write("\2\2\u0188\u0189\n\13\2\2\u0189v\3\2\2\2\u018a\u0190\7")
        buf.write("$\2\2\u018b\u018c\7^\2\2\u018c\u018f\5s:\2\u018d\u018f")
        buf.write("\5u;\2\u018e\u018b\3\2\2\2\u018e\u018d\3\2\2\2\u018f\u0192")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write("\u0193\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194\7$\2\2")
        buf.write("\u0194\u0195\b<\5\2\u0195\u0196\b<\6\2\u0196x\3\2\2\2")
        buf.write("\u0197\u0198\5c\62\2\u0198\u0199\7p\2\2\u0199\u019a\7")
        buf.write("q\2\2\u019a\u019b\7p\2\2\u019b\u019c\7g\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019d\u019e\5e\63\2\u019ez\3\2\2\2\u019f\u01a0")
        buf.write("\13\2\2\2\u01a0\u01a1\b>\7\2\u01a1|\3\2\2\2\u01a2\u01a3")
        buf.write("\13\2\2\2\u01a3\u01a4\b?\b\2\u01a4~\3\2\2\2\u01a5\u01a6")
        buf.write("\13\2\2\2\u01a6\u01a7\b@\t\2\u01a7\u0080\3\2\2\2\21\2")
        buf.write("\u0084\u008e\u009c\u0120\u0163\u0167\u016b\u016e\u0176")
        buf.write("\u017b\u0180\u0184\u018e\u0190\n\b\2\2\3\65\2\3\66\3\3")
        buf.write("<\4\3<\5\3>\6\3?\7\3@\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    CCOMMENT = 2
    CPPCOMMENT = 3
    KWVOID = 4
    KWAUTO = 5
    KWINT = 6
    KWFLOAT = 7
    KWBOO = 8
    KWSTR = 9
    KWARR = 10
    KWINHERIT = 11
    KWFUNC = 12
    KWTRUE = 13
    KWFALSE = 14
    KWFOR = 15
    KWWHILE = 16
    KWDO = 17
    KWBRK = 18
    KWCONT = 19
    KWRTN = 20
    KWIF = 21
    KWELSE = 22
    KWOF = 23
    KWOUT = 24
    ID = 25
    ADDOP = 26
    SUBOP = 27
    MULOP = 28
    DIVOP = 29
    MODOP = 30
    EXC = 31
    ANDOP = 32
    OROP = 33
    EQLOP = 34
    DIFOP = 35
    LARGEOP = 36
    LEQLOP = 37
    SMALLOP = 38
    SEQLOP = 39
    CONCATOP = 40
    DOT = 41
    CM = 42
    SM = 43
    CL = 44
    LB = 45
    RB = 46
    LSB = 47
    RSB = 48
    LCB = 49
    RCB = 50
    EQL = 51
    LITINT = 52
    LITFLOAT = 53
    LITBOO = 54
    LITSTR = 55
    LITARR = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void'", "'auto'", "'integer'", "'float'", "'boolean'", "'string'", 
            "'array'", "'inherit'", "'function'", "'true'", "'false'", "'for'", 
            "'while'", "'do'", "'break'", "'continue'", "'return'", "'if'", 
            "'else'", "'of'", "'out'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'>'", "'>='", "'<'", 
            "'<='", "'::'", "'.'", "','", "';'", "':'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
            "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
            "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", "KWCONT", 
            "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", 
            "MULOP", "DIVOP", "MODOP", "EXC", "ANDOP", "OROP", "EQLOP", 
            "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", 
            "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
            "EQL", "LITINT", "LITFLOAT", "LITBOO", "LITSTR", "LITARR", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
                  "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
                  "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", 
                  "KWCONT", "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", 
                  "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EXC", 
                  "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", 
                  "SMALLOP", "SEQLOP", "CONCATOP", "DOT", "CM", "SM", "CL", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "EQL", "LITINT", 
                  "LITFLOAT", "Decimal", "Exponent", "LITBOO", "DoubleQuote", 
                  "InvDoubleQuote", "LITSTR", "LITARR", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[51] = self.LITINT_action 
            actions[52] = self.LITFLOAT_action 
            actions[58] = self.LITSTR_action 
            actions[60] = self.ERROR_CHAR_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LITINT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def LITFLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def LITSTR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace('"','')
     

        if actionIndex == 3:
            self.text = self.text.replace('\\','\\"')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


