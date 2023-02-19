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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u019e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\6\6\u0092\n")
        buf.write("\6\r\6\16\6\u0093\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\7\34\u0115\n\34\f\34\16\34\u0118\13\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)")
        buf.write("\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\3\67\7\67\u0158\n\67\f\67\16\67\u015b")
        buf.write("\13\67\3\67\5\67\u015e\n\67\38\38\58\u0162\n8\38\58\u0165")
        buf.write("\n8\38\38\39\39\79\u016b\n9\f9\169\u016e\139\3:\3:\5:")
        buf.write("\u0172\n:\3:\6:\u0175\n:\r:\16:\u0176\3;\3;\5;\u017b\n")
        buf.write(";\3<\3<\3=\3=\3>\3>\3>\3>\7>\u0185\n>\f>\16>\u0188\13")
        buf.write(">\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3A\3A\3")
        buf.write("A\3B\3B\3B\2\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q\2s\2u:w\2y\2{;}<\177=\u0081>\u0083?\3\2")
        buf.write("\13\5\2\n\f\16\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\63")
        buf.write(";\4\2\62;aa\3\2\62;\4\2GGgg\4\2--//\3\2$$\2\u01a5\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2u")
        buf.write("\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2\2\5\u0088\3\2\2\2")
        buf.write("\7\u008a\3\2\2\2\t\u008d\3\2\2\2\13\u0091\3\2\2\2\r\u0097")
        buf.write("\3\2\2\2\17\u009c\3\2\2\2\21\u00a1\3\2\2\2\23\u00a9\3")
        buf.write("\2\2\2\25\u00af\3\2\2\2\27\u00b7\3\2\2\2\31\u00be\3\2")
        buf.write("\2\2\33\u00c4\3\2\2\2\35\u00cc\3\2\2\2\37\u00d5\3\2\2")
        buf.write("\2!\u00da\3\2\2\2#\u00e0\3\2\2\2%\u00e4\3\2\2\2\'\u00ea")
        buf.write("\3\2\2\2)\u00ed\3\2\2\2+\u00f3\3\2\2\2-\u00fc\3\2\2\2")
        buf.write("/\u0103\3\2\2\2\61\u0106\3\2\2\2\63\u010b\3\2\2\2\65\u010e")
        buf.write("\3\2\2\2\67\u0112\3\2\2\29\u0119\3\2\2\2;\u011b\3\2\2")
        buf.write("\2=\u011d\3\2\2\2?\u011f\3\2\2\2A\u0121\3\2\2\2C\u0123")
        buf.write("\3\2\2\2E\u0125\3\2\2\2G\u0128\3\2\2\2I\u012b\3\2\2\2")
        buf.write("K\u012e\3\2\2\2M\u0131\3\2\2\2O\u0133\3\2\2\2Q\u0136\3")
        buf.write("\2\2\2S\u0138\3\2\2\2U\u013b\3\2\2\2W\u013e\3\2\2\2Y\u0140")
        buf.write("\3\2\2\2[\u0142\3\2\2\2]\u0144\3\2\2\2_\u0146\3\2\2\2")
        buf.write("a\u0148\3\2\2\2c\u014a\3\2\2\2e\u014c\3\2\2\2g\u014e\3")
        buf.write("\2\2\2i\u0150\3\2\2\2k\u0152\3\2\2\2m\u015d\3\2\2\2o\u015f")
        buf.write("\3\2\2\2q\u0168\3\2\2\2s\u016f\3\2\2\2u\u017a\3\2\2\2")
        buf.write("w\u017c\3\2\2\2y\u017e\3\2\2\2{\u0180\3\2\2\2}\u018d\3")
        buf.write("\2\2\2\177\u0195\3\2\2\2\u0081\u0198\3\2\2\2\u0083\u019b")
        buf.write("\3\2\2\2\u0085\u0086\7\61\2\2\u0086\u0087\7\61\2\2\u0087")
        buf.write("\4\3\2\2\2\u0088\u0089\7\f\2\2\u0089\6\3\2\2\2\u008a\u008b")
        buf.write("\7\61\2\2\u008b\u008c\7,\2\2\u008c\b\3\2\2\2\u008d\u008e")
        buf.write("\7,\2\2\u008e\u008f\7\61\2\2\u008f\n\3\2\2\2\u0090\u0092")
        buf.write("\t\2\2\2\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\3\2\2\2")
        buf.write("\u0095\u0096\b\6\2\2\u0096\f\3\2\2\2\u0097\u0098\7x\2")
        buf.write("\2\u0098\u0099\7q\2\2\u0099\u009a\7k\2\2\u009a\u009b\7")
        buf.write("f\2\2\u009b\16\3\2\2\2\u009c\u009d\7c\2\2\u009d\u009e")
        buf.write("\7w\2\2\u009e\u009f\7v\2\2\u009f\u00a0\7q\2\2\u00a0\20")
        buf.write("\3\2\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4")
        buf.write("\7v\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7i\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\u00a8\7t\2\2\u00a8\22\3\2\2\2\u00a9\u00aa")
        buf.write("\7h\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad")
        buf.write("\7c\2\2\u00ad\u00ae\7v\2\2\u00ae\24\3\2\2\2\u00af\u00b0")
        buf.write("\7d\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3")
        buf.write("\7n\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6")
        buf.write("\7p\2\2\u00b6\26\3\2\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\u00bd\7i\2\2\u00bd\30\3\2\2\2\u00be\u00bf")
        buf.write("\7c\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7{\2\2\u00c3\32\3\2\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7j\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7v\2\2\u00cb\34\3\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce")
        buf.write("\7w\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0\7e\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7p\2\2\u00d4\36\3\2\2\2\u00d5\u00d6\7v\2\2\u00d6\u00d7")
        buf.write("\7t\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9\7g\2\2\u00d9 \3")
        buf.write("\2\2\2\u00da\u00db\7h\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd")
        buf.write("\7n\2\2\u00dd\u00de\7u\2\2\u00de\u00df\7g\2\2\u00df\"")
        buf.write("\3\2\2\2\u00e0\u00e1\7h\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3")
        buf.write("\7t\2\2\u00e3$\3\2\2\2\u00e4\u00e5\7y\2\2\u00e5\u00e6")
        buf.write("\7j\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9")
        buf.write("\7g\2\2\u00e9&\3\2\2\2\u00ea\u00eb\7f\2\2\u00eb\u00ec")
        buf.write("\7q\2\2\u00ec(\3\2\2\2\u00ed\u00ee\7d\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2")
        buf.write("\7m\2\2\u00f2*\3\2\2\2\u00f3\u00f4\7e\2\2\u00f4\u00f5")
        buf.write("\7q\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8")
        buf.write("\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb,\3\2\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe")
        buf.write("\7g\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7w\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7p\2\2\u0102.\3\2\2\2\u0103\u0104")
        buf.write("\7k\2\2\u0104\u0105\7h\2\2\u0105\60\3\2\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107\u0108\7n\2\2\u0108\u0109\7u\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a\62\3\2\2\2\u010b\u010c\7q\2\2\u010c\u010d")
        buf.write("\7h\2\2\u010d\64\3\2\2\2\u010e\u010f\7q\2\2\u010f\u0110")
        buf.write("\7w\2\2\u0110\u0111\7v\2\2\u0111\66\3\2\2\2\u0112\u0116")
        buf.write("\t\3\2\2\u0113\u0115\t\4\2\2\u0114\u0113\3\2\2\2\u0115")
        buf.write("\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u01178\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\7-\2\2")
        buf.write("\u011a:\3\2\2\2\u011b\u011c\7/\2\2\u011c<\3\2\2\2\u011d")
        buf.write("\u011e\7,\2\2\u011e>\3\2\2\2\u011f\u0120\7\61\2\2\u0120")
        buf.write("@\3\2\2\2\u0121\u0122\7\'\2\2\u0122B\3\2\2\2\u0123\u0124")
        buf.write("\7#\2\2\u0124D\3\2\2\2\u0125\u0126\7(\2\2\u0126\u0127")
        buf.write("\7(\2\2\u0127F\3\2\2\2\u0128\u0129\7~\2\2\u0129\u012a")
        buf.write("\7~\2\2\u012aH\3\2\2\2\u012b\u012c\7?\2\2\u012c\u012d")
        buf.write("\7?\2\2\u012dJ\3\2\2\2\u012e\u012f\7#\2\2\u012f\u0130")
        buf.write("\7?\2\2\u0130L\3\2\2\2\u0131\u0132\7@\2\2\u0132N\3\2\2")
        buf.write("\2\u0133\u0134\7@\2\2\u0134\u0135\7?\2\2\u0135P\3\2\2")
        buf.write("\2\u0136\u0137\7>\2\2\u0137R\3\2\2\2\u0138\u0139\7>\2")
        buf.write("\2\u0139\u013a\7?\2\2\u013aT\3\2\2\2\u013b\u013c\7<\2")
        buf.write("\2\u013c\u013d\7<\2\2\u013dV\3\2\2\2\u013e\u013f\7\60")
        buf.write("\2\2\u013fX\3\2\2\2\u0140\u0141\7.\2\2\u0141Z\3\2\2\2")
        buf.write("\u0142\u0143\7=\2\2\u0143\\\3\2\2\2\u0144\u0145\7<\2\2")
        buf.write("\u0145^\3\2\2\2\u0146\u0147\7*\2\2\u0147`\3\2\2\2\u0148")
        buf.write("\u0149\7+\2\2\u0149b\3\2\2\2\u014a\u014b\7]\2\2\u014b")
        buf.write("d\3\2\2\2\u014c\u014d\7_\2\2\u014df\3\2\2\2\u014e\u014f")
        buf.write("\7}\2\2\u014fh\3\2\2\2\u0150\u0151\7\177\2\2\u0151j\3")
        buf.write("\2\2\2\u0152\u0153\7?\2\2\u0153l\3\2\2\2\u0154\u015e\7")
        buf.write("\62\2\2\u0155\u0159\t\5\2\2\u0156\u0158\t\6\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015a\u015c\3\2\2\2\u015b\u0159\3")
        buf.write("\2\2\2\u015c\u015e\b\67\3\2\u015d\u0154\3\2\2\2\u015d")
        buf.write("\u0155\3\2\2\2\u015en\3\2\2\2\u015f\u0161\5m\67\2\u0160")
        buf.write("\u0162\5q9\2\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0164\3\2\2\2\u0163\u0165\5s:\2\u0164\u0163\3\2\2\2\u0164")
        buf.write("\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\b8\4\2")
        buf.write("\u0167p\3\2\2\2\u0168\u016c\7\60\2\2\u0169\u016b\t\7\2")
        buf.write("\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016dr\3\2\2\2\u016e\u016c")
        buf.write("\3\2\2\2\u016f\u0171\t\b\2\2\u0170\u0172\t\t\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174\3\2\2\2")
        buf.write("\u0173\u0175\t\7\2\2\u0174\u0173\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177t")
        buf.write("\3\2\2\2\u0178\u017b\5\37\20\2\u0179\u017b\5!\21\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017bv\3\2\2\2\u017c")
        buf.write("\u017d\7$\2\2\u017dx\3\2\2\2\u017e\u017f\n\n\2\2\u017f")
        buf.write("z\3\2\2\2\u0180\u0186\7$\2\2\u0181\u0182\7^\2\2\u0182")
        buf.write("\u0185\5w<\2\u0183\u0185\5y=\2\u0184\u0181\3\2\2\2\u0184")
        buf.write("\u0183\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0186\u0187\3\2\2\2\u0187\u0189\3\2\2\2\u0188\u0186\3")
        buf.write("\2\2\2\u0189\u018a\7$\2\2\u018a\u018b\b>\5\2\u018b\u018c")
        buf.write("\b>\6\2\u018c|\3\2\2\2\u018d\u018e\5g\64\2\u018e\u018f")
        buf.write("\7p\2\2\u018f\u0190\7q\2\2\u0190\u0191\7p\2\2\u0191\u0192")
        buf.write("\7g\2\2\u0192\u0193\3\2\2\2\u0193\u0194\5i\65\2\u0194")
        buf.write("~\3\2\2\2\u0195\u0196\13\2\2\2\u0196\u0197\b@\7\2\u0197")
        buf.write("\u0080\3\2\2\2\u0198\u0199\13\2\2\2\u0199\u019a\bA\b\2")
        buf.write("\u019a\u0082\3\2\2\2\u019b\u019c\13\2\2\2\u019c\u019d")
        buf.write("\bB\t\2\u019d\u0084\3\2\2\2\17\2\u0093\u0116\u0159\u015d")
        buf.write("\u0161\u0164\u016c\u0171\u0176\u017a\u0184\u0186\n\b\2")
        buf.write("\2\3\67\2\38\3\3>\4\3>\5\3@\6\3A\7\3B\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    WS = 5
    KWVOID = 6
    KWAUTO = 7
    KWINT = 8
    KWFLOAT = 9
    KWBOO = 10
    KWSTR = 11
    KWARR = 12
    KWINHERIT = 13
    KWFUNC = 14
    KWTRUE = 15
    KWFALSE = 16
    KWFOR = 17
    KWWHILE = 18
    KWDO = 19
    KWBRK = 20
    KWCONT = 21
    KWRTN = 22
    KWIF = 23
    KWELSE = 24
    KWOF = 25
    KWOUT = 26
    ID = 27
    ADDOP = 28
    SUBOP = 29
    MULOP = 30
    DIVOP = 31
    MODOP = 32
    EXC = 33
    ANDOP = 34
    OROP = 35
    EQLOP = 36
    DIFOP = 37
    LARGEOP = 38
    LEQLOP = 39
    SMALLOP = 40
    SEQLOP = 41
    CONCATOP = 42
    DOT = 43
    CM = 44
    SM = 45
    CL = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    LCB = 51
    RCB = 52
    EQL = 53
    LITINT = 54
    LITFLOAT = 55
    LITBOO = 56
    LITSTR = 57
    LITARR = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'//'", "'\n'", "'/*'", "'*/'", "'void'", "'auto'", "'integer'", 
            "'float'", "'boolean'", "'string'", "'array'", "'inherit'", 
            "'function'", "'true'", "'false'", "'for'", "'while'", "'do'", 
            "'break'", "'continue'", "'return'", "'if'", "'else'", "'of'", 
            "'out'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'::'", "'.'", 
            "','", "';'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "KWVOID", "KWAUTO", "KWINT", "KWFLOAT", "KWBOO", "KWSTR", 
            "KWARR", "KWINHERIT", "KWFUNC", "KWTRUE", "KWFALSE", "KWFOR", 
            "KWWHILE", "KWDO", "KWBRK", "KWCONT", "KWRTN", "KWIF", "KWELSE", 
            "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
            "EXC", "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", 
            "SMALLOP", "SEQLOP", "CONCATOP", "DOT", "CM", "SM", "CL", "LB", 
            "RB", "LSB", "RSB", "LCB", "RCB", "EQL", "LITINT", "LITFLOAT", 
            "LITBOO", "LITSTR", "LITARR", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "WS", "KWVOID", "KWAUTO", 
                  "KWINT", "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", 
                  "KWFUNC", "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", 
                  "KWBRK", "KWCONT", "KWRTN", "KWIF", "KWELSE", "KWOF", 
                  "KWOUT", "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                  "EXC", "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", 
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
            actions[53] = self.LITINT_action 
            actions[54] = self.LITFLOAT_action 
            actions[60] = self.LITSTR_action 
            actions[62] = self.ERROR_CHAR_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
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
     


