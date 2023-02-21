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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\u019b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3d\n\3\3\4\3\4\5\4h\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5o\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5}\n\5\3\5\3\5\5\5\u0081\n\5")
        buf.write("\3\6\3\6\3\6\5\6\u0086\n\6\3\7\3\7\3\7\3\7\5\7\u008c\n")
        buf.write("\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0096\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u009d\n\n\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00a5\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00ac\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00bb\n\17\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u00c5\n\20\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00cc\n\21\3\22\5\22\u00cf\n\22\3\22\5\22\u00d2\n\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u00de\n\24\3\25\3\25\5\25\u00e2\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00ee\n\26\3\27")
        buf.write("\3\27\3\27\5\27\u00f3\n\27\3\27\3\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\3\30\5\30\u00fd\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u0104\n\31\3\32\3\32\5\32\u0108\n\32\3\33\3\33\3")
        buf.write("\33\5\33\u010d\n\33\3\34\3\34\3\34\5\34\u0112\n\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\7\35\u0119\n\35\f\35\16\35\u011c")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u0127\n\37\3 \3 \3 \3 \3 \5 \u012e\n \3!\3!\3!\3!")
        buf.write("\3!\3!\7!\u0136\n!\f!\16!\u0139\13!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\7\"\u0141\n\"\f\"\16\"\u0144\13\"\3#\3#\3#\3#\3")
        buf.write("#\3#\7#\u014c\n#\f#\16#\u014f\13#\3$\3$\3$\3$\3$\3$\5")
        buf.write("$\u0157\n$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0162\n$\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+")
        buf.write("\3+\5+\u0188\n+\3+\3+\3,\3,\5,\u018e\n,\3,\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3-\3.\3.\3.\2\68@BD/\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\2\t\3\2\b\f\3\2\7\f\3\2/\64\3\2-.\3\2\'(\3\2)+\3\2\34")
        buf.write("%\2\u019e\2\\\3\2\2\2\4c\3\2\2\2\6g\3\2\2\2\b\u0080\3")
        buf.write("\2\2\2\n\u0085\3\2\2\2\f\u008b\3\2\2\2\16\u008d\3\2\2")
        buf.write("\2\20\u0095\3\2\2\2\22\u009c\3\2\2\2\24\u009e\3\2\2\2")
        buf.write("\26\u00a4\3\2\2\2\30\u00ab\3\2\2\2\32\u00ad\3\2\2\2\34")
        buf.write("\u00b1\3\2\2\2\36\u00c4\3\2\2\2 \u00cb\3\2\2\2\"\u00ce")
        buf.write("\3\2\2\2$\u00d7\3\2\2\2&\u00dd\3\2\2\2(\u00e1\3\2\2\2")
        buf.write("*\u00ed\3\2\2\2,\u00f2\3\2\2\2.\u00fc\3\2\2\2\60\u0103")
        buf.write("\3\2\2\2\62\u0107\3\2\2\2\64\u010c\3\2\2\2\66\u0111\3")
        buf.write("\2\2\28\u0113\3\2\2\2:\u011d\3\2\2\2<\u0126\3\2\2\2>\u012d")
        buf.write("\3\2\2\2@\u012f\3\2\2\2B\u013a\3\2\2\2D\u0145\3\2\2\2")
        buf.write("F\u0161\3\2\2\2H\u0163\3\2\2\2J\u0165\3\2\2\2L\u0171\3")
        buf.write("\2\2\2N\u0177\3\2\2\2P\u017f\3\2\2\2R\u0182\3\2\2\2T\u0185")
        buf.write("\3\2\2\2V\u018d\3\2\2\2X\u0194\3\2\2\2Z\u0198\3\2\2\2")
        buf.write("\\]\5\4\3\2]^\7\2\2\3^\3\3\2\2\2_`\5\6\4\2`a\5\4\3\2a")
        buf.write("d\3\2\2\2bd\5\6\4\2c_\3\2\2\2cb\3\2\2\2d\5\3\2\2\2eh\5")
        buf.write("\b\5\2fh\5\34\17\2ge\3\2\2\2gf\3\2\2\2h\7\3\2\2\2ij\5")
        buf.write("\n\6\2jk\79\2\2kn\5\16\b\2lm\7@\2\2mo\5.\30\2nl\3\2\2")
        buf.write("\2no\3\2\2\2op\3\2\2\2pq\78\2\2q\u0081\3\2\2\2rs\5\n\6")
        buf.write("\2st\79\2\2tu\7\r\2\2uv\7<\2\2vw\5\20\t\2wx\7=\2\2xy\7")
        buf.write("\32\2\2y|\5\16\b\2z{\7@\2\2{}\5\26\f\2|z\3\2\2\2|}\3\2")
        buf.write("\2\2}~\3\2\2\2~\177\78\2\2\177\u0081\3\2\2\2\u0080i\3")
        buf.write("\2\2\2\u0080r\3\2\2\2\u0081\t\3\2\2\2\u0082\u0083\7&\2")
        buf.write("\2\u0083\u0086\5\f\7\2\u0084\u0086\7&\2\2\u0085\u0082")
        buf.write("\3\2\2\2\u0085\u0084\3\2\2\2\u0086\13\3\2\2\2\u0087\u0088")
        buf.write("\7\67\2\2\u0088\u0089\7&\2\2\u0089\u008c\5\f\7\2\u008a")
        buf.write("\u008c\3\2\2\2\u008b\u0087\3\2\2\2\u008b\u008a\3\2\2\2")
        buf.write("\u008c\r\3\2\2\2\u008d\u008e\t\2\2\2\u008e\17\3\2\2\2")
        buf.write("\u008f\u0090\5\24\13\2\u0090\u0091\5\22\n\2\u0091\u0096")
        buf.write("\3\2\2\2\u0092\u0093\5\24\13\2\u0093\u0094\b\t\1\2\u0094")
        buf.write("\u0096\3\2\2\2\u0095\u008f\3\2\2\2\u0095\u0092\3\2\2\2")
        buf.write("\u0096\21\3\2\2\2\u0097\u0098\7\67\2\2\u0098\u0099\5\24")
        buf.write("\13\2\u0099\u009a\5\22\n\2\u009a\u009d\3\2\2\2\u009b\u009d")
        buf.write("\b\n\1\2\u009c\u0097\3\2\2\2\u009c\u009b\3\2\2\2\u009d")
        buf.write("\23\3\2\2\2\u009e\u009f\7A\2\2\u009f\25\3\2\2\2\u00a0")
        buf.write("\u00a1\5\32\16\2\u00a1\u00a2\5\30\r\2\u00a2\u00a5\3\2")
        buf.write("\2\2\u00a3\u00a5\5\32\16\2\u00a4\u00a0\3\2\2\2\u00a4\u00a3")
        buf.write("\3\2\2\2\u00a5\27\3\2\2\2\u00a6\u00a7\7\67\2\2\u00a7\u00a8")
        buf.write("\5\32\16\2\u00a8\u00a9\5\30\r\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00ac\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab\u00aa\3\2\2\2")
        buf.write("\u00ac\31\3\2\2\2\u00ad\u00ae\7>\2\2\u00ae\u00af\5.\30")
        buf.write("\2\u00af\u00b0\7?\2\2\u00b0\33\3\2\2\2\u00b1\u00b2\7&")
        buf.write("\2\2\u00b2\u00b3\79\2\2\u00b3\u00b4\7\17\2\2\u00b4\u00b5")
        buf.write("\5$\23\2\u00b5\u00b6\7:\2\2\u00b6\u00b7\5\36\20\2\u00b7")
        buf.write("\u00ba\7;\2\2\u00b8\u00b9\7\16\2\2\u00b9\u00bb\7&\2\2")
        buf.write("\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\3")
        buf.write("\2\2\2\u00bc\u00bd\7>\2\2\u00bd\u00be\5&\24\2\u00be\u00bf")
        buf.write("\7?\2\2\u00bf\35\3\2\2\2\u00c0\u00c1\5\"\22\2\u00c1\u00c2")
        buf.write("\5 \21\2\u00c2\u00c5\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4")
        buf.write("\u00c0\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\37\3\2\2\2\u00c6")
        buf.write("\u00c7\7\67\2\2\u00c7\u00c8\5\"\22\2\u00c8\u00c9\5 \21")
        buf.write("\2\u00c9\u00cc\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c6")
        buf.write("\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc!\3\2\2\2\u00cd\u00cf")
        buf.write("\7\16\2\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00d2\7\33\2\2\u00d1\u00d0\3\2\2")
        buf.write("\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4")
        buf.write("\7&\2\2\u00d4\u00d5\79\2\2\u00d5\u00d6\5\16\b\2\u00d6")
        buf.write("#\3\2\2\2\u00d7\u00d8\t\3\2\2\u00d8%\3\2\2\2\u00d9\u00da")
        buf.write("\5(\25\2\u00da\u00db\5&\24\2\u00db\u00de\3\2\2\2\u00dc")
        buf.write("\u00de\3\2\2\2\u00dd\u00d9\3\2\2\2\u00dd\u00dc\3\2\2\2")
        buf.write("\u00de\'\3\2\2\2\u00df\u00e2\5\b\5\2\u00e0\u00e2\5*\26")
        buf.write("\2\u00e1\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2)\3\2")
        buf.write("\2\2\u00e3\u00ee\5,\27\2\u00e4\u00ee\5H%\2\u00e5\u00ee")
        buf.write("\5J&\2\u00e6\u00ee\5L\'\2\u00e7\u00ee\5N(\2\u00e8\u00ee")
        buf.write("\5P)\2\u00e9\u00ee\5R*\2\u00ea\u00ee\5T+\2\u00eb\u00ee")
        buf.write("\5V,\2\u00ec\u00ee\5X-\2\u00ed\u00e3\3\2\2\2\u00ed\u00e4")
        buf.write("\3\2\2\2\u00ed\u00e5\3\2\2\2\u00ed\u00e6\3\2\2\2\u00ed")
        buf.write("\u00e7\3\2\2\2\u00ed\u00e8\3\2\2\2\u00ed\u00e9\3\2\2\2")
        buf.write("\u00ed\u00ea\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3")
        buf.write("\2\2\2\u00ee+\3\2\2\2\u00ef\u00f3\7&\2\2\u00f0\u00f1\7")
        buf.write("&\2\2\u00f1\u00f3\5:\36\2\u00f2\u00ef\3\2\2\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\7@\2\2\u00f5")
        buf.write("\u00f6\5\62\32\2\u00f6\u00f7\78\2\2\u00f7-\3\2\2\2\u00f8")
        buf.write("\u00f9\5\62\32\2\u00f9\u00fa\5\60\31\2\u00fa\u00fd\3\2")
        buf.write("\2\2\u00fb\u00fd\3\2\2\2\u00fc\u00f8\3\2\2\2\u00fc\u00fb")
        buf.write("\3\2\2\2\u00fd/\3\2\2\2\u00fe\u00ff\7\67\2\2\u00ff\u0100")
        buf.write("\5\62\32\2\u0100\u0101\5\60\31\2\u0101\u0104\3\2\2\2\u0102")
        buf.write("\u0104\3\2\2\2\u0103\u00fe\3\2\2\2\u0103\u0102\3\2\2\2")
        buf.write("\u0104\61\3\2\2\2\u0105\u0108\5\64\33\2\u0106\u0108\5")
        buf.write("<\37\2\u0107\u0105\3\2\2\2\u0107\u0106\3\2\2\2\u0108\63")
        buf.write("\3\2\2\2\u0109\u010a\7,\2\2\u010a\u010d\5\64\33\2\u010b")
        buf.write("\u010d\5\66\34\2\u010c\u0109\3\2\2\2\u010c\u010b\3\2\2")
        buf.write("\2\u010d\65\3\2\2\2\u010e\u010f\7(\2\2\u010f\u0112\5\66")
        buf.write("\34\2\u0110\u0112\58\35\2\u0111\u010e\3\2\2\2\u0111\u0110")
        buf.write("\3\2\2\2\u0112\67\3\2\2\2\u0113\u0114\b\35\1\2\u0114\u0115")
        buf.write("\5F$\2\u0115\u011a\3\2\2\2\u0116\u0117\f\4\2\2\u0117\u0119")
        buf.write("\5:\36\2\u0118\u0116\3\2\2\2\u0119\u011c\3\2\2\2\u011a")
        buf.write("\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b9\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011d\u011e\7<\2\2\u011e\u011f\5\20\t\2")
        buf.write("\u011f\u0120\7=\2\2\u0120;\3\2\2\2\u0121\u0122\5> \2\u0122")
        buf.write("\u0123\7\65\2\2\u0123\u0124\5> \2\u0124\u0127\3\2\2\2")
        buf.write("\u0125\u0127\5> \2\u0126\u0121\3\2\2\2\u0126\u0125\3\2")
        buf.write("\2\2\u0127=\3\2\2\2\u0128\u0129\5@!\2\u0129\u012a\t\4")
        buf.write("\2\2\u012a\u012b\5@!\2\u012b\u012e\3\2\2\2\u012c\u012e")
        buf.write("\5@!\2\u012d\u0128\3\2\2\2\u012d\u012c\3\2\2\2\u012e?")
        buf.write("\3\2\2\2\u012f\u0130\b!\1\2\u0130\u0131\5B\"\2\u0131\u0137")
        buf.write("\3\2\2\2\u0132\u0133\f\4\2\2\u0133\u0134\t\5\2\2\u0134")
        buf.write("\u0136\5B\"\2\u0135\u0132\3\2\2\2\u0136\u0139\3\2\2\2")
        buf.write("\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138A\3\2\2")
        buf.write("\2\u0139\u0137\3\2\2\2\u013a\u013b\b\"\1\2\u013b\u013c")
        buf.write("\5D#\2\u013c\u0142\3\2\2\2\u013d\u013e\f\4\2\2\u013e\u013f")
        buf.write("\t\6\2\2\u013f\u0141\5D#\2\u0140\u013d\3\2\2\2\u0141\u0144")
        buf.write("\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143")
        buf.write("C\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0146\b#\1\2\u0146")
        buf.write("\u0147\5F$\2\u0147\u014d\3\2\2\2\u0148\u0149\f\4\2\2\u0149")
        buf.write("\u014a\t\7\2\2\u014a\u014c\5F$\2\u014b\u0148\3\2\2\2\u014c")
        buf.write("\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014eE\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0162\7A\2\2")
        buf.write("\u0151\u0162\7B\2\2\u0152\u0162\7C\2\2\u0153\u0162\7D")
        buf.write("\2\2\u0154\u0156\7&\2\2\u0155\u0157\5:\36\2\u0156\u0155")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0162\3\2\2\2\u0158")
        buf.write("\u0162\5V,\2\u0159\u015a\7:\2\2\u015a\u015b\5\62\32\2")
        buf.write("\u015b\u015c\7;\2\2\u015c\u0162\3\2\2\2\u015d\u015e\7")
        buf.write(">\2\2\u015e\u015f\5.\30\2\u015f\u0160\7?\2\2\u0160\u0162")
        buf.write("\3\2\2\2\u0161\u0150\3\2\2\2\u0161\u0151\3\2\2\2\u0161")
        buf.write("\u0152\3\2\2\2\u0161\u0153\3\2\2\2\u0161\u0154\3\2\2\2")
        buf.write("\u0161\u0158\3\2\2\2\u0161\u0159\3\2\2\2\u0161\u015d\3")
        buf.write("\2\2\2\u0162G\3\2\2\2\u0163\u0164\7\3\2\2\u0164I\3\2\2")
        buf.write("\2\u0165\u0166\7\22\2\2\u0166\u0167\7:\2\2\u0167\u0168")
        buf.write("\7&\2\2\u0168\u0169\7@\2\2\u0169\u016a\5\62\32\2\u016a")
        buf.write("\u016b\7\67\2\2\u016b\u016c\5\62\32\2\u016c\u016d\7\67")
        buf.write("\2\2\u016d\u016e\5\62\32\2\u016e\u016f\7;\2\2\u016f\u0170")
        buf.write("\5*\26\2\u0170K\3\2\2\2\u0171\u0172\7\23\2\2\u0172\u0173")
        buf.write("\7:\2\2\u0173\u0174\5\62\32\2\u0174\u0175\7;\2\2\u0175")
        buf.write("\u0176\5*\26\2\u0176M\3\2\2\2\u0177\u0178\7\24\2\2\u0178")
        buf.write("\u0179\5X-\2\u0179\u017a\7\23\2\2\u017a\u017b\7:\2\2\u017b")
        buf.write("\u017c\5\62\32\2\u017c\u017d\7;\2\2\u017d\u017e\78\2\2")
        buf.write("\u017eO\3\2\2\2\u017f\u0180\7\25\2\2\u0180\u0181\78\2")
        buf.write("\2\u0181Q\3\2\2\2\u0182\u0183\7\26\2\2\u0183\u0184\78")
        buf.write("\2\2\u0184S\3\2\2\2\u0185\u0187\7\27\2\2\u0186\u0188\5")
        buf.write("\62\32\2\u0187\u0186\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018a\78\2\2\u018aU\3\2\2\2\u018b")
        buf.write("\u018e\5Z.\2\u018c\u018e\7&\2\2\u018d\u018b\3\2\2\2\u018d")
        buf.write("\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\7:\2\2")
        buf.write("\u0190\u0191\5.\30\2\u0191\u0192\7;\2\2\u0192\u0193\7")
        buf.write("8\2\2\u0193W\3\2\2\2\u0194\u0195\7>\2\2\u0195\u0196\5")
        buf.write("&\24\2\u0196\u0197\7?\2\2\u0197Y\3\2\2\2\u0198\u0199\t")
        buf.write("\b\2\2\u0199[\3\2\2\2%cgn|\u0080\u0085\u008b\u0095\u009c")
        buf.write("\u00a4\u00ab\u00ba\u00c4\u00cb\u00ce\u00d1\u00dd\u00e1")
        buf.write("\u00ed\u00f2\u00fc\u0103\u0107\u010c\u0111\u011a\u0126")
        buf.write("\u012d\u0137\u0142\u014d\u0156\u0161\u0187\u018d")
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
                     "'out'", "'readInteger'", "'printInteger'", "'readFloat'", 
                     "'writeFloat'", "'readBoolean'", "'printBoolean'", 
                     "'readString'", "'printString'", "'super'", "'preventDefault()'", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'>'", "'>='", "'<'", 
                     "'<='", "'::'", "'.'", "','", "';'", "':'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WS", "CCOMMENT", "CPPCOMMENT", 
                      "KWVOID", "KWAUTO", "KWINT", "KWFLOAT", "KWBOO", "KWSTR", 
                      "KWARR", "KWINHERIT", "KWFUNC", "KWTRUE", "KWFALSE", 
                      "KWFOR", "KWWHILE", "KWDO", "KWBRK", "KWCONT", "KWRTN", 
                      "KWIF", "KWELSE", "KWOF", "KWOUT", "SFREADINT", "SFPRINTINT", 
                      "SFREADFLOAT", "SFPRINTFLOAT", "SFREADBOOL", "SFPRINTBOOL", 
                      "SFREADSTR", "SFPRINTSTR", "SFSUPER", "SFPREVENT", 
                      "ID", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                      "EXCOP", "ANDOP", "OROP", "EQLOP", "DIFOP", "LARGEOP", 
                      "LEQLOP", "SMALLOP", "SEQLOP", "CONCATOP", "DOT", 
                      "CM", "SM", "CL", "LB", "RB", "LSB", "RSB", "LCB", 
                      "RCB", "EQL", "LITINT", "LITFLOAT", "LITBOO", "LITSTR", 
                      "ERROR_CHAR", "NCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
    RULE_whilestmt = 37
    RULE_dowhilestmt = 38
    RULE_breakstmt = 39
    RULE_continuestmt = 40
    RULE_rtnstmt = 41
    RULE_callstmt = 42
    RULE_blockstmt = 43
    RULE_specialfunc = 44

    ruleNames =  [ "program", "declist", "decl", "vardecl", "idlist", "ids", 
                   "vartyp", "idxlist", "idxs", "idx", "arraylist", "arrays", 
                   "array", "funcdecl", "paralist", "paras", "para", "functyp", 
                   "bodylist", "bodydecl", "stmt", "assignstmt", "exprlist", 
                   "exprs", "expr", "unexpr", "unexpr1", "unexpr2", "idxop", 
                   "biexpr", "biexpr1", "biexpr2", "biexpr3", "biexpr4", 
                   "operand", "ifstmt", "forstmt", "whilestmt", "dowhilestmt", 
                   "breakstmt", "continuestmt", "rtnstmt", "callstmt", "blockstmt", 
                   "specialfunc" ]

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
    SFREADINT=26
    SFPRINTINT=27
    SFREADFLOAT=28
    SFPRINTFLOAT=29
    SFREADBOOL=30
    SFPRINTBOOL=31
    SFREADSTR=32
    SFPRINTSTR=33
    SFSUPER=34
    SFPREVENT=35
    ID=36
    ADDOP=37
    SUBOP=38
    MULOP=39
    DIVOP=40
    MODOP=41
    EXCOP=42
    ANDOP=43
    OROP=44
    EQLOP=45
    DIFOP=46
    LARGEOP=47
    LEQLOP=48
    SMALLOP=49
    SEQLOP=50
    CONCATOP=51
    DOT=52
    CM=53
    SM=54
    CL=55
    LB=56
    RB=57
    LSB=58
    RSB=59
    LCB=60
    RCB=61
    EQL=62
    LITINT=63
    LITFLOAT=64
    LITBOO=65
    LITSTR=66
    ERROR_CHAR=67
    NCLOSE_STRING=68
    ILLEGAL_ESCAPE=69

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
            self.state = 90
            self.declist()
            self.state = 91
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
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.decl()
                self.state = 94
                self.declist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
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
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
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
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.idlist()
                self.state = 104
                self.match(MT22Parser.CL)
                self.state = 105
                self.vartyp()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MT22Parser.EQL:
                    self.state = 106
                    self.match(MT22Parser.EQL)
                    self.state = 107
                    self.exprlist()


                self.state = 110
                self.match(MT22Parser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.idlist()
                self.state = 113
                self.match(MT22Parser.CL)
                self.state = 114
                self.match(MT22Parser.KWARR)
                self.state = 115
                self.match(MT22Parser.LSB)
                self.state = 116
                self.idxlist()
                self.state = 117
                self.match(MT22Parser.RSB)
                self.state = 118
                self.match(MT22Parser.KWOF)
                self.state = 119
                self.vartyp()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MT22Parser.EQL:
                    self.state = 120
                    self.match(MT22Parser.EQL)
                    self.state = 121
                    self.arraylist()


                self.state = 124
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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(MT22Parser.ID)
                self.state = 129
                self.ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
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
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(MT22Parser.CM)
                self.state = 134
                self.match(MT22Parser.ID)
                self.state = 135
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
            self.state = 139
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
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.idx()
                self.state = 142
                self.idxs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
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
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(MT22Parser.CM)
                self.state = 150
                self.idx()
                self.state = 151
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
            self.state = 156
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
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.array()
                self.state = 159
                self.arrays()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
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
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(MT22Parser.CM)
                self.state = 165
                self.array()
                self.state = 166
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
            self.state = 171
            self.match(MT22Parser.LCB)
            self.state = 172
            self.exprlist()
            self.state = 173
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
            self.state = 175
            self.match(MT22Parser.ID)
            self.state = 176
            self.match(MT22Parser.CL)
            self.state = 177
            self.match(MT22Parser.KWFUNC)
            self.state = 178
            self.functyp()
            self.state = 179
            self.match(MT22Parser.LB)
            self.state = 180
            self.paralist()
            self.state = 181
            self.match(MT22Parser.RB)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWINHERIT:
                self.state = 182
                self.match(MT22Parser.KWINHERIT)
                self.state = 183
                self.match(MT22Parser.ID)


            self.state = 186
            self.match(MT22Parser.LCB)
            self.state = 187
            self.bodylist()
            self.state = 188
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
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.KWINHERIT, MT22Parser.KWOUT, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.para()
                self.state = 191
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
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(MT22Parser.CM)
                self.state = 197
                self.para()
                self.state = 198
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
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWINHERIT:
                self.state = 203
                self.match(MT22Parser.KWINHERIT)


            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.KWOUT:
                self.state = 206
                self.match(MT22Parser.KWOUT)


            self.state = 209
            self.match(MT22Parser.ID)
            self.state = 210
            self.match(MT22Parser.CL)
            self.state = 211
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
            self.state = 213
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
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.T__0, MT22Parser.KWFOR, MT22Parser.KWWHILE, MT22Parser.KWDO, MT22Parser.KWBRK, MT22Parser.KWCONT, MT22Parser.KWRTN, MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT, MT22Parser.ID, MT22Parser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.bodydecl()
                self.state = 216
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
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
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
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.forstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.dowhilestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 230
                self.breakstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 231
                self.continuestmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 232
                self.rtnstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 233
                self.callstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 234
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
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 237
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.state = 238
                self.match(MT22Parser.ID)
                self.state = 239
                self.idxop()
                pass


            self.state = 242
            self.match(MT22Parser.EQL)
            self.state = 243
            self.expr()
            self.state = 244
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
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT, MT22Parser.ID, MT22Parser.SUBOP, MT22Parser.EXCOP, MT22Parser.LB, MT22Parser.LCB, MT22Parser.LITINT, MT22Parser.LITFLOAT, MT22Parser.LITBOO, MT22Parser.LITSTR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.expr()
                self.state = 247
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
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(MT22Parser.CM)
                self.state = 253
                self.expr()
                self.state = 254
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
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.unexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
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
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.EXCOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(MT22Parser.EXCOP)
                self.state = 264
                self.unexpr()
                pass
            elif token in [MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT, MT22Parser.ID, MT22Parser.SUBOP, MT22Parser.LB, MT22Parser.LCB, MT22Parser.LITINT, MT22Parser.LITFLOAT, MT22Parser.LITBOO, MT22Parser.LITSTR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
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
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(MT22Parser.SUBOP)
                self.state = 269
                self.unexpr1()
                pass
            elif token in [MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT, MT22Parser.ID, MT22Parser.LB, MT22Parser.LCB, MT22Parser.LITINT, MT22Parser.LITFLOAT, MT22Parser.LITBOO, MT22Parser.LITSTR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
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
            self.state = 274
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Unexpr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unexpr2)
                    self.state = 276
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 277
                    self.idxop() 
                self.state = 282
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
            self.state = 283
            self.match(MT22Parser.LSB)
            self.state = 284
            self.idxlist()
            self.state = 285
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
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.biexpr1()
                self.state = 288
                self.match(MT22Parser.CONCATOP)
                self.state = 289
                self.biexpr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.biexpr2(0)
                self.state = 295
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQLOP) | (1 << MT22Parser.DIFOP) | (1 << MT22Parser.LARGEOP) | (1 << MT22Parser.LEQLOP) | (1 << MT22Parser.SMALLOP) | (1 << MT22Parser.SEQLOP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 296
                self.biexpr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
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
            self.state = 302
            self.biexpr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Biexpr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_biexpr2)
                    self.state = 304
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 305
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ANDOP or _la==MT22Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 306
                    self.biexpr3(0) 
                self.state = 311
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
            self.state = 313
            self.biexpr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Biexpr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_biexpr3)
                    self.state = 315
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 316
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADDOP or _la==MT22Parser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 317
                    self.biexpr4(0) 
                self.state = 322
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
            self.state = 324
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Biexpr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_biexpr4)
                    self.state = 326
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 327
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MULOP) | (1 << MT22Parser.DIVOP) | (1 << MT22Parser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 328
                    self.operand() 
                self.state = 333
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

        def idxop(self):
            return self.getTypedRuleContext(MT22Parser.IdxopContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

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
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(MT22Parser.LITINT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(MT22Parser.LITFLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 336
                self.match(MT22Parser.LITBOO)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 337
                self.match(MT22Parser.LITSTR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 338
                self.match(MT22Parser.ID)
                self.state = 340
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 339
                    self.idxop()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 342
                self.callstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 343
                self.match(MT22Parser.LB)
                self.state = 344
                self.expr()
                self.state = 345
                self.match(MT22Parser.RB)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 347
                self.match(MT22Parser.LCB)
                self.state = 348
                self.exprlist()
                self.state = 349
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
            self.state = 353
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
            self.state = 355
            self.match(MT22Parser.KWFOR)
            self.state = 356
            self.match(MT22Parser.LB)
            self.state = 357
            self.match(MT22Parser.ID)
            self.state = 358
            self.match(MT22Parser.EQL)
            self.state = 359
            self.expr()
            self.state = 360
            self.match(MT22Parser.CM)
            self.state = 361
            self.expr()
            self.state = 362
            self.match(MT22Parser.CM)
            self.state = 363
            self.expr()
            self.state = 364
            self.match(MT22Parser.RB)
            self.state = 365
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
        self.enterRule(localctx, 74, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(MT22Parser.KWWHILE)
            self.state = 368
            self.match(MT22Parser.LB)
            self.state = 369
            self.expr()
            self.state = 370
            self.match(MT22Parser.RB)
            self.state = 371
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
        self.enterRule(localctx, 76, self.RULE_dowhilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(MT22Parser.KWDO)
            self.state = 374
            self.blockstmt()
            self.state = 375
            self.match(MT22Parser.KWWHILE)
            self.state = 376
            self.match(MT22Parser.LB)
            self.state = 377
            self.expr()
            self.state = 378
            self.match(MT22Parser.RB)
            self.state = 379
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
        self.enterRule(localctx, 78, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(MT22Parser.KWBRK)
            self.state = 382
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
        self.enterRule(localctx, 80, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MT22Parser.KWCONT)
            self.state = 385
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
        self.enterRule(localctx, 82, self.RULE_rtnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(MT22Parser.KWRTN)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 26)) & ~0x3f) == 0 and ((1 << (_la - 26)) & ((1 << (MT22Parser.SFREADINT - 26)) | (1 << (MT22Parser.SFPRINTINT - 26)) | (1 << (MT22Parser.SFREADFLOAT - 26)) | (1 << (MT22Parser.SFPRINTFLOAT - 26)) | (1 << (MT22Parser.SFREADBOOL - 26)) | (1 << (MT22Parser.SFPRINTBOOL - 26)) | (1 << (MT22Parser.SFREADSTR - 26)) | (1 << (MT22Parser.SFPRINTSTR - 26)) | (1 << (MT22Parser.SFSUPER - 26)) | (1 << (MT22Parser.SFPREVENT - 26)) | (1 << (MT22Parser.ID - 26)) | (1 << (MT22Parser.SUBOP - 26)) | (1 << (MT22Parser.EXCOP - 26)) | (1 << (MT22Parser.LB - 26)) | (1 << (MT22Parser.LCB - 26)) | (1 << (MT22Parser.LITINT - 26)) | (1 << (MT22Parser.LITFLOAT - 26)) | (1 << (MT22Parser.LITBOO - 26)) | (1 << (MT22Parser.LITSTR - 26)))) != 0):
                self.state = 388
                self.expr()


            self.state = 391
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

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SM(self):
            return self.getToken(MT22Parser.SM, 0)

        def specialfunc(self):
            return self.getTypedRuleContext(MT22Parser.SpecialfuncContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SFREADINT, MT22Parser.SFPRINTINT, MT22Parser.SFREADFLOAT, MT22Parser.SFPRINTFLOAT, MT22Parser.SFREADBOOL, MT22Parser.SFPRINTBOOL, MT22Parser.SFREADSTR, MT22Parser.SFPRINTSTR, MT22Parser.SFSUPER, MT22Parser.SFPREVENT]:
                self.state = 393
                self.specialfunc()
                pass
            elif token in [MT22Parser.ID]:
                self.state = 394
                self.match(MT22Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 397
            self.match(MT22Parser.LB)
            self.state = 398
            self.exprlist()
            self.state = 399
            self.match(MT22Parser.RB)
            self.state = 400
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
        self.enterRule(localctx, 86, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(MT22Parser.LCB)
            self.state = 403
            self.bodylist()
            self.state = 404
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
        self.enterRule(localctx, 88, self.RULE_specialfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
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
         




