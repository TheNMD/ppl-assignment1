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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u021f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\6\2\u0091\n\2\r\2\16\2\u0092")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009b\n\3\f\3\16\3\u009e")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00a9\n")
        buf.write("\4\f\4\16\4\u00ac\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3$\3$\7$\u01a2\n$\f$\16$\u01a5\13$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.")
        buf.write("\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3?\7?\u01e5")
        buf.write("\n?\f?\16?\u01e8\13?\3?\5?\u01eb\n?\3@\3@\5@\u01ef\n@")
        buf.write("\3@\5@\u01f2\n@\3@\3@\3A\3A\7A\u01f8\nA\fA\16A\u01fb\13")
        buf.write("A\3B\3B\5B\u01ff\nB\3B\6B\u0202\nB\rB\16B\u0203\3C\3C")
        buf.write("\5C\u0208\nC\3D\3D\3D\3D\7D\u020e\nD\fD\16D\u0211\13D")
        buf.write("\3D\3D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3\u009c\2H\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("=y>{?}@\177A\u0081\2\u0083\2\u0085B\u0087C\u0089D\u008b")
        buf.write("E\u008dF\3\2\r\5\2\n\f\16\17\"\"\4\2\f\f\17\17\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\3\2\63;\4\2\62;aa\3\2\62;\4\2GGgg")
        buf.write("\4\2--//\n\2$$))^^ddhhppttvv\7\2\n\f\16\17$$))^^\2\u022a")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\3\u0090\3\2\2\2\5\u0096\3\2\2\2\7\u00a4\3\2\2\2\t\u00af")
        buf.write("\3\2\2\2\13\u00b4\3\2\2\2\r\u00b9\3\2\2\2\17\u00c1\3\2")
        buf.write("\2\2\21\u00c7\3\2\2\2\23\u00cf\3\2\2\2\25\u00d6\3\2\2")
        buf.write("\2\27\u00dc\3\2\2\2\31\u00e4\3\2\2\2\33\u00ed\3\2\2\2")
        buf.write("\35\u00f2\3\2\2\2\37\u00f8\3\2\2\2!\u00fc\3\2\2\2#\u0102")
        buf.write("\3\2\2\2%\u0105\3\2\2\2\'\u010b\3\2\2\2)\u0114\3\2\2\2")
        buf.write("+\u011b\3\2\2\2-\u011e\3\2\2\2/\u0123\3\2\2\2\61\u0126")
        buf.write("\3\2\2\2\63\u012a\3\2\2\2\65\u0136\3\2\2\2\67\u0143\3")
        buf.write("\2\2\29\u014d\3\2\2\2;\u0158\3\2\2\2=\u0164\3\2\2\2?\u0171")
        buf.write("\3\2\2\2A\u017c\3\2\2\2C\u0188\3\2\2\2E\u018e\3\2\2\2")
        buf.write("G\u019f\3\2\2\2I\u01a6\3\2\2\2K\u01a8\3\2\2\2M\u01aa\3")
        buf.write("\2\2\2O\u01ac\3\2\2\2Q\u01ae\3\2\2\2S\u01b0\3\2\2\2U\u01b2")
        buf.write("\3\2\2\2W\u01b5\3\2\2\2Y\u01b8\3\2\2\2[\u01bb\3\2\2\2")
        buf.write("]\u01be\3\2\2\2_\u01c0\3\2\2\2a\u01c3\3\2\2\2c\u01c5\3")
        buf.write("\2\2\2e\u01c8\3\2\2\2g\u01cb\3\2\2\2i\u01cd\3\2\2\2k\u01cf")
        buf.write("\3\2\2\2m\u01d1\3\2\2\2o\u01d3\3\2\2\2q\u01d5\3\2\2\2")
        buf.write("s\u01d7\3\2\2\2u\u01d9\3\2\2\2w\u01db\3\2\2\2y\u01dd\3")
        buf.write("\2\2\2{\u01df\3\2\2\2}\u01ea\3\2\2\2\177\u01ec\3\2\2\2")
        buf.write("\u0081\u01f5\3\2\2\2\u0083\u01fc\3\2\2\2\u0085\u0207\3")
        buf.write("\2\2\2\u0087\u0209\3\2\2\2\u0089\u0216\3\2\2\2\u008b\u0219")
        buf.write("\3\2\2\2\u008d\u021c\3\2\2\2\u008f\u0091\t\2\2\2\u0090")
        buf.write("\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\b")
        buf.write("\2\2\2\u0095\4\3\2\2\2\u0096\u0097\7\61\2\2\u0097\u0098")
        buf.write("\7,\2\2\u0098\u009c\3\2\2\2\u0099\u009b\13\2\2\2\u009a")
        buf.write("\u0099\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009c\u009a\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009c\3")
        buf.write("\2\2\2\u009f\u00a0\7,\2\2\u00a0\u00a1\7\61\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a3\b\3\2\2\u00a3\6\3\2\2\2\u00a4\u00a5")
        buf.write("\7\61\2\2\u00a5\u00a6\7\61\2\2\u00a6\u00aa\3\2\2\2\u00a7")
        buf.write("\u00a9\n\3\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2")
        buf.write("\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\3")
        buf.write("\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\b\4\2\2\u00ae\b")
        buf.write("\3\2\2\2\u00af\u00b0\7x\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2")
        buf.write("\7k\2\2\u00b2\u00b3\7f\2\2\u00b3\n\3\2\2\2\u00b4\u00b5")
        buf.write("\7c\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\f\3\2\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb")
        buf.write("\7p\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be")
        buf.write("\7i\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7t\2\2\u00c0\16")
        buf.write("\3\2\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7v\2\2\u00c6\20")
        buf.write("\3\2\2\2\u00c7\u00c8\7d\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7q\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd")
        buf.write("\7c\2\2\u00cd\u00ce\7p\2\2\u00ce\22\3\2\2\2\u00cf\u00d0")
        buf.write("\7u\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7i\2\2\u00d5\24")
        buf.write("\3\2\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7{\2\2\u00db\26")
        buf.write("\3\2\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df")
        buf.write("\7j\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2")
        buf.write("\7k\2\2\u00e2\u00e3\7v\2\2\u00e3\30\3\2\2\2\u00e4\u00e5")
        buf.write("\7h\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7e\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7p\2\2\u00ec\32\3\2\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0\7w\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\34\3\2\2\2\u00f2\u00f3\7h\2\2\u00f3\u00f4")
        buf.write("\7c\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6\7u\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7\36\3\2\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa")
        buf.write("\7q\2\2\u00fa\u00fb\7t\2\2\u00fb \3\2\2\2\u00fc\u00fd")
        buf.write("\7y\2\2\u00fd\u00fe\7j\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7n\2\2\u0100\u0101\7g\2\2\u0101\"\3\2\2\2\u0102\u0103")
        buf.write("\7f\2\2\u0103\u0104\7q\2\2\u0104$\3\2\2\2\u0105\u0106")
        buf.write("\7d\2\2\u0106\u0107\7t\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7c\2\2\u0109\u010a\7m\2\2\u010a&\3\2\2\2\u010b\u010c")
        buf.write("\7e\2\2\u010c\u010d\7q\2\2\u010d\u010e\7p\2\2\u010e\u010f")
        buf.write("\7v\2\2\u010f\u0110\7k\2\2\u0110\u0111\7p\2\2\u0111\u0112")
        buf.write("\7w\2\2\u0112\u0113\7g\2\2\u0113(\3\2\2\2\u0114\u0115")
        buf.write("\7t\2\2\u0115\u0116\7g\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7w\2\2\u0118\u0119\7t\2\2\u0119\u011a\7p\2\2\u011a*\3")
        buf.write("\2\2\2\u011b\u011c\7k\2\2\u011c\u011d\7h\2\2\u011d,\3")
        buf.write("\2\2\2\u011e\u011f\7g\2\2\u011f\u0120\7n\2\2\u0120\u0121")
        buf.write("\7u\2\2\u0121\u0122\7g\2\2\u0122.\3\2\2\2\u0123\u0124")
        buf.write("\7q\2\2\u0124\u0125\7h\2\2\u0125\60\3\2\2\2\u0126\u0127")
        buf.write("\7q\2\2\u0127\u0128\7w\2\2\u0128\u0129\7v\2\2\u0129\62")
        buf.write("\3\2\2\2\u012a\u012b\7t\2\2\u012b\u012c\7g\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7f\2\2\u012e\u012f\7K\2\2\u012f\u0130")
        buf.write("\7p\2\2\u0130\u0131\7v\2\2\u0131\u0132\7g\2\2\u0132\u0133")
        buf.write("\7i\2\2\u0133\u0134\7g\2\2\u0134\u0135\7t\2\2\u0135\64")
        buf.write("\3\2\2\2\u0136\u0137\7r\2\2\u0137\u0138\7t\2\2\u0138\u0139")
        buf.write("\7k\2\2\u0139\u013a\7p\2\2\u013a\u013b\7v\2\2\u013b\u013c")
        buf.write("\7K\2\2\u013c\u013d\7p\2\2\u013d\u013e\7v\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7i\2\2\u0140\u0141\7g\2\2\u0141\u0142")
        buf.write("\7t\2\2\u0142\66\3\2\2\2\u0143\u0144\7t\2\2\u0144\u0145")
        buf.write("\7g\2\2\u0145\u0146\7c\2\2\u0146\u0147\7f\2\2\u0147\u0148")
        buf.write("\7H\2\2\u0148\u0149\7n\2\2\u0149\u014a\7q\2\2\u014a\u014b")
        buf.write("\7c\2\2\u014b\u014c\7v\2\2\u014c8\3\2\2\2\u014d\u014e")
        buf.write("\7y\2\2\u014e\u014f\7t\2\2\u014f\u0150\7k\2\2\u0150\u0151")
        buf.write("\7v\2\2\u0151\u0152\7g\2\2\u0152\u0153\7H\2\2\u0153\u0154")
        buf.write("\7n\2\2\u0154\u0155\7q\2\2\u0155\u0156\7c\2\2\u0156\u0157")
        buf.write("\7v\2\2\u0157:\3\2\2\2\u0158\u0159\7t\2\2\u0159\u015a")
        buf.write("\7g\2\2\u015a\u015b\7c\2\2\u015b\u015c\7f\2\2\u015c\u015d")
        buf.write("\7D\2\2\u015d\u015e\7q\2\2\u015e\u015f\7q\2\2\u015f\u0160")
        buf.write("\7n\2\2\u0160\u0161\7g\2\2\u0161\u0162\7c\2\2\u0162\u0163")
        buf.write("\7p\2\2\u0163<\3\2\2\2\u0164\u0165\7r\2\2\u0165\u0166")
        buf.write("\7t\2\2\u0166\u0167\7k\2\2\u0167\u0168\7p\2\2\u0168\u0169")
        buf.write("\7v\2\2\u0169\u016a\7D\2\2\u016a\u016b\7q\2\2\u016b\u016c")
        buf.write("\7q\2\2\u016c\u016d\7n\2\2\u016d\u016e\7g\2\2\u016e\u016f")
        buf.write("\7c\2\2\u016f\u0170\7p\2\2\u0170>\3\2\2\2\u0171\u0172")
        buf.write("\7t\2\2\u0172\u0173\7g\2\2\u0173\u0174\7c\2\2\u0174\u0175")
        buf.write("\7f\2\2\u0175\u0176\7U\2\2\u0176\u0177\7v\2\2\u0177\u0178")
        buf.write("\7t\2\2\u0178\u0179\7k\2\2\u0179\u017a\7p\2\2\u017a\u017b")
        buf.write("\7i\2\2\u017b@\3\2\2\2\u017c\u017d\7r\2\2\u017d\u017e")
        buf.write("\7t\2\2\u017e\u017f\7k\2\2\u017f\u0180\7p\2\2\u0180\u0181")
        buf.write("\7v\2\2\u0181\u0182\7U\2\2\u0182\u0183\7v\2\2\u0183\u0184")
        buf.write("\7t\2\2\u0184\u0185\7k\2\2\u0185\u0186\7p\2\2\u0186\u0187")
        buf.write("\7i\2\2\u0187B\3\2\2\2\u0188\u0189\7u\2\2\u0189\u018a")
        buf.write("\7w\2\2\u018a\u018b\7r\2\2\u018b\u018c\7g\2\2\u018c\u018d")
        buf.write("\7t\2\2\u018dD\3\2\2\2\u018e\u018f\7r\2\2\u018f\u0190")
        buf.write("\7t\2\2\u0190\u0191\7g\2\2\u0191\u0192\7x\2\2\u0192\u0193")
        buf.write("\7g\2\2\u0193\u0194\7p\2\2\u0194\u0195\7v\2\2\u0195\u0196")
        buf.write("\7F\2\2\u0196\u0197\7g\2\2\u0197\u0198\7h\2\2\u0198\u0199")
        buf.write("\7c\2\2\u0199\u019a\7w\2\2\u019a\u019b\7n\2\2\u019b\u019c")
        buf.write("\7v\2\2\u019c\u019d\7*\2\2\u019d\u019e\7+\2\2\u019eF\3")
        buf.write("\2\2\2\u019f\u01a3\t\4\2\2\u01a0\u01a2\t\5\2\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4H\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6")
        buf.write("\u01a7\7-\2\2\u01a7J\3\2\2\2\u01a8\u01a9\7/\2\2\u01a9")
        buf.write("L\3\2\2\2\u01aa\u01ab\7,\2\2\u01abN\3\2\2\2\u01ac\u01ad")
        buf.write("\7\61\2\2\u01adP\3\2\2\2\u01ae\u01af\7\'\2\2\u01afR\3")
        buf.write("\2\2\2\u01b0\u01b1\7#\2\2\u01b1T\3\2\2\2\u01b2\u01b3\7")
        buf.write("(\2\2\u01b3\u01b4\7(\2\2\u01b4V\3\2\2\2\u01b5\u01b6\7")
        buf.write("~\2\2\u01b6\u01b7\7~\2\2\u01b7X\3\2\2\2\u01b8\u01b9\7")
        buf.write("?\2\2\u01b9\u01ba\7?\2\2\u01baZ\3\2\2\2\u01bb\u01bc\7")
        buf.write("#\2\2\u01bc\u01bd\7?\2\2\u01bd\\\3\2\2\2\u01be\u01bf\7")
        buf.write("@\2\2\u01bf^\3\2\2\2\u01c0\u01c1\7@\2\2\u01c1\u01c2\7")
        buf.write("?\2\2\u01c2`\3\2\2\2\u01c3\u01c4\7>\2\2\u01c4b\3\2\2\2")
        buf.write("\u01c5\u01c6\7>\2\2\u01c6\u01c7\7?\2\2\u01c7d\3\2\2\2")
        buf.write("\u01c8\u01c9\7<\2\2\u01c9\u01ca\7<\2\2\u01caf\3\2\2\2")
        buf.write("\u01cb\u01cc\7\60\2\2\u01cch\3\2\2\2\u01cd\u01ce\7.\2")
        buf.write("\2\u01cej\3\2\2\2\u01cf\u01d0\7=\2\2\u01d0l\3\2\2\2\u01d1")
        buf.write("\u01d2\7<\2\2\u01d2n\3\2\2\2\u01d3\u01d4\7*\2\2\u01d4")
        buf.write("p\3\2\2\2\u01d5\u01d6\7+\2\2\u01d6r\3\2\2\2\u01d7\u01d8")
        buf.write("\7]\2\2\u01d8t\3\2\2\2\u01d9\u01da\7_\2\2\u01dav\3\2\2")
        buf.write("\2\u01db\u01dc\7}\2\2\u01dcx\3\2\2\2\u01dd\u01de\7\177")
        buf.write("\2\2\u01dez\3\2\2\2\u01df\u01e0\7?\2\2\u01e0|\3\2\2\2")
        buf.write("\u01e1\u01eb\7\62\2\2\u01e2\u01e6\t\6\2\2\u01e3\u01e5")
        buf.write("\t\7\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6")
        buf.write("\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e9\3\2\2\2")
        buf.write("\u01e8\u01e6\3\2\2\2\u01e9\u01eb\b?\3\2\u01ea\u01e1\3")
        buf.write("\2\2\2\u01ea\u01e2\3\2\2\2\u01eb~\3\2\2\2\u01ec\u01ee")
        buf.write("\5}?\2\u01ed\u01ef\5\u0081A\2\u01ee\u01ed\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01f2\5\u0083")
        buf.write("B\2\u01f1\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3")
        buf.write("\3\2\2\2\u01f3\u01f4\b@\4\2\u01f4\u0080\3\2\2\2\u01f5")
        buf.write("\u01f9\7\60\2\2\u01f6\u01f8\t\b\2\2\u01f7\u01f6\3\2\2")
        buf.write("\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa")
        buf.write("\3\2\2\2\u01fa\u0082\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc")
        buf.write("\u01fe\t\t\2\2\u01fd\u01ff\t\n\2\2\u01fe\u01fd\3\2\2\2")
        buf.write("\u01fe\u01ff\3\2\2\2\u01ff\u0201\3\2\2\2\u0200\u0202\t")
        buf.write("\b\2\2\u0201\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0084\3\2\2\2\u0205")
        buf.write("\u0208\5\33\16\2\u0206\u0208\5\35\17\2\u0207\u0205\3\2")
        buf.write("\2\2\u0207\u0206\3\2\2\2\u0208\u0086\3\2\2\2\u0209\u020f")
        buf.write("\7$\2\2\u020a\u020b\7^\2\2\u020b\u020e\t\13\2\2\u020c")
        buf.write("\u020e\n\f\2\2\u020d\u020a\3\2\2\2\u020d\u020c\3\2\2\2")
        buf.write("\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3")
        buf.write("\2\2\2\u0210\u0212\3\2\2\2\u0211\u020f\3\2\2\2\u0212\u0213")
        buf.write("\7$\2\2\u0213\u0214\bD\5\2\u0214\u0215\bD\6\2\u0215\u0088")
        buf.write("\3\2\2\2\u0216\u0217\13\2\2\2\u0217\u0218\bE\7\2\u0218")
        buf.write("\u008a\3\2\2\2\u0219\u021a\13\2\2\2\u021a\u021b\bF\b\2")
        buf.write("\u021b\u008c\3\2\2\2\u021c\u021d\13\2\2\2\u021d\u021e")
        buf.write("\bG\t\2\u021e\u008e\3\2\2\2\21\2\u0092\u009c\u00aa\u01a3")
        buf.write("\u01e6\u01ea\u01ee\u01f1\u01f9\u01fe\u0203\u0207\u020d")
        buf.write("\u020f\n\b\2\2\3?\2\3@\3\3D\4\3D\5\3E\6\3F\7\3G\b")
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
    SFREADINT = 25
    SFPRINTINT = 26
    SFREADFLOAT = 27
    SFPRINTFLOAT = 28
    SFREADBOOL = 29
    SFPRINTBOOL = 30
    SFREADSTR = 31
    SFPRINTSTR = 32
    SFSUPER = 33
    SFPREVENT = 34
    ID = 35
    ADDOP = 36
    SUBOP = 37
    MULOP = 38
    DIVOP = 39
    MODOP = 40
    EXCOP = 41
    ANDOP = 42
    OROP = 43
    EQLOP = 44
    DIFOP = 45
    LARGEOP = 46
    LEQLOP = 47
    SMALLOP = 48
    SEQLOP = 49
    CONCATOP = 50
    DOT = 51
    CM = 52
    SM = 53
    CL = 54
    LB = 55
    RB = 56
    LSB = 57
    RSB = 58
    LCB = 59
    RCB = 60
    EQL = 61
    LITINT = 62
    LITFLOAT = 63
    LITBOO = 64
    LITSTR = 65
    ERROR_CHAR = 66
    NCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void'", "'auto'", "'integer'", "'float'", "'boolean'", "'string'", 
            "'array'", "'inherit'", "'function'", "'true'", "'false'", "'for'", 
            "'while'", "'do'", "'break'", "'continue'", "'return'", "'if'", 
            "'else'", "'of'", "'out'", "'readInteger'", "'printInteger'", 
            "'readFloat'", "'writeFloat'", "'readBoolean'", "'printBoolean'", 
            "'readString'", "'printString'", "'super'", "'preventDefault()'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'>'", "'>='", "'<'", "'<='", "'::'", "'.'", "','", 
            "';'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
            "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
            "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", "KWCONT", 
            "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", "SFREADINT", "SFPRINTINT", 
            "SFREADFLOAT", "SFPRINTFLOAT", "SFREADBOOL", "SFPRINTBOOL", 
            "SFREADSTR", "SFPRINTSTR", "SFSUPER", "SFPREVENT", "ID", "ADDOP", 
            "SUBOP", "MULOP", "DIVOP", "MODOP", "EXCOP", "ANDOP", "OROP", 
            "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", 
            "CONCATOP", "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", 
            "LCB", "RCB", "EQL", "LITINT", "LITFLOAT", "LITBOO", "LITSTR", 
            "ERROR_CHAR", "NCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
                  "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
                  "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", 
                  "KWCONT", "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", 
                  "SFREADINT", "SFPRINTINT", "SFREADFLOAT", "SFPRINTFLOAT", 
                  "SFREADBOOL", "SFPRINTBOOL", "SFREADSTR", "SFPRINTSTR", 
                  "SFSUPER", "SFPREVENT", "ID", "ADDOP", "SUBOP", "MULOP", 
                  "DIVOP", "MODOP", "EXCOP", "ANDOP", "OROP", "EQLOP", "DIFOP", 
                  "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", 
                  "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", 
                  "RCB", "EQL", "LITINT", "LITFLOAT", "Decimal", "Exponent", 
                  "LITBOO", "LITSTR", "ERROR_CHAR", "NCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[61] = self.LITINT_action 
            actions[62] = self.LITFLOAT_action 
            actions[66] = self.LITSTR_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.NCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
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
     


