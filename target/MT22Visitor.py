# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declist.
    def visitDeclist(self, ctx:MT22Parser.DeclistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ids.
    def visitIds(self, ctx:MT22Parser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vartyp.
    def visitVartyp(self, ctx:MT22Parser.VartypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idxlist.
    def visitIdxlist(self, ctx:MT22Parser.IdxlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idxs.
    def visitIdxs(self, ctx:MT22Parser.IdxsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idx.
    def visitIdx(self, ctx:MT22Parser.IdxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylist.
    def visitArraylist(self, ctx:MT22Parser.ArraylistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrays.
    def visitArrays(self, ctx:MT22Parser.ArraysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array.
    def visitArray(self, ctx:MT22Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paralist.
    def visitParalist(self, ctx:MT22Parser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paras.
    def visitParas(self, ctx:MT22Parser.ParasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para.
    def visitPara(self, ctx:MT22Parser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functyp.
    def visitFunctyp(self, ctx:MT22Parser.FunctypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bodylist.
    def visitBodylist(self, ctx:MT22Parser.BodylistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bodydecl.
    def visitBodydecl(self, ctx:MT22Parser.BodydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprs.
    def visitExprs(self, ctx:MT22Parser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unexpr.
    def visitUnexpr(self, ctx:MT22Parser.UnexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unexpr1.
    def visitUnexpr1(self, ctx:MT22Parser.Unexpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unexpr2.
    def visitUnexpr2(self, ctx:MT22Parser.Unexpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idxop.
    def visitIdxop(self, ctx:MT22Parser.IdxopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#biexpr.
    def visitBiexpr(self, ctx:MT22Parser.BiexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#biexpr1.
    def visitBiexpr1(self, ctx:MT22Parser.Biexpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#biexpr2.
    def visitBiexpr2(self, ctx:MT22Parser.Biexpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#biexpr3.
    def visitBiexpr3(self, ctx:MT22Parser.Biexpr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#biexpr4.
    def visitBiexpr4(self, ctx:MT22Parser.Biexpr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#rtnstmt.
    def visitRtnstmt(self, ctx:MT22Parser.RtnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return self.visitChildren(ctx)



del MT22Parser