import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):


    def test_procedure2(self):
        input = """procedure main();var a: integer;
                                     b,c:real;
                                 begin end"""
        expect = str(Program([FuncDecl(Id("main"),[],
                                [VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),FloatType())],[[],[]],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,302))
