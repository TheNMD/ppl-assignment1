# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u017f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3^\n\3\3\4\3\4\5\4b\n\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5i\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\5\5w\n\5\3\5\3\5\5\5{\n\5\3\6\3\6\3\6\5\6\u0080\n")
        buf.write("\6\3\7\3\7\3\7\3\7\5\7\u0086\n\7\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u0090\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u0097")
        buf.write("\n\n\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u009f\n\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u00a6\n\r\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00b5\n\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00bf\n\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u00c6\n\21\3\22\5\22\u00c9")
        buf.write("\n\22\3\22\5\22\u00cc\n\22\3\22\3\22\3\22\3\22\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\5\24\u00d8\n\24\3\25\3\25\5\25")
        buf.write("\u00dc\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5")
        buf.write("\26\u00e6\n\26\3\27\3\27\3\27\5\27\u00eb\n\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u00f5\n\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u00fc\n\31\3\32\3\32\5\32\u0100")
        buf.write("\n\32\3\33\3\33\3\33\5\33\u0105\n\33\3\34\3\34\3\34\5")
        buf.write("\34\u010a\n\34\3\35\3\35\3\35\3\35\3\35\7\35\u0111\n\35")
        buf.write("\f\35\16\35\u0114\13\35\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u011f\n\37\3 \3 \3 \3 \3 \5 \u0126")
        buf.write("\n \3!\3!\3!\3!\3!\3!\7!\u012e\n!\f!\16!\u0131\13!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\7\"\u0139\n\"\f\"\16\"\u013c\13\"")
        buf.write("\3#\3#\3#\3#\3#\3#\7#\u0144\n#\f#\16#\u0147\13#\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0159\n")
        buf.write("$\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\5)\u0171\n)\3)\3)\3*\3*\3*\3*\3*\3*")
        buf.write("\3+\3+\3+\3+\3+\2\68@BD,\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRT\2\b\3\2")
        buf.write("\b\f\3\2\7\f\3\2%*\3\2#$\3\2\35\36\3\2\37!\2\u0182\2V")
        buf.write("\3\2\2\2\4]\3\2\2\2\6a\3\2\2\2\bz\3\2\2\2\n\177\3\2\2")
        buf.write("\2\f\u0085\3\2\2\2\16\u0087\3\2\2\2\20\u008f\3\2\2\2\22")
        buf.write("\u0096\3\2\2\2\24\u0098\3\2\2\2\26\u009e\3\2\2\2\30\u00a5")
        buf.write("\3\2\2\2\32\u00a7\3\2\2\2\34\u00ab\3\2\2\2\36\u00be\3")
        buf.write("\2\2\2 \u00c5\3\2\2\2\"\u00c8\3\2\2\2$\u00d1\3\2\2\2&")
        buf.write("\u00d7\3\2\2\2(\u00db\3\2\2\2*\u00e5\3\2\2\2,\u00ea\3")
        buf.write("\2\2\2.\u00f4\3\2\2\2\60\u00fb\3\2\2\2\62\u00ff\3\2\2")
        buf.write("\2\64\u0104\3\2\2\2\66\u0109\3\2\2\28\u010b\3\2\2\2:\u0115")
        buf.write("\3\2\2\2<\u011e\3\2\2\2>\u0125\3\2\2\2@\u0127\3\2\2\2")
        buf.write("B\u0132\3\2\2\2D\u013d\3\2\2\2F\u0158\3\2\2\2H\u015a\3")
        buf.write("\2\2\2J\u015c\3\2\2\2L\u0168\3\2\2\2N\u016b\3\2\2\2P\u016e")
        buf.write("\3\2\2\2R\u0174\3\2\2\2T\u017a\3\2\2\2VW\5\4\3\2WX\7\2")
        buf.write("\2\3X\3\3\2\2\2YZ\5\6\4\2Z[\5\4\3\2[^\3\2\2\2\\^\5\6\4")
        buf.write("\2]Y\3\2\2\2]\\\3\2\2\2^\5\3\2\2\2_b\5\b\5\2`b\5\34\17")
        buf.write("\2a_\3\2\2\2a`\3\2\2\2b\7\3\2\2\2cd\5\n\6\2de\7/\2\2e")
        buf.write("h\5\16\b\2fg\7\66\2\2gi\5.\30\2hf\3\2\2\2hi\3\2\2\2ij")
        buf.write("\3\2\2\2jk\7.\2\2k{\3\2\2\2lm\5\n\6\2mn\7/\2\2no\7\r\2")
        buf.write("\2op\7\62\2\2pq\5\20\t\2qr\7\63\2\2rs\7\32\2\2sv\5\16")
        buf.write("\b\2tu\7\66\2\2uw\5\26\f\2vt\3\2\2\2vw\3\2\2\2wx\3\2\2")
        buf.write("\2xy\7.\2\2y{\3\2\2\2zc\3\2\2\2zl\3\2\2\2{\t\3\2\2\2|")
        buf.write("}\7\34\2\2}\u0080\5\f\7\2~\u0080\7\34\2\2\177|\3\2\2\2")
        buf.write("\177~\3\2\2\2\u0080\13\3\2\2\2\u0081\u0082\7-\2\2\u0082")
        buf.write("\u0083\7\34\2\2\u0083\u0086\5\f\7\2\u0084\u0086\3\2\2")
        buf.write("\2\u0085\u0081\3\2\2\2\u0085\u0084\3\2\2\2\u0086\r\3\2")
        buf.write("\2\2\u0087\u0088\t\2\2\2\u0088\17\3\2\2\2\u0089\u008a")
        buf.write("\5\24\13\2\u008a\u008b\5\22\n\2\u008b\u0090\3\2\2\2\u008c")
        buf.write("\u008d\5\24\13\2\u008d\u008e\b\t\1\2\u008e\u0090\3\2\2")
        buf.write("\2\u008f\u0089\3\2\2\2\u008f\u008c\3\2\2\2\u0090\21\3")
        buf.write("\2\2\2\u0091\u0092\7-\2\2\u0092\u0093\5\24\13\2\u0093")
        buf.write("\u0094\5\22\n\2\u0094\u0097\3\2\2\2\u0095\u0097\b\n\1")
        buf.write("\2\u0096\u0091\3\2\2\2\u0096\u0095\3\2\2\2\u0097\23\3")
        buf.write("\2\2\2\u0098\u0099\7\67\2\2\u0099\25\3\2\2\2\u009a\u009b")
        buf.write("\5\32\16\2\u009b\u009c\5\30\r\2\u009c\u009f\3\2\2\2\u009d")
        buf.write("\u009f\5\32\16\2\u009e\u009a\3\2\2\2\u009e\u009d\3\2\2")
        buf.write("\2\u009f\27\3\2\2\2\u00a0\u00a1\7-\2\2\u00a1\u00a2\5\32")
        buf.write("\16\2\u00a2\u00a3\5\30\r\2\u00a3\u00a6\3\2\2\2\u00a4\u00a6")
        buf.write("\3\2\2\2\u00a5\u00a0\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6")
        buf.write("\31\3\2\2\2\u00a7\u00a8\7\64\2\2\u00a8\u00a9\5.\30\2\u00a9")
        buf.write("\u00aa\7\65\2\2\u00aa\33\3\2\2\2\u00ab\u00ac\7\34\2\2")
        buf.write("\u00ac\u00ad\7/\2\2\u00ad\u00ae\7\17\2\2\u00ae\u00af\5")
        buf.write("$\23\2\u00af\u00b0\7\60\2\2\u00b0\u00b1\5\36\20\2\u00b1")
        buf.write("\u00b4\7\61\2\2\u00b2\u00b3\7\16\2\2\u00b3\u00b5\7\34")
        buf.write("\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6")
        buf.write("\3\2\2\2\u00b6\u00b7\7\64\2\2\u00b7\u00b8\5&\24\2\u00b8")
        buf.write("\u00b9\7\65\2\2\u00b9\35\3\2\2\2\u00ba\u00bb\5\"\22\2")
        buf.write("\u00bb\u00bc\5 \21\2\u00bc\u00bf\3\2\2\2\u00bd\u00bf\3")
        buf.write("\2\2\2\u00be\u00ba\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf\37")
        buf.write("\3\2\2\2\u00c0\u00c1\7-\2\2\u00c1\u00c2\5\"\22\2\u00c2")
        buf.write("\u00c3\5 \21\2\u00c3\u00c6\3\2\2\2\u00c4\u00c6\3\2\2\2")
        buf.write("\u00c5\u00c0\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6!\3\2\2")
        buf.write("\2\u00c7\u00c9\7\16\2\2\u00c8\u00c7\3\2\2\2\u00c8\u00c9")
        buf.write("\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00cc\7\33\2\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00ce\7\34\2\2\u00ce\u00cf\7/\2\2\u00cf\u00d0\5")
        buf.write("\16\b\2\u00d0#\3\2\2\2\u00d1\u00d2\t\3\2\2\u00d2%\3\2")
        buf.write("\2\2\u00d3\u00d4\5(\25\2\u00d4\u00d5\5&\24\2\u00d5\u00d8")
        buf.write("\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d3\3\2\2\2\u00d7")
        buf.write("\u00d6\3\2\2\2\u00d8\'\3\2\2\2\u00d9\u00dc\5\b\5\2\u00da")
        buf.write("\u00dc\5*\26\2\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2")
        buf.write("\u00dc)\3\2\2\2\u00dd\u00e6\5,\27\2\u00de\u00e6\5H%\2")
        buf.write("\u00df\u00e6\5J&\2\u00e0\u00e6\5L\'\2\u00e1\u00e6\5N(")
        buf.write("\2\u00e2\u00e6\5P)\2\u00e3\u00e6\5R*\2\u00e4\u00e6\5T")
        buf.write("+\2\u00e5\u00dd\3\2\2\2\u00e5\u00de\3\2\2\2\u00e5\u00df")
        buf.write("\3\2\2\2\u00e5\u00e0\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e5")
        buf.write("\u00e2\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e6+\3\2\2\2\u00e7\u00eb\7\34\2\2\u00e8\u00e9\7\34")
        buf.write("\2\2\u00e9\u00eb\5:\36\2\u00ea\u00e7\3\2\2\2\u00ea\u00e8")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\7\66\2\2\u00ed")
        buf.write("\u00ee\5\62\32\2\u00ee\u00ef\7.\2\2\u00ef-\3\2\2\2\u00f0")
        buf.write("\u00f1\5\62\32\2\u00f1\u00f2\5\60\31\2\u00f2\u00f5\3\2")
        buf.write("\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00f0\3\2\2\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f5/\3\2\2\2\u00f6\u00f7\7-\2\2\u00f7\u00f8")
        buf.write("\5\62\32\2\u00f8\u00f9\5\60\31\2\u00f9\u00fc\3\2\2\2\u00fa")
        buf.write("\u00fc\3\2\2\2\u00fb\u00f6\3\2\2\2\u00fb\u00fa\3\2\2\2")
        buf.write("\u00fc\61\3\2\2\2\u00fd\u0100\5\64\33\2\u00fe\u0100\5")
        buf.write("<\37\2\u00ff\u00fd\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100\63")
        buf.write("\3\2\2\2\u0101\u0102\7\"\2\2\u0102\u0105\5\64\33\2\u0103")
        buf.write("\u0105\5\66\34\2\u0104\u0101\3\2\2\2\u0104\u0103\3\2\2")
        buf.write("\2\u0105\65\3\2\2\2\u0106\u0107\7\36\2\2\u0107\u010a\5")
        buf.write("\66\34\2\u0108\u010a\58\35\2\u0109\u0106\3\2\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u010a\67\3\2\2\2\u010b\u010c\b\35\1\2\u010c")
        buf.write("\u010d\5F$\2\u010d\u0112\3\2\2\2\u010e\u010f\f\4\2\2\u010f")
        buf.write("\u0111\5:\36\2\u0110\u010e\3\2\2\2\u0111\u0114\3\2\2\2")
        buf.write("\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u01139\3\2\2")
        buf.write("\2\u0114\u0112\3\2\2\2\u0115\u0116\7\62\2\2\u0116\u0117")
        buf.write("\5\20\t\2\u0117\u0118\7\63\2\2\u0118;\3\2\2\2\u0119\u011a")
        buf.write("\5> \2\u011a\u011b\7+\2\2\u011b\u011c\5> \2\u011c\u011f")
        buf.write("\3\2\2\2\u011d\u011f\5> \2\u011e\u0119\3\2\2\2\u011e\u011d")
        buf.write("\3\2\2\2\u011f=\3\2\2\2\u0120\u0121\5@!\2\u0121\u0122")
        buf.write("\t\4\2\2\u0122\u0123\5@!\2\u0123\u0126\3\2\2\2\u0124\u0126")
        buf.write("\5@!\2\u0125\u0120\3\2\2\2\u0125\u0124\3\2\2\2\u0126?")
        buf.write("\3\2\2\2\u0127\u0128\b!\1\2\u0128\u0129\5B\"\2\u0129\u012f")
        buf.write("\3\2\2\2\u012a\u012b\f\4\2\2\u012b\u012c\t\5\2\2\u012c")
        buf.write("\u012e\5B\"\2\u012d\u012a\3\2\2\2\u012e\u0131\3\2\2\2")
        buf.write("\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130A\3\2\2")
        buf.write("\2\u0131\u012f\3\2\2\2\u0132\u0133\b\"\1\2\u0133\u0134")
        buf.write("\5D#\2\u0134\u013a\3\2\2\2\u0135\u0136\f\4\2\2\u0136\u0137")
        buf.write("\t\6\2\2\u0137\u0139\5D#\2\u0138\u0135\3\2\2\2\u0139\u013c")
        buf.write("\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("C\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013e\b#\1\2\u013e")
        buf.write("\u013f\5F$\2\u013f\u0145\3\2\2\2\u0140\u0141\f\4\2\2\u0141")
        buf.write("\u0142\t\7\2\2\u0142\u0144\5F$\2\u0143\u0140\3\2\2\2\u0144")
        buf.write("\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write("\u0146E\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0159\7\67\2")
        buf.write("\2\u0149\u0159\78\2\2\u014a\u0159\79\2\2\u014b\u0159\7")
        buf.write(":\2\2\u014c\u0159\7\34\2\2\u014d\u0159\5R*\2\u014e\u014f")
        buf.write("\7\60\2\2\u014f\u0150\5\62\32\2\u0150\u0151\7\61\2\2\u0151")
        buf.write("\u0159\3\2\2\2\u0152\u0153\7\34\2\2\u0153\u0159\5:\36")
        buf.write("\2\u0154\u0155\7\64\2\2\u0155\u0156\5.\30\2\u0156\u0157")
        buf.write("\7\65\2\2\u0157\u0159\3\2\2\2\u0158\u0148\3\2\2\2\u0158")
        buf.write("\u0149\3\2\2\2\u0158\u014a\3\2\2\2\u0158\u014b\3\2\2\2")
        buf.write("\u0158\u014c\3\2\2\2\u0158\u014d\3\2\2\2\u0158\u014e\3")
        buf.write("\2\2\2\u0158\u0152\3\2\2\2\u0158\u0154\3\2\2\2\u0159G")
        buf.write("\3\2\2\2\u015a\u015b\7\3\2\2\u015bI\3\2\2\2\u015c\u015d")
        buf.write("\7\22\2\2\u015d\u015e\7\60\2\2\u015e\u015f\7\34\2\2\u015f")
        buf.write("\u0160\7\66\2\2\u0160\u0161\5\62\32\2\u0161\u0162\7-\2")
        buf.write("\2\u0162\u0163\5\62\32\2\u0163\u0164\7-\2\2\u0164\u0165")
        buf.write("\5\62\32\2\u0165\u0166\7\61\2\2\u0166\u0167\5*\26\2\u0167")
        buf.write("K\3\2\2\2\u0168\u0169\7\25\2\2\u0169\u016a\7.\2\2\u016a")
        buf.write("M\3\2\2\2\u016b\u016c\7\26\2\2\u016c\u016d\7.\2\2\u016d")
        buf.write("O\3\2\2\2\u016e\u0170\7\27\2\2\u016f\u0171\5\62\32\2\u0170")
        buf.write("\u016f\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172\3\2\2\2")
        buf.write("\u0172\u0173\7.\2\2\u0173Q\3\2\2\2\u0174\u0175\7\34\2")
        buf.write("\2\u0175\u0176\7\60\2\2\u0176\u0177\5.\30\2\u0177\u0178")
        buf.write("\7\61\2\2\u0178\u0179\7.\2\2\u0179S\3\2\2\2\u017a\u017b")
        buf.write("\7\64\2\2\u017b\u017c\5&\24\2\u017c\u017d\7\65\2\2\u017d")
        buf.write("U\3\2\2\2#]ahvz\177\u0085\u008f\u0096\u009e\u00a5\u00b4")
        buf.write("\u00be\u00c5\u00c8\u00cb\u00d7\u00db\u00e5\u00ea\u00f4")
        buf.write("\u00fb\u00ff\u0104\u0109\u0112\u011e\u0125\u012f\u013a")
        buf.write("\u0145\u0158\u0170")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ifstmt'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'void'", "'auto'", "'integer'", "'float'", 
                     "'boolean'", "'string'", "'array'", "'inherit'", "'function'", 
                     "'true'", "'false'", "'for'", "'while'", "'do'", "'break'", 
                     "'continue'", "'return'", "'if'", "'else'", "'of'", 
                     "'out'", "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'>'", "'>='", 
                     "'<'", "'<='", "'::'", "'.'", "','", "';'", "':'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WS", "CCOMMENT", "CPPCOMMENT", 
                      "KWVOID", "KWAUTO", "KWINT", "KWFLOAT", "KWBOO", "KWSTR", 
                      "KWARR", "KWINHERIT", "KWFUNC", "KWTRUE", "KWFALSE", 
                      "KWFOR", "KWWHILE", "KWDO", "KWBRK", "KWCONT", "KWRTN", 
                      "KWIF", "KWELSE", "KWOF", "KWOUT", "ID", "ADDOP", 
                      "SUBOP", "MULOP", "DIVOP", "MODOP", "EXCOP", "ANDOP", 
                      "OROP", "EQLOP", "DIFOP", "LARGEOP", "LEQLOP", "SMALLOP", 
                      "SEQLOP", "CONCATOP", "DOT", "CM", "SM", "CL", "LB", 
                      "RB", "LSB", "RSB", "LCB", "RCB", "EQL", "LITINT", 
                      "LITFLOAT", "LITBOO", "LITSTR" ]

    RULE_program = 0
    RULE_declist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_idlist = 4
    RULE_ids = 5
    RULE_vartyp = 6
    RULE_idxlist = 7
    RULE_idxs = 8
    RULE_idx = 9
    RULE_arraylist = 10
    RULE_arrays = 11
    RULE_array = 12
    RULE_funcdecl = 13
    RULE_paralist = 14
    RULE_paras = 15
    RULE_para = 16
    RULE_functyp = 17
    RULE_bodylist = 18
    RULE_bodydecl = 19
    RULE_stmt = 20
    RULE_assignstmt = 21
    RULE_exprlist = 22
    RULE_exprs = 23
    RULE_expr = 24
    RULE_unexpr = 25
    RULE_unexpr1 = 26
    RULE_unexpr2 = 27
    RULE_idxop = 28
    RULE_biexpr = 29
    RULE_biexpr1 = 30
    RULE_biexpr2 = 31
    RULE_biexpr3 = 32
    RULE_biexpr4 = 33
    RULE_operand = 34
    RULE_ifstmt = 35
    RULE_forstmt = 36
    RULE_breakstmt = 37
    RULE_continuestmt = 38
    RULE_rtnstmt = 39
    RULE_callstmt = 40
    RULE_blockstmt = 41

    ruleNames =  [ "program", "declist", "decl", "vardecl", "idlist", "ids", 
                   "vartyp", "idxlist", "idxs", "idx", "arraylist", "arrays", 
                   "array", "funcdecl", "paralist", "paras", "para", "functyp", 
                   "bodylist", "bodydecl", "stmt", "assignstmt", "exprlist", 
                   "exprs", "expr", "unexpr", "unexpr1", "unexpr2", "idxop", 
                   "biexpr", "biexpr1", "biexpr2", "biexpr3", "biexpr4", 
                   "operand", "ifstmt", "forstmt", "breakstmt", "continuestmt", 
                   "rtnstmt", "callstmt", "blockstmt" ]

    EOF = Token.EOF
    T__0=1
    WS=2
    CCOMMENT=3
    CPPCOMMENT=4
    KWVOID=5
    KWAUTO=6
    KWINT=7
    KWFLOAT=8
    KWBOO=9
    KWSTR=10
    KWARR=11
    KWINHERIT=12
    KWFUNC=13
    KWTRUE=14
    KWFALSE=15
    KWFOR=16
    KWWHILE=17
    KWDO=18
    KWBRK=19
    KWCONT=20
    KWRTN=21
    KWIF=22
    KWELSE=23
    KWOF=24
    KWOUT=25
    ID=26
    ADDOP=27
    SUBOP=28
    MULOP=29
    DIVOP=30
    MODOP=31
    EXCOP=32
    ANDOP=33
    OROP=34
    EQLOP=35
    DIFOP=36
    LARGEOP=37
    LEQLOP=38
    SMALLOP=39
    SEQLOP=40
    CONCATOP=41
    DOT=42
    CM=43
    SM=44
    CL=45
    LB=46
    RB=47
    LSB=48
    RSB=49
    LCB=50
    RCB=51
    EQL=52
    LITINT=53
    LITFLOAT=54
    LITBOO=55
    LITSTR=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declist(self):
            return self.getTypedRuleContext(MT22Parser.DeclistContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.declist()
            self.state = 85
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def declist(self):
            return self.getTypedRuleContext(MT22Parser.DeclistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_declist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclist" ):
                return visitor.visitDeclist(self)
            else:
                return visitor.visitChildren(self)




    def declist(self):

        localctx = MT22Parser.DeclistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declist)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.decl()
                self.state = 88
                self.declist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def CL(self):
            return self.getToken(MT22Parser.CL, 0)

        def vartyp(self):
            return self.getTypedRuleContext(MT22Parser.VartypContext,0)


        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def EQL(self):
            return self.getToken(MT22Parser.EQL, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def KWARR(self):
            return self.getToken(MT22Parser.KWARR, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def idxlist(self):
            return self.getTypedRuleContext(MT22Parser.IdxlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def KWOF(self):
            return self.getToken(MT22Parser.KWOF, 0)

        def arraylist(self):
            return self.getTypedRuleContext(MT22Parser.ArraylistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.idlist()
                self.state = 98
                self.match(MT22Parser.CL)
                self.state = 99
                self.vartyp()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MT22Parser.EQL:
                    self.state = 100
                    self.match(MT22Parser.EQL)
                    self.state = 101
                    self.exprlist()


                self.state = 104
                self.match(MT22Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.idlist()
                self.state = 107
                self.match(MT22Parser.CL)
                self.state = 108
                self.match(MT22Parser.KWARR)
                self.state = 109
                self.match(MT22Parser.LSB)
                self.state = 110
                self.idxlist()
                self.state = 111
                self.match(MT22Parser.RSB)
                self.state = 112
                self.match(MT22Parser.KWOF)
                self.state = 113
                self.vartyp()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MT22Parser.EQL:
                    self.state = 114
                    self.match(MT22Parser.EQL)
                    self.state = 115
                    self.arraylist()


                self.state = 118
                self.match(MT22Parser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def ids(self):
            return self.getTypedRuleContext(MT22Parser.IdsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idlist)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(MT22Parser.ID)
                self.state = 123
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MT22Parser.CM, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def ids(self):
            return self.getTypedRuleContext(MT22Parser.IdsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = MT22Parser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ids)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(MT22Parser.CM)
                self.state = 128
                self.match(MT22Parser.ID)
                self.state = 129
                self.ids()
                pass
            elif token in [MT22Parser.CL]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWINT(self):
            return self.getToken(MT22Parser.KWINT, 0)

        def KWFLOAT(self):
            return self.getToken(MT22Parser.KWFLOAT, 0)

        def KWBOO(self):
            return self.getToken(MT22Parser.KWBOO, 0)

        def KWSTR(self):
            return self.getToken(MT22Parser.KWSTR, 0)

        def KWAUTO(self):
            return self.getToken(MT22Parser.KWAUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_vartyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartyp" ):
                return visitor.visitVartyp(self)
            else:
                return visitor.visitChildren(self)




    def vartyp(self):

        localctx = MT22Parser.VartypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vartyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.KWAUTO) | (1 << MT22Parser.KWINT) | (1 << MT22Parser.KWFLOAT) | (1 << MT22Parser.KWBOO) | (1 << MT22Parser.KWSTR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdxlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idx(self):
            return self.getTypedRuleContext(MT22Parser.IdxContext,0)


        def idxs(self):
            return self.getTypedRuleContext(MT22Parser.IdxsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idxlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdxlist" ):
                return visitor.visitIdxlist(self)
            else:
                return visitor.visitChildren(self)




    def idxlist(self):

        localctx = MT22Parser.IdxlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idxlist)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.idx()
                self.state = 136
                self.idxs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.idx()
                self.text = self.text.replace('_','')
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdxsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MT22Parser.CM, 0)

        def idx(self):
            return self.getTypedRuleContext(MT22Parser.IdxContext,0)


        def idxs(self):
            return self.getTypedRuleContext(MT22Parser.IdxsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idxs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdxs" ):
                return visitor.visitIdxs(self)
            else:
                return visitor.visitChildren(self)




    def idxs(self):

        localctx = MT22Parser.IdxsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idxs)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(MT22Parser.CM)
                self.state = 144
                self.idx()
                self.state = 145
                self.idxs()
                pass
            elif token in [MT22Parser.RSB]:
                self.enterOuterAlt(localctx, 2)
                self.text = self.text.replace('_','')
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITINT(self):
            return self.getToken(MT22Parser.LITINT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_idx

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx" ):
                return visitor.visitIdx(self)
            else:
                return visitor.visitChildren(self)




    def idx(self):

        localctx = MT22Parser.IdxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(MT22Parser.LITINT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(MT22Parser.ArrayContext,0)


        def arrays(self):
            return self.getTypedRuleContext(MT22Parser.ArraysContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraylist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylist" ):
                return visitor.visitArraylist(self)
            else:
                return visitor.visitChildren(self)




    def arraylist(self):

        localctx = MT22Parser.ArraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arraylist)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.array()
                self.state = 153
                self.arrays()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraysContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MT22Parser.CM, 0)

        def array(self):
            return self.getTypedRuleContext(MT22Parser.ArrayContext,0)


        def arrays(self):
            return self.getTypedRuleContext(MT22Parser.ArraysContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arrays

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrays" ):
                return visitor.visitArrays(self)
            else:
                return visitor.visitChildren(self)




    def arrays(self):

        localctx = MT22Parser.ArraysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrays)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(MT22Parser.CM)
                self.state = 159
                self.array()
                self.state = 160
                self.arrays()
                pass
            elif token in [MT22Parser.SM]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MT22Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MT22Parser.LCB)
            self.state = 166
            self.exprlist()
            self.state = 167
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def CL(self):
            return self.getToken(MT22Parser.CL, 0)

        def KWFUNC(self):
            return self.getToken(MT22Parser.KWFUNC, 0)

        def functyp(self):
            return self.getTypedRuleContext(MT22Parser.FunctypContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def paralist(self):
            return self.getTypedRuleContext(MT22Parser.ParalistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def bodylist(self):
            return self.getTypedRuleContext(MT22Parser.BodylistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def KWINHERIT(self):
            return self.getToken(MT22Parser.KWINHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(MT22Parser.ID)
            self.state = 170
            self.match(MT22Parser.CL)
            self.state = 171
            self.match(MT22Parser.KWFUNC)
            self.state = 172
            self.functyp()
            self.state = 173
            self.match(MT22Parser.LB)
            self.state = 174
            self.paralist()
            self.state = 175
            self.match(MT22Parser.RB)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWINHERIT:
                self.state = 176
                self.match(MT22Parser.KWINHERIT)
                self.state = 177
                self.match(MT22Parser.ID)


            self.state = 180
            self.match(MT22Parser.LCB)
            self.state = 181
            self.bodylist()
            self.state = 182
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(MT22Parser.ParaContext,0)


        def paras(self):
            return self.getTypedRuleContext(MT22Parser.ParasContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = MT22Parser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paralist)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.KWINHERIT, MT22Parser.KWOUT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.para()
                self.state = 185
                self.paras()
                pass
            elif token in [MT22Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MT22Parser.CM, 0)

        def para(self):
            return self.getTypedRuleContext(MT22Parser.ParaContext,0)


        def paras(self):
            return self.getTypedRuleContext(MT22Parser.ParasContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paras

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParas" ):
                return visitor.visitParas(self)
            else:
                return visitor.visitChildren(self)




    def paras(self):

        localctx = MT22Parser.ParasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paras)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(MT22Parser.CM)
                self.state = 191
                self.para()
                self.state = 192
                self.paras()
                pass
            elif token in [MT22Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def CL(self):
            return self.getToken(MT22Parser.CL, 0)

        def vartyp(self):
            return self.getTypedRuleContext(MT22Parser.VartypContext,0)


        def KWINHERIT(self):
            return self.getToken(MT22Parser.KWINHERIT, 0)

        def KWOUT(self):
            return self.getToken(MT22Parser.KWOUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MT22Parser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWINHERIT:
                self.state = 197
                self.match(MT22Parser.KWINHERIT)


            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWOUT:
                self.state = 200
                self.match(MT22Parser.KWOUT)


            self.state = 203
            self.match(MT22Parser.ID)
            self.state = 204
            self.match(MT22Parser.CL)
            self.state = 205
            self.vartyp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWINT(self):
            return self.getToken(MT22Parser.KWINT, 0)

        def KWFLOAT(self):
            return self.getToken(MT22Parser.KWFLOAT, 0)

        def KWBOO(self):
            return self.getToken(MT22Parser.KWBOO, 0)

        def KWSTR(self):
            return self.getToken(MT22Parser.KWSTR, 0)

        def KWAUTO(self):
            return self.getToken(MT22Parser.KWAUTO, 0)

        def KWVOID(self):
            return self.getToken(MT22Parser.KWVOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functyp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctyp" ):
                return visitor.visitFunctyp(self)
            else:
                return visitor.visitChildren(self)




    def functyp(self):

        localctx = MT22Parser.FunctypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.KWVOID) | (1 << MT22Parser.KWAUTO) | (1 << MT22Parser.KWINT) | (1 << MT22Parser.KWFLOAT) | (1 << MT22Parser.KWBOO) | (1 << MT22Parser.KWSTR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodylistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bodydecl(self):
            return self.getTypedRuleContext(MT22Parser.BodydeclContext,0)


        def bodylist(self):
            return self.getTypedRuleContext(MT22Parser.BodylistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_bodylist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodylist" ):
                return visitor.visitBodylist(self)
            else:
                return visitor.visitChildren(self)




    def bodylist(self):

        localctx = MT22Parser.BodylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_bodylist)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0, MT22Parser.KWFOR, MT22Parser.KWBRK, MT22Parser.KWCONT, MT22Parser.KWRTN, MT22Parser.ID, MT22Parser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.bodydecl()
                self.state = 210
                self.bodylist()
                pass
            elif token in [MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_bodydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodydecl" ):
                return visitor.visitBodydecl(self)
            else:
                return visitor.visitChildren(self)




    def bodydecl(self):

        localctx = MT22Parser.BodydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_bodydecl)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MT22Parser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MT22Parser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MT22Parser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestmtContext,0)


        def rtnstmt(self):
            return self.getTypedRuleContext(MT22Parser.RtnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.breakstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 223
                self.continuestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 224
                self.rtnstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 225
                self.callstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 226
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQL(self):
            return self.getToken(MT22Parser.EQL, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def idxop(self):
            return self.getTypedRuleContext(MT22Parser.IdxopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 229
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.state = 230
                self.match(MT22Parser.ID)
                self.state = 231
                self.idxop()
                pass


            self.state = 234
            self.match(MT22Parser.EQL)
            self.state = 235
            self.expr()
            self.state = 236
            self.match(MT22Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def exprs(self):
            return self.getTypedRuleContext(MT22Parser.ExprsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exprlist)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ID, MT22Parser.SUBOP, MT22Parser.EXCOP, MT22Parser.LB, MT22Parser.LCB, MT22Parser.LITINT, MT22Parser.LITFLOAT, MT22Parser.LITBOO, MT22Parser.LITSTR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.expr()
                self.state = 239
                self.exprs()
                pass
            elif token in [MT22Parser.SM, MT22Parser.RB, MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MT22Parser.CM, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def exprs(self):
            return self.getTypedRuleContext(MT22Parser.ExprsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = MT22Parser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exprs)
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.match(MT22Parser.CM)
                self.state = 245
                self.expr()
                self.state = 246
                self.exprs()
                pass
            elif token in [MT22Parser.SM, MT22Parser.RB, MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unexpr(self):
            return self.getTypedRuleContext(MT22Parser.UnexprContext,0)


        def biexpr(self):
            return self.getTypedRuleContext(MT22Parser.BiexprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.unexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.biexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCOP(self):
            return self.getToken(MT22Parser.EXCOP, 0)

        def unexpr(self):
            return self.getTypedRuleContext(MT22Parser.UnexprContext,0)


        def unexpr1(self):
            return self.getTypedRuleContext(MT22Parser.Unexpr1Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_unexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnexpr" ):
                return visitor.visitUnexpr(self)
            else:
                return visitor.visitChildren(self)




    def unexpr(self):

        localctx = MT22Parser.UnexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_unexpr)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.EXCOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(MT22Parser.EXCOP)
                self.state = 256
                self.unexpr()
                pass
            elif token in [MT22Parser.ID, MT22Parser.SUBOP, MT22Parser.LB, MT22Parser.LCB, MT22Parser.LITINT, MT22Parser.LITFLOAT, MT22Parser.LITBOO, MT22Parser.LITSTR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.unexpr1()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unexpr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBOP(self):
            return self.getToken(MT22Parser.SUBOP, 0)

        def unexpr1(self):
            return self.getTypedRuleContext(MT22Parser.Unexpr1Context,0)


        def unexpr2(self):
            return self.getTypedRuleContext(MT22Parser.Unexpr2Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_unexpr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnexpr1" ):
                return visitor.visitUnexpr1(self)
            else:
                return visitor.visitChildren(self)




    def unexpr1(self):

        localctx = MT22Parser.Unexpr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_unexpr1)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(MT22Parser.SUBOP)
                self.state = 261
                self.unexpr1()
                pass
            elif token in [MT22Parser.ID, MT22Parser.LB, MT22Parser.LCB, MT22Parser.LITINT, MT22Parser.LITFLOAT, MT22Parser.LITBOO, MT22Parser.LITSTR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.unexpr2(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unexpr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def unexpr2(self):
            return self.getTypedRuleContext(MT22Parser.Unexpr2Context,0)


        def idxop(self):
            return self.getTypedRuleContext(MT22Parser.IdxopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_unexpr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnexpr2" ):
                return visitor.visitUnexpr2(self)
            else:
                return visitor.visitChildren(self)



    def unexpr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Unexpr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_unexpr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Unexpr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unexpr2)
                    self.state = 268
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 269
                    self.idxop() 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdxopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def idxlist(self):
            return self.getTypedRuleContext(MT22Parser.IdxlistContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_idxop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdxop" ):
                return visitor.visitIdxop(self)
            else:
                return visitor.visitChildren(self)




    def idxop(self):

        localctx = MT22Parser.IdxopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_idxop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(MT22Parser.LSB)
            self.state = 276
            self.idxlist()
            self.state = 277
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BiexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def biexpr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Biexpr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Biexpr1Context,i)


        def CONCATOP(self):
            return self.getToken(MT22Parser.CONCATOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_biexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBiexpr" ):
                return visitor.visitBiexpr(self)
            else:
                return visitor.visitChildren(self)




    def biexpr(self):

        localctx = MT22Parser.BiexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_biexpr)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.biexpr1()
                self.state = 280
                self.match(MT22Parser.CONCATOP)
                self.state = 281
                self.biexpr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.biexpr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Biexpr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def biexpr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Biexpr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Biexpr2Context,i)


        def EQLOP(self):
            return self.getToken(MT22Parser.EQLOP, 0)

        def DIFOP(self):
            return self.getToken(MT22Parser.DIFOP, 0)

        def LARGEOP(self):
            return self.getToken(MT22Parser.LARGEOP, 0)

        def LEQLOP(self):
            return self.getToken(MT22Parser.LEQLOP, 0)

        def SMALLOP(self):
            return self.getToken(MT22Parser.SMALLOP, 0)

        def SEQLOP(self):
            return self.getToken(MT22Parser.SEQLOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_biexpr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBiexpr1" ):
                return visitor.visitBiexpr1(self)
            else:
                return visitor.visitChildren(self)




    def biexpr1(self):

        localctx = MT22Parser.Biexpr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_biexpr1)
        self._la = 0 # Token type
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.biexpr2(0)
                self.state = 287
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQLOP) | (1 << MT22Parser.DIFOP) | (1 << MT22Parser.LARGEOP) | (1 << MT22Parser.LEQLOP) | (1 << MT22Parser.SMALLOP) | (1 << MT22Parser.SEQLOP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 288
                self.biexpr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.biexpr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Biexpr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def biexpr3(self):
            return self.getTypedRuleContext(MT22Parser.Biexpr3Context,0)


        def biexpr2(self):
            return self.getTypedRuleContext(MT22Parser.Biexpr2Context,0)


        def ANDOP(self):
            return self.getToken(MT22Parser.ANDOP, 0)

        def OROP(self):
            return self.getToken(MT22Parser.OROP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_biexpr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBiexpr2" ):
                return visitor.visitBiexpr2(self)
            else:
                return visitor.visitChildren(self)



    def biexpr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Biexpr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_biexpr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.biexpr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Biexpr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_biexpr2)
                    self.state = 296
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 297
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ANDOP or _la==MT22Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 298
                    self.biexpr3(0) 
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Biexpr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def biexpr4(self):
            return self.getTypedRuleContext(MT22Parser.Biexpr4Context,0)


        def biexpr3(self):
            return self.getTypedRuleContext(MT22Parser.Biexpr3Context,0)


        def ADDOP(self):
            return self.getToken(MT22Parser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(MT22Parser.SUBOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_biexpr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBiexpr3" ):
                return visitor.visitBiexpr3(self)
            else:
                return visitor.visitChildren(self)



    def biexpr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Biexpr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_biexpr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.biexpr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Biexpr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_biexpr3)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADDOP or _la==MT22Parser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 309
                    self.biexpr4(0) 
                self.state = 314
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Biexpr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def biexpr4(self):
            return self.getTypedRuleContext(MT22Parser.Biexpr4Context,0)


        def MULOP(self):
            return self.getToken(MT22Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(MT22Parser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(MT22Parser.MODOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_biexpr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBiexpr4" ):
                return visitor.visitBiexpr4(self)
            else:
                return visitor.visitChildren(self)



    def biexpr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Biexpr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_biexpr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Biexpr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_biexpr4)
                    self.state = 318
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 319
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MULOP) | (1 << MT22Parser.DIVOP) | (1 << MT22Parser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 320
                    self.operand() 
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITINT(self):
            return self.getToken(MT22Parser.LITINT, 0)

        def LITFLOAT(self):
            return self.getToken(MT22Parser.LITFLOAT, 0)

        def LITBOO(self):
            return self.getToken(MT22Parser.LITBOO, 0)

        def LITSTR(self):
            return self.getToken(MT22Parser.LITSTR, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def idxop(self):
            return self.getTypedRuleContext(MT22Parser.IdxopContext,0)


        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_operand)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(MT22Parser.LITINT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(MT22Parser.LITFLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.match(MT22Parser.LITBOO)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 329
                self.match(MT22Parser.LITSTR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 330
                self.match(MT22Parser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 331
                self.callstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 332
                self.match(MT22Parser.LB)
                self.state = 333
                self.expr()
                self.state = 334
                self.match(MT22Parser.RB)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 336
                self.match(MT22Parser.ID)
                self.state = 337
                self.idxop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 338
                self.match(MT22Parser.LCB)
                self.state = 339
                self.exprlist()
                self.state = 340
                self.match(MT22Parser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MT22Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MT22Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWFOR(self):
            return self.getToken(MT22Parser.KWFOR, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def EQL(self):
            return self.getToken(MT22Parser.EQL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.CM)
            else:
                return self.getToken(MT22Parser.CM, i)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MT22Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(MT22Parser.KWFOR)
            self.state = 347
            self.match(MT22Parser.LB)
            self.state = 348
            self.match(MT22Parser.ID)
            self.state = 349
            self.match(MT22Parser.EQL)
            self.state = 350
            self.expr()
            self.state = 351
            self.match(MT22Parser.CM)
            self.state = 352
            self.expr()
            self.state = 353
            self.match(MT22Parser.CM)
            self.state = 354
            self.expr()
            self.state = 355
            self.match(MT22Parser.RB)
            self.state = 356
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWBRK(self):
            return self.getToken(MT22Parser.KWBRK, 0)

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MT22Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(MT22Parser.KWBRK)
            self.state = 359
            self.match(MT22Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWCONT(self):
            return self.getToken(MT22Parser.KWCONT, 0)

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MT22Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(MT22Parser.KWCONT)
            self.state = 362
            self.match(MT22Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RtnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWRTN(self):
            return self.getToken(MT22Parser.KWRTN, 0)

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_rtnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRtnstmt" ):
                return visitor.visitRtnstmt(self)
            else:
                return visitor.visitChildren(self)




    def rtnstmt(self):

        localctx = MT22Parser.RtnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_rtnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MT22Parser.KWRTN)
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.ID) | (1 << MT22Parser.SUBOP) | (1 << MT22Parser.EXCOP) | (1 << MT22Parser.LB) | (1 << MT22Parser.LCB) | (1 << MT22Parser.LITINT) | (1 << MT22Parser.LITFLOAT) | (1 << MT22Parser.LITBOO) | (1 << MT22Parser.LITSTR))) != 0):
                self.state = 365
                self.expr()


            self.state = 368
            self.match(MT22Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(MT22Parser.ID)
            self.state = 371
            self.match(MT22Parser.LB)
            self.state = 372
            self.exprlist()
            self.state = 373
            self.match(MT22Parser.RB)
            self.state = 374
            self.match(MT22Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def bodylist(self):
            return self.getTypedRuleContext(MT22Parser.BodylistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = MT22Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(MT22Parser.LCB)
            self.state = 377
            self.bodylist()
            self.state = 378
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[27] = self.unexpr2_sempred
        self._predicates[31] = self.biexpr2_sempred
        self._predicates[32] = self.biexpr3_sempred
        self._predicates[33] = self.biexpr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def unexpr2_sempred(self, localctx:Unexpr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def biexpr2_sempred(self, localctx:Biexpr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def biexpr3_sempred(self, localctx:Biexpr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def biexpr4_sempred(self, localctx:Biexpr4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




