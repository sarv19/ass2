import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

#########        Varde       #############
    def test_varde1(self):
        input = """var a:integer;"""
        expect = str(Program([VarDecl(Id("a"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,100))

    def test_varde2(self):
        input = """var a, b, c:real;"""
        expect = str(Program([VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,101))

    def test_varde3(self):
        input = """var a, b, c:string;"""
        expect = str(Program([VarDecl(Id("a"),StringType()),VarDecl(Id("b"),StringType()),VarDecl(Id("c"),StringType())]))
        self.assertTrue(TestAST.test(input,expect,102))

    def test_varde4(self):
        input = """var a: array [1 .. 5] of boolean;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,5,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,103))

    def test_varde5(self):
        input = """var a: array [1 .. 5] of boolean;
                       Name, Sum: INTEGER;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,5,BoolType())),
                                          VarDecl(Id("Name"),IntType()),VarDecl(Id("Sum"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,104))

    def test_varde6(self):
        input = """var a: array [1 .. 5] of boolean;
                       e,f:real;
                       Name, Sum: INTEGER;"""
        expect = str(Program([VarDecl(Id("a"),ArrayType(1,5,BoolType())),
                                            VarDecl(Id("e"),FloatType()),VarDecl(Id("f"),FloatType()),
                                            VarDecl(Id("Name"),IntType()),VarDecl(Id("Sum"),IntType())]))
        self.assertTrue(TestAST.test(input,expect,105))

#########        Funcde       #############
    def test_function1(self):
        input = """function foo (a:integer):integer;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,201))

    def test_function2(self):
        input = """function foo (a:integer):integer;
        var d, f:real;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("foo"),
                [VarDecl(Id("a"),IntType())],
                [VarDecl(Id("d"),FloatType()),VarDecl(Id("f"),FloatType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,202))

    def test_function3(self):
        input = """function Empty(a:integer):real;
        var d, f:real;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("Empty"),[VarDecl(Id("a"),IntType())],
                                                 [VarDecl(Id("d"),FloatType()),VarDecl(Id("f"),FloatType())]
                                                 ,[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,203))

    def test_function4(self):
        input = """function Empty(a,b,c:real):string;
        var d, f:boolean;
            i: integer;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("Empty"),[VarDecl(Id("a"),FloatType()),
                                                  VarDecl(Id("b"),FloatType()),
                                                  VarDecl(Id("c"),FloatType())],
                                                  [VarDecl(Id("d"),BoolType()),VarDecl(Id("f"),BoolType()),
                                                  VarDecl(Id("i"),IntType())],[],StringType())]))
        self.assertTrue(TestAST.test(input,expect,204))

    def test_function5(self):
        input = """function Empty(a:real;c:array [0 .. 10] of integer):string;
        var d, f:boolean;
            i: integer;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("Empty"),[VarDecl(Id("a"),FloatType()),
                                                 VarDecl(Id("c"),ArrayType(0,10,IntType()))],
                                                 [VarDecl(Id("d"),BoolType()),VarDecl(Id("f"),BoolType()),
                                                 VarDecl(Id("i"),IntType())],[],StringType())]))
        self.assertTrue(TestAST.test(input,expect,205))

    def test_function6(self):
        input = """function Empty(a:real;k:integer):array [-4 .. -9] of real;
        var d, f:boolean;
            i: integer;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("Empty"),[VarDecl(Id("a"),FloatType()),
                                                  VarDecl(Id("k"),IntType())],
                                                 [VarDecl(Id("d"),BoolType()),VarDecl(Id("f"),BoolType()),
                                                 VarDecl(Id("i"),IntType())],[],ArrayType(-4,-9,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,206))

    def test_function7(self):
        input = """function noVar(a:real;k:integer):array [4 .. 9] of real;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("noVar"),[VarDecl(Id("a"),FloatType()),
                                                  VarDecl(Id("k"),IntType())],
                                                 [],[],ArrayType(4,9,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,207))


#########        Procde       #############
    def test_procedure1(self):
        input = """procedure foo (a:integer);
        begin

        end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_procedure2(self):
        input = """procedure foo (a:integer);
        var d, f:real;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("foo"),
                [VarDecl(Id("a"),IntType())],
                [VarDecl(Id("d"),FloatType()),VarDecl(Id("f"),FloatType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_procedure3(self):
        input = """procedure Empty(a:integer);
        var d: array [0 .. 34] of real;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("Empty"),[VarDecl(Id("a"),IntType())],
                                                  [VarDecl(Id("d"),ArrayType(0,34,FloatType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_procedure4(self):
        input = """procedure Empty(a,b,c:real);
        var d, f:boolean;
            i: integer;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("Empty"),[VarDecl(Id("a"),FloatType()),
                                                  VarDecl(Id("b"),FloatType()),
                                                  VarDecl(Id("c"),FloatType())],
                                                  [VarDecl(Id("d"),BoolType()),VarDecl(Id("f"),BoolType()),
                                                  VarDecl(Id("i"),IntType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_procedure5(self):
        input = """procedure Empty(a:real;c:array [-1 .. 10] of integer);
        var d, f:boolean;
            i: integer;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("Empty"),[VarDecl(Id("a"),FloatType()),
                                                 VarDecl(Id("c"),ArrayType(-1,10,IntType()))],
                                                 [VarDecl(Id("d"),BoolType()),VarDecl(Id("f"),BoolType()),
                                                 VarDecl(Id("i"),IntType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_procedure6(self):
        input = """procedure Empty(a:real;k:integer);
        var d, f:boolean;
            i: array [4 .. 9] of BOOLEAN;
        begin

        end"""
        expect = str(Program([FuncDecl(Id("Empty"),[VarDecl(Id("a"),FloatType()),
                                                  VarDecl(Id("k"),IntType())],
                                                  [VarDecl(Id("d"),BoolType()),VarDecl(Id("f"),BoolType()),
                                                  VarDecl(Id("i"),ArrayType(4,9,BoolType()))],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_procedure7(self):
        input = """procedure noVar(a:real;k:integer);
        begin

        end"""
        expect = str(Program([FuncDecl(Id("noVar"),[VarDecl(Id("a"),FloatType()),
                                                   VarDecl(Id("k"),IntType())],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_procedure8(self):
        input = """procedure noParam();
        begin

        end"""
        expect = str(Program([FuncDecl(Id("noParam"),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,308))



#########        Types       #############
    def test_types1(self):
        input = """
        var a: inteGeR;
        var b: reAl;
        var c: strINg;
        var e: array [-1 .. 100] of booLEan;
        """
        expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),
                              VarDecl(Id("c"),StringType()),VarDecl(Id("e"),
                              ArrayType(-1,100,BoolType()))]))
        self.assertTrue(TestAST.test(input,expect,401))


#########        precedence       #############

#########        expression       #############
#########   index
    def test_index1(self):
        input = """
        procedure main();
        BEGIN
        foo(2)[a]:=a[b];
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],
                                   [Assign(ArrayCell(CallExpr(Id("foo"),
                                   [IntLiteral(2)]),Id("a")),ArrayCell(Id("a"),Id("b")))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,601))

    def test_index2(self):
        input = """
        procedure main();
        BEGIN
        foo(2-4*5)[a+b]:=a[e[f[c]]];
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],
                                  [Assign(ArrayCell(CallExpr(Id("foo"),
                                  [BinaryOp("-",IntLiteral(2),BinaryOp("*",IntLiteral(4),IntLiteral(5)))]),
                                  BinaryOp("+",Id("a"),Id("b"))),ArrayCell(Id("a"),
                                  ArrayCell(Id("e"),ArrayCell(Id("f"),Id("c")))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,602))

#########   invocation
    def test_invo1(self):
        input = """
        procedure main();
        BEGIN
        nopara();
        foo(a);
        foo2(foo(a));
        sum(x,y);
        pt(n,m,k);
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],
                             [CallStmt(Id("nopara"),[]),CallStmt(Id("foo"),[Id("a")]),
                             CallStmt(Id("foo2"),[CallExpr(Id("foo"),[Id("a")])]),
                             CallStmt(Id("sum"),[Id("x"),Id("y")]),
                             CallStmt(Id("pt"),[Id("n"),Id("m"),Id("k")])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,611))


#########        statement       #############
#########   assign
    def test_assign1(self):
        input = """
        procedure testass();
        BEGIN
        a:=5;
        a:=b:=c:=d:=5;
        a:=b:= foo(a);
        a :=b[10]:=foo()[3]:=x:=1;
        end
        """
        expect = str(Program([FuncDecl(Id("testass"),[],[],
                             [Assign(Id("a"),IntLiteral(5)),
                             Assign(Id("d"),IntLiteral(5)),
                             Assign(Id("c"),Id("d")),Assign(Id("b"),Id("c")),
                             Assign(Id("a"),Id("b")),Assign(Id("b"),CallExpr(Id("foo"),[Id("a")])),
                             Assign(Id("a"),Id("b")),Assign(Id("x"),IntLiteral(1)),
                             Assign(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3)),Id("x")),
                             Assign(ArrayCell(Id("b"),IntLiteral(10)),
                                        ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(3))),
                            Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(10)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,701))

    def test_index2(self):
        input = """
        procedure testass();
        BEGIN
        vec[1] := vec[2] := vector[3] := 0;
        teststring := "insert letters here";
        end
        """
        expect = str(Program([FuncDecl(Id("testass"),[],[],
                             [Assign(ArrayCell(Id("vector"),IntLiteral(3)),IntLiteral(0)),
                             Assign(ArrayCell(Id("vec"),IntLiteral(2)),ArrayCell(Id("vector"),IntLiteral(3))),
                             Assign(ArrayCell(Id("vec"),IntLiteral(1)),ArrayCell(Id("vec"),IntLiteral(2))),
                             Assign(Id("teststring"),StringLiteral("insert letters here"))])]))
        self.assertTrue(TestAST.test(input,expect,702))

    def test_index2(self):
        input = """
        procedure testass();
        BEGIN
        x:=getInt(stdin);
        y:=x*2;
        vector[3] := foo()[b] := a;
        end
        """
        expect = str(Program([FuncDecl(Id("testass"),[],[],
                             [Assign(Id("x"),CallExpr(Id("getInt"),[Id("stdin")])),
                             Assign(Id("y"),BinaryOp("*",Id("x"),IntLiteral(2))),
                             Assign(ArrayCell(CallExpr(Id("foo"),[]),Id("b")),Id("a")),
                             Assign(ArrayCell(Id("vector"),IntLiteral(3)),
                                        ArrayCell(CallExpr(Id("foo"),[]),Id("b")))])]))
        self.assertTrue(TestAST.test(input,expect,703))

#########   if/while/for/with
    def test_ifwhileforwith(self):
        input = """
        procedure main();
        BEGIN
        foo(2)[a]:=a[b];
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],
                                   [Assign(ArrayCell(CallExpr(Id("foo"),
                                   [IntLiteral(2)]),Id("a")),ArrayCell(Id("a"),Id("b")))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,601))

#########   +beak/continue/return

#########   call

#########   compoud
