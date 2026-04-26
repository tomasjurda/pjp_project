from ProjectParserListener import ProjectParserListener, ProjectParser
from SymbolTable import SymbolTable


class MyListener(ProjectParserListener):
    def __init__(self):
        super().__init__()
        self.symbol_table = SymbolTable()
        self.types = {}

    # Enter a parse tree produced by ProjectParser#program.
    def enterProgram(self, ctx:ProjectParser.ProgramContext):
        pass

    # Exit a parse tree produced by ProjectParser#program.
    def exitProgram(self, ctx:ProjectParser.ProgramContext):
        pass


    # Enter a parse tree produced by ProjectParser#emptyStmt.
    def enterEmptyStmt(self, ctx:ProjectParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#emptyStmt.
    def exitEmptyStmt(self, ctx:ProjectParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by ProjectParser#declStmt.
    def enterDeclStmt(self, ctx:ProjectParser.DeclStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#declStmt.
    def exitDeclStmt(self, ctx:ProjectParser.DeclStmtContext):
        pass


    # Enter a parse tree produced by ProjectParser#exprStmt.
    def enterExprStmt(self, ctx:ProjectParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#exprStmt.
    def exitExprStmt(self, ctx:ProjectParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by ProjectParser#readStmt.
    def enterReadStmt(self, ctx:ProjectParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#readStmt.
    def exitReadStmt(self, ctx:ProjectParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by ProjectParser#writeStmt.
    def enterWriteStmt(self, ctx:ProjectParser.WriteStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#writeStmt.
    def exitWriteStmt(self, ctx:ProjectParser.WriteStmtContext):
        pass


    # Enter a parse tree produced by ProjectParser#blockStmt.
    def enterBlockStmt(self, ctx:ProjectParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#blockStmt.
    def exitBlockStmt(self, ctx:ProjectParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by ProjectParser#ifStmt.
    def enterIfStmt(self, ctx:ProjectParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#ifStmt.
    def exitIfStmt(self, ctx:ProjectParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ProjectParser#whileStmt.
    def enterWhileStmt(self, ctx:ProjectParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#whileStmt.
    def exitWhileStmt(self, ctx:ProjectParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ProjectParser#type.
    def enterType(self, ctx:ProjectParser.TypeContext):
        pass

    # Exit a parse tree produced by ProjectParser#type.
    def exitType(self, ctx:ProjectParser.TypeContext):
        pass


    # Enter a parse tree produced by ProjectParser#intExpr.
    def enterIntExpr(self, ctx:ProjectParser.IntExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#intExpr.
    def exitIntExpr(self, ctx:ProjectParser.IntExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#addSubConcatExpr.
    def enterAddSubConcatExpr(self, ctx:ProjectParser.AddSubConcatExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#addSubConcatExpr.
    def exitAddSubConcatExpr(self, ctx:ProjectParser.AddSubConcatExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#orExpr.
    def enterOrExpr(self, ctx:ProjectParser.OrExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#orExpr.
    def exitOrExpr(self, ctx:ProjectParser.OrExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#mulDivModExpr.
    def enterMulDivModExpr(self, ctx:ProjectParser.MulDivModExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#mulDivModExpr.
    def exitMulDivModExpr(self, ctx:ProjectParser.MulDivModExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#parensExpr.
    def enterParensExpr(self, ctx:ProjectParser.ParensExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#parensExpr.
    def exitParensExpr(self, ctx:ProjectParser.ParensExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#stringExpr.
    def enterStringExpr(self, ctx:ProjectParser.StringExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#stringExpr.
    def exitStringExpr(self, ctx:ProjectParser.StringExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#floatExpr.
    def enterFloatExpr(self, ctx:ProjectParser.FloatExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#floatExpr.
    def exitFloatExpr(self, ctx:ProjectParser.FloatExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#eqExpr.
    def enterEqExpr(self, ctx:ProjectParser.EqExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#eqExpr.
    def exitEqExpr(self, ctx:ProjectParser.EqExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#notExpr.
    def enterNotExpr(self, ctx:ProjectParser.NotExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#notExpr.
    def exitNotExpr(self, ctx:ProjectParser.NotExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:ProjectParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:ProjectParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#boolExpr.
    def enterBoolExpr(self, ctx:ProjectParser.BoolExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#boolExpr.
    def exitBoolExpr(self, ctx:ProjectParser.BoolExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#relExpr.
    def enterRelExpr(self, ctx:ProjectParser.RelExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#relExpr.
    def exitRelExpr(self, ctx:ProjectParser.RelExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#assignExpr.
    def enterAssignExpr(self, ctx:ProjectParser.AssignExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#assignExpr.
    def exitAssignExpr(self, ctx:ProjectParser.AssignExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#idExpr.
    def enterIdExpr(self, ctx:ProjectParser.IdExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#idExpr.
    def exitIdExpr(self, ctx:ProjectParser.IdExprContext):
        pass


    # Enter a parse tree produced by ProjectParser#andExpr.
    def enterAndExpr(self, ctx:ProjectParser.AndExprContext):
        pass

    # Exit a parse tree produced by ProjectParser#andExpr.
    def exitAndExpr(self, ctx:ProjectParser.AndExprContext):
        pass
    
