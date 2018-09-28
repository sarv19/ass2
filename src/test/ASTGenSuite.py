import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """var a, b, c:integer;"""
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,300))
    #
    # def test_simple_function(self):
    #     """More complex program"""
    #     input = """function foo ():INTEGER; begin
    #         putIntLn(4);
    #     end"""
    #     expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,301))
    #
    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """procedure main (); begin
    #         getIntLn();
    #     end
    #     function foo ():INTEGER; begin
    #         putIntLn(4);
    #     end"""
    #     expect = str(Program([
    #             FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
    #             FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
    #     self.assertTrue(TestAST.test(input,expect,302))
    def test_procedure(self):
        input = """procedure main();var a: integer;begin end"""
        expect = """Program([FuncDecl(Id(main),[],VoidType(),[VarDecl(Id(a),IntType)],[[],[]])])"""
        self.assertTrue(TestAST.test(input,expect,301))

    def test_procedure2(self):
        input = """procedure main();var a: integer;
                                     b,c:real;
                                 begin end"""
        expect = """Program([FuncDecl(Id(main),[],VoidType(),[VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType)],[[],[]])])"""
        self.assertTrue(TestAST.test(input,expect,302))
