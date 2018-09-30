from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce
#flatten_mix
def flatten(l):
    return list(reduce(lambda x, y: x + y if(isinstance(y, list)) else x + [y], l, []))
class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(flatten([self.visit(x) for x in ctx.manydeclares()]))
    def visitManydeclares(self, ctx:MPParser.ManydeclaresContext):
        if ctx.varde():
            return self.visit(ctx.varde())
        if ctx.funcde():
            return self.visit(ctx.funcde())
        if ctx.procede():
            return self.visit(ctx.procede())
    # def visitFuncdecl(self,ctx:MPParser.FuncdeclContext):
    #     local,cpstmt = self.visit(ctx.body())
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt,
    #                     self.visit(ctx.mtype()))
    # #
    # def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
    #     local,cpstmt = self.visit(ctx.body())
    #     return FuncDecl(Id(ctx.ID().getText()),
    #                     [],
    #                     local,
    #                     cpstmt)
    # #
    def visitCompostate(self,ctx:MPParser.CompostateContext):
        return [self.visit(x) for x in ctx.statement()]
    # #
    # def visitStmt(self,ctx:MPParser.StmtContext):
    #     return self.visit(ctx.funcall())
    # #
    # def visitFuncall(self,ctx:MPParser.FuncallContext):
    #     return CallStmt(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])
    # #
    # def visitExp(self,ctx:MPParser.ExpContext):
    #     return IntLiteral(int(ctx.INTLIT().getText()))
    # #
    # def visitMtype(self,ctx:MPParser.MtypeContext):
    #    return IntType()
    def visitVarde(self, ctx:MPParser.VardeContext):
        return flatten([self.visit(x) for x in ctx.var_list()])

    def visitVar_list(self, ctx:MPParser.Var_listContext):
        _type = self.visit(ctx.vartype())
        _id = self.visit(ctx.idlist())
        return list(map(lambda x: VarDecl(x,_type),_id))

    def visitProcede(self, ctx:MPParser.ProcedeContext):
        if ctx.varde():
            local = flatten([self.visit(ctx.varde())])
        else:
            local = []
        cpstmt = self.visit(ctx.compostate())
        id = Id(ctx.procede1().ID().getText())
        param = self.visit(ctx.procede1())
        return FuncDecl(id,
                        param,
                        local,
                        cpstmt)
    def visitProcede1(self, ctx:MPParser.Procede1Context):
        if (ctx.parade()):
            return flatten([self.visit(ctx.parade())])
        return []

    def visitParade(self, ctx:MPParser.ParadeContext):
        return flatten([self.visit(x) for x in ctx.parade1()])

    def visitParade1(self, ctx:MPParser.Parade1Context):
        _type = self.visit(ctx.vartype())
        _id = self.visit(ctx.idlist())
        return list(map(lambda x: VarDecl(x,_type),_id))

    def visitIdlist(self, ctx:MPParser.IdlistContext):
        return [Id(x.getText()) for x in ctx.ID()]

    def visitVartype(self, ctx:MPParser.VartypeContext):
        if (ctx.primtype()):
            return self.visit(ctx.primtype())
        else:
            return self.visit(ctx.arrtype())

    def visitPrimtype(self, ctx:MPParser.PrimtypeContext):
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.INTEGER():
            return IntType()
        if ctx.REAL():
            return FloatType()
        if ctx.STRING():
            return StringType()

    def visitArrtype(self, ctx:MPParser.ArrtypeContext):
        eleType = self.visit(ctx.primtype())
        lower = ctx.INTLIT(0)
        upper = ctx.INTLIT(1)
        return ArrayType(lower, upper, eleType)

    def visitFuncde(self, ctx:MPParser.FuncdeContext):
        cpstmt = self.visit(ctx.compostate())
        id = Id(ctx.funcde1().ID().getText())
        param = self.visit(ctx.funcde1())
        varType = self.visit(ctx.vartype())
        if ctx.varde():
            local = flatten([self.visit(ctx.varde())])
        else:
            local = []
        return FuncDecl(id,
                        param,
                        local,
                        cpstmt,
                        varType)

    def visitFuncde1(self, ctx:MPParser.Funcde1Context):
        if (ctx.parade()):
            return flatten([self.visit(ctx.parade())])
        return []

    def visitStatement(self, ctx:MPParser.StatementContext):
        if (ctx.semistatement()):
            return self.visit(ctx.semistatement())
        else:
            return self.visit(ctx.nomistatement())

    def visitSemistatement(self, ctx:MPParser.SemistatementContext):
        if (ctx.assignstate()):
            return self.visit(ctx.assignstate())
        elif (ctx.breakstate()):
            return self.visit(ctx.breakstate())
        elif (ctx.contstate()):
            return self.visit(ctx.contstate())
        elif (ctx.returnsate()):
            return self.visit(ctx.returnsate())
        else:
            return self.visit(ctx.callstate())

    def visitNomistatement(self, ctx:MPParser.NomistatementContext):
        if (ctx.ifstate()):
            return self.visit(ctx.ifstate())
        elif (ctx.forstate()):
            return self.visit(ctx.forstate())
        elif (ctx.whilestate()):
            return self.visit(ctx.whilestate())
        elif (ctx.compostate()):
            return self.visit(ctx.compostate())
        else:
            return self.visit(ctx.withstate())

    def visitAssignstate(self, ctx:MPParser.AssignstateContext):
        return self.visit(ctx.assignstate1())

    def visitAssignstate1(self, ctx:MPParser.Assignstate1Context):
        if ctx.assignstate1():
            a= [self.visit (ctx.assignstate1())]
        if ctx.expression():
            a=[self.visit(ctx.expression())]
        a.append(self.visit(ctx.lhs()))
        b=reduce (lambda x,y: Assign(y,x), list(a))
        print(b)
        return b

    def visitLhs(self, ctx:MPParser.LhsContext):
        if (ctx.ID()):
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.indexexpre())

    def visitIndexexpre(self, ctx:MPParser.IndexexpreContext):
        arr = self.visit(ctx.factor())
        idx = [self.visit(x for x in expression())]
        return ArrayCell(arr, idx)

    def visitFactor(self, ctx:MPParser.FactorContext):
        if (ctx.exp1()):
            return self.visit(ctx.exp1())
        elif (ctx.ID()):
            return Id(ctx.ID().getText())
        elif (ctx.INTLIT()):
            return IntLiteral(ctx.INTLIT().getText())
        elif (ctx.BOOLLIT()):
            return BooleanLiteral(ctx.BOOLLIT().getText())
        elif (ctx.REALLIT()):
            return FloatLiteral(ctx.REALLIT().getText())
        elif (ctx.STRINGLIT()):
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return self.visit(ctx.invoexpre())

    def visitExp1(self, ctx:MPParser.Exp1Context):
        if (ctx.AND() and ctx.THEN()):
            return BinaryOp("andthen",self.visit(exp1()),self.visit(ctx.exp2()))
        elif (ctx.OR() and ctx.ELSE()):
                return BinaryOp("orelse",self.visit(exp1()),self.visit(ctx.exp2()))
        else:
            return self.visit(ctx.exp2())

    def visitExp2(self, ctx:MPParser.Exp2Context):
        if (ctx.EQ()):
            return BinaryOp("=",self.visit(exp3()),self.visit(ctx.exp3()))
        elif (ctx.NOTEQ()):
            return BinaryOp("<>",self.visit(exp3()),self.visit(ctx.exp3()))
        elif (ctx.LESSTN()):
            return BinaryOp("<",self.visit(exp3()),self.visit(ctx.exp3()))
        elif (ctx.GRETN()):
            return BinaryOp(">",self.visit(exp3()),self.visit(ctx.exp3()))
        elif (ctx.GREEQ()):
            return BinaryOp(">=",self.visit(exp3()),self.visit(ctx.exp3()))
        elif (ctx.LESSEQ()):
            return BinaryOp("<=",self.visit(exp3()),self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())

    def visitExp3(self, ctx:MPParser.Exp3Context):
        if (ctx.ADD()):
            return BinaryOp("+",self.visit(exp3()),self.visit(ctx.exp4()))
        elif (ctx.SUBNE()):
            return BinaryOp("-",self.visit(exp3()),self.visit(ctx.exp4()))
        elif (ctx.OR()):
            return BinaryOp("OR",self.visit(exp3()),self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())

    def visitExp4(self, ctx:MPParser.Exp4Context):
        if (ctx.DIVSI()):
            return BinaryOp("/",self.visit(exp4()),self.visit(ctx.exp5()))
        elif (ctx.MUL()):
            return BinaryOp("*",self.visit(exp4()),self.visit(ctx.exp5()))
        elif (ctx.MOD()):
            return BinaryOp("MOD",self.visit(exp4()),self.visit(ctx.exp5()))
        elif (ctx.AND()):
            return BinaryOp("AND",self.visit(exp4()),self.visit(ctx.exp5()))
        elif (ctx.DIV()):
            return BinaryOp("DIV",self.visit(exp4()),self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp5())

    def visitExp5(self, ctx:MPParser.Exp5Context):
        if (ctx.NOT()):
            return UnaryOp("NOT",self.vist(ctx.exp5()))
        elif (ctx.SUBNE()):
            return UnaryOp("-",self.vist(ctx.exp5()))
        else:
            return self.visit(ctx.exp6())

    def visitExp6(self, ctx:MPParser.Exp6Context):
        if (ctx.factor()):
            return self.visit(ctx.factor())
        else:
            return self.visit(ctx.indexexpre())

    def visitInvoexpre(self, ctx:MPParser.InvoexpreContext):
        method = Id(ctx.ID().getText())
        param = [self.visit(x) for x in expression()]
        return CallExpr(method, param)

    def visitExpression(self, ctx:MPParser.ExpressionContext):
        pass

    def visitBreakstate(self, ctx:MPParser.BreakstateContext ):
        pass

    def visitContstate(self, ctx:MPParser.ContstateContext):
        pass

    def visitReturnsate(self, ctx:MPParser.ReturnsateContext):
        pass

    def visitCallstate(self, ctx:MPParser.CallstateContext):
        pass

    def visitIfstate(self, ctx:MPParser.IfstateContext):
        pass

    def visitForstate(self, ctx:MPParser.ForstateContext):
        pass

    def visitWhilestate(self, ctx:MPParser.WhilestateContext):
        pass

    def visitWithstate(self, ctx:MPParser.WithstateContext):
        pass
