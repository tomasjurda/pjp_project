from ProjectParserVisitor import ProjectParserVisitor, ProjectParser


class MyVisitor(ProjectParserVisitor):
    def __init__(self, symbol_table, types):
        super().__init__()
        self.symbol_table = symbol_table
        self.types = types

    # Visit a parse tree produced by ProjectParser#emptyStmt.
    def visitEmptyStmt(self, ctx: ProjectParser.EmptyStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#declStmt.
    def visitDeclStmt(self, ctx: ProjectParser.DeclStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#exprStmt.
    def visitExprStmt(self, ctx: ProjectParser.ExprStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#readStmt.
    def visitReadStmt(self, ctx: ProjectParser.ReadStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#writeStmt.
    def visitWriteStmt(self, ctx: ProjectParser.WriteStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#blockStmt.
    def visitBlockStmt(self, ctx: ProjectParser.BlockStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#ifStmt.
    def visitIfStmt(self, ctx: ProjectParser.IfStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#whileStmt.
    def visitWhileStmt(self, ctx: ProjectParser.WhileStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#type.
    def visitType(self, ctx: ProjectParser.TypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#intExpr.
    def visitIntExpr(self, ctx: ProjectParser.IntExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#addSubConcatExpr.
    def visitAddSubConcatExpr(self, ctx: ProjectParser.AddSubConcatExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#orExpr.
    def visitOrExpr(self, ctx: ProjectParser.OrExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#mulDivModExpr.
    def visitMulDivModExpr(self, ctx: ProjectParser.MulDivModExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#parensExpr.
    def visitParensExpr(self, ctx: ProjectParser.ParensExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#stringExpr.
    def visitStringExpr(self, ctx: ProjectParser.StringExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#floatExpr.
    def visitFloatExpr(self, ctx: ProjectParser.FloatExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#eqExpr.
    def visitEqExpr(self, ctx: ProjectParser.EqExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#notExpr.
    def visitNotExpr(self, ctx: ProjectParser.NotExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx: ProjectParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#boolExpr.
    def visitBoolExpr(self, ctx: ProjectParser.BoolExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#relExpr.
    def visitRelExpr(self, ctx: ProjectParser.RelExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#assignExpr.
    def visitAssignExpr(self, ctx: ProjectParser.AssignExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#idExpr.
    def visitIdExpr(self, ctx: ProjectParser.IdExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ProjectParser#andExpr.
    def visitAndExpr(self, ctx: ProjectParser.AndExprContext):
        return self.visitChildren(ctx)
