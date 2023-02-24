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
studentName = "Nguyen Manh Dan";



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0230\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\6\f\u0106\n\f\r\f\16\f\u0107")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\7\r\u0110\n\r\f\r\16\r\u0113")
        buf.write("\13\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\7\16\u011e")
        buf.write("\n\16\f\16\16\16\u0121\13\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\7$\u01a2\n$\f$\16$\u01a5")
        buf.write("\13$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=")
        buf.write("\3=\3>\3>\3?\3?\3?\7?\u01e5\n?\f?\16?\u01e8\13?\3?\5?")
        buf.write("\u01eb\n?\3@\3@\5@\u01ef\n@\3@\5@\u01f2\n@\3@\3@\3A\3")
        buf.write("A\7A\u01f8\nA\fA\16A\u01fb\13A\3B\3B\5B\u01ff\nB\3B\6")
        buf.write("B\u0202\nB\rB\16B\u0203\3C\3C\5C\u0208\nC\3D\3D\7D\u020c")
        buf.write("\nD\fD\16D\u020f\13D\3D\3D\3D\3E\3E\3E\5E\u0217\nE\3F")
        buf.write("\3F\7F\u021b\nF\fF\16F\u021e\13F\3F\3F\3F\3F\3F\3G\3G")
        buf.write("\7G\u0227\nG\fG\16G\u022a\13G\3G\3G\3H\3H\3H\3\u0111\2")
        buf.write("I\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;")
        buf.write("u<w=y>{?}@\177A\u0081\2\u0083\2\u0085B\u0087C\u0089\2")
        buf.write("\u008bD\u008dE\u008fF\3\2\r\5\2\n\f\16\17\"\"\4\2\f\f")
        buf.write("\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\4\2\62;aa\3\2")
        buf.write("\62;\4\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\5\2\f\f$$^^\2")
        buf.write("\u023c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\3\u0091\3\2\2\2\5\u009d\3\2\2\2\7\u00aa\3\2\2")
        buf.write("\2\t\u00b4\3\2\2\2\13\u00bf\3\2\2\2\r\u00cb\3\2\2\2\17")
        buf.write("\u00d8\3\2\2\2\21\u00e3\3\2\2\2\23\u00ef\3\2\2\2\25\u00f5")
        buf.write("\3\2\2\2\27\u0105\3\2\2\2\31\u010b\3\2\2\2\33\u0119\3")
        buf.write("\2\2\2\35\u0124\3\2\2\2\37\u0129\3\2\2\2!\u012e\3\2\2")
        buf.write("\2#\u0136\3\2\2\2%\u013c\3\2\2\2\'\u0144\3\2\2\2)\u014b")
        buf.write("\3\2\2\2+\u0151\3\2\2\2-\u0159\3\2\2\2/\u0162\3\2\2\2")
        buf.write("\61\u0167\3\2\2\2\63\u016d\3\2\2\2\65\u0171\3\2\2\2\67")
        buf.write("\u0177\3\2\2\29\u017a\3\2\2\2;\u0180\3\2\2\2=\u0189\3")
        buf.write("\2\2\2?\u0190\3\2\2\2A\u0193\3\2\2\2C\u0198\3\2\2\2E\u019b")
        buf.write("\3\2\2\2G\u019f\3\2\2\2I\u01a6\3\2\2\2K\u01a8\3\2\2\2")
        buf.write("M\u01aa\3\2\2\2O\u01ac\3\2\2\2Q\u01ae\3\2\2\2S\u01b0\3")
        buf.write("\2\2\2U\u01b2\3\2\2\2W\u01b5\3\2\2\2Y\u01b8\3\2\2\2[\u01bb")
        buf.write("\3\2\2\2]\u01be\3\2\2\2_\u01c0\3\2\2\2a\u01c3\3\2\2\2")
        buf.write("c\u01c5\3\2\2\2e\u01c8\3\2\2\2g\u01cb\3\2\2\2i\u01cd\3")
        buf.write("\2\2\2k\u01cf\3\2\2\2m\u01d1\3\2\2\2o\u01d3\3\2\2\2q\u01d5")
        buf.write("\3\2\2\2s\u01d7\3\2\2\2u\u01d9\3\2\2\2w\u01db\3\2\2\2")
        buf.write("y\u01dd\3\2\2\2{\u01df\3\2\2\2}\u01ea\3\2\2\2\177\u01ec")
        buf.write("\3\2\2\2\u0081\u01f5\3\2\2\2\u0083\u01fc\3\2\2\2\u0085")
        buf.write("\u0207\3\2\2\2\u0087\u0209\3\2\2\2\u0089\u0216\3\2\2\2")
        buf.write("\u008b\u0218\3\2\2\2\u008d\u0224\3\2\2\2\u008f\u022d\3")
        buf.write("\2\2\2\u0091\u0092\7t\2\2\u0092\u0093\7g\2\2\u0093\u0094")
        buf.write("\7c\2\2\u0094\u0095\7f\2\2\u0095\u0096\7K\2\2\u0096\u0097")
        buf.write("\7p\2\2\u0097\u0098\7v\2\2\u0098\u0099\7g\2\2\u0099\u009a")
        buf.write("\7i\2\2\u009a\u009b\7g\2\2\u009b\u009c\7t\2\2\u009c\4")
        buf.write("\3\2\2\2\u009d\u009e\7r\2\2\u009e\u009f\7t\2\2\u009f\u00a0")
        buf.write("\7k\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3")
        buf.write("\7K\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6")
        buf.write("\7g\2\2\u00a6\u00a7\7i\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7t\2\2\u00a9\6\3\2\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7f\2\2\u00ae\u00af")
        buf.write("\7H\2\2\u00af\u00b0\7n\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2")
        buf.write("\7c\2\2\u00b2\u00b3\7v\2\2\u00b3\b\3\2\2\2\u00b4\u00b5")
        buf.write("\7y\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8")
        buf.write("\7v\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7H\2\2\u00ba\u00bb")
        buf.write("\7n\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\n\3\2\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7f\2\2\u00c3\u00c4")
        buf.write("\7D\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7")
        buf.write("\7n\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\f\3\2\2\2\u00cb\u00cc\7r\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\u00d1\7D\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3")
        buf.write("\7q\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6")
        buf.write("\7c\2\2\u00d6\u00d7\7p\2\2\u00d7\16\3\2\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7c\2\2\u00db\u00dc")
        buf.write("\7f\2\2\u00dc\u00dd\7U\2\2\u00dd\u00de\7v\2\2\u00de\u00df")
        buf.write("\7t\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2")
        buf.write("\7i\2\2\u00e2\20\3\2\2\2\u00e3\u00e4\7r\2\2\u00e4\u00e5")
        buf.write("\7t\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\u00e9\7U\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7t\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7i\2\2\u00ee\22\3\2\2\2\u00ef\u00f0\7u\2\2\u00f0\u00f1")
        buf.write("\7w\2\2\u00f1\u00f2\7r\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4\24\3\2\2\2\u00f5\u00f6\7r\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7x\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7F\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7h\2\2\u00ff\u0100")
        buf.write("\7c\2\2\u0100\u0101\7w\2\2\u0101\u0102\7n\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\26\3\2\2\2\u0104\u0106\t\2\2\2\u0105\u0104")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0105\3\2\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\b\f\2\2")
        buf.write("\u010a\30\3\2\2\2\u010b\u010c\7\61\2\2\u010c\u010d\7,")
        buf.write("\2\2\u010d\u0111\3\2\2\2\u010e\u0110\13\2\2\2\u010f\u010e")
        buf.write("\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u0112\3\2\2\2\u0111")
        buf.write("\u010f\3\2\2\2\u0112\u0114\3\2\2\2\u0113\u0111\3\2\2\2")
        buf.write("\u0114\u0115\7,\2\2\u0115\u0116\7\61\2\2\u0116\u0117\3")
        buf.write("\2\2\2\u0117\u0118\b\r\2\2\u0118\32\3\2\2\2\u0119\u011a")
        buf.write("\7\61\2\2\u011a\u011b\7\61\2\2\u011b\u011f\3\2\2\2\u011c")
        buf.write("\u011e\n\3\2\2\u011d\u011c\3\2\2\2\u011e\u0121\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122\3")
        buf.write("\2\2\2\u0121\u011f\3\2\2\2\u0122\u0123\b\16\2\2\u0123")
        buf.write("\34\3\2\2\2\u0124\u0125\7x\2\2\u0125\u0126\7q\2\2\u0126")
        buf.write("\u0127\7k\2\2\u0127\u0128\7f\2\2\u0128\36\3\2\2\2\u0129")
        buf.write("\u012a\7c\2\2\u012a\u012b\7w\2\2\u012b\u012c\7v\2\2\u012c")
        buf.write("\u012d\7q\2\2\u012d \3\2\2\2\u012e\u012f\7k\2\2\u012f")
        buf.write("\u0130\7p\2\2\u0130\u0131\7v\2\2\u0131\u0132\7g\2\2\u0132")
        buf.write("\u0133\7i\2\2\u0133\u0134\7g\2\2\u0134\u0135\7t\2\2\u0135")
        buf.write("\"\3\2\2\2\u0136\u0137\7h\2\2\u0137\u0138\7n\2\2\u0138")
        buf.write("\u0139\7q\2\2\u0139\u013a\7c\2\2\u013a\u013b\7v\2\2\u013b")
        buf.write("$\3\2\2\2\u013c\u013d\7d\2\2\u013d\u013e\7q\2\2\u013e")
        buf.write("\u013f\7q\2\2\u013f\u0140\7n\2\2\u0140\u0141\7g\2\2\u0141")
        buf.write("\u0142\7c\2\2\u0142\u0143\7p\2\2\u0143&\3\2\2\2\u0144")
        buf.write("\u0145\7u\2\2\u0145\u0146\7v\2\2\u0146\u0147\7t\2\2\u0147")
        buf.write("\u0148\7k\2\2\u0148\u0149\7p\2\2\u0149\u014a\7i\2\2\u014a")
        buf.write("(\3\2\2\2\u014b\u014c\7c\2\2\u014c\u014d\7t\2\2\u014d")
        buf.write("\u014e\7t\2\2\u014e\u014f\7c\2\2\u014f\u0150\7{\2\2\u0150")
        buf.write("*\3\2\2\2\u0151\u0152\7k\2\2\u0152\u0153\7p\2\2\u0153")
        buf.write("\u0154\7j\2\2\u0154\u0155\7g\2\2\u0155\u0156\7t\2\2\u0156")
        buf.write("\u0157\7k\2\2\u0157\u0158\7v\2\2\u0158,\3\2\2\2\u0159")
        buf.write("\u015a\7h\2\2\u015a\u015b\7w\2\2\u015b\u015c\7p\2\2\u015c")
        buf.write("\u015d\7e\2\2\u015d\u015e\7v\2\2\u015e\u015f\7k\2\2\u015f")
        buf.write("\u0160\7q\2\2\u0160\u0161\7p\2\2\u0161.\3\2\2\2\u0162")
        buf.write("\u0163\7v\2\2\u0163\u0164\7t\2\2\u0164\u0165\7w\2\2\u0165")
        buf.write("\u0166\7g\2\2\u0166\60\3\2\2\2\u0167\u0168\7h\2\2\u0168")
        buf.write("\u0169\7c\2\2\u0169\u016a\7n\2\2\u016a\u016b\7u\2\2\u016b")
        buf.write("\u016c\7g\2\2\u016c\62\3\2\2\2\u016d\u016e\7h\2\2\u016e")
        buf.write("\u016f\7q\2\2\u016f\u0170\7t\2\2\u0170\64\3\2\2\2\u0171")
        buf.write("\u0172\7y\2\2\u0172\u0173\7j\2\2\u0173\u0174\7k\2\2\u0174")
        buf.write("\u0175\7n\2\2\u0175\u0176\7g\2\2\u0176\66\3\2\2\2\u0177")
        buf.write("\u0178\7f\2\2\u0178\u0179\7q\2\2\u01798\3\2\2\2\u017a")
        buf.write("\u017b\7d\2\2\u017b\u017c\7t\2\2\u017c\u017d\7g\2\2\u017d")
        buf.write("\u017e\7c\2\2\u017e\u017f\7m\2\2\u017f:\3\2\2\2\u0180")
        buf.write("\u0181\7e\2\2\u0181\u0182\7q\2\2\u0182\u0183\7p\2\2\u0183")
        buf.write("\u0184\7v\2\2\u0184\u0185\7k\2\2\u0185\u0186\7p\2\2\u0186")
        buf.write("\u0187\7w\2\2\u0187\u0188\7g\2\2\u0188<\3\2\2\2\u0189")
        buf.write("\u018a\7t\2\2\u018a\u018b\7g\2\2\u018b\u018c\7v\2\2\u018c")
        buf.write("\u018d\7w\2\2\u018d\u018e\7t\2\2\u018e\u018f\7p\2\2\u018f")
        buf.write(">\3\2\2\2\u0190\u0191\7k\2\2\u0191\u0192\7h\2\2\u0192")
        buf.write("@\3\2\2\2\u0193\u0194\7g\2\2\u0194\u0195\7n\2\2\u0195")
        buf.write("\u0196\7u\2\2\u0196\u0197\7g\2\2\u0197B\3\2\2\2\u0198")
        buf.write("\u0199\7q\2\2\u0199\u019a\7h\2\2\u019aD\3\2\2\2\u019b")
        buf.write("\u019c\7q\2\2\u019c\u019d\7w\2\2\u019d\u019e\7v\2\2\u019e")
        buf.write("F\3\2\2\2\u019f\u01a3\t\4\2\2\u01a0\u01a2\t\5\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4H\3\2\2\2\u01a5\u01a3\3\2\2")
        buf.write("\2\u01a6\u01a7\7-\2\2\u01a7J\3\2\2\2\u01a8\u01a9\7/\2")
        buf.write("\2\u01a9L\3\2\2\2\u01aa\u01ab\7,\2\2\u01abN\3\2\2\2\u01ac")
        buf.write("\u01ad\7\61\2\2\u01adP\3\2\2\2\u01ae\u01af\7\'\2\2\u01af")
        buf.write("R\3\2\2\2\u01b0\u01b1\7#\2\2\u01b1T\3\2\2\2\u01b2\u01b3")
        buf.write("\7(\2\2\u01b3\u01b4\7(\2\2\u01b4V\3\2\2\2\u01b5\u01b6")
        buf.write("\7~\2\2\u01b6\u01b7\7~\2\2\u01b7X\3\2\2\2\u01b8\u01b9")
        buf.write("\7?\2\2\u01b9\u01ba\7?\2\2\u01baZ\3\2\2\2\u01bb\u01bc")
        buf.write("\7#\2\2\u01bc\u01bd\7?\2\2\u01bd\\\3\2\2\2\u01be\u01bf")
        buf.write("\7@\2\2\u01bf^\3\2\2\2\u01c0\u01c1\7@\2\2\u01c1\u01c2")
        buf.write("\7?\2\2\u01c2`\3\2\2\2\u01c3\u01c4\7>\2\2\u01c4b\3\2\2")
        buf.write("\2\u01c5\u01c6\7>\2\2\u01c6\u01c7\7?\2\2\u01c7d\3\2\2")
        buf.write("\2\u01c8\u01c9\7<\2\2\u01c9\u01ca\7<\2\2\u01caf\3\2\2")
        buf.write("\2\u01cb\u01cc\7\60\2\2\u01cch\3\2\2\2\u01cd\u01ce\7.")
        buf.write("\2\2\u01cej\3\2\2\2\u01cf\u01d0\7=\2\2\u01d0l\3\2\2\2")
        buf.write("\u01d1\u01d2\7<\2\2\u01d2n\3\2\2\2\u01d3\u01d4\7*\2\2")
        buf.write("\u01d4p\3\2\2\2\u01d5\u01d6\7+\2\2\u01d6r\3\2\2\2\u01d7")
        buf.write("\u01d8\7]\2\2\u01d8t\3\2\2\2\u01d9\u01da\7_\2\2\u01da")
        buf.write("v\3\2\2\2\u01db\u01dc\7}\2\2\u01dcx\3\2\2\2\u01dd\u01de")
        buf.write("\7\177\2\2\u01dez\3\2\2\2\u01df\u01e0\7?\2\2\u01e0|\3")
        buf.write("\2\2\2\u01e1\u01eb\7\62\2\2\u01e2\u01e6\t\6\2\2\u01e3")
        buf.write("\u01e5\t\7\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e8\3\2\2\2")
        buf.write("\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e9\3")
        buf.write("\2\2\2\u01e8\u01e6\3\2\2\2\u01e9\u01eb\b?\3\2\u01ea\u01e1")
        buf.write("\3\2\2\2\u01ea\u01e2\3\2\2\2\u01eb~\3\2\2\2\u01ec\u01ee")
        buf.write("\5}?\2\u01ed\u01ef\5\u0081A\2\u01ee\u01ed\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01f2\5\u0083")
        buf.write("B\2\u01f1\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3")
        buf.write("\3\2\2\2\u01f3\u01f4\b@\4\2\u01f4\u0080\3\2\2\2\u01f5")
        buf.write("\u01f9\5g\64\2\u01f6\u01f8\t\b\2\2\u01f7\u01f6\3\2\2\2")
        buf.write("\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3")
        buf.write("\2\2\2\u01fa\u0082\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u01fe")
        buf.write("\t\t\2\2\u01fd\u01ff\t\n\2\2\u01fe\u01fd\3\2\2\2\u01fe")
        buf.write("\u01ff\3\2\2\2\u01ff\u0201\3\2\2\2\u0200\u0202\t\b\2\2")
        buf.write("\u0201\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0201\3")
        buf.write("\2\2\2\u0203\u0204\3\2\2\2\u0204\u0084\3\2\2\2\u0205\u0208")
        buf.write("\5/\30\2\u0206\u0208\5\61\31\2\u0207\u0205\3\2\2\2\u0207")
        buf.write("\u0206\3\2\2\2\u0208\u0086\3\2\2\2\u0209\u020d\7$\2\2")
        buf.write("\u020a\u020c\5\u0089E\2\u020b\u020a\3\2\2\2\u020c\u020f")
        buf.write("\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e")
        buf.write("\u0210\3\2\2\2\u020f\u020d\3\2\2\2\u0210\u0211\7$\2\2")
        buf.write("\u0211\u0212\bD\5\2\u0212\u0088\3\2\2\2\u0213\u0214\7")
        buf.write("^\2\2\u0214\u0217\t\13\2\2\u0215\u0217\n\f\2\2\u0216\u0213")
        buf.write("\3\2\2\2\u0216\u0215\3\2\2\2\u0217\u008a\3\2\2\2\u0218")
        buf.write("\u021c\7$\2\2\u0219\u021b\5\u0089E\2\u021a\u0219\3\2\2")
        buf.write("\2\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d")
        buf.write("\3\2\2\2\u021d\u021f\3\2\2\2\u021e\u021c\3\2\2\2\u021f")
        buf.write("\u0220\7^\2\2\u0220\u0221\n\13\2\2\u0221\u0222\3\2\2\2")
        buf.write("\u0222\u0223\bF\6\2\u0223\u008c\3\2\2\2\u0224\u0228\7")
        buf.write("$\2\2\u0225\u0227\5\u0089E\2\u0226\u0225\3\2\2\2\u0227")
        buf.write("\u022a\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2")
        buf.write("\u0229\u022b\3\2\2\2\u022a\u0228\3\2\2\2\u022b\u022c\b")
        buf.write("G\7\2\u022c\u008e\3\2\2\2\u022d\u022e\13\2\2\2\u022e\u022f")
        buf.write("\bH\b\2\u022f\u0090\3\2\2\2\23\2\u0107\u0111\u011f\u01a3")
        buf.write("\u01e6\u01ea\u01ee\u01f1\u01f9\u01fe\u0203\u0207\u020d")
        buf.write("\u0216\u021c\u0228\t\b\2\2\3?\2\3@\3\3D\4\3F\5\3G\6\3")
        buf.write("H\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    WS = 11
    CCOMMENT = 12
    CPPCOMMENT = 13
    KWVOID = 14
    KWAUTO = 15
    KWINT = 16
    KWFLOAT = 17
    KWBOO = 18
    KWSTR = 19
    KWARR = 20
    KWINHERIT = 21
    KWFUNC = 22
    KWTRUE = 23
    KWFALSE = 24
    KWFOR = 25
    KWWHILE = 26
    KWDO = 27
    KWBRK = 28
    KWCONT = 29
    KWRTN = 30
    KWIF = 31
    KWELSE = 32
    KWOF = 33
    KWOUT = 34
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
    ILLEGAL_ESCAPE = 66
    UNCLOSED_STRING = 67
    ERROR_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'void'", "'auto'", "'integer'", 
            "'float'", "'boolean'", "'string'", "'array'", "'inherit'", 
            "'function'", "'true'", "'false'", "'for'", "'while'", "'do'", 
            "'break'", "'continue'", "'return'", "'if'", "'else'", "'of'", 
            "'out'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'::'", "'.'", 
            "','", "';'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", "KWAUTO", "KWINT", 
            "KWFLOAT", "KWBOO", "KWSTR", "KWARR", "KWINHERIT", "KWFUNC", 
            "KWTRUE", "KWFALSE", "KWFOR", "KWWHILE", "KWDO", "KWBRK", "KWCONT", 
            "KWRTN", "KWIF", "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", 
            "MULOP", "DIVOP", "MODOP", "EXCOP", "ANDOP", "OROP", "EQLOP", 
            "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", 
            "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
            "EQL", "LITINT", "LITFLOAT", "LITBOO", "LITSTR", "ILLEGAL_ESCAPE", 
            "UNCLOSED_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "WS", "CCOMMENT", "CPPCOMMENT", 
                  "KWVOID", "KWAUTO", "KWINT", "KWFLOAT", "KWBOO", "KWSTR", 
                  "KWARR", "KWINHERIT", "KWFUNC", "KWTRUE", "KWFALSE", "KWFOR", 
                  "KWWHILE", "KWDO", "KWBRK", "KWCONT", "KWRTN", "KWIF", 
                  "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", "SUBOP", "MULOP", 
                  "DIVOP", "MODOP", "EXCOP", "ANDOP", "OROP", "EQLOP", "DIFOP", 
                  "LARGEOP", "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", 
                  "DOT", "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", 
                  "RCB", "EQL", "LITINT", "LITFLOAT", "Decimal", "Exponent", 
                  "LITBOO", "LITSTR", "Char", "ILLEGAL_ESCAPE", "UNCLOSED_STRING", 
                  "ERROR_CHAR" ]

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
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.UNCLOSED_STRING_action 
            actions[70] = self.ERROR_CHAR_action 
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
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


