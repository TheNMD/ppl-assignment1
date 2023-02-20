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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29")
        buf.write("\u0187\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\6\2w\n\2\r\2\16\2x\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0081")
        buf.write("\n\3\f\3\16\3\u0084\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\7\4\u008f\n\4\f\4\16\4\u0092\13\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\7\32\u0113\n\32\f\32\16\32\u0116")
        buf.write("\13\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3")
        buf.write("\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3")
        buf.write("%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\65\7\65\u0156\n\65\f\65\16")
        buf.write("\65\u0159\13\65\3\65\5\65\u015c\n\65\3\66\3\66\5\66\u0160")
        buf.write("\n\66\3\66\5\66\u0163\n\66\3\66\3\66\3\67\3\67\7\67\u0169")
        buf.write("\n\67\f\67\16\67\u016c\13\67\38\38\58\u0170\n8\38\68\u0173")
        buf.write("\n8\r8\168\u0174\39\39\59\u0179\n9\3:\3:\3:\3:\7:\u017f")
        buf.write("\n:\f:\16:\u0182\13:\3:\3:\3:\3:\3\u0082\2;\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q8s9\3\2\r\5")
        buf.write("\2\n\f\16\17\"\"\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\3\2\63;\4\2\62;aa\3\2\62;\4\2GGgg\4\2--//\n\2$$))")
        buf.write("^^ddhhppttvv\7\2\n\f\16\17$$))^^\2\u0192\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3v\3\2\2\2\5|\3\2")
        buf.write("\2\2\7\u008a\3\2\2\2\t\u0095\3\2\2\2\13\u009a\3\2\2\2")
        buf.write("\r\u009f\3\2\2\2\17\u00a7\3\2\2\2\21\u00ad\3\2\2\2\23")
        buf.write("\u00b5\3\2\2\2\25\u00bc\3\2\2\2\27\u00c2\3\2\2\2\31\u00ca")
        buf.write("\3\2\2\2\33\u00d3\3\2\2\2\35\u00d8\3\2\2\2\37\u00de\3")
        buf.write("\2\2\2!\u00e2\3\2\2\2#\u00e8\3\2\2\2%\u00eb\3\2\2\2\'")
        buf.write("\u00f1\3\2\2\2)\u00fa\3\2\2\2+\u0101\3\2\2\2-\u0104\3")
        buf.write("\2\2\2/\u0109\3\2\2\2\61\u010c\3\2\2\2\63\u0110\3\2\2")
        buf.write("\2\65\u0117\3\2\2\2\67\u0119\3\2\2\29\u011b\3\2\2\2;\u011d")
        buf.write("\3\2\2\2=\u011f\3\2\2\2?\u0121\3\2\2\2A\u0123\3\2\2\2")
        buf.write("C\u0126\3\2\2\2E\u0129\3\2\2\2G\u012c\3\2\2\2I\u012f\3")
        buf.write("\2\2\2K\u0131\3\2\2\2M\u0134\3\2\2\2O\u0136\3\2\2\2Q\u0139")
        buf.write("\3\2\2\2S\u013c\3\2\2\2U\u013e\3\2\2\2W\u0140\3\2\2\2")
        buf.write("Y\u0142\3\2\2\2[\u0144\3\2\2\2]\u0146\3\2\2\2_\u0148\3")
        buf.write("\2\2\2a\u014a\3\2\2\2c\u014c\3\2\2\2e\u014e\3\2\2\2g\u0150")
        buf.write("\3\2\2\2i\u015b\3\2\2\2k\u015d\3\2\2\2m\u0166\3\2\2\2")
        buf.write("o\u016d\3\2\2\2q\u0178\3\2\2\2s\u017a\3\2\2\2uw\t\2\2")
        buf.write("\2vu\3\2\2\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2\2yz\3\2\2\2z")
        buf.write("{\b\2\2\2{\4\3\2\2\2|}\7\61\2\2}~\7,\2\2~\u0082\3\2\2")
        buf.write("\2\177\u0081\13\2\2\2\u0080\177\3\2\2\2\u0081\u0084\3")
        buf.write("\2\2\2\u0082\u0083\3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0085")
        buf.write("\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086\7,\2\2\u0086")
        buf.write("\u0087\7\61\2\2\u0087\u0088\3\2\2\2\u0088\u0089\b\3\2")
        buf.write("\2\u0089\6\3\2\2\2\u008a\u008b\7\61\2\2\u008b\u008c\7")
        buf.write("\61\2\2\u008c\u0090\3\2\2\2\u008d\u008f\n\3\2\2\u008e")
        buf.write("\u008d\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u0093\3\2\2\2\u0092\u0090\3")
        buf.write("\2\2\2\u0093\u0094\b\4\2\2\u0094\b\3\2\2\2\u0095\u0096")
        buf.write("\7x\2\2\u0096\u0097\7q\2\2\u0097\u0098\7k\2\2\u0098\u0099")
        buf.write("\7f\2\2\u0099\n\3\2\2\2\u009a\u009b\7c\2\2\u009b\u009c")
        buf.write("\7w\2\2\u009c\u009d\7v\2\2\u009d\u009e\7q\2\2\u009e\f")
        buf.write("\3\2\2\2\u009f\u00a0\7k\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2")
        buf.write("\7v\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7i\2\2\u00a4\u00a5")
        buf.write("\7g\2\2\u00a5\u00a6\7t\2\2\u00a6\16\3\2\2\2\u00a7\u00a8")
        buf.write("\7h\2\2\u00a8\u00a9\7n\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab")
        buf.write("\7c\2\2\u00ab\u00ac\7v\2\2\u00ac\20\3\2\2\2\u00ad\u00ae")
        buf.write("\7d\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1")
        buf.write("\7n\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4")
        buf.write("\7p\2\2\u00b4\22\3\2\2\2\u00b5\u00b6\7u\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba")
        buf.write("\7p\2\2\u00ba\u00bb\7i\2\2\u00bb\24\3\2\2\2\u00bc\u00bd")
        buf.write("\7c\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0")
        buf.write("\7c\2\2\u00c0\u00c1\7{\2\2\u00c1\26\3\2\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7j\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\30\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc")
        buf.write("\7w\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7e\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\32\3\2\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7t\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7\7g\2\2\u00d7\34")
        buf.write("\3\2\2\2\u00d8\u00d9\7h\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7n\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7g\2\2\u00dd\36")
        buf.write("\3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1 \3\2\2\2\u00e2\u00e3\7y\2\2\u00e3\u00e4")
        buf.write("\7j\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7\"\3\2\2\2\u00e8\u00e9\7f\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea$\3\2\2\2\u00eb\u00ec\7d\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0")
        buf.write("\7m\2\2\u00f0&\3\2\2\2\u00f1\u00f2\7e\2\2\u00f2\u00f3")
        buf.write("\7q\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6")
        buf.write("\7k\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9")
        buf.write("\7g\2\2\u00f9(\3\2\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff")
        buf.write("\7t\2\2\u00ff\u0100\7p\2\2\u0100*\3\2\2\2\u0101\u0102")
        buf.write("\7k\2\2\u0102\u0103\7h\2\2\u0103,\3\2\2\2\u0104\u0105")
        buf.write("\7g\2\2\u0105\u0106\7n\2\2\u0106\u0107\7u\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108.\3\2\2\2\u0109\u010a\7q\2\2\u010a\u010b")
        buf.write("\7h\2\2\u010b\60\3\2\2\2\u010c\u010d\7q\2\2\u010d\u010e")
        buf.write("\7w\2\2\u010e\u010f\7v\2\2\u010f\62\3\2\2\2\u0110\u0114")
        buf.write("\t\4\2\2\u0111\u0113\t\5\2\2\u0112\u0111\3\2\2\2\u0113")
        buf.write("\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2")
        buf.write("\u0115\64\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118\7-\2")
        buf.write("\2\u0118\66\3\2\2\2\u0119\u011a\7/\2\2\u011a8\3\2\2\2")
        buf.write("\u011b\u011c\7,\2\2\u011c:\3\2\2\2\u011d\u011e\7\61\2")
        buf.write("\2\u011e<\3\2\2\2\u011f\u0120\7\'\2\2\u0120>\3\2\2\2\u0121")
        buf.write("\u0122\7#\2\2\u0122@\3\2\2\2\u0123\u0124\7(\2\2\u0124")
        buf.write("\u0125\7(\2\2\u0125B\3\2\2\2\u0126\u0127\7~\2\2\u0127")
        buf.write("\u0128\7~\2\2\u0128D\3\2\2\2\u0129\u012a\7?\2\2\u012a")
        buf.write("\u012b\7?\2\2\u012bF\3\2\2\2\u012c\u012d\7#\2\2\u012d")
        buf.write("\u012e\7?\2\2\u012eH\3\2\2\2\u012f\u0130\7@\2\2\u0130")
        buf.write("J\3\2\2\2\u0131\u0132\7@\2\2\u0132\u0133\7?\2\2\u0133")
        buf.write("L\3\2\2\2\u0134\u0135\7>\2\2\u0135N\3\2\2\2\u0136\u0137")
        buf.write("\7>\2\2\u0137\u0138\7?\2\2\u0138P\3\2\2\2\u0139\u013a")
        buf.write("\7<\2\2\u013a\u013b\7<\2\2\u013bR\3\2\2\2\u013c\u013d")
        buf.write("\7\60\2\2\u013dT\3\2\2\2\u013e\u013f\7.\2\2\u013fV\3\2")
        buf.write("\2\2\u0140\u0141\7=\2\2\u0141X\3\2\2\2\u0142\u0143\7<")
        buf.write("\2\2\u0143Z\3\2\2\2\u0144\u0145\7*\2\2\u0145\\\3\2\2\2")
        buf.write("\u0146\u0147\7+\2\2\u0147^\3\2\2\2\u0148\u0149\7]\2\2")
        buf.write("\u0149`\3\2\2\2\u014a\u014b\7_\2\2\u014bb\3\2\2\2\u014c")
        buf.write("\u014d\7}\2\2\u014dd\3\2\2\2\u014e\u014f\7\177\2\2\u014f")
        buf.write("f\3\2\2\2\u0150\u0151\7?\2\2\u0151h\3\2\2\2\u0152\u015c")
        buf.write("\7\62\2\2\u0153\u0157\t\6\2\2\u0154\u0156\t\7\2\2\u0155")
        buf.write("\u0154\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2")
        buf.write("\u0157\u0158\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u0157\3")
        buf.write("\2\2\2\u015a\u015c\b\65\3\2\u015b\u0152\3\2\2\2\u015b")
        buf.write("\u0153\3\2\2\2\u015cj\3\2\2\2\u015d\u015f\5i\65\2\u015e")
        buf.write("\u0160\5m\67\2\u015f\u015e\3\2\2\2\u015f\u0160\3\2\2\2")
        buf.write("\u0160\u0162\3\2\2\2\u0161\u0163\5o8\2\u0162\u0161\3\2")
        buf.write("\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165")
        buf.write("\b\66\4\2\u0165l\3\2\2\2\u0166\u016a\7\60\2\2\u0167\u0169")
        buf.write("\t\b\2\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016bn\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016d\u016f\t\t\2\2\u016e\u0170\t\n\2\2")
        buf.write("\u016f\u016e\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0172\3")
        buf.write("\2\2\2\u0171\u0173\t\b\2\2\u0172\u0171\3\2\2\2\u0173\u0174")
        buf.write("\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("p\3\2\2\2\u0176\u0179\5\33\16\2\u0177\u0179\5\35\17\2")
        buf.write("\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179r\3\2\2")
        buf.write("\2\u017a\u0180\7$\2\2\u017b\u017c\7^\2\2\u017c\u017f\t")
        buf.write("\13\2\2\u017d\u017f\n\f\2\2\u017e\u017b\3\2\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u0180\3")
        buf.write("\2\2\2\u0183\u0184\7$\2\2\u0184\u0185\b:\5\2\u0185\u0186")
        buf.write("\b:\6\2\u0186t\3\2\2\2\21\2x\u0082\u0090\u0114\u0157\u015b")
        buf.write("\u015f\u0162\u016a\u016f\u0174\u0178\u017e\u0180\7\b\2")
        buf.write("\2\3\65\2\3\66\3\3:\4\3:\5")
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
    EXCOP = 31
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
            "MULOP", "DIVOP", "MODOP", "EXCOP", "ANDOP", "OROP", "EQLOP", 
            "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", 
            "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
            "EQL", "LITINT", "LITFLOAT", "LITBOO", "LITSTR" ]

    ruleNames = [ "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
                  "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
                  "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", 
                  "KWCONT", "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", 
                  "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EXCOP", 
                  "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", 
                  "SMALLOP", "SEQLOP", "CONCATOP", "DOT", "CM", "SM", "CL", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "EQL", "LITINT", 
                  "LITFLOAT", "Decimal", "Exponent", "LITBOO", "LITSTR" ]

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
            actions[56] = self.LITSTR_action 
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
     


