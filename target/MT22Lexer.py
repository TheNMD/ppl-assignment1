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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u0190\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\u0080\n\3\r")
        buf.write("\3\16\3\u0081\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u008a\n\4\f")
        buf.write("\4\16\4\u008d\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\7\5\u0098\n\5\f\5\16\5\u009b\13\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\7\33\u011c\n\33\f\33\16\33\u011f")
        buf.write("\13\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.")
        buf.write("\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\66\7\66\u015f\n\66\f\66\16")
        buf.write("\66\u0162\13\66\3\66\5\66\u0165\n\66\3\67\3\67\5\67\u0169")
        buf.write("\n\67\3\67\5\67\u016c\n\67\3\67\3\67\38\38\78\u0172\n")
        buf.write("8\f8\168\u0175\138\39\39\59\u0179\n9\39\69\u017c\n9\r")
        buf.write("9\169\u017d\3:\3:\5:\u0182\n:\3;\3;\3;\3;\7;\u0188\n;")
        buf.write("\f;\16;\u018b\13;\3;\3;\3;\3;\3\u008b\2<\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o\2q\2s9u:\3\2\r\5\2\n\f")
        buf.write("\16\17\"\"\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2")
        buf.write("\63;\4\2\62;aa\3\2\62;\4\2GGgg\4\2--//\n\2$$))^^ddhhp")
        buf.write("pttvv\7\2\n\f\16\17$$))^^\2\u019b\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\3w\3\2\2\2")
        buf.write("\5\177\3\2\2\2\7\u0085\3\2\2\2\t\u0093\3\2\2\2\13\u009e")
        buf.write("\3\2\2\2\r\u00a3\3\2\2\2\17\u00a8\3\2\2\2\21\u00b0\3\2")
        buf.write("\2\2\23\u00b6\3\2\2\2\25\u00be\3\2\2\2\27\u00c5\3\2\2")
        buf.write("\2\31\u00cb\3\2\2\2\33\u00d3\3\2\2\2\35\u00dc\3\2\2\2")
        buf.write("\37\u00e1\3\2\2\2!\u00e7\3\2\2\2#\u00eb\3\2\2\2%\u00f1")
        buf.write("\3\2\2\2\'\u00f4\3\2\2\2)\u00fa\3\2\2\2+\u0103\3\2\2\2")
        buf.write("-\u010a\3\2\2\2/\u010d\3\2\2\2\61\u0112\3\2\2\2\63\u0115")
        buf.write("\3\2\2\2\65\u0119\3\2\2\2\67\u0120\3\2\2\29\u0122\3\2")
        buf.write("\2\2;\u0124\3\2\2\2=\u0126\3\2\2\2?\u0128\3\2\2\2A\u012a")
        buf.write("\3\2\2\2C\u012c\3\2\2\2E\u012f\3\2\2\2G\u0132\3\2\2\2")
        buf.write("I\u0135\3\2\2\2K\u0138\3\2\2\2M\u013a\3\2\2\2O\u013d\3")
        buf.write("\2\2\2Q\u013f\3\2\2\2S\u0142\3\2\2\2U\u0145\3\2\2\2W\u0147")
        buf.write("\3\2\2\2Y\u0149\3\2\2\2[\u014b\3\2\2\2]\u014d\3\2\2\2")
        buf.write("_\u014f\3\2\2\2a\u0151\3\2\2\2c\u0153\3\2\2\2e\u0155\3")
        buf.write("\2\2\2g\u0157\3\2\2\2i\u0159\3\2\2\2k\u0164\3\2\2\2m\u0166")
        buf.write("\3\2\2\2o\u016f\3\2\2\2q\u0176\3\2\2\2s\u0181\3\2\2\2")
        buf.write("u\u0183\3\2\2\2wx\7k\2\2xy\7h\2\2yz\7u\2\2z{\7v\2\2{|")
        buf.write("\7o\2\2|}\7v\2\2}\4\3\2\2\2~\u0080\t\2\2\2\177~\3\2\2")
        buf.write("\2\u0080\u0081\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3")
        buf.write("\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\b\3\2\2\u0084\6")
        buf.write("\3\2\2\2\u0085\u0086\7\61\2\2\u0086\u0087\7,\2\2\u0087")
        buf.write("\u008b\3\2\2\2\u0088\u008a\13\2\2\2\u0089\u0088\3\2\2")
        buf.write("\2\u008a\u008d\3\2\2\2\u008b\u008c\3\2\2\2\u008b\u0089")
        buf.write("\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e")
        buf.write("\u008f\7,\2\2\u008f\u0090\7\61\2\2\u0090\u0091\3\2\2\2")
        buf.write("\u0091\u0092\b\4\2\2\u0092\b\3\2\2\2\u0093\u0094\7\61")
        buf.write("\2\2\u0094\u0095\7\61\2\2\u0095\u0099\3\2\2\2\u0096\u0098")
        buf.write("\n\3\2\2\u0097\u0096\3\2\2\2\u0098\u009b\3\2\2\2\u0099")
        buf.write("\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009c\u009d\b\5\2\2\u009d\n\3\2\2")
        buf.write("\2\u009e\u009f\7x\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1\7")
        buf.write("k\2\2\u00a1\u00a2\7f\2\2\u00a2\f\3\2\2\2\u00a3\u00a4\7")
        buf.write("c\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7q\2\2\u00a7\16\3\2\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad")
        buf.write("\7i\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7t\2\2\u00af\20")
        buf.write("\3\2\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3")
        buf.write("\7q\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5\7v\2\2\u00b5\22")
        buf.write("\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc")
        buf.write("\7c\2\2\u00bc\u00bd\7p\2\2\u00bd\24\3\2\2\2\u00be\u00bf")
        buf.write("\7u\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2")
        buf.write("\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7i\2\2\u00c4\26")
        buf.write("\3\2\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7{\2\2\u00ca\30")
        buf.write("\3\2\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce")
        buf.write("\7j\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1")
        buf.write("\7k\2\2\u00d1\u00d2\7v\2\2\u00d2\32\3\2\2\2\u00d3\u00d4")
        buf.write("\7h\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7")
        buf.write("\7e\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da")
        buf.write("\7q\2\2\u00da\u00db\7p\2\2\u00db\34\3\2\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7w\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0\36\3\2\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3")
        buf.write("\7c\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5\7u\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6 \3\2\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7t\2\2\u00ea\"\3\2\2\2\u00eb\u00ec")
        buf.write("\7y\2\2\u00ec\u00ed\7j\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef")
        buf.write("\7n\2\2\u00ef\u00f0\7g\2\2\u00f0$\3\2\2\2\u00f1\u00f2")
        buf.write("\7f\2\2\u00f2\u00f3\7q\2\2\u00f3&\3\2\2\2\u00f4\u00f5")
        buf.write("\7d\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8")
        buf.write("\7c\2\2\u00f8\u00f9\7m\2\2\u00f9(\3\2\2\2\u00fa\u00fb")
        buf.write("\7e\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe")
        buf.write("\7v\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101")
        buf.write("\7w\2\2\u0101\u0102\7g\2\2\u0102*\3\2\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\u0105\7g\2\2\u0105\u0106\7v\2\2\u0106\u0107")
        buf.write("\7w\2\2\u0107\u0108\7t\2\2\u0108\u0109\7p\2\2\u0109,\3")
        buf.write("\2\2\2\u010a\u010b\7k\2\2\u010b\u010c\7h\2\2\u010c.\3")
        buf.write("\2\2\2\u010d\u010e\7g\2\2\u010e\u010f\7n\2\2\u010f\u0110")
        buf.write("\7u\2\2\u0110\u0111\7g\2\2\u0111\60\3\2\2\2\u0112\u0113")
        buf.write("\7q\2\2\u0113\u0114\7h\2\2\u0114\62\3\2\2\2\u0115\u0116")
        buf.write("\7q\2\2\u0116\u0117\7w\2\2\u0117\u0118\7v\2\2\u0118\64")
        buf.write("\3\2\2\2\u0119\u011d\t\4\2\2\u011a\u011c\t\5\2\2\u011b")
        buf.write("\u011a\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2")
        buf.write("\u011d\u011e\3\2\2\2\u011e\66\3\2\2\2\u011f\u011d\3\2")
        buf.write("\2\2\u0120\u0121\7-\2\2\u01218\3\2\2\2\u0122\u0123\7/")
        buf.write("\2\2\u0123:\3\2\2\2\u0124\u0125\7,\2\2\u0125<\3\2\2\2")
        buf.write("\u0126\u0127\7\61\2\2\u0127>\3\2\2\2\u0128\u0129\7\'\2")
        buf.write("\2\u0129@\3\2\2\2\u012a\u012b\7#\2\2\u012bB\3\2\2\2\u012c")
        buf.write("\u012d\7(\2\2\u012d\u012e\7(\2\2\u012eD\3\2\2\2\u012f")
        buf.write("\u0130\7~\2\2\u0130\u0131\7~\2\2\u0131F\3\2\2\2\u0132")
        buf.write("\u0133\7?\2\2\u0133\u0134\7?\2\2\u0134H\3\2\2\2\u0135")
        buf.write("\u0136\7#\2\2\u0136\u0137\7?\2\2\u0137J\3\2\2\2\u0138")
        buf.write("\u0139\7@\2\2\u0139L\3\2\2\2\u013a\u013b\7@\2\2\u013b")
        buf.write("\u013c\7?\2\2\u013cN\3\2\2\2\u013d\u013e\7>\2\2\u013e")
        buf.write("P\3\2\2\2\u013f\u0140\7>\2\2\u0140\u0141\7?\2\2\u0141")
        buf.write("R\3\2\2\2\u0142\u0143\7<\2\2\u0143\u0144\7<\2\2\u0144")
        buf.write("T\3\2\2\2\u0145\u0146\7\60\2\2\u0146V\3\2\2\2\u0147\u0148")
        buf.write("\7.\2\2\u0148X\3\2\2\2\u0149\u014a\7=\2\2\u014aZ\3\2\2")
        buf.write("\2\u014b\u014c\7<\2\2\u014c\\\3\2\2\2\u014d\u014e\7*\2")
        buf.write("\2\u014e^\3\2\2\2\u014f\u0150\7+\2\2\u0150`\3\2\2\2\u0151")
        buf.write("\u0152\7]\2\2\u0152b\3\2\2\2\u0153\u0154\7_\2\2\u0154")
        buf.write("d\3\2\2\2\u0155\u0156\7}\2\2\u0156f\3\2\2\2\u0157\u0158")
        buf.write("\7\177\2\2\u0158h\3\2\2\2\u0159\u015a\7?\2\2\u015aj\3")
        buf.write("\2\2\2\u015b\u0165\7\62\2\2\u015c\u0160\t\6\2\2\u015d")
        buf.write("\u015f\t\7\2\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2")
        buf.write("\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0163\3")
        buf.write("\2\2\2\u0162\u0160\3\2\2\2\u0163\u0165\b\66\3\2\u0164")
        buf.write("\u015b\3\2\2\2\u0164\u015c\3\2\2\2\u0165l\3\2\2\2\u0166")
        buf.write("\u0168\5k\66\2\u0167\u0169\5o8\2\u0168\u0167\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a\u016c\5q9\2\u016b")
        buf.write("\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016d\u016e\b\67\4\2\u016en\3\2\2\2\u016f\u0173\7\60")
        buf.write("\2\2\u0170\u0172\t\b\2\2\u0171\u0170\3\2\2\2\u0172\u0175")
        buf.write("\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("p\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0178\t\t\2\2\u0177")
        buf.write("\u0179\t\n\2\2\u0178\u0177\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\u017b\3\2\2\2\u017a\u017c\t\b\2\2\u017b\u017a\3")
        buf.write("\2\2\2\u017c\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017er\3\2\2\2\u017f\u0182\5\35\17\2\u0180\u0182")
        buf.write("\5\37\20\2\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("t\3\2\2\2\u0183\u0189\7$\2\2\u0184\u0185\7^\2\2\u0185")
        buf.write("\u0188\t\13\2\2\u0186\u0188\n\f\2\2\u0187\u0184\3\2\2")
        buf.write("\2\u0187\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018c\u018d\7$\2\2\u018d\u018e\b;\5\2\u018e")
        buf.write("\u018f\b;\6\2\u018fv\3\2\2\2\21\2\u0081\u008b\u0099\u011d")
        buf.write("\u0160\u0164\u0168\u016b\u0173\u0178\u017d\u0181\u0187")
        buf.write("\u0189\7\b\2\2\3\66\2\3\67\3\3;\4\3;\5")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WS = 2
    CCOMMENT = 3
    CPPCOMMENT = 4
    KWVOID = 5
    KWAUTO = 6
    KWINT = 7
    KWFLOAT = 8
    KWBOO = 9
    KWSTR = 10
    KWARR = 11
    KWINHERIT = 12
    KWFUNC = 13
    KWTRUE = 14
    KWFALSE = 15
    KWFOR = 16
    KWWHILE = 17
    KWDO = 18
    KWBRK = 19
    KWCONT = 20
    KWRTN = 21
    KWIF = 22
    KWELSE = 23
    KWOF = 24
    KWOUT = 25
    ID = 26
    ADDOP = 27
    SUBOP = 28
    MULOP = 29
    DIVOP = 30
    MODOP = 31
    EXCOP = 32
    ANDOP = 33
    OROP = 34
    EQLOP = 35
    DIFOP = 36
    LARGEOP = 37
    LEQLOP = 38
    SMALLOP = 39
    SEQLOP = 40
    CONCATOP = 41
    DOT = 42
    CM = 43
    SM = 44
    CL = 45
    LB = 46
    RB = 47
    LSB = 48
    RSB = 49
    LCB = 50
    RCB = 51
    EQL = 52
    LITINT = 53
    LITFLOAT = 54
    LITBOO = 55
    LITSTR = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'ifstmt'", "'void'", "'auto'", "'integer'", "'float'", "'boolean'", 
            "'string'", "'array'", "'inherit'", "'function'", "'true'", 
            "'false'", "'for'", "'while'", "'do'", "'break'", "'continue'", 
            "'return'", "'if'", "'else'", "'of'", "'out'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'>'", "'>='", "'<'", "'<='", "'::'", "'.'", "','", "';'", "':'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
            "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
            "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", "KWCONT", 
            "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", 
            "MULOP", "DIVOP", "MODOP", "EXCOP", "ANDOP", "OROP", "EQLOP", 
            "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", 
            "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
            "EQL", "LITINT", "LITFLOAT", "LITBOO", "LITSTR" ]

    ruleNames = [ "T__0", "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", 
                  "KWINT", "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", 
                  "KWFUNC", "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", 
                  "KWBRK", "KWCONT", "KWRTN", "KWIF", "KWELSE", "KWOF", 
                  "KWOUT", "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                  "EXCOP", "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", 
                  "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", "DOT", "CM", 
                  "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "EQL", 
                  "LITINT", "LITFLOAT", "Decimal", "Exponent", "LITBOO", 
                  "LITSTR" ]

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
            actions[52] = self.LITINT_action 
            actions[53] = self.LITFLOAT_action 
            actions[57] = self.LITSTR_action 
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
     


