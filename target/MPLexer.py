# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u025f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\5\25\u00e5\n\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\6O\u01c1")
        buf.write("\nO\rO\16O\u01c2\3O\3O\3P\5P\u01c8\nP\3P\7P\u01cb\nP\f")
        buf.write("P\16P\u01ce\13P\3Q\6Q\u01d1\nQ\rQ\16Q\u01d2\3R\6R\u01d6")
        buf.write("\nR\rR\16R\u01d7\3R\5R\u01db\nR\3R\7R\u01de\nR\fR\16R")
        buf.write("\u01e1\13R\3R\7R\u01e4\nR\fR\16R\u01e7\13R\3R\3R\5R\u01eb")
        buf.write("\nR\3R\6R\u01ee\nR\rR\16R\u01ef\5R\u01f2\nR\3R\7R\u01f5")
        buf.write("\nR\fR\16R\u01f8\13R\3R\5R\u01fb\nR\3R\6R\u01fe\nR\rR")
        buf.write("\16R\u01ff\3R\3R\5R\u0204\nR\3R\6R\u0207\nR\rR\16R\u0208")
        buf.write("\5R\u020b\nR\5R\u020d\nR\3S\3S\3S\3S\7S\u0213\nS\fS\16")
        buf.write("S\u0216\13S\3S\3S\3S\3T\3T\5T\u021d\nT\3T\3T\3U\3U\5U")
        buf.write("\u0223\nU\3V\3V\3V\3V\7V\u0229\nV\fV\16V\u022c\13V\3V")
        buf.write("\3V\3V\3W\3W\7W\u0233\nW\fW\16W\u0236\13W\3W\3W\3X\3X")
        buf.write("\3X\3X\7X\u023e\nX\fX\16X\u0241\13X\3Y\3Y\3Y\5Y\u0246")
        buf.write("\nY\3Y\7Y\u0249\nY\fY\16Y\u024c\13Y\3Y\3Y\3Z\3Z\3Z\3Z")
        buf.write("\7Z\u0254\nZ\fZ\16Z\u0257\13Z\3Z\3Z\3Z\3Z\3[\3[\3[\4\u022a")
        buf.write("\u0234\2\\\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\2i\2k\2")
        buf.write("m\2o\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093")
        buf.write("\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\65\u009f\66\u00a1")
        buf.write("\67\u00a38\u00a59\u00a7:\u00a9;\u00ab<\u00ad=\u00af>\u00b1")
        buf.write("?\u00b3@\u00b5A\3\2$\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4")
        buf.write("\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMm")
        buf.write("m\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2")
        buf.write("TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4")
        buf.write("\2[[{{\4\2\\\\||\3\2\62;\5\2\13\f\17\17\"\"\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\n\2$$))^^ddhhppttvv\7\2\n\f\16\17$$)")
        buf.write(")^^\4\2\f\f\17\17\7\2\13\f\16\17$$))^^\2\u0260\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2\u009d\3\2")
        buf.write("\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2")
        buf.write("\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\3\u00b7\3\2\2\2\5\u00b9")
        buf.write("\3\2\2\2\7\u00bb\3\2\2\2\t\u00bd\3\2\2\2\13\u00bf\3\2")
        buf.write("\2\2\r\u00c1\3\2\2\2\17\u00c3\3\2\2\2\21\u00c5\3\2\2\2")
        buf.write("\23\u00c7\3\2\2\2\25\u00ca\3\2\2\2\27\u00cc\3\2\2\2\31")
        buf.write("\u00ce\3\2\2\2\33\u00d1\3\2\2\2\35\u00d3\3\2\2\2\37\u00d6")
        buf.write("\3\2\2\2!\u00d8\3\2\2\2#\u00da\3\2\2\2%\u00dc\3\2\2\2")
        buf.write("\'\u00df\3\2\2\2)\u00e4\3\2\2\2+\u00e6\3\2\2\2-\u00ec")
        buf.write("\3\2\2\2/\u00f5\3\2\2\2\61\u00f9\3\2\2\2\63\u00fc\3\2")
        buf.write("\2\2\65\u0103\3\2\2\2\67\u0106\3\2\2\29\u0109\3\2\2\2")
        buf.write(";\u010e\3\2\2\2=\u0113\3\2\2\2?\u011a\3\2\2\2A\u0120\3")
        buf.write("\2\2\2C\u0126\3\2\2\2E\u012a\3\2\2\2G\u0133\3\2\2\2I\u013d")
        buf.write("\3\2\2\2K\u0141\3\2\2\2M\u0146\3\2\2\2O\u014c\3\2\2\2")
        buf.write("Q\u0152\3\2\2\2S\u0155\3\2\2\2U\u015a\3\2\2\2W\u0162\3")
        buf.write("\2\2\2Y\u016a\3\2\2\2[\u0171\3\2\2\2]\u0175\3\2\2\2_\u0179")
        buf.write("\3\2\2\2a\u017c\3\2\2\2c\u0180\3\2\2\2e\u0184\3\2\2\2")
        buf.write("g\u0189\3\2\2\2i\u018b\3\2\2\2k\u018d\3\2\2\2m\u018f\3")
        buf.write("\2\2\2o\u0191\3\2\2\2q\u0193\3\2\2\2s\u0195\3\2\2\2u\u0197")
        buf.write("\3\2\2\2w\u0199\3\2\2\2y\u019b\3\2\2\2{\u019d\3\2\2\2")
        buf.write("}\u019f\3\2\2\2\177\u01a1\3\2\2\2\u0081\u01a3\3\2\2\2")
        buf.write("\u0083\u01a5\3\2\2\2\u0085\u01a7\3\2\2\2\u0087\u01a9\3")
        buf.write("\2\2\2\u0089\u01ab\3\2\2\2\u008b\u01ad\3\2\2\2\u008d\u01af")
        buf.write("\3\2\2\2\u008f\u01b1\3\2\2\2\u0091\u01b3\3\2\2\2\u0093")
        buf.write("\u01b5\3\2\2\2\u0095\u01b7\3\2\2\2\u0097\u01b9\3\2\2\2")
        buf.write("\u0099\u01bb\3\2\2\2\u009b\u01bd\3\2\2\2\u009d\u01c0\3")
        buf.write("\2\2\2\u009f\u01c7\3\2\2\2\u00a1\u01d0\3\2\2\2\u00a3\u020c")
        buf.write("\3\2\2\2\u00a5\u020e\3\2\2\2\u00a7\u021c\3\2\2\2\u00a9")
        buf.write("\u0222\3\2\2\2\u00ab\u0224\3\2\2\2\u00ad\u0230\3\2\2\2")
        buf.write("\u00af\u0239\3\2\2\2\u00b1\u0242\3\2\2\2\u00b3\u024f\3")
        buf.write("\2\2\2\u00b5\u025c\3\2\2\2\u00b7\u00b8\7*\2\2\u00b8\4")
        buf.write("\3\2\2\2\u00b9\u00ba\7+\2\2\u00ba\6\3\2\2\2\u00bb\u00bc")
        buf.write("\7]\2\2\u00bc\b\3\2\2\2\u00bd\u00be\7_\2\2\u00be\n\3\2")
        buf.write("\2\2\u00bf\u00c0\7=\2\2\u00c0\f\3\2\2\2\u00c1\u00c2\7")
        buf.write(".\2\2\u00c2\16\3\2\2\2\u00c3\u00c4\7?\2\2\u00c4\20\3\2")
        buf.write("\2\2\u00c5\u00c6\7<\2\2\u00c6\22\3\2\2\2\u00c7\u00c8\7")
        buf.write("\60\2\2\u00c8\u00c9\7\60\2\2\u00c9\24\3\2\2\2\u00ca\u00cb")
        buf.write("\7-\2\2\u00cb\26\3\2\2\2\u00cc\u00cd\7,\2\2\u00cd\30\3")
        buf.write("\2\2\2\u00ce\u00cf\7>\2\2\u00cf\u00d0\7@\2\2\u00d0\32")
        buf.write("\3\2\2\2\u00d1\u00d2\7>\2\2\u00d2\34\3\2\2\2\u00d3\u00d4")
        buf.write("\7>\2\2\u00d4\u00d5\7?\2\2\u00d5\36\3\2\2\2\u00d6\u00d7")
        buf.write("\7/\2\2\u00d7 \3\2\2\2\u00d8\u00d9\7\61\2\2\u00d9\"\3")
        buf.write("\2\2\2\u00da\u00db\7@\2\2\u00db$\3\2\2\2\u00dc\u00dd\7")
        buf.write("@\2\2\u00dd\u00de\7?\2\2\u00de&\3\2\2\2\u00df\u00e0\7")
        buf.write("<\2\2\u00e0\u00e1\7?\2\2\u00e1(\3\2\2\2\u00e2\u00e5\5")
        buf.write("K&\2\u00e3\u00e5\5M\'\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3")
        buf.write("\3\2\2\2\u00e5*\3\2\2\2\u00e6\u00e7\5i\65\2\u00e7\u00e8")
        buf.write("\5\u0089E\2\u00e8\u00e9\5o8\2\u00e9\u00ea\5g\64\2\u00ea")
        buf.write("\u00eb\5{>\2\u00eb,\3\2\2\2\u00ec\u00ed\5k\66\2\u00ed")
        buf.write("\u00ee\5\u0083B\2\u00ee\u00ef\5\u0081A\2\u00ef\u00f0\5")
        buf.write("\u008dG\2\u00f0\u00f1\5w<\2\u00f1\u00f2\5\u0081A\2\u00f2")
        buf.write("\u00f3\5\u008fH\2\u00f3\u00f4\5o8\2\u00f4.\3\2\2\2\u00f5")
        buf.write("\u00f6\5q9\2\u00f6\u00f7\5\u0083B\2\u00f7\u00f8\5\u0089")
        buf.write("E\2\u00f8\60\3\2\2\2\u00f9\u00fa\5\u008dG\2\u00fa\u00fb")
        buf.write("\5\u0083B\2\u00fb\62\3\2\2\2\u00fc\u00fd\5m\67\2\u00fd")
        buf.write("\u00fe\5\u0083B\2\u00fe\u00ff\5\u0093J\2\u00ff\u0100\5")
        buf.write("\u0081A\2\u0100\u0101\5\u008dG\2\u0101\u0102\5\u0083B")
        buf.write("\2\u0102\64\3\2\2\2\u0103\u0104\5m\67\2\u0104\u0105\5")
        buf.write("\u0083B\2\u0105\66\3\2\2\2\u0106\u0107\5w<\2\u0107\u0108")
        buf.write("\5q9\2\u01088\3\2\2\2\u0109\u010a\5\u008dG\2\u010a\u010b")
        buf.write("\5u;\2\u010b\u010c\5o8\2\u010c\u010d\5\u0081A\2\u010d")
        buf.write(":\3\2\2\2\u010e\u010f\5o8\2\u010f\u0110\5}?\2\u0110\u0111")
        buf.write("\5\u008bF\2\u0111\u0112\5o8\2\u0112<\3\2\2\2\u0113\u0114")
        buf.write("\5\u0089E\2\u0114\u0115\5o8\2\u0115\u0116\5\u008dG\2\u0116")
        buf.write("\u0117\5\u008fH\2\u0117\u0118\5\u0089E\2\u0118\u0119\5")
        buf.write("\u0081A\2\u0119>\3\2\2\2\u011a\u011b\5\u0093J\2\u011b")
        buf.write("\u011c\5u;\2\u011c\u011d\5w<\2\u011d\u011e\5}?\2\u011e")
        buf.write("\u011f\5o8\2\u011f@\3\2\2\2\u0120\u0121\5i\65\2\u0121")
        buf.write("\u0122\5o8\2\u0122\u0123\5s:\2\u0123\u0124\5w<\2\u0124")
        buf.write("\u0125\5\u0081A\2\u0125B\3\2\2\2\u0126\u0127\5o8\2\u0127")
        buf.write("\u0128\5\u0081A\2\u0128\u0129\5m\67\2\u0129D\3\2\2\2\u012a")
        buf.write("\u012b\5q9\2\u012b\u012c\5\u008fH\2\u012c\u012d\5\u0081")
        buf.write("A\2\u012d\u012e\5k\66\2\u012e\u012f\5\u008dG\2\u012f\u0130")
        buf.write("\5w<\2\u0130\u0131\5\u0083B\2\u0131\u0132\5\u0081A\2\u0132")
        buf.write("F\3\2\2\2\u0133\u0134\5\u0085C\2\u0134\u0135\5\u0089E")
        buf.write("\2\u0135\u0136\5\u0083B\2\u0136\u0137\5k\66\2\u0137\u0138")
        buf.write("\5o8\2\u0138\u0139\5m\67\2\u0139\u013a\5\u008fH\2\u013a")
        buf.write("\u013b\5\u0089E\2\u013b\u013c\5o8\2\u013cH\3\2\2\2\u013d")
        buf.write("\u013e\5\u0091I\2\u013e\u013f\5g\64\2\u013f\u0140\5\u0089")
        buf.write("E\2\u0140J\3\2\2\2\u0141\u0142\5\u008dG\2\u0142\u0143")
        buf.write("\5\u0089E\2\u0143\u0144\5\u008fH\2\u0144\u0145\5o8\2\u0145")
        buf.write("L\3\2\2\2\u0146\u0147\5q9\2\u0147\u0148\5g\64\2\u0148")
        buf.write("\u0149\5}?\2\u0149\u014a\5\u008bF\2\u014a\u014b\5o8\2")
        buf.write("\u014bN\3\2\2\2\u014c\u014d\5g\64\2\u014d\u014e\5\u0089")
        buf.write("E\2\u014e\u014f\5\u0089E\2\u014f\u0150\5g\64\2\u0150\u0151")
        buf.write("\5\u0097L\2\u0151P\3\2\2\2\u0152\u0153\5\u0083B\2\u0153")
        buf.write("\u0154\5q9\2\u0154R\3\2\2\2\u0155\u0156\5\u0089E\2\u0156")
        buf.write("\u0157\5o8\2\u0157\u0158\5g\64\2\u0158\u0159\5}?\2\u0159")
        buf.write("T\3\2\2\2\u015a\u015b\5i\65\2\u015b\u015c\5\u0083B\2\u015c")
        buf.write("\u015d\5\u0083B\2\u015d\u015e\5}?\2\u015e\u015f\5o8\2")
        buf.write("\u015f\u0160\5g\64\2\u0160\u0161\5\u0081A\2\u0161V\3\2")
        buf.write("\2\2\u0162\u0163\5w<\2\u0163\u0164\5\u0081A\2\u0164\u0165")
        buf.write("\5\u008dG\2\u0165\u0166\5o8\2\u0166\u0167\5s:\2\u0167")
        buf.write("\u0168\5o8\2\u0168\u0169\5\u0089E\2\u0169X\3\2\2\2\u016a")
        buf.write("\u016b\5\u008bF\2\u016b\u016c\5\u008dG\2\u016c\u016d\5")
        buf.write("\u0089E\2\u016d\u016e\5w<\2\u016e\u016f\5\u0081A\2\u016f")
        buf.write("\u0170\5s:\2\u0170Z\3\2\2\2\u0171\u0172\5\u0081A\2\u0172")
        buf.write("\u0173\5\u0083B\2\u0173\u0174\5\u008dG\2\u0174\\\3\2\2")
        buf.write("\2\u0175\u0176\5g\64\2\u0176\u0177\5\u0081A\2\u0177\u0178")
        buf.write("\5m\67\2\u0178^\3\2\2\2\u0179\u017a\5\u0083B\2\u017a\u017b")
        buf.write("\5\u0089E\2\u017b`\3\2\2\2\u017c\u017d\5m\67\2\u017d\u017e")
        buf.write("\5w<\2\u017e\u017f\5\u0091I\2\u017fb\3\2\2\2\u0180\u0181")
        buf.write("\5\177@\2\u0181\u0182\5\u0083B\2\u0182\u0183\5m\67\2\u0183")
        buf.write("d\3\2\2\2\u0184\u0185\5\u0093J\2\u0185\u0186\5w<\2\u0186")
        buf.write("\u0187\5\u008dG\2\u0187\u0188\5u;\2\u0188f\3\2\2\2\u0189")
        buf.write("\u018a\t\2\2\2\u018ah\3\2\2\2\u018b\u018c\t\3\2\2\u018c")
        buf.write("j\3\2\2\2\u018d\u018e\t\4\2\2\u018el\3\2\2\2\u018f\u0190")
        buf.write("\t\5\2\2\u0190n\3\2\2\2\u0191\u0192\t\6\2\2\u0192p\3\2")
        buf.write("\2\2\u0193\u0194\t\7\2\2\u0194r\3\2\2\2\u0195\u0196\t")
        buf.write("\b\2\2\u0196t\3\2\2\2\u0197\u0198\t\t\2\2\u0198v\3\2\2")
        buf.write("\2\u0199\u019a\t\n\2\2\u019ax\3\2\2\2\u019b\u019c\t\13")
        buf.write("\2\2\u019cz\3\2\2\2\u019d\u019e\t\f\2\2\u019e|\3\2\2\2")
        buf.write("\u019f\u01a0\t\r\2\2\u01a0~\3\2\2\2\u01a1\u01a2\t\16\2")
        buf.write("\2\u01a2\u0080\3\2\2\2\u01a3\u01a4\t\17\2\2\u01a4\u0082")
        buf.write("\3\2\2\2\u01a5\u01a6\t\20\2\2\u01a6\u0084\3\2\2\2\u01a7")
        buf.write("\u01a8\t\21\2\2\u01a8\u0086\3\2\2\2\u01a9\u01aa\t\22\2")
        buf.write("\2\u01aa\u0088\3\2\2\2\u01ab\u01ac\t\23\2\2\u01ac\u008a")
        buf.write("\3\2\2\2\u01ad\u01ae\t\24\2\2\u01ae\u008c\3\2\2\2\u01af")
        buf.write("\u01b0\t\25\2\2\u01b0\u008e\3\2\2\2\u01b1\u01b2\t\26\2")
        buf.write("\2\u01b2\u0090\3\2\2\2\u01b3\u01b4\t\27\2\2\u01b4\u0092")
        buf.write("\3\2\2\2\u01b5\u01b6\t\30\2\2\u01b6\u0094\3\2\2\2\u01b7")
        buf.write("\u01b8\t\31\2\2\u01b8\u0096\3\2\2\2\u01b9\u01ba\t\32\2")
        buf.write("\2\u01ba\u0098\3\2\2\2\u01bb\u01bc\t\33\2\2\u01bc\u009a")
        buf.write("\3\2\2\2\u01bd\u01be\t\34\2\2\u01be\u009c\3\2\2\2\u01bf")
        buf.write("\u01c1\t\35\2\2\u01c0\u01bf\3\2\2\2\u01c1\u01c2\3\2\2")
        buf.write("\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4")
        buf.write("\3\2\2\2\u01c4\u01c5\bO\2\2\u01c5\u009e\3\2\2\2\u01c6")
        buf.write("\u01c8\t\36\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01cc\3\2\2")
        buf.write("\2\u01c9\u01cb\t\37\2\2\u01ca\u01c9\3\2\2\2\u01cb\u01ce")
        buf.write("\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd")
        buf.write("\u00a0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d1\t\34\2")
        buf.write("\2\u01d0\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u00a2\3\2\2\2\u01d4")
        buf.write("\u01d6\t\34\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2")
        buf.write("\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01da")
        buf.write("\3\2\2\2\u01d9\u01db\7\60\2\2\u01da\u01d9\3\2\2\2\u01da")
        buf.write("\u01db\3\2\2\2\u01db\u01df\3\2\2\2\u01dc\u01de\t\34\2")
        buf.write("\2\u01dd\u01dc\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd")
        buf.write("\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01f1\3\2\2\2\u01e1")
        buf.write("\u01df\3\2\2\2\u01e2\u01e4\t\34\2\2\u01e3\u01e2\3\2\2")
        buf.write("\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8")
        buf.write("\u01ea\t\6\2\2\u01e9\u01eb\7/\2\2\u01ea\u01e9\3\2\2\2")
        buf.write("\u01ea\u01eb\3\2\2\2\u01eb\u01ed\3\2\2\2\u01ec\u01ee\t")
        buf.write("\34\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f2\3\2\2\2")
        buf.write("\u01f1\u01e5\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u020d\3")
        buf.write("\2\2\2\u01f3\u01f5\t\34\2\2\u01f4\u01f3\3\2\2\2\u01f5")
        buf.write("\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2")
        buf.write("\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fb\7")
        buf.write("\60\2\2\u01fa\u01f9\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb")
        buf.write("\u01fd\3\2\2\2\u01fc\u01fe\t\34\2\2\u01fd\u01fc\3\2\2")
        buf.write("\2\u01fe\u01ff\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200")
        buf.write("\3\2\2\2\u0200\u020a\3\2\2\2\u0201\u0203\t\6\2\2\u0202")
        buf.write("\u0204\7/\2\2\u0203\u0202\3\2\2\2\u0203\u0204\3\2\2\2")
        buf.write("\u0204\u0206\3\2\2\2\u0205\u0207\t\34\2\2\u0206\u0205")
        buf.write("\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0206\3\2\2\2\u0208")
        buf.write("\u0209\3\2\2\2\u0209\u020b\3\2\2\2\u020a\u0201\3\2\2\2")
        buf.write("\u020a\u020b\3\2\2\2\u020b\u020d\3\2\2\2\u020c\u01d5\3")
        buf.write("\2\2\2\u020c\u01f6\3\2\2\2\u020d\u00a4\3\2\2\2\u020e\u0214")
        buf.write("\7$\2\2\u020f\u0210\7^\2\2\u0210\u0213\t \2\2\u0211\u0213")
        buf.write("\n!\2\2\u0212\u020f\3\2\2\2\u0212\u0211\3\2\2\2\u0213")
        buf.write("\u0216\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2")
        buf.write("\u0215\u0217\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0218\7")
        buf.write("$\2\2\u0218\u0219\bS\3\2\u0219\u00a6\3\2\2\2\u021a\u021d")
        buf.write("\5\u00a9U\2\u021b\u021d\5\u00afX\2\u021c\u021a\3\2\2\2")
        buf.write("\u021c\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u021f\b")
        buf.write("T\2\2\u021f\u00a8\3\2\2\2\u0220\u0223\5\u00abV\2\u0221")
        buf.write("\u0223\5\u00adW\2\u0222\u0220\3\2\2\2\u0222\u0221\3\2")
        buf.write("\2\2\u0223\u00aa\3\2\2\2\u0224\u0225\7*\2\2\u0225\u0226")
        buf.write("\7,\2\2\u0226\u022a\3\2\2\2\u0227\u0229\13\2\2\2\u0228")
        buf.write("\u0227\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u022b\3\2\2\2")
        buf.write("\u022a\u0228\3\2\2\2\u022b\u022d\3\2\2\2\u022c\u022a\3")
        buf.write("\2\2\2\u022d\u022e\7,\2\2\u022e\u022f\7+\2\2\u022f\u00ac")
        buf.write("\3\2\2\2\u0230\u0234\7}\2\2\u0231\u0233\13\2\2\2\u0232")
        buf.write("\u0231\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0235\3\2\2\2")
        buf.write("\u0234\u0232\3\2\2\2\u0235\u0237\3\2\2\2\u0236\u0234\3")
        buf.write("\2\2\2\u0237\u0238\7\177\2\2\u0238\u00ae\3\2\2\2\u0239")
        buf.write("\u023a\7\61\2\2\u023a\u023b\7\61\2\2\u023b\u023f\3\2\2")
        buf.write("\2\u023c\u023e\n\"\2\2\u023d\u023c\3\2\2\2\u023e\u0241")
        buf.write("\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240")
        buf.write("\u00b0\3\2\2\2\u0241\u023f\3\2\2\2\u0242\u024a\7$\2\2")
        buf.write("\u0243\u0245\7^\2\2\u0244\u0246\t \2\2\u0245\u0244\3\2")
        buf.write("\2\2\u0246\u0249\3\2\2\2\u0247\u0249\n!\2\2\u0248\u0243")
        buf.write("\3\2\2\2\u0248\u0247\3\2\2\2\u0249\u024c\3\2\2\2\u024a")
        buf.write("\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024d\3\2\2\2")
        buf.write("\u024c\u024a\3\2\2\2\u024d\u024e\bY\4\2\u024e\u00b2\3")
        buf.write("\2\2\2\u024f\u0255\7$\2\2\u0250\u0254\n#\2\2\u0251\u0252")
        buf.write("\7^\2\2\u0252\u0254\t \2\2\u0253\u0250\3\2\2\2\u0253\u0251")
        buf.write("\3\2\2\2\u0254\u0257\3\2\2\2\u0255\u0253\3\2\2\2\u0255")
        buf.write("\u0256\3\2\2\2\u0256\u0258\3\2\2\2\u0257\u0255\3\2\2\2")
        buf.write("\u0258\u0259\7^\2\2\u0259\u025a\n \2\2\u025a\u025b\bZ")
        buf.write("\5\2\u025b\u00b4\3\2\2\2\u025c\u025d\13\2\2\2\u025d\u025e")
        buf.write("\b[\6\2\u025e\u00b6\3\2\2\2#\2\u00e4\u01c2\u01c7\u01ca")
        buf.write("\u01cc\u01d2\u01d7\u01da\u01df\u01e5\u01ea\u01ef\u01f1")
        buf.write("\u01f6\u01fa\u01ff\u0203\u0208\u020a\u020c\u0212\u0214")
        buf.write("\u021c\u0222\u022a\u0234\u023f\u0245\u0248\u024a\u0253")
        buf.write("\u0255\7\b\2\2\3S\2\3Y\3\3Z\4\3[\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LB = 1
    RB = 2
    LQ = 3
    RQ = 4
    SEMI = 5
    CM = 6
    EQ = 7
    COL = 8
    DD = 9
    ADD = 10
    MUL = 11
    NOTEQ = 12
    LESSTN = 13
    LESSEQ = 14
    SUBNE = 15
    DIVSI = 16
    GRETN = 17
    GREEQ = 18
    ASSI = 19
    BOOLLIT = 20
    BREAK = 21
    CONTINUE = 22
    FOR = 23
    TO = 24
    DOWNTO = 25
    DO = 26
    IF = 27
    THEN = 28
    ELSE = 29
    RETURN = 30
    WHILE = 31
    BEGIN = 32
    END = 33
    FUNCTION = 34
    PROCEDURE = 35
    VAR = 36
    TRUE = 37
    FALSE = 38
    ARRAY = 39
    OF = 40
    REAL = 41
    BOOLEAN = 42
    INTEGER = 43
    STRING = 44
    NOT = 45
    AND = 46
    OR = 47
    DIV = 48
    MOD = 49
    WITH = 50
    WS = 51
    ID = 52
    INTLIT = 53
    REALLIT = 54
    STRINGLIT = 55
    CMT = 56
    BLKCMT = 57
    TRACMT = 58
    BLCMT = 59
    LINECMT = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "';'", "','", "'='", "':'", "'..'", 
            "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'>'", "'>='", 
            "':='" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", "DD", "ADD", 
            "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", "GRETN", 
            "GREEQ", "ASSI", "BOOLLIT", "BREAK", "CONTINUE", "FOR", "TO", 
            "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", 
            "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", 
            "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", 
            "OR", "DIV", "MOD", "WITH", "WS", "ID", "INTLIT", "REALLIT", 
            "STRINGLIT", "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LB", "RB", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", "DD", 
                  "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", 
                  "GRETN", "GREEQ", "ASSI", "BOOLLIT", "BREAK", "CONTINUE", 
                  "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", 
                  "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", 
                  "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "WITH", "A", 
                  "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", 
                  "X", "Y", "Z", "NUM", "WS", "ID", "INTLIT", "REALLIT", 
                  "STRINGLIT", "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[81] = self.STRINGLIT_action 
            actions[87] = self.UNCLOSE_STRING_action 
            actions[88] = self.ILLEGAL_ESCAPE_action 
            actions[89] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:len(self.text) - 1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


