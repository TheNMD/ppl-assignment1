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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u019f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4j")
        buf.write("\n\4\3\5\3\5\5\5n\n\5\3\6\3\6\3\6\3\6\3\6\5\6u\n\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0083")
        buf.write("\n\6\3\7\3\7\3\7\5\7\u0088\n\7\3\b\3\b\3\b\3\b\5\b\u008e")
        buf.write("\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0098\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u009f\n\13\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ac\n\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\5\16\u00b6\n\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00bd\n\17\3\20\5\20\u00c0\n\20\3\20\5")
        buf.write("\20\u00c3\n\20\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00cf\n\22\3\23\3\23\3\23\5\23\u00d4\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u00df\n\24\3\25\3\25\3\25\5\25\u00e4\n\25\3\25\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\3\26\5\26\u00ee\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u00f5\n\27\3\30\3\30\3\30\3\30\3")
        buf.write("\30\5\30\u00fc\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u0103")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u010b\n\32\f")
        buf.write("\32\16\32\u010e\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7")
        buf.write("\33\u0116\n\33\f\33\16\33\u0119\13\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\7\34\u0121\n\34\f\34\16\34\u0124\13\34\3")
        buf.write("\35\3\35\3\35\5\35\u0129\n\35\3\36\3\36\3\36\5\36\u012e")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0136\n\37\3")
        buf.write("\37\3\37\3\37\5\37\u013b\n\37\3 \3 \3 \3 \3!\3!\5!\u0143")
        buf.write("\n!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\5$\u0153")
        buf.write("\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u015e\n%\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u016e\n&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(")
        buf.write("\3(\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\5")
        buf.write(",\u0192\n,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\2\5\62")
        buf.write("\64\66\60\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\\2\t\3\2\7\13\3\2")
        buf.write("\6\13\3\2.\63\3\2,-\3\2&\'\3\2(*\3\2\33$\2\u019f\2^\3")
        buf.write("\2\2\2\4b\3\2\2\2\6i\3\2\2\2\bm\3\2\2\2\n\u0082\3\2\2")
        buf.write("\2\f\u0087\3\2\2\2\16\u008d\3\2\2\2\20\u008f\3\2\2\2\22")
        buf.write("\u0097\3\2\2\2\24\u009e\3\2\2\2\26\u00a0\3\2\2\2\30\u00a2")
        buf.write("\3\2\2\2\32\u00b5\3\2\2\2\34\u00bc\3\2\2\2\36\u00bf\3")
        buf.write("\2\2\2 \u00c8\3\2\2\2\"\u00ce\3\2\2\2$\u00d3\3\2\2\2&")
        buf.write("\u00de\3\2\2\2(\u00e3\3\2\2\2*\u00ed\3\2\2\2,\u00f4\3")
        buf.write("\2\2\2.\u00fb\3\2\2\2\60\u0102\3\2\2\2\62\u0104\3\2\2")
        buf.write("\2\64\u010f\3\2\2\2\66\u011a\3\2\2\28\u0128\3\2\2\2:\u012d")
        buf.write("\3\2\2\2<\u013a\3\2\2\2>\u013c\3\2\2\2@\u0142\3\2\2\2")
        buf.write("B\u0148\3\2\2\2D\u014c\3\2\2\2F\u0152\3\2\2\2H\u015d\3")
        buf.write("\2\2\2J\u016d\3\2\2\2L\u016f\3\2\2\2N\u017b\3\2\2\2P\u0181")
        buf.write("\3\2\2\2R\u0189\3\2\2\2T\u018c\3\2\2\2V\u018f\3\2\2\2")
        buf.write("X\u0195\3\2\2\2Z\u0198\3\2\2\2\\\u019c\3\2\2\2^_\7=\2")
        buf.write("\2_`\5*\26\2`a\7>\2\2a\3\3\2\2\2bc\5\6\4\2cd\7\2\2\3d")
        buf.write("\5\3\2\2\2ef\5\b\5\2fg\5\6\4\2gj\3\2\2\2hj\5\b\5\2ie\3")
        buf.write("\2\2\2ih\3\2\2\2j\7\3\2\2\2kn\5\n\6\2ln\5\30\r\2mk\3\2")
        buf.write("\2\2ml\3\2\2\2n\t\3\2\2\2op\5\f\7\2pq\78\2\2qt\5\20\t")
        buf.write("\2rs\7?\2\2su\5*\26\2tr\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw")
        buf.write("\7\67\2\2w\u0083\3\2\2\2xy\5\f\7\2yz\78\2\2z{\7\f\2\2")
        buf.write("{|\7;\2\2|}\5\22\n\2}~\7<\2\2~\177\7\31\2\2\177\u0080")
        buf.write("\5\20\t\2\u0080\u0081\7\67\2\2\u0081\u0083\3\2\2\2\u0082")
        buf.write("o\3\2\2\2\u0082x\3\2\2\2\u0083\13\3\2\2\2\u0084\u0085")
        buf.write("\7%\2\2\u0085\u0088\5\16\b\2\u0086\u0088\7%\2\2\u0087")
        buf.write("\u0084\3\2\2\2\u0087\u0086\3\2\2\2\u0088\r\3\2\2\2\u0089")
        buf.write("\u008a\7\66\2\2\u008a\u008b\7%\2\2\u008b\u008e\5\16\b")
        buf.write("\2\u008c\u008e\3\2\2\2\u008d\u0089\3\2\2\2\u008d\u008c")
        buf.write("\3\2\2\2\u008e\17\3\2\2\2\u008f\u0090\t\2\2\2\u0090\21")
        buf.write("\3\2\2\2\u0091\u0092\5\26\f\2\u0092\u0093\5\24\13\2\u0093")
        buf.write("\u0098\3\2\2\2\u0094\u0095\5\26\f\2\u0095\u0096\b\n\1")
        buf.write("\2\u0096\u0098\3\2\2\2\u0097\u0091\3\2\2\2\u0097\u0094")
        buf.write("\3\2\2\2\u0098\23\3\2\2\2\u0099\u009a\7\66\2\2\u009a\u009b")
        buf.write("\5\26\f\2\u009b\u009c\5\24\13\2\u009c\u009f\3\2\2\2\u009d")
        buf.write("\u009f\b\13\1\2\u009e\u0099\3\2\2\2\u009e\u009d\3\2\2")
        buf.write("\2\u009f\25\3\2\2\2\u00a0\u00a1\7@\2\2\u00a1\27\3\2\2")
        buf.write("\2\u00a2\u00a3\7%\2\2\u00a3\u00a4\78\2\2\u00a4\u00a5\7")
        buf.write("\16\2\2\u00a5\u00a6\5 \21\2\u00a6\u00a7\79\2\2\u00a7\u00a8")
        buf.write("\5\32\16\2\u00a8\u00ab\7:\2\2\u00a9\u00aa\7\r\2\2\u00aa")
        buf.write("\u00ac\7%\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\u00ae\7=\2\2\u00ae\u00af\5")
        buf.write("\"\22\2\u00af\u00b0\7>\2\2\u00b0\31\3\2\2\2\u00b1\u00b2")
        buf.write("\5\36\20\2\u00b2\u00b3\5\34\17\2\u00b3\u00b6\3\2\2\2\u00b4")
        buf.write("\u00b6\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b6\33\3\2\2\2\u00b7\u00b8\7\66\2\2\u00b8\u00b9\5\36")
        buf.write("\20\2\u00b9\u00ba\5\34\17\2\u00ba\u00bd\3\2\2\2\u00bb")
        buf.write("\u00bd\3\2\2\2\u00bc\u00b7\3\2\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bd\35\3\2\2\2\u00be\u00c0\7\r\2\2\u00bf\u00be\3\2")
        buf.write("\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00c3")
        buf.write("\7\32\2\2\u00c2\u00c1\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c4\3\2\2\2\u00c4\u00c5\7%\2\2\u00c5\u00c6\78\2\2\u00c6")
        buf.write("\u00c7\5\20\t\2\u00c7\37\3\2\2\2\u00c8\u00c9\t\3\2\2\u00c9")
        buf.write("!\3\2\2\2\u00ca\u00cb\5$\23\2\u00cb\u00cc\5\"\22\2\u00cc")
        buf.write("\u00cf\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00ca\3\2\2\2")
        buf.write("\u00ce\u00cd\3\2\2\2\u00cf#\3\2\2\2\u00d0\u00d4\5\n\6")
        buf.write("\2\u00d1\u00d4\5&\24\2\u00d2\u00d4\5F$\2\u00d3\u00d0\3")
        buf.write("\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4%")
        buf.write("\3\2\2\2\u00d5\u00df\5(\25\2\u00d6\u00df\5L\'\2\u00d7")
        buf.write("\u00df\5N(\2\u00d8\u00df\5P)\2\u00d9\u00df\5R*\2\u00da")
        buf.write("\u00df\5T+\2\u00db\u00df\5V,\2\u00dc\u00df\5X-\2\u00dd")
        buf.write("\u00df\5Z.\2\u00de\u00d5\3\2\2\2\u00de\u00d6\3\2\2\2\u00de")
        buf.write("\u00d7\3\2\2\2\u00de\u00d8\3\2\2\2\u00de\u00d9\3\2\2\2")
        buf.write("\u00de\u00da\3\2\2\2\u00de\u00db\3\2\2\2\u00de\u00dc\3")
        buf.write("\2\2\2\u00de\u00dd\3\2\2\2\u00df\'\3\2\2\2\u00e0\u00e4")
        buf.write("\7%\2\2\u00e1\u00e2\7%\2\2\u00e2\u00e4\5> \2\u00e3\u00e0")
        buf.write("\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5")
        buf.write("\u00e6\7?\2\2\u00e6\u00e7\5.\30\2\u00e7\u00e8\7\67\2\2")
        buf.write("\u00e8)\3\2\2\2\u00e9\u00ea\5.\30\2\u00ea\u00eb\5,\27")
        buf.write("\2\u00eb\u00ee\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00e9")
        buf.write("\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee+\3\2\2\2\u00ef\u00f0")
        buf.write("\7\66\2\2\u00f0\u00f1\5.\30\2\u00f1\u00f2\5,\27\2\u00f2")
        buf.write("\u00f5\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00ef\3\2\2\2")
        buf.write("\u00f4\u00f3\3\2\2\2\u00f5-\3\2\2\2\u00f6\u00f7\5\60\31")
        buf.write("\2\u00f7\u00f8\7\64\2\2\u00f8\u00f9\5\60\31\2\u00f9\u00fc")
        buf.write("\3\2\2\2\u00fa\u00fc\5\60\31\2\u00fb\u00f6\3\2\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fc/\3\2\2\2\u00fd\u00fe\5\62\32\2\u00fe")
        buf.write("\u00ff\t\4\2\2\u00ff\u0100\5\62\32\2\u0100\u0103\3\2\2")
        buf.write("\2\u0101\u0103\5\62\32\2\u0102\u00fd\3\2\2\2\u0102\u0101")
        buf.write("\3\2\2\2\u0103\61\3\2\2\2\u0104\u0105\b\32\1\2\u0105\u0106")
        buf.write("\5\64\33\2\u0106\u010c\3\2\2\2\u0107\u0108\f\4\2\2\u0108")
        buf.write("\u0109\t\5\2\2\u0109\u010b\5\64\33\2\u010a\u0107\3\2\2")
        buf.write("\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\63\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110")
        buf.write("\b\33\1\2\u0110\u0111\5\66\34\2\u0111\u0117\3\2\2\2\u0112")
        buf.write("\u0113\f\4\2\2\u0113\u0114\t\6\2\2\u0114\u0116\5\66\34")
        buf.write("\2\u0115\u0112\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\65\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u011a\u011b\b\34\1\2\u011b\u011c\58\35\2\u011c")
        buf.write("\u0122\3\2\2\2\u011d\u011e\f\4\2\2\u011e\u011f\t\7\2\2")
        buf.write("\u011f\u0121\58\35\2\u0120\u011d\3\2\2\2\u0121\u0124\3")
        buf.write("\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\67")
        buf.write("\3\2\2\2\u0124\u0122\3\2\2\2\u0125\u0126\7+\2\2\u0126")
        buf.write("\u0129\58\35\2\u0127\u0129\5:\36\2\u0128\u0125\3\2\2\2")
        buf.write("\u0128\u0127\3\2\2\2\u01299\3\2\2\2\u012a\u012b\7\'\2")
        buf.write("\2\u012b\u012e\5:\36\2\u012c\u012e\5<\37\2\u012d\u012a")
        buf.write("\3\2\2\2\u012d\u012c\3\2\2\2\u012e;\3\2\2\2\u012f\u013b")
        buf.write("\7@\2\2\u0130\u013b\7A\2\2\u0131\u013b\7B\2\2\u0132\u013b")
        buf.write("\7C\2\2\u0133\u0135\7%\2\2\u0134\u0136\5> \2\u0135\u0134")
        buf.write("\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u013b\3\2\2\2\u0137")
        buf.write("\u013b\5@!\2\u0138\u013b\5B\"\2\u0139\u013b\5D#\2\u013a")
        buf.write("\u012f\3\2\2\2\u013a\u0130\3\2\2\2\u013a\u0131\3\2\2\2")
        buf.write("\u013a\u0132\3\2\2\2\u013a\u0133\3\2\2\2\u013a\u0137\3")
        buf.write("\2\2\2\u013a\u0138\3\2\2\2\u013a\u0139\3\2\2\2\u013b=")
        buf.write("\3\2\2\2\u013c\u013d\7;\2\2\u013d\u013e\5\22\n\2\u013e")
        buf.write("\u013f\7<\2\2\u013f?\3\2\2\2\u0140\u0143\5\\/\2\u0141")
        buf.write("\u0143\7%\2\2\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144\u0145\79\2\2\u0145\u0146\5")
        buf.write("*\26\2\u0146\u0147\7:\2\2\u0147A\3\2\2\2\u0148\u0149\7")
        buf.write("9\2\2\u0149\u014a\5.\30\2\u014a\u014b\7:\2\2\u014bC\3")
        buf.write("\2\2\2\u014c\u014d\7=\2\2\u014d\u014e\5*\26\2\u014e\u014f")
        buf.write("\7>\2\2\u014fE\3\2\2\2\u0150\u0153\5H%\2\u0151\u0153\5")
        buf.write("J&\2\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153G\3")
        buf.write("\2\2\2\u0154\u0155\7\27\2\2\u0155\u0156\79\2\2\u0156\u0157")
        buf.write("\5.\30\2\u0157\u0158\7:\2\2\u0158\u0159\5H%\2\u0159\u015a")
        buf.write("\7\30\2\2\u015a\u015b\5H%\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015e\5&\24\2\u015d\u0154\3\2\2\2\u015d\u015c\3\2\2\2")
        buf.write("\u015eI\3\2\2\2\u015f\u0160\7\27\2\2\u0160\u0161\79\2")
        buf.write("\2\u0161\u0162\5.\30\2\u0162\u0163\7:\2\2\u0163\u0164")
        buf.write("\5F$\2\u0164\u016e\3\2\2\2\u0165\u0166\7\27\2\2\u0166")
        buf.write("\u0167\79\2\2\u0167\u0168\5.\30\2\u0168\u0169\7:\2\2\u0169")
        buf.write("\u016a\5H%\2\u016a\u016b\7\30\2\2\u016b\u016c\5J&\2\u016c")
        buf.write("\u016e\3\2\2\2\u016d\u015f\3\2\2\2\u016d\u0165\3\2\2\2")
        buf.write("\u016eK\3\2\2\2\u016f\u0170\7\21\2\2\u0170\u0171\79\2")
        buf.write("\2\u0171\u0172\7%\2\2\u0172\u0173\7?\2\2\u0173\u0174\5")
        buf.write(".\30\2\u0174\u0175\7\66\2\2\u0175\u0176\5.\30\2\u0176")
        buf.write("\u0177\7\66\2\2\u0177\u0178\5.\30\2\u0178\u0179\7:\2\2")
        buf.write("\u0179\u017a\5&\24\2\u017aM\3\2\2\2\u017b\u017c\7\22\2")
        buf.write("\2\u017c\u017d\79\2\2\u017d\u017e\5.\30\2\u017e\u017f")
        buf.write("\7:\2\2\u017f\u0180\5&\24\2\u0180O\3\2\2\2\u0181\u0182")
        buf.write("\7\23\2\2\u0182\u0183\5Z.\2\u0183\u0184\7\22\2\2\u0184")
        buf.write("\u0185\79\2\2\u0185\u0186\5.\30\2\u0186\u0187\7:\2\2\u0187")
        buf.write("\u0188\7\67\2\2\u0188Q\3\2\2\2\u0189\u018a\7\24\2\2\u018a")
        buf.write("\u018b\7\67\2\2\u018bS\3\2\2\2\u018c\u018d\7\25\2\2\u018d")
        buf.write("\u018e\7\67\2\2\u018eU\3\2\2\2\u018f\u0191\7\26\2\2\u0190")
        buf.write("\u0192\5.\30\2\u0191\u0190\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193\u0194\7\67\2\2\u0194W\3\2\2")
        buf.write("\2\u0195\u0196\5@!\2\u0196\u0197\7\67\2\2\u0197Y\3\2\2")
        buf.write("\2\u0198\u0199\7=\2\2\u0199\u019a\5\"\22\2\u019a\u019b")
        buf.write("\7>\2\2\u019b[\3\2\2\2\u019c\u019d\t\b\2\2\u019d]\3\2")
        buf.write("\2\2#imt\u0082\u0087\u008d\u0097\u009e\u00ab\u00b5\u00bc")
        buf.write("\u00bf\u00c2\u00ce\u00d3\u00de\u00e3\u00ed\u00f4\u00fb")
        buf.write("\u0102\u010c\u0117\u0122\u0128\u012d\u0135\u013a\u0142")
        buf.write("\u0152\u015d\u016d\u0191")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'void'", "'auto'", "'integer'", "'float'", "'boolean'", 
                     "'string'", "'array'", "'inherit'", "'function'", "'true'", 
                     "'false'", "'for'", "'while'", "'do'", "'break'", "'continue'", 
                     "'return'", "'if'", "'else'", "'of'", "'out'", "'readInteger'", 
                     "'printInteger'", "'readFloat'", "'writeFloat'", "'readBoolean'", 
                     "'printBoolean'", "'readString'", "'printString'", 
                     "'super'", "'preventDefault()'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'::'", 
                     "'.'", "','", "';'", "':'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "WS", "CCOMMENT", "CPPCOMMENT", "KWVOID", 
                      "KWAUTO", "KWINT", "KWFLOAT", "KWBOO", "KWSTR", "KWARR", 
                      "KWINHERIT", "KWFUNC", "KWTRUE", "KWFALSE", "KWFOR", 
                      "KWWHILE", "KWDO", "KWBRK", "KWCONT", "KWRTN", "KWIF", 
                      "KWELSE", "KWOF", "KWOUT", "SFREADINT", "SFPRINTINT", 
                      "SFREADFLOAT", "SFPRINTFLOAT", "SFREADBOOL", "SFPRINTBOOL", 
                      "SFREADSTR", "SFPRINTSTR", "SFSUPER", "SFPREVENT", 
                      "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                      "EXCOP", "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", 
                      "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", "DOT", 
                      "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", 
                      "RCB", "EQL", "LITINT", "LITFLOAT", "LITBOO", "LITSTR", 
                      "ERROR_CHAR", "NCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_litarr = 0
    RULE_program = 1
    RULE_declist = 2
    RULE_decl = 3
    RULE_vardecl = 4
    RULE_idlist = 5
    RULE_ids = 6
    RULE_vartyp = 7
    RULE_idxlist = 8
    RULE_idxs = 9
    RULE_idx = 10
    RULE_funcdecl = 11
    RULE_paralist = 12
    RULE_paras = 13
    RULE_para = 14
    RULE_functyp = 15
    RULE_bodylist = 16
    RULE_bodydecl = 17
    RULE_stmt = 18
    RULE_assignstmt = 19
    RULE_exprlist = 20
    RULE_exprs = 21
    RULE_expr = 22
    RULE_expr1 = 23
    RULE_expr2 = 24
    RULE_expr3 = 25
    RULE_expr4 = 26
    RULE_expr5 = 27
    RULE_expr6 = 28
    RULE_operand = 29
    RULE_idxop = 30
    RULE_funccall = 31
    RULE_subexpr = 32
    RULE_subarr = 33
    RULE_ifstmt = 34
    RULE_matchstmt = 35
    RULE_unmatchstmt = 36
    RULE_forstmt = 37
    RULE_whilestmt = 38
    RULE_dowhilestmt = 39
    RULE_breakstmt = 40
    RULE_continuestmt = 41
    RULE_rtnstmt = 42
    RULE_callstmt = 43
    RULE_blockstmt = 44
    RULE_specialfunc = 45

    ruleNames =  [ "litarr", "program", "declist", "decl", "vardecl", "idlist", 
                   "ids", "vartyp", "idxlist", "idxs", "idx", "funcdecl", 
                   "paralist", "paras", "para", "functyp", "bodylist", "bodydecl", 
                   "stmt", "assignstmt", "exprlist", "exprs", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "operand", 
                   "idxop", "funccall", "subexpr", "subarr", "ifstmt", "matchstmt", 
                   "unmatchstmt", "forstmt", "whilestmt", "dowhilestmt", 
                   "breakstmt", "continuestmt", "rtnstmt", "callstmt", "blockstmt", 
                   "specialfunc" ]

    EOF = Token.EOF
    WS=1
    CCOMMENT=2
    CPPCOMMENT=3
    KWVOID=4
    KWAUTO=5
    KWINT=6
    KWFLOAT=7
    KWBOO=8
    KWSTR=9
    KWARR=10
    KWINHERIT=11
    KWFUNC=12
    KWTRUE=13
    KWFALSE=14
    KWFOR=15
    KWWHILE=16
    KWDO=17
    KWBRK=18
    KWCONT=19
    KWRTN=20
    KWIF=21
    KWELSE=22
    KWOF=23
    KWOUT=24
    SFREADINT=25
    SFPRINTINT=26
    SFREADFLOAT=27
    SFPRINTFLOAT=28
    SFREADBOOL=29
    SFPRINTBOOL=30
    SFREADSTR=31
    SFPRINTSTR=32
    SFSUPER=33
    SFPREVENT=34
    ID=35
    ADDOP=36
    SUBOP=37
    MULOP=38
    DIVOP=39
    MODOP=40
    EXCOP=41
    ANDOP=42
    OROP=43
    EQLOP=44
    DIFOP=45
    LARGEOP=46
    LEQLOP=47
    SMALLOP=48
    SEQLOP=49
    CONCATOP=50
    DOT=51
    CM=52
    SM=53
    CL=54
    LB=55
    RB=56
    LSB=57
    RSB=58
    LCB=59
    RCB=60
    EQL=61
    LITINT=62
    LITFLOAT=63
    LITBOO=64
    LITSTR=65
    ERROR_CHAR=66
    NCLOSE_STRING=67
    ILLEGAL_ESCAPE=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LitarrContext(ParserRuleContext):
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
            return MT22Parser.RULE_litarr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLitarr" ):
                return visitor.visitLitarr(self)
            else:
                return visitor.visitChildren(self)




    def litarr(self):

        localctx = MT22Parser.LitarrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_litarr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MT22Parser.LCB)
            self.state = 93
            self.exprlist()
            self.state = 94
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 2, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.declist()
            self.state = 97
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
        self.enterRule(localctx, 4, self.RULE_declist)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.decl()
                self.state = 100
                self.declist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
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
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
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

        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.idlist()
                self.state = 110
                self.match(MT22Parser.CL)
                self.state = 111
                self.vartyp()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MT22Parser.EQL:
                    self.state = 112
                    self.match(MT22Parser.EQL)
                    self.state = 113
                    self.exprlist()


                self.state = 116
                self.match(MT22Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.idlist()
                self.state = 119
                self.match(MT22Parser.CL)
                self.state = 120
                self.match(MT22Parser.KWARR)
                self.state = 121
                self.match(MT22Parser.LSB)
                self.state = 122
                self.idxlist()
                self.state = 123
                self.match(MT22Parser.RSB)
                self.state = 124
                self.match(MT22Parser.KWOF)
                self.state = 125
                self.vartyp()
                self.state = 126
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
        self.enterRule(localctx, 10, self.RULE_idlist)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(MT22Parser.ID)
                self.state = 131
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
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
        self.enterRule(localctx, 12, self.RULE_ids)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(MT22Parser.CM)
                self.state = 136
                self.match(MT22Parser.ID)
                self.state = 137
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
        self.enterRule(localctx, 14, self.RULE_vartyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
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
        self.enterRule(localctx, 16, self.RULE_idxlist)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.idx()
                self.state = 144
                self.idxs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
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
        self.enterRule(localctx, 18, self.RULE_idxs)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(MT22Parser.CM)
                self.state = 152
                self.idx()
                self.state = 153
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
        self.enterRule(localctx, 20, self.RULE_idx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(MT22Parser.LITINT)
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
        self.enterRule(localctx, 22, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MT22Parser.ID)
            self.state = 161
            self.match(MT22Parser.CL)
            self.state = 162
            self.match(MT22Parser.KWFUNC)
            self.state = 163
            self.functyp()
            self.state = 164
            self.match(MT22Parser.LB)
            self.state = 165
            self.paralist()
            self.state = 166
            self.match(MT22Parser.RB)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWINHERIT:
                self.state = 167
                self.match(MT22Parser.KWINHERIT)
                self.state = 168
                self.match(MT22Parser.ID)


            self.state = 171
            self.match(MT22Parser.LCB)
            self.state = 172
            self.bodylist()
            self.state = 173
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
        self.enterRule(localctx, 24, self.RULE_paralist)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.KWINHERIT, MT22Parser.KWOUT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.para()
                self.state = 176
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
        self.enterRule(localctx, 26, self.RULE_paras)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(MT22Parser.CM)
                self.state = 182
                self.para()
                self.state = 183
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
        self.enterRule(localctx, 28, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWINHERIT:
                self.state = 188
                self.match(MT22Parser.KWINHERIT)


            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWOUT:
                self.state = 191
                self.match(MT22Parser.KWOUT)


            self.state = 194
            self.match(MT22Parser.ID)
            self.state = 195
            self.match(MT22Parser.CL)
            self.state = 196
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
        self.enterRule(localctx, 30, self.RULE_functyp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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
        self.enterRule(localctx, 32, self.RULE_bodylist)
        try:
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.KWFOR, MT22Parser.KWWHILE, MT22Parser.KWDO, MT22Parser.KWBRK, MT22Parser.KWCONT, MT22Parser.KWRTN, MT22Parser.KWIF, MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT, MT22Parser.ID, MT22Parser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.bodydecl()
                self.state = 201
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


        def ifstmt(self):
            return self.getTypedRuleContext(MT22Parser.IfstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_bodydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodydecl" ):
                return visitor.visitBodydecl(self)
            else:
                return visitor.visitChildren(self)




    def bodydecl(self):

        localctx = MT22Parser.BodydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_bodydecl)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.ifstmt()
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


        def forstmt(self):
            return self.getTypedRuleContext(MT22Parser.ForstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(MT22Parser.WhilestmtContext,0)


        def dowhilestmt(self):
            return self.getTypedRuleContext(MT22Parser.DowhilestmtContext,0)


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
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.forstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.whilestmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.dowhilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 216
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 217
                self.rtnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 218
                self.callstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 219
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
        self.enterRule(localctx, 38, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 222
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.state = 223
                self.match(MT22Parser.ID)
                self.state = 224
                self.idxop()
                pass


            self.state = 227
            self.match(MT22Parser.EQL)
            self.state = 228
            self.expr()
            self.state = 229
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
        self.enterRule(localctx, 40, self.RULE_exprlist)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT, MT22Parser.ID, MT22Parser.SUBOP, MT22Parser.EXCOP, MT22Parser.LB, MT22Parser.LCB, MT22Parser.LITINT, MT22Parser.LITFLOAT, MT22Parser.LITBOO, MT22Parser.LITSTR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.expr()
                self.state = 232
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
        self.enterRule(localctx, 42, self.RULE_exprs)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(MT22Parser.CM)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def CONCATOP(self):
            return self.getToken(MT22Parser.CONCATOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.expr1()
                self.state = 245
                self.match(MT22Parser.CONCATOP)
                self.state = 246
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


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
            return MT22Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.expr2(0)
                self.state = 252
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQLOP) | (1 << MT22Parser.DIFOP) | (1 << MT22Parser.LARGEOP) | (1 << MT22Parser.LEQLOP) | (1 << MT22Parser.SMALLOP) | (1 << MT22Parser.SEQLOP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 253
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def ANDOP(self):
            return self.getToken(MT22Parser.ANDOP, 0)

        def OROP(self):
            return self.getToken(MT22Parser.OROP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 261
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 262
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ANDOP or _la==MT22Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 263
                    self.expr3(0) 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def ADDOP(self):
            return self.getToken(MT22Parser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(MT22Parser.SUBOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 272
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 273
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADDOP or _la==MT22Parser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 274
                    self.expr4(0) 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def MULOP(self):
            return self.getToken(MT22Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(MT22Parser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(MT22Parser.MODOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 288
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 283
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 284
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MULOP) | (1 << MT22Parser.DIVOP) | (1 << MT22Parser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 285
                    self.expr5() 
                self.state = 290
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCOP(self):
            return self.getToken(MT22Parser.EXCOP, 0)

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr5)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.EXCOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(MT22Parser.EXCOP)
                self.state = 292
                self.expr5()
                pass
            elif token in [MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT, MT22Parser.ID, MT22Parser.SUBOP, MT22Parser.LB, MT22Parser.LCB, MT22Parser.LITINT, MT22Parser.LITFLOAT, MT22Parser.LITBOO, MT22Parser.LITSTR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBOP(self):
            return self.getToken(MT22Parser.SUBOP, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr6)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(MT22Parser.SUBOP)
                self.state = 297
                self.expr6()
                pass
            elif token in [MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT, MT22Parser.ID, MT22Parser.LB, MT22Parser.LCB, MT22Parser.LITINT, MT22Parser.LITFLOAT, MT22Parser.LITBOO, MT22Parser.LITSTR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.operand()
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

        def idxop(self):
            return self.getTypedRuleContext(MT22Parser.IdxopContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MT22Parser.FunccallContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(MT22Parser.SubexprContext,0)


        def subarr(self):
            return self.getTypedRuleContext(MT22Parser.SubarrContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_operand)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.match(MT22Parser.LITINT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(MT22Parser.LITFLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(MT22Parser.LITBOO)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 304
                self.match(MT22Parser.LITSTR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 305
                self.match(MT22Parser.ID)
                self.state = 307
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 306
                    self.idxop()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 309
                self.funccall()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 310
                self.subexpr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 311
                self.subarr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 60, self.RULE_idxop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(MT22Parser.LSB)
            self.state = 315
            self.idxlist()
            self.state = 316
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def specialfunc(self):
            return self.getTypedRuleContext(MT22Parser.SpecialfuncContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MT22Parser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funccall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT]:
                self.state = 318
                self.specialfunc()
                pass
            elif token in [MT22Parser.ID]:
                self.state = 319
                self.match(MT22Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 322
            self.match(MT22Parser.LB)
            self.state = 323
            self.exprlist()
            self.state = 324
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = MT22Parser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(MT22Parser.LB)
            self.state = 327
            self.expr()
            self.state = 328
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubarrContext(ParserRuleContext):
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
            return MT22Parser.RULE_subarr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubarr" ):
                return visitor.visitSubarr(self)
            else:
                return visitor.visitChildren(self)




    def subarr(self):

        localctx = MT22Parser.SubarrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_subarr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(MT22Parser.LCB)
            self.state = 331
            self.exprlist()
            self.state = 332
            self.match(MT22Parser.RCB)
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

        def matchstmt(self):
            return self.getTypedRuleContext(MT22Parser.MatchstmtContext,0)


        def unmatchstmt(self):
            return self.getTypedRuleContext(MT22Parser.UnmatchstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MT22Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_ifstmt)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.matchstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.unmatchstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWIF(self):
            return self.getToken(MT22Parser.KWIF, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def matchstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.MatchstmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.MatchstmtContext,i)


        def KWELSE(self):
            return self.getToken(MT22Parser.KWELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_matchstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchstmt" ):
                return visitor.visitMatchstmt(self)
            else:
                return visitor.visitChildren(self)




    def matchstmt(self):

        localctx = MT22Parser.MatchstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_matchstmt)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.KWIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(MT22Parser.KWIF)
                self.state = 339
                self.match(MT22Parser.LB)
                self.state = 340
                self.expr()
                self.state = 341
                self.match(MT22Parser.RB)
                self.state = 342
                self.matchstmt()
                self.state = 343
                self.match(MT22Parser.KWELSE)
                self.state = 344
                self.matchstmt()
                pass
            elif token in [MT22Parser.KWFOR, MT22Parser.KWWHILE, MT22Parser.KWDO, MT22Parser.KWBRK, MT22Parser.KWCONT, MT22Parser.KWRTN, MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT, MT22Parser.ID, MT22Parser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.stmt()
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


    class UnmatchstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWIF(self):
            return self.getToken(MT22Parser.KWIF, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def ifstmt(self):
            return self.getTypedRuleContext(MT22Parser.IfstmtContext,0)


        def matchstmt(self):
            return self.getTypedRuleContext(MT22Parser.MatchstmtContext,0)


        def KWELSE(self):
            return self.getToken(MT22Parser.KWELSE, 0)

        def unmatchstmt(self):
            return self.getTypedRuleContext(MT22Parser.UnmatchstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_unmatchstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnmatchstmt" ):
                return visitor.visitUnmatchstmt(self)
            else:
                return visitor.visitChildren(self)




    def unmatchstmt(self):

        localctx = MT22Parser.UnmatchstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_unmatchstmt)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(MT22Parser.KWIF)
                self.state = 350
                self.match(MT22Parser.LB)
                self.state = 351
                self.expr()
                self.state = 352
                self.match(MT22Parser.RB)
                self.state = 353
                self.ifstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.match(MT22Parser.KWIF)
                self.state = 356
                self.match(MT22Parser.LB)
                self.state = 357
                self.expr()
                self.state = 358
                self.match(MT22Parser.RB)
                self.state = 359
                self.matchstmt()
                self.state = 360
                self.match(MT22Parser.KWELSE)
                self.state = 361
                self.unmatchstmt()
                pass


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
        self.enterRule(localctx, 74, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MT22Parser.KWFOR)
            self.state = 366
            self.match(MT22Parser.LB)
            self.state = 367
            self.match(MT22Parser.ID)
            self.state = 368
            self.match(MT22Parser.EQL)
            self.state = 369
            self.expr()
            self.state = 370
            self.match(MT22Parser.CM)
            self.state = 371
            self.expr()
            self.state = 372
            self.match(MT22Parser.CM)
            self.state = 373
            self.expr()
            self.state = 374
            self.match(MT22Parser.RB)
            self.state = 375
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWWHILE(self):
            return self.getToken(MT22Parser.KWWHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = MT22Parser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(MT22Parser.KWWHILE)
            self.state = 378
            self.match(MT22Parser.LB)
            self.state = 379
            self.expr()
            self.state = 380
            self.match(MT22Parser.RB)
            self.state = 381
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWDO(self):
            return self.getToken(MT22Parser.KWDO, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def KWWHILE(self):
            return self.getToken(MT22Parser.KWWHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhilestmt" ):
                return visitor.visitDowhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhilestmt(self):

        localctx = MT22Parser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(MT22Parser.KWDO)
            self.state = 384
            self.blockstmt()
            self.state = 385
            self.match(MT22Parser.KWWHILE)
            self.state = 386
            self.match(MT22Parser.LB)
            self.state = 387
            self.expr()
            self.state = 388
            self.match(MT22Parser.RB)
            self.state = 389
            self.match(MT22Parser.SM)
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
        self.enterRule(localctx, 80, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(MT22Parser.KWBRK)
            self.state = 392
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
        self.enterRule(localctx, 82, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(MT22Parser.KWCONT)
            self.state = 395
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
        self.enterRule(localctx, 84, self.RULE_rtnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(MT22Parser.KWRTN)
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 25)) & ~0x3f) == 0 and ((1 << (_la - 25)) & ((1 << (MT22Parser.SFREADINT - 25)) | (1 << (MT22Parser.SFPRINTINT - 25)) | (1 << (MT22Parser.SFREADFLOAT - 25)) | (1 << (MT22Parser.SFPRINTFLOAT - 25)) | (1 << (MT22Parser.SFREADBOOL - 25)) | (1 << (MT22Parser.SFPRINTBOOL - 25)) | (1 << (MT22Parser.SFREADSTR - 25)) | (1 << (MT22Parser.SFPRINTSTR - 25)) | (1 << (MT22Parser.SFSUPER - 25)) | (1 << (MT22Parser.SFPREVENT - 25)) | (1 << (MT22Parser.ID - 25)) | (1 << (MT22Parser.SUBOP - 25)) | (1 << (MT22Parser.EXCOP - 25)) | (1 << (MT22Parser.LB - 25)) | (1 << (MT22Parser.LCB - 25)) | (1 << (MT22Parser.LITINT - 25)) | (1 << (MT22Parser.LITFLOAT - 25)) | (1 << (MT22Parser.LITBOO - 25)) | (1 << (MT22Parser.LITSTR - 25)))) != 0):
                self.state = 398
                self.expr()


            self.state = 401
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

        def funccall(self):
            return self.getTypedRuleContext(MT22Parser.FunccallContext,0)


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
        self.enterRule(localctx, 86, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.funccall()
            self.state = 404
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
        self.enterRule(localctx, 88, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(MT22Parser.LCB)
            self.state = 407
            self.bodylist()
            self.state = 408
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SFREADINT(self):
            return self.getToken(MT22Parser.SFREADINT, 0)

        def SFPRINTINT(self):
            return self.getToken(MT22Parser.SFPRINTINT, 0)

        def SFREADFLOAT(self):
            return self.getToken(MT22Parser.SFREADFLOAT, 0)

        def SFPRINTFLOAT(self):
            return self.getToken(MT22Parser.SFPRINTFLOAT, 0)

        def SFREADBOOL(self):
            return self.getToken(MT22Parser.SFREADBOOL, 0)

        def SFPRINTBOOL(self):
            return self.getToken(MT22Parser.SFPRINTBOOL, 0)

        def SFREADSTR(self):
            return self.getToken(MT22Parser.SFREADSTR, 0)

        def SFPRINTSTR(self):
            return self.getToken(MT22Parser.SFPRINTSTR, 0)

        def SFSUPER(self):
            return self.getToken(MT22Parser.SFSUPER, 0)

        def SFPREVENT(self):
            return self.getToken(MT22Parser.SFPREVENT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_specialfunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecialfunc" ):
                return visitor.visitSpecialfunc(self)
            else:
                return visitor.visitChildren(self)




    def specialfunc(self):

        localctx = MT22Parser.SpecialfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_specialfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.SFREADINT) | (1 << MT22Parser.SFPRINTINT) | (1 << MT22Parser.SFREADFLOAT) | (1 << MT22Parser.SFPRINTFLOAT) | (1 << MT22Parser.SFREADBOOL) | (1 << MT22Parser.SFPRINTBOOL) | (1 << MT22Parser.SFREADSTR) | (1 << MT22Parser.SFPRINTSTR) | (1 << MT22Parser.SFSUPER) | (1 << MT22Parser.SFPREVENT))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.expr2_sempred
        self._predicates[25] = self.expr3_sempred
        self._predicates[26] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




