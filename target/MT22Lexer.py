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
        buf.write("\u01ab\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u008d\n\3\f\3\16\3\u0090")
        buf.write("\13\3\3\4\3\4\3\4\3\4\7\4\u0096\n\4\f\4\16\4\u0099\13")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\7\32\u011b\n")
        buf.write("\32\f\32\16\32\u011e\13\32\3\33\3\33\3\34\3\34\3\35\3")
        buf.write("\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)")
        buf.write("\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\7\65")
        buf.write("\u015e\n\65\f\65\16\65\u0161\13\65\3\65\5\65\u0164\n\65")
        buf.write("\3\66\3\66\5\66\u0168\n\66\3\66\5\66\u016b\n\66\3\66\3")
        buf.write("\66\3\67\3\67\7\67\u0171\n\67\f\67\16\67\u0174\13\67\3")
        buf.write("8\38\58\u0178\n8\38\68\u017b\n8\r8\168\u017c\39\39\59")
        buf.write("\u0181\n9\3:\3:\3;\3;\3<\3<\3<\3<\7<\u018b\n<\f<\16<\u018e")
        buf.write("\13<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3>\6>\u019d\n")
        buf.write(">\r>\16>\u019e\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\4\u008e")
        buf.write("\u0097\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m\2o\2q8s\2u\2w9y:{;}<\177=\u0081>\3\2\13\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\3\2\63;\4\2\62;aa\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\3\2$$\5\2\n\f\16\17\"\"\2\u01b4\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2q\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2")
        buf.write("\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083")
        buf.write("\3\2\2\2\5\u0088\3\2\2\2\7\u0091\3\2\2\2\t\u009d\3\2\2")
        buf.write("\2\13\u00a2\3\2\2\2\r\u00a7\3\2\2\2\17\u00af\3\2\2\2\21")
        buf.write("\u00b5\3\2\2\2\23\u00bd\3\2\2\2\25\u00c4\3\2\2\2\27\u00ca")
        buf.write("\3\2\2\2\31\u00d2\3\2\2\2\33\u00db\3\2\2\2\35\u00e0\3")
        buf.write("\2\2\2\37\u00e6\3\2\2\2!\u00ea\3\2\2\2#\u00f0\3\2\2\2")
        buf.write("%\u00f3\3\2\2\2\'\u00f9\3\2\2\2)\u0102\3\2\2\2+\u0109")
        buf.write("\3\2\2\2-\u010c\3\2\2\2/\u0111\3\2\2\2\61\u0114\3\2\2")
        buf.write("\2\63\u0118\3\2\2\2\65\u011f\3\2\2\2\67\u0121\3\2\2\2")
        buf.write("9\u0123\3\2\2\2;\u0125\3\2\2\2=\u0127\3\2\2\2?\u0129\3")
        buf.write("\2\2\2A\u012b\3\2\2\2C\u012e\3\2\2\2E\u0131\3\2\2\2G\u0134")
        buf.write("\3\2\2\2I\u0137\3\2\2\2K\u0139\3\2\2\2M\u013c\3\2\2\2")
        buf.write("O\u013e\3\2\2\2Q\u0141\3\2\2\2S\u0144\3\2\2\2U\u0146\3")
        buf.write("\2\2\2W\u0148\3\2\2\2Y\u014a\3\2\2\2[\u014c\3\2\2\2]\u014e")
        buf.write("\3\2\2\2_\u0150\3\2\2\2a\u0152\3\2\2\2c\u0154\3\2\2\2")
        buf.write("e\u0156\3\2\2\2g\u0158\3\2\2\2i\u0163\3\2\2\2k\u0165\3")
        buf.write("\2\2\2m\u016e\3\2\2\2o\u0175\3\2\2\2q\u0180\3\2\2\2s\u0182")
        buf.write("\3\2\2\2u\u0184\3\2\2\2w\u0186\3\2\2\2y\u0193\3\2\2\2")
        buf.write("{\u019c\3\2\2\2}\u01a2\3\2\2\2\177\u01a5\3\2\2\2\u0081")
        buf.write("\u01a8\3\2\2\2\u0083\u0084\7g\2\2\u0084\u0085\7z\2\2\u0085")
        buf.write("\u0086\7r\2\2\u0086\u0087\7t\2\2\u0087\4\3\2\2\2\u0088")
        buf.write("\u0089\7\61\2\2\u0089\u008a\7\61\2\2\u008a\u008e\3\2\2")
        buf.write("\2\u008b\u008d\13\2\2\2\u008c\u008b\3\2\2\2\u008d\u0090")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008e\u008c\3\2\2\2\u008f")
        buf.write("\6\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\7\61\2\2\u0092")
        buf.write("\u0093\7,\2\2\u0093\u0097\3\2\2\2\u0094\u0096\13\2\2\2")
        buf.write("\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0098\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097")
        buf.write("\3\2\2\2\u009a\u009b\7,\2\2\u009b\u009c\7\61\2\2\u009c")
        buf.write("\b\3\2\2\2\u009d\u009e\7x\2\2\u009e\u009f\7q\2\2\u009f")
        buf.write("\u00a0\7k\2\2\u00a0\u00a1\7f\2\2\u00a1\n\3\2\2\2\u00a2")
        buf.write("\u00a3\7c\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5\7v\2\2\u00a5")
        buf.write("\u00a6\7q\2\2\u00a6\f\3\2\2\2\u00a7\u00a8\7k\2\2\u00a8")
        buf.write("\u00a9\7p\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab\7g\2\2\u00ab")
        buf.write("\u00ac\7i\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7t\2\2\u00ae")
        buf.write("\16\3\2\2\2\u00af\u00b0\7h\2\2\u00b0\u00b1\7n\2\2\u00b1")
        buf.write("\u00b2\7q\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4\7v\2\2\u00b4")
        buf.write("\20\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7\7q\2\2\u00b7")
        buf.write("\u00b8\7q\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba\7g\2\2\u00ba")
        buf.write("\u00bb\7c\2\2\u00bb\u00bc\7p\2\2\u00bc\22\3\2\2\2\u00bd")
        buf.write("\u00be\7u\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7t\2\2\u00c0")
        buf.write("\u00c1\7k\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7i\2\2\u00c3")
        buf.write("\24\3\2\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7t\2\2\u00c6")
        buf.write("\u00c7\7t\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7{\2\2\u00c9")
        buf.write("\26\3\2\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc")
        buf.write("\u00cd\7j\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7t\2\2\u00cf")
        buf.write("\u00d0\7k\2\2\u00d0\u00d1\7v\2\2\u00d1\30\3\2\2\2\u00d2")
        buf.write("\u00d3\7h\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5\7p\2\2\u00d5")
        buf.write("\u00d6\7e\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7k\2\2\u00d8")
        buf.write("\u00d9\7q\2\2\u00d9\u00da\7p\2\2\u00da\32\3\2\2\2\u00db")
        buf.write("\u00dc\7v\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de\7w\2\2\u00de")
        buf.write("\u00df\7g\2\2\u00df\34\3\2\2\2\u00e0\u00e1\7h\2\2\u00e1")
        buf.write("\u00e2\7c\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4\7u\2\2\u00e4")
        buf.write("\u00e5\7g\2\2\u00e5\36\3\2\2\2\u00e6\u00e7\7h\2\2\u00e7")
        buf.write("\u00e8\7q\2\2\u00e8\u00e9\7t\2\2\u00e9 \3\2\2\2\u00ea")
        buf.write("\u00eb\7y\2\2\u00eb\u00ec\7j\2\2\u00ec\u00ed\7k\2\2\u00ed")
        buf.write("\u00ee\7n\2\2\u00ee\u00ef\7g\2\2\u00ef\"\3\2\2\2\u00f0")
        buf.write("\u00f1\7f\2\2\u00f1\u00f2\7q\2\2\u00f2$\3\2\2\2\u00f3")
        buf.write("\u00f4\7d\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7g\2\2\u00f6")
        buf.write("\u00f7\7c\2\2\u00f7\u00f8\7m\2\2\u00f8&\3\2\2\2\u00f9")
        buf.write("\u00fa\7e\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7p\2\2\u00fc")
        buf.write("\u00fd\7v\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff")
        buf.write("\u0100\7w\2\2\u0100\u0101\7g\2\2\u0101(\3\2\2\2\u0102")
        buf.write("\u0103\7t\2\2\u0103\u0104\7g\2\2\u0104\u0105\7v\2\2\u0105")
        buf.write("\u0106\7w\2\2\u0106\u0107\7t\2\2\u0107\u0108\7p\2\2\u0108")
        buf.write("*\3\2\2\2\u0109\u010a\7k\2\2\u010a\u010b\7h\2\2\u010b")
        buf.write(",\3\2\2\2\u010c\u010d\7g\2\2\u010d\u010e\7n\2\2\u010e")
        buf.write("\u010f\7u\2\2\u010f\u0110\7g\2\2\u0110.\3\2\2\2\u0111")
        buf.write("\u0112\7q\2\2\u0112\u0113\7h\2\2\u0113\60\3\2\2\2\u0114")
        buf.write("\u0115\7q\2\2\u0115\u0116\7w\2\2\u0116\u0117\7v\2\2\u0117")
        buf.write("\62\3\2\2\2\u0118\u011c\t\2\2\2\u0119\u011b\t\3\2\2\u011a")
        buf.write("\u0119\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2")
        buf.write("\u011c\u011d\3\2\2\2\u011d\64\3\2\2\2\u011e\u011c\3\2")
        buf.write("\2\2\u011f\u0120\7-\2\2\u0120\66\3\2\2\2\u0121\u0122\7")
        buf.write("/\2\2\u01228\3\2\2\2\u0123\u0124\7,\2\2\u0124:\3\2\2\2")
        buf.write("\u0125\u0126\7\61\2\2\u0126<\3\2\2\2\u0127\u0128\7\'\2")
        buf.write("\2\u0128>\3\2\2\2\u0129\u012a\7#\2\2\u012a@\3\2\2\2\u012b")
        buf.write("\u012c\7(\2\2\u012c\u012d\7(\2\2\u012dB\3\2\2\2\u012e")
        buf.write("\u012f\7~\2\2\u012f\u0130\7~\2\2\u0130D\3\2\2\2\u0131")
        buf.write("\u0132\7?\2\2\u0132\u0133\7?\2\2\u0133F\3\2\2\2\u0134")
        buf.write("\u0135\7#\2\2\u0135\u0136\7?\2\2\u0136H\3\2\2\2\u0137")
        buf.write("\u0138\7@\2\2\u0138J\3\2\2\2\u0139\u013a\7@\2\2\u013a")
        buf.write("\u013b\7?\2\2\u013bL\3\2\2\2\u013c\u013d\7>\2\2\u013d")
        buf.write("N\3\2\2\2\u013e\u013f\7>\2\2\u013f\u0140\7?\2\2\u0140")
        buf.write("P\3\2\2\2\u0141\u0142\7<\2\2\u0142\u0143\7<\2\2\u0143")
        buf.write("R\3\2\2\2\u0144\u0145\7\60\2\2\u0145T\3\2\2\2\u0146\u0147")
        buf.write("\7.\2\2\u0147V\3\2\2\2\u0148\u0149\7=\2\2\u0149X\3\2\2")
        buf.write("\2\u014a\u014b\7<\2\2\u014bZ\3\2\2\2\u014c\u014d\7*\2")
        buf.write("\2\u014d\\\3\2\2\2\u014e\u014f\7+\2\2\u014f^\3\2\2\2\u0150")
        buf.write("\u0151\7]\2\2\u0151`\3\2\2\2\u0152\u0153\7_\2\2\u0153")
        buf.write("b\3\2\2\2\u0154\u0155\7}\2\2\u0155d\3\2\2\2\u0156\u0157")
        buf.write("\7\177\2\2\u0157f\3\2\2\2\u0158\u0159\7?\2\2\u0159h\3")
        buf.write("\2\2\2\u015a\u0164\7\62\2\2\u015b\u015f\t\4\2\2\u015c")
        buf.write("\u015e\t\5\2\2\u015d\u015c\3\2\2\2\u015e\u0161\3\2\2\2")
        buf.write("\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0162\3")
        buf.write("\2\2\2\u0161\u015f\3\2\2\2\u0162\u0164\b\65\2\2\u0163")
        buf.write("\u015a\3\2\2\2\u0163\u015b\3\2\2\2\u0164j\3\2\2\2\u0165")
        buf.write("\u0167\5i\65\2\u0166\u0168\5m\67\2\u0167\u0166\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168\u016a\3\2\2\2\u0169\u016b\5")
        buf.write("o8\2\u016a\u0169\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c")
        buf.write("\3\2\2\2\u016c\u016d\b\66\3\2\u016dl\3\2\2\2\u016e\u0172")
        buf.write("\7\60\2\2\u016f\u0171\t\6\2\2\u0170\u016f\3\2\2\2\u0171")
        buf.write("\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173n\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0177\t\7\2")
        buf.write("\2\u0176\u0178\t\b\2\2\u0177\u0176\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u0178\u017a\3\2\2\2\u0179\u017b\t\6\2\2\u017a")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017dp\3\2\2\2\u017e\u0181\5\33\16")
        buf.write("\2\u017f\u0181\5\35\17\2\u0180\u017e\3\2\2\2\u0180\u017f")
        buf.write("\3\2\2\2\u0181r\3\2\2\2\u0182\u0183\7$\2\2\u0183t\3\2")
        buf.write("\2\2\u0184\u0185\n\t\2\2\u0185v\3\2\2\2\u0186\u018c\7")
        buf.write("$\2\2\u0187\u0188\7^\2\2\u0188\u018b\5s:\2\u0189\u018b")
        buf.write("\5u;\2\u018a\u0187\3\2\2\2\u018a\u0189\3\2\2\2\u018b\u018e")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("\u018f\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\7$\2\2")
        buf.write("\u0190\u0191\b<\4\2\u0191\u0192\b<\5\2\u0192x\3\2\2\2")
        buf.write("\u0193\u0194\5c\62\2\u0194\u0195\7p\2\2\u0195\u0196\7")
        buf.write("q\2\2\u0196\u0197\7p\2\2\u0197\u0198\7g\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199\u019a\5e\63\2\u019az\3\2\2\2\u019b\u019d")
        buf.write("\t\n\2\2\u019c\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0\u01a1\b>\6\2\u01a1|\3\2\2\2\u01a2\u01a3\13\2\2")
        buf.write("\2\u01a3\u01a4\b?\7\2\u01a4~\3\2\2\2\u01a5\u01a6\13\2")
        buf.write("\2\2\u01a6\u01a7\b@\b\2\u01a7\u0080\3\2\2\2\u01a8\u01a9")
        buf.write("\13\2\2\2\u01a9\u01aa\bA\t\2\u01aa\u0082\3\2\2\2\21\2")
        buf.write("\u008e\u0097\u011c\u015f\u0163\u0167\u016a\u0172\u0177")
        buf.write("\u017c\u0180\u018a\u018c\u019e\n\3\65\2\3\66\3\3<\4\3")
        buf.write("<\5\b\2\2\3?\6\3@\7\3A\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
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
    WS = 57
    ERROR_CHAR = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'expr'", "'void'", "'auto'", "'integer'", "'float'", "'boolean'", 
            "'string'", "'array'", "'inherit'", "'function'", "'true'", 
            "'false'", "'for'", "'while'", "'do'", "'break'", "'continue'", 
            "'return'", "'if'", "'else'", "'of'", "'out'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'>'", "'>='", "'<'", "'<='", "'::'", "'.'", "','", "';'", "':'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", "KWFLOAT", 
            "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", "KWTRUE", 
            "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", "KWCONT", "KWRTN", 
            "KWIF", "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", "MULOP", 
            "DIVOP", "MODOP", "EXC", "ANDOP", "OROP", "EQLOP", "DIFOP", 
            "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", "DOT", 
            "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "EQL", 
            "LITINT", "LITFLOAT", "LITBOO", "LITSTR", "LITARR", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", 
                  "KWINT", "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", 
                  "KWFUNC", "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", 
                  "KWBRK", "KWCONT", "KWRTN", "KWIF", "KWELSE", "KWOF", 
                  "KWOUT", "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                  "EXC", "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", 
                  "SMALLOP", "SEQLOP", "CONCATOP", "DOT", "CM", "SM", "CL", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "EQL", "LITINT", 
                  "LITFLOAT", "Decimal", "Exponent", "LITBOO", "DoubleQuote", 
                  "InvDoubleQuote", "LITSTR", "LITARR", "WS", "ERROR_CHAR", 
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
            actions[51] = self.LITINT_action 
            actions[52] = self.LITFLOAT_action 
            actions[58] = self.LITSTR_action 
            actions[61] = self.ERROR_CHAR_action 
            actions[62] = self.UNCLOSE_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
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
     


