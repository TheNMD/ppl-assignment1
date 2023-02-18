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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u019a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\7\2\u0084")
        buf.write("\n\2\f\2\16\2\u0087\13\2\3\3\3\3\3\3\3\3\7\3\u008d\n\3")
        buf.write("\f\3\16\3\u0090\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\7\31\u0112\n\31\f\31\16\31\u0115\13\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\64\7\64\u0155\n\64\f\64\16\64\u0158\13\64\3\64\5")
        buf.write("\64\u015b\n\64\3\65\3\65\5\65\u015f\n\65\3\65\5\65\u0162")
        buf.write("\n\65\3\65\3\65\3\66\3\66\7\66\u0168\n\66\f\66\16\66\u016b")
        buf.write("\13\66\3\67\3\67\5\67\u016f\n\67\3\67\6\67\u0172\n\67")
        buf.write("\r\67\16\67\u0173\38\38\58\u0178\n8\39\39\3:\3:\3;\3;")
        buf.write("\3;\3;\7;\u0182\n;\f;\16;\u0185\13;\3;\3;\3;\3;\3<\6<")
        buf.write("\u018c\n<\r<\16<\u018d\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3")
        buf.write("?\4\u0085\u008e\2@\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g")
        buf.write("\65i\66k\67m8o9q\2s\2u:w;y<{=}>\3\2\13\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\3\2\63;\4\2\62;aa\3\2\62;\4\2GGgg\4\2--//")
        buf.write("\3\2$$\5\2\n\f\16\17\"\"\2\u01a5\2\3\3\2\2\2\2\5\3\2\2")
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
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177\3\2\2\2\5\u0088")
        buf.write("\3\2\2\2\7\u0094\3\2\2\2\t\u0099\3\2\2\2\13\u009e\3\2")
        buf.write("\2\2\r\u00a6\3\2\2\2\17\u00ac\3\2\2\2\21\u00b4\3\2\2\2")
        buf.write("\23\u00bb\3\2\2\2\25\u00c1\3\2\2\2\27\u00c9\3\2\2\2\31")
        buf.write("\u00d2\3\2\2\2\33\u00d7\3\2\2\2\35\u00dd\3\2\2\2\37\u00e1")
        buf.write("\3\2\2\2!\u00e7\3\2\2\2#\u00ea\3\2\2\2%\u00f0\3\2\2\2")
        buf.write("\'\u00f9\3\2\2\2)\u0100\3\2\2\2+\u0103\3\2\2\2-\u0108")
        buf.write("\3\2\2\2/\u010b\3\2\2\2\61\u010f\3\2\2\2\63\u0116\3\2")
        buf.write("\2\2\65\u0118\3\2\2\2\67\u011a\3\2\2\29\u011c\3\2\2\2")
        buf.write(";\u011e\3\2\2\2=\u0120\3\2\2\2?\u0122\3\2\2\2A\u0125\3")
        buf.write("\2\2\2C\u0128\3\2\2\2E\u012b\3\2\2\2G\u012e\3\2\2\2I\u0130")
        buf.write("\3\2\2\2K\u0133\3\2\2\2M\u0135\3\2\2\2O\u0138\3\2\2\2")
        buf.write("Q\u013b\3\2\2\2S\u013d\3\2\2\2U\u013f\3\2\2\2W\u0141\3")
        buf.write("\2\2\2Y\u0143\3\2\2\2[\u0145\3\2\2\2]\u0147\3\2\2\2_\u0149")
        buf.write("\3\2\2\2a\u014b\3\2\2\2c\u014d\3\2\2\2e\u014f\3\2\2\2")
        buf.write("g\u015a\3\2\2\2i\u015c\3\2\2\2k\u0165\3\2\2\2m\u016c\3")
        buf.write("\2\2\2o\u0177\3\2\2\2q\u0179\3\2\2\2s\u017b\3\2\2\2u\u017d")
        buf.write("\3\2\2\2w\u018b\3\2\2\2y\u0191\3\2\2\2{\u0194\3\2\2\2")
        buf.write("}\u0197\3\2\2\2\177\u0080\7\61\2\2\u0080\u0081\7\61\2")
        buf.write("\2\u0081\u0085\3\2\2\2\u0082\u0084\13\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0086\3\2\2\2\u0085")
        buf.write("\u0083\3\2\2\2\u0086\4\3\2\2\2\u0087\u0085\3\2\2\2\u0088")
        buf.write("\u0089\7\61\2\2\u0089\u008a\7,\2\2\u008a\u008e\3\2\2\2")
        buf.write("\u008b\u008d\13\2\2\2\u008c\u008b\3\2\2\2\u008d\u0090")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008e\u008c\3\2\2\2\u008f")
        buf.write("\u0091\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\7,\2\2")
        buf.write("\u0092\u0093\7\61\2\2\u0093\6\3\2\2\2\u0094\u0095\7x\2")
        buf.write("\2\u0095\u0096\7q\2\2\u0096\u0097\7k\2\2\u0097\u0098\7")
        buf.write("f\2\2\u0098\b\3\2\2\2\u0099\u009a\7c\2\2\u009a\u009b\7")
        buf.write("w\2\2\u009b\u009c\7v\2\2\u009c\u009d\7q\2\2\u009d\n\3")
        buf.write("\2\2\2\u009e\u009f\7k\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7i\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\7t\2\2\u00a5\f\3\2\2\2\u00a6\u00a7")
        buf.write("\7h\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa")
        buf.write("\7c\2\2\u00aa\u00ab\7v\2\2\u00ab\16\3\2\2\2\u00ac\u00ad")
        buf.write("\7d\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7n\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3\20\3\2\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9")
        buf.write("\7p\2\2\u00b9\u00ba\7i\2\2\u00ba\22\3\2\2\2\u00bb\u00bc")
        buf.write("\7c\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7c\2\2\u00bf\u00c0\7{\2\2\u00c0\24\3\2\2\2\u00c1\u00c2")
        buf.write("\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7j\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\26\3\2\2\2\u00c9\u00ca\7h\2\2\u00ca\u00cb")
        buf.write("\7w\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7e\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\30\3\2\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4")
        buf.write("\7t\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6\7g\2\2\u00d6\32")
        buf.write("\3\2\2\2\u00d7\u00d8\7h\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da")
        buf.write("\7n\2\2\u00da\u00db\7u\2\2\u00db\u00dc\7g\2\2\u00dc\34")
        buf.write("\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df\7q\2\2\u00df\u00e0")
        buf.write("\7t\2\2\u00e0\36\3\2\2\2\u00e1\u00e2\7y\2\2\u00e2\u00e3")
        buf.write("\7j\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6 \3\2\2\2\u00e7\u00e8\7f\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\"\3\2\2\2\u00ea\u00eb\7d\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef")
        buf.write("\7m\2\2\u00ef$\3\2\2\2\u00f0\u00f1\7e\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5")
        buf.write("\7k\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8&\3\2\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe\u00ff\7p\2\2\u00ff(\3\2\2\2\u0100\u0101")
        buf.write("\7k\2\2\u0101\u0102\7h\2\2\u0102*\3\2\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104\u0105\7n\2\2\u0105\u0106\7u\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107,\3\2\2\2\u0108\u0109\7q\2\2\u0109\u010a")
        buf.write("\7h\2\2\u010a.\3\2\2\2\u010b\u010c\7q\2\2\u010c\u010d")
        buf.write("\7w\2\2\u010d\u010e\7v\2\2\u010e\60\3\2\2\2\u010f\u0113")
        buf.write("\t\2\2\2\u0110\u0112\t\3\2\2\u0111\u0110\3\2\2\2\u0112")
        buf.write("\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114\62\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0117\7-\2")
        buf.write("\2\u0117\64\3\2\2\2\u0118\u0119\7/\2\2\u0119\66\3\2\2")
        buf.write("\2\u011a\u011b\7,\2\2\u011b8\3\2\2\2\u011c\u011d\7\61")
        buf.write("\2\2\u011d:\3\2\2\2\u011e\u011f\7\'\2\2\u011f<\3\2\2\2")
        buf.write("\u0120\u0121\7#\2\2\u0121>\3\2\2\2\u0122\u0123\7(\2\2")
        buf.write("\u0123\u0124\7(\2\2\u0124@\3\2\2\2\u0125\u0126\7~\2\2")
        buf.write("\u0126\u0127\7~\2\2\u0127B\3\2\2\2\u0128\u0129\7?\2\2")
        buf.write("\u0129\u012a\7?\2\2\u012aD\3\2\2\2\u012b\u012c\7#\2\2")
        buf.write("\u012c\u012d\7?\2\2\u012dF\3\2\2\2\u012e\u012f\7@\2\2")
        buf.write("\u012fH\3\2\2\2\u0130\u0131\7@\2\2\u0131\u0132\7?\2\2")
        buf.write("\u0132J\3\2\2\2\u0133\u0134\7>\2\2\u0134L\3\2\2\2\u0135")
        buf.write("\u0136\7>\2\2\u0136\u0137\7?\2\2\u0137N\3\2\2\2\u0138")
        buf.write("\u0139\7<\2\2\u0139\u013a\7<\2\2\u013aP\3\2\2\2\u013b")
        buf.write("\u013c\7\60\2\2\u013cR\3\2\2\2\u013d\u013e\7.\2\2\u013e")
        buf.write("T\3\2\2\2\u013f\u0140\7=\2\2\u0140V\3\2\2\2\u0141\u0142")
        buf.write("\7<\2\2\u0142X\3\2\2\2\u0143\u0144\7*\2\2\u0144Z\3\2\2")
        buf.write("\2\u0145\u0146\7+\2\2\u0146\\\3\2\2\2\u0147\u0148\7]\2")
        buf.write("\2\u0148^\3\2\2\2\u0149\u014a\7_\2\2\u014a`\3\2\2\2\u014b")
        buf.write("\u014c\7}\2\2\u014cb\3\2\2\2\u014d\u014e\7\177\2\2\u014e")
        buf.write("d\3\2\2\2\u014f\u0150\7?\2\2\u0150f\3\2\2\2\u0151\u015b")
        buf.write("\7\62\2\2\u0152\u0156\t\4\2\2\u0153\u0155\t\5\2\2\u0154")
        buf.write("\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u0156\3")
        buf.write("\2\2\2\u0159\u015b\b\64\2\2\u015a\u0151\3\2\2\2\u015a")
        buf.write("\u0152\3\2\2\2\u015bh\3\2\2\2\u015c\u015e\5g\64\2\u015d")
        buf.write("\u015f\5k\66\2\u015e\u015d\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0161\3\2\2\2\u0160\u0162\5m\67\2\u0161\u0160\3")
        buf.write("\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164")
        buf.write("\b\65\3\2\u0164j\3\2\2\2\u0165\u0169\7\60\2\2\u0166\u0168")
        buf.write("\t\6\2\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016al\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016e\t\7\2\2\u016d\u016f\t\b\2\2")
        buf.write("\u016e\u016d\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0171\3")
        buf.write("\2\2\2\u0170\u0172\t\6\2\2\u0171\u0170\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("n\3\2\2\2\u0175\u0178\5\31\r\2\u0176\u0178\5\33\16\2\u0177")
        buf.write("\u0175\3\2\2\2\u0177\u0176\3\2\2\2\u0178p\3\2\2\2\u0179")
        buf.write("\u017a\7$\2\2\u017ar\3\2\2\2\u017b\u017c\n\t\2\2\u017c")
        buf.write("t\3\2\2\2\u017d\u0183\7$\2\2\u017e\u017f\7^\2\2\u017f")
        buf.write("\u0182\5q9\2\u0180\u0182\5s:\2\u0181\u017e\3\2\2\2\u0181")
        buf.write("\u0180\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0183\u0184\3\2\2\2\u0184\u0186\3\2\2\2\u0185\u0183\3")
        buf.write("\2\2\2\u0186\u0187\7$\2\2\u0187\u0188\b;\4\2\u0188\u0189")
        buf.write("\b;\5\2\u0189v\3\2\2\2\u018a\u018c\t\n\2\2\u018b\u018a")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\b<\6\2")
        buf.write("\u0190x\3\2\2\2\u0191\u0192\13\2\2\2\u0192\u0193\b=\7")
        buf.write("\2\u0193z\3\2\2\2\u0194\u0195\13\2\2\2\u0195\u0196\b>")
        buf.write("\b\2\u0196|\3\2\2\2\u0197\u0198\13\2\2\2\u0198\u0199\b")
        buf.write("?\t\2\u0199~\3\2\2\2\21\2\u0085\u008e\u0113\u0156\u015a")
        buf.write("\u015e\u0161\u0169\u016e\u0173\u0177\u0181\u0183\u018d")
        buf.write("\n\3\64\2\3\65\3\3;\4\3;\5\b\2\2\3=\6\3>\7\3?\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CCOMMENT = 1
    CPPCOMMENT = 2
    KWVOID = 3
    KWAUTO = 4
    KWINT = 5
    KWFLOAT = 6
    KWBOO = 7
    KWSTR = 8
    KWARR = 9
    KWINHERIT = 10
    KWFUNC = 11
    KWTRUE = 12
    KWFALSE = 13
    KWFOR = 14
    KWWHILE = 15
    KWDO = 16
    KWBRK = 17
    KWCONT = 18
    KWRTN = 19
    KWIF = 20
    KWELSE = 21
    KWOF = 22
    KWOUT = 23
    ID = 24
    ADDOP = 25
    SUBOP = 26
    MULOP = 27
    DIVOP = 28
    MODOP = 29
    EXC = 30
    ANDOP = 31
    OROP = 32
    EQLOP = 33
    DIFOP = 34
    LARGEOP = 35
    LEQLOP = 36
    SMALLOP = 37
    SEQLOP = 38
    CONCATOP = 39
    DOT = 40
    CM = 41
    SM = 42
    CL = 43
    LB = 44
    RB = 45
    LSB = 46
    RSB = 47
    LCB = 48
    RCB = 49
    EQL = 50
    LITINT = 51
    LITFLOAT = 52
    LITDEC = 53
    LITEXP = 54
    LITBOO = 55
    LITSTR = 56
    WS = 57
    ERROR_CHAR = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60

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
            "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", "KWFLOAT", 
            "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", "KWTRUE", 
            "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", "KWCONT", "KWRTN", 
            "KWIF", "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", "MULOP", 
            "DIVOP", "MODOP", "EXC", "ANDOP", "OROP", "EQLOP", "DIFOP", 
            "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", "DOT", 
            "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "EQL", 
            "LITINT", "LITFLOAT", "LITDEC", "LITEXP", "LITBOO", "LITSTR", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
                  "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
                  "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", 
                  "KWCONT", "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", 
                  "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EXC", 
                  "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", 
                  "SMALLOP", "SEQLOP", "CONCATOP", "DOT", "CM", "SM", "CL", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "EQL", "LITINT", 
                  "LITFLOAT", "LITDEC", "LITEXP", "LITBOO", "DoubleQuote", 
                  "InvDoubleQuote", "LITSTR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[50] = self.LITINT_action 
            actions[51] = self.LITFLOAT_action 
            actions[57] = self.LITSTR_action 
            actions[59] = self.ERROR_CHAR_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
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
     


