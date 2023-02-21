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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u0196\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\6\2}\n\2\r\2\16\2~\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\7\3\u0087\n\3\f\3\16\3\u008a\13\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u0095\n\4\f\4\16\4\u0098")
        buf.write("\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\7\32\u0119\n")
        buf.write("\32\f\32\16\32\u011c\13\32\3\33\3\33\3\34\3\34\3\35\3")
        buf.write("\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)")
        buf.write("\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\7\65")
        buf.write("\u015c\n\65\f\65\16\65\u015f\13\65\3\65\5\65\u0162\n\65")
        buf.write("\3\66\3\66\5\66\u0166\n\66\3\66\5\66\u0169\n\66\3\66\3")
        buf.write("\66\3\67\3\67\7\67\u016f\n\67\f\67\16\67\u0172\13\67\3")
        buf.write("8\38\58\u0176\n8\38\68\u0179\n8\r8\168\u017a\39\39\59")
        buf.write("\u017f\n9\3:\3:\3:\3:\7:\u0185\n:\f:\16:\u0188\13:\3:")
        buf.write("\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3\u0088\2>\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q8s9u:w;")
        buf.write("y<\3\2\r\5\2\n\f\16\17\"\"\4\2\f\f\17\17\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\3\2\63;\4\2\62;aa\3\2\62;\4\2GGgg\4\2--")
        buf.write("//\n\2$$))^^ddhhppttvv\7\2\n\f\16\17$$))^^\2\u01a1\2\3")
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
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u")
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\3|\3\2\2\2\5\u0082\3\2")
        buf.write("\2\2\7\u0090\3\2\2\2\t\u009b\3\2\2\2\13\u00a0\3\2\2\2")
        buf.write("\r\u00a5\3\2\2\2\17\u00ad\3\2\2\2\21\u00b3\3\2\2\2\23")
        buf.write("\u00bb\3\2\2\2\25\u00c2\3\2\2\2\27\u00c8\3\2\2\2\31\u00d0")
        buf.write("\3\2\2\2\33\u00d9\3\2\2\2\35\u00de\3\2\2\2\37\u00e4\3")
        buf.write("\2\2\2!\u00e8\3\2\2\2#\u00ee\3\2\2\2%\u00f1\3\2\2\2\'")
        buf.write("\u00f7\3\2\2\2)\u0100\3\2\2\2+\u0107\3\2\2\2-\u010a\3")
        buf.write("\2\2\2/\u010f\3\2\2\2\61\u0112\3\2\2\2\63\u0116\3\2\2")
        buf.write("\2\65\u011d\3\2\2\2\67\u011f\3\2\2\29\u0121\3\2\2\2;\u0123")
        buf.write("\3\2\2\2=\u0125\3\2\2\2?\u0127\3\2\2\2A\u0129\3\2\2\2")
        buf.write("C\u012c\3\2\2\2E\u012f\3\2\2\2G\u0132\3\2\2\2I\u0135\3")
        buf.write("\2\2\2K\u0137\3\2\2\2M\u013a\3\2\2\2O\u013c\3\2\2\2Q\u013f")
        buf.write("\3\2\2\2S\u0142\3\2\2\2U\u0144\3\2\2\2W\u0146\3\2\2\2")
        buf.write("Y\u0148\3\2\2\2[\u014a\3\2\2\2]\u014c\3\2\2\2_\u014e\3")
        buf.write("\2\2\2a\u0150\3\2\2\2c\u0152\3\2\2\2e\u0154\3\2\2\2g\u0156")
        buf.write("\3\2\2\2i\u0161\3\2\2\2k\u0163\3\2\2\2m\u016c\3\2\2\2")
        buf.write("o\u0173\3\2\2\2q\u017e\3\2\2\2s\u0180\3\2\2\2u\u018d\3")
        buf.write("\2\2\2w\u0190\3\2\2\2y\u0193\3\2\2\2{}\t\2\2\2|{\3\2\2")
        buf.write("\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2")
        buf.write("\u0080\u0081\b\2\2\2\u0081\4\3\2\2\2\u0082\u0083\7\61")
        buf.write("\2\2\u0083\u0084\7,\2\2\u0084\u0088\3\2\2\2\u0085\u0087")
        buf.write("\13\2\2\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088")
        buf.write("\u0089\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008b\3\2\2\2")
        buf.write("\u008a\u0088\3\2\2\2\u008b\u008c\7,\2\2\u008c\u008d\7")
        buf.write("\61\2\2\u008d\u008e\3\2\2\2\u008e\u008f\b\3\2\2\u008f")
        buf.write("\6\3\2\2\2\u0090\u0091\7\61\2\2\u0091\u0092\7\61\2\2\u0092")
        buf.write("\u0096\3\2\2\2\u0093\u0095\n\3\2\2\u0094\u0093\3\2\2\2")
        buf.write("\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3")
        buf.write("\2\2\2\u0097\u0099\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009a")
        buf.write("\b\4\2\2\u009a\b\3\2\2\2\u009b\u009c\7x\2\2\u009c\u009d")
        buf.write("\7q\2\2\u009d\u009e\7k\2\2\u009e\u009f\7f\2\2\u009f\n")
        buf.write("\3\2\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3")
        buf.write("\7v\2\2\u00a3\u00a4\7q\2\2\u00a4\f\3\2\2\2\u00a5\u00a6")
        buf.write("\7k\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9")
        buf.write("\7g\2\2\u00a9\u00aa\7i\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\16\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af")
        buf.write("\7n\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\20\3\2\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7p\2\2\u00ba\22")
        buf.write("\3\2\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7i\2\2\u00c1\24\3\2\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7")
        buf.write("\7{\2\2\u00c7\26\3\2\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7j\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7v\2\2\u00cf\30")
        buf.write("\3\2\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7e\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7p\2\2\u00d8\32")
        buf.write("\3\2\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7t\2\2\u00db\u00dc")
        buf.write("\7w\2\2\u00dc\u00dd\7g\2\2\u00dd\34\3\2\2\2\u00de\u00df")
        buf.write("\7h\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2")
        buf.write("\7u\2\2\u00e2\u00e3\7g\2\2\u00e3\36\3\2\2\2\u00e4\u00e5")
        buf.write("\7h\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7t\2\2\u00e7 \3")
        buf.write("\2\2\2\u00e8\u00e9\7y\2\2\u00e9\u00ea\7j\2\2\u00ea\u00eb")
        buf.write("\7k\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed\7g\2\2\u00ed\"")
        buf.write("\3\2\2\2\u00ee\u00ef\7f\2\2\u00ef\u00f0\7q\2\2\u00f0$")
        buf.write("\3\2\2\2\u00f1\u00f2\7d\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7m\2\2\u00f6&\3")
        buf.write("\2\2\2\u00f7\u00f8\7e\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7g\2\2\u00ff(\3")
        buf.write("\2\2\2\u0100\u0101\7t\2\2\u0101\u0102\7g\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\u0104\7w\2\2\u0104\u0105\7t\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106*\3\2\2\2\u0107\u0108\7k\2\2\u0108\u0109")
        buf.write("\7h\2\2\u0109,\3\2\2\2\u010a\u010b\7g\2\2\u010b\u010c")
        buf.write("\7n\2\2\u010c\u010d\7u\2\2\u010d\u010e\7g\2\2\u010e.\3")
        buf.write("\2\2\2\u010f\u0110\7q\2\2\u0110\u0111\7h\2\2\u0111\60")
        buf.write("\3\2\2\2\u0112\u0113\7q\2\2\u0113\u0114\7w\2\2\u0114\u0115")
        buf.write("\7v\2\2\u0115\62\3\2\2\2\u0116\u011a\t\4\2\2\u0117\u0119")
        buf.write("\t\5\2\2\u0118\u0117\3\2\2\2\u0119\u011c\3\2\2\2\u011a")
        buf.write("\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b\64\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011d\u011e\7-\2\2\u011e\66\3\2\2\2\u011f")
        buf.write("\u0120\7/\2\2\u01208\3\2\2\2\u0121\u0122\7,\2\2\u0122")
        buf.write(":\3\2\2\2\u0123\u0124\7\61\2\2\u0124<\3\2\2\2\u0125\u0126")
        buf.write("\7\'\2\2\u0126>\3\2\2\2\u0127\u0128\7#\2\2\u0128@\3\2")
        buf.write("\2\2\u0129\u012a\7(\2\2\u012a\u012b\7(\2\2\u012bB\3\2")
        buf.write("\2\2\u012c\u012d\7~\2\2\u012d\u012e\7~\2\2\u012eD\3\2")
        buf.write("\2\2\u012f\u0130\7?\2\2\u0130\u0131\7?\2\2\u0131F\3\2")
        buf.write("\2\2\u0132\u0133\7#\2\2\u0133\u0134\7?\2\2\u0134H\3\2")
        buf.write("\2\2\u0135\u0136\7@\2\2\u0136J\3\2\2\2\u0137\u0138\7@")
        buf.write("\2\2\u0138\u0139\7?\2\2\u0139L\3\2\2\2\u013a\u013b\7>")
        buf.write("\2\2\u013bN\3\2\2\2\u013c\u013d\7>\2\2\u013d\u013e\7?")
        buf.write("\2\2\u013eP\3\2\2\2\u013f\u0140\7<\2\2\u0140\u0141\7<")
        buf.write("\2\2\u0141R\3\2\2\2\u0142\u0143\7\60\2\2\u0143T\3\2\2")
        buf.write("\2\u0144\u0145\7.\2\2\u0145V\3\2\2\2\u0146\u0147\7=\2")
        buf.write("\2\u0147X\3\2\2\2\u0148\u0149\7<\2\2\u0149Z\3\2\2\2\u014a")
        buf.write("\u014b\7*\2\2\u014b\\\3\2\2\2\u014c\u014d\7+\2\2\u014d")
        buf.write("^\3\2\2\2\u014e\u014f\7]\2\2\u014f`\3\2\2\2\u0150\u0151")
        buf.write("\7_\2\2\u0151b\3\2\2\2\u0152\u0153\7}\2\2\u0153d\3\2\2")
        buf.write("\2\u0154\u0155\7\177\2\2\u0155f\3\2\2\2\u0156\u0157\7")
        buf.write("?\2\2\u0157h\3\2\2\2\u0158\u0162\7\62\2\2\u0159\u015d")
        buf.write("\t\6\2\2\u015a\u015c\t\7\2\2\u015b\u015a\3\2\2\2\u015c")
        buf.write("\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u0160\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0162\b")
        buf.write("\65\3\2\u0161\u0158\3\2\2\2\u0161\u0159\3\2\2\2\u0162")
        buf.write("j\3\2\2\2\u0163\u0165\5i\65\2\u0164\u0166\5m\67\2\u0165")
        buf.write("\u0164\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0168\3\2\2\2")
        buf.write("\u0167\u0169\5o8\2\u0168\u0167\3\2\2\2\u0168\u0169\3\2")
        buf.write("\2\2\u0169\u016a\3\2\2\2\u016a\u016b\b\66\4\2\u016bl\3")
        buf.write("\2\2\2\u016c\u0170\7\60\2\2\u016d\u016f\t\b\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171n\3\2\2\2\u0172\u0170\3\2\2")
        buf.write("\2\u0173\u0175\t\t\2\2\u0174\u0176\t\n\2\2\u0175\u0174")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0178\3\2\2\2\u0177")
        buf.write("\u0179\t\b\2\2\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017bp\3\2\2")
        buf.write("\2\u017c\u017f\5\33\16\2\u017d\u017f\5\35\17\2\u017e\u017c")
        buf.write("\3\2\2\2\u017e\u017d\3\2\2\2\u017fr\3\2\2\2\u0180\u0186")
        buf.write("\7$\2\2\u0181\u0182\7^\2\2\u0182\u0185\t\13\2\2\u0183")
        buf.write("\u0185\n\f\2\2\u0184\u0181\3\2\2\2\u0184\u0183\3\2\2\2")
        buf.write("\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3")
        buf.write("\2\2\2\u0187\u0189\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a")
        buf.write("\7$\2\2\u018a\u018b\b:\5\2\u018b\u018c\b:\6\2\u018ct\3")
        buf.write("\2\2\2\u018d\u018e\13\2\2\2\u018e\u018f\b;\7\2\u018fv")
        buf.write("\3\2\2\2\u0190\u0191\13\2\2\2\u0191\u0192\b<\b\2\u0192")
        buf.write("x\3\2\2\2\u0193\u0194\13\2\2\2\u0194\u0195\b=\t\2\u0195")
        buf.write("z\3\2\2\2\21\2~\u0088\u0096\u011a\u015d\u0161\u0165\u0168")
        buf.write("\u0170\u0175\u017a\u017e\u0184\u0186\n\b\2\2\3\65\2\3")
        buf.write("\66\3\3:\4\3:\5\3;\6\3<\7\3=\b")
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
    ERROR_CHAR = 56
    NCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58

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
            "EQL", "LITINT", "LITFLOAT", "LITBOO", "LITSTR", "ERROR_CHAR", 
            "NCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
                  "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
                  "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", 
                  "KWCONT", "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", 
                  "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EXCOP", 
                  "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", 
                  "SMALLOP", "SEQLOP", "CONCATOP", "DOT", "CM", "SM", "CL", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "EQL", "LITINT", 
                  "LITFLOAT", "Decimal", "Exponent", "LITBOO", "LITSTR", 
                  "ERROR_CHAR", "NCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[57] = self.ERROR_CHAR_action 
            actions[58] = self.NCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
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
     

    def NCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


