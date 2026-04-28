from ProjectParserListener import ProjectParserListener
from ProjectParser import ProjectParser
from SymbolTable import SymbolTable


class MyListener(ProjectParserListener):
    def __init__(self):
        super().__init__()
        self.errors = []

        self.symbol_table = SymbolTable(self.errors)
        self.types = {}

    # Exit a parse tree produced by ProjectParser#program.
    def exitProgram(self, ctx: ProjectParser.ProgramContext):
        pass

    # Exit a parse tree produced by ProjectParser#emptyStmt.
    def exitEmptyStmt(self, ctx: ProjectParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#declStmt.
    def exitDeclStmt(self, ctx: ProjectParser.DeclStmtContext):
        dtype = self.types.get(ctx.type_(), "error")
        line = ctx.start.line

        for id_node in ctx.IDENTIFIER():
            self.symbol_table.declare(id_node.getText(), dtype, line)

    # Exit a parse tree produced by ProjectParser#exprStmt.
    def exitExprStmt(self, ctx: ProjectParser.ExprStmtContext):
        self.types[ctx] = self.types.get(ctx.expression(), "error")

    # Exit a parse tree produced by ProjectParser#readStmt.
    def exitReadStmt(self, ctx: ProjectParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#writeStmt.
    def exitWriteStmt(self, ctx: ProjectParser.WriteStmtContext):
        pass

    def exitFopenStmt(self, ctx: ProjectParser.FopenStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#blockStmt.
    def exitBlockStmt(self, ctx: ProjectParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by ProjectParser#ifStmt.
    def exitIfStmt(self, ctx: ProjectParser.IfStmtContext):
        dtype = self.types.get(ctx.expression(), "error")
        line = ctx.start.line

        if dtype != "bool":
            self.errors.append(
                f"Type Error [Line {line}]: Condition must yield boolean value"
            )

    # Exit a parse tree produced by ProjectParser#whileStmt.
    def exitWhileStmt(self, ctx: ProjectParser.WhileStmtContext):
        dtype = self.types.get(ctx.expression(), "error")
        line = ctx.start.line

        if dtype != "bool":
            self.errors.append(
                f"Type Error [Line {line}]: Condition must yield boolean value"
            )

    # Exit a parse tree produced by ProjectParser#type.
    def exitType(self, ctx: ProjectParser.TypeContext):
        dtype = ctx.getText()
        self.types[ctx] = dtype

    # Exit a parse tree produced by ProjectParser#intExpr.
    def exitIntExpr(self, ctx: ProjectParser.IntExprContext):
        self.types[ctx] = "int"

    # Exit a parse tree produced by ProjectParser#addSubConcatExpr.
    def exitAddSubConcatExpr(self, ctx: ProjectParser.AddSubConcatExprContext):
        left = self.types.get(ctx.expression()[0], "error")
        right = self.types.get(ctx.expression()[1], "error")
        operator = ctx.op.text
        line = ctx.start.line

        if left == "error" or right == "error":
            self.types[ctx] = "error"

        if operator == ".":
            if left == "string" and right == "string":
                self.types[ctx] = "string"
            else:
                self.errors.append(
                    f"Type Error [Line {line}]: Concat used for other than string."
                )
                self.types[ctx] = "error"
        else:
            if left in ["bool", "string"] or right in ["bool", "string"]:
                self.errors.append(
                    f"Type Error [Line {line}]: Operator {operator} not defined for {left} and {right}"
                )
                self.types[ctx] = "error"
            elif left == "float" or right == "float":
                self.types[ctx] = "float"
            else:
                self.types[ctx] = "int"

    # Exit a parse tree produced by ProjectParser#orExpr.
    def exitOrExpr(self, ctx: ProjectParser.OrExprContext):
        left = self.types.get(ctx.expression()[0], "error")
        right = self.types.get(ctx.expression()[1], "error")
        line = ctx.start.line

        if left == "error" or right == "error":
            self.types[ctx] = "error"
            return

        if left == "bool" and right == "bool":
            self.types[ctx] = "bool"
        else:
            self.errors.append(
                f"Type Error [Line {line}]: Logic OR not defined for {left} and {right}"
            )
            self.types[ctx] = "error"

    # Exit a parse tree produced by ProjectParser#mulDivModExpr.
    def exitMulDivModExpr(self, ctx: ProjectParser.MulDivModExprContext):
        left = self.types.get(ctx.expression()[0], "error")
        right = self.types.get(ctx.expression()[1], "error")
        operator = ctx.op.text
        line = ctx.start.line

        if left == "error" or right == "error":
            self.types[ctx] = "error"

        if left in ["string", "bool"] or right in ["string", "bool"]:
            self.errors.append(
                f"Type Error [Line {line}]: Operator {operator} not defined for {left} and {right}"
            )
            self.types[ctx] = "error"
            return

        if operator == "%":
            if left == "int" and right == "int":
                self.types[ctx] = "int"
            else:
                self.errors.append(
                    f"Type Error [Line {line}]: Module can be used only with integers.."
                )
                self.types[ctx] = "error"
        else:
            if left == "float" or right == "float":
                self.types[ctx] = "float"
            else:
                self.types[ctx] = "int"

    # Exit a parse tree produced by ProjectParser#parensExpr.
    def exitParensExpr(self, ctx: ProjectParser.ParensExprContext):
        self.types[ctx] = self.types.get(ctx.expression(), "error")

    # Exit a parse tree produced by ProjectParser#stringExpr.
    def exitStringExpr(self, ctx: ProjectParser.StringExprContext):
        self.types[ctx] = "string"

    # Exit a parse tree produced by ProjectParser#floatExpr.
    def exitFloatExpr(self, ctx: ProjectParser.FloatExprContext):
        self.types[ctx] = "float"

    # Exit a parse tree produced by ProjectParser#eqExpr.
    def exitEqExpr(self, ctx: ProjectParser.EqExprContext):
        left = self.types.get(ctx.expression()[0], "error")
        right = self.types.get(ctx.expression()[1], "error")
        operator = ctx.op.text
        line = ctx.start.line

        if left == "error" or right == "error":
            self.types[ctx] = "error"
            return

        if (
            (left == "float" and right == "int")
            or (left == "int" and right == "float")
            or (left == right and left in ["float", "int", "string"])
        ):
            self.types[ctx] = "bool"
        else:
            self.errors.append(
                f"Type Error [Line {line}]: Operator {operator} not defined for {left} and {right}"
            )
            self.types[ctx] = "error"

    # Exit a parse tree produced by ProjectParser#notExpr.
    def exitNotExpr(self, ctx: ProjectParser.NotExprContext):
        expr = self.types.get(ctx.expression(), "error")
        line = ctx.start.line

        if expr != "bool":
            self.errors.append(
                f"Type Error [Line {line}]: Unary negation not defined for {expr}"
            )
            self.types[ctx] = "error"
        else:
            self.types[ctx] = "bool"

    # Exit a parse tree produced by ProjectParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx: ProjectParser.UnaryMinusExprContext):
        self.types[ctx] = self.types.get(ctx.expression(), "error")

    # Exit a parse tree produced by ProjectParser#ternExpr.
    def exitTernExpr(self, ctx: ProjectParser.TernExprContext):
        condition = self.types[ctx.expression()[0]]
        true = self.types[ctx.expression()[1]]
        false = self.types[ctx.expression()[2]]

        line = ctx.start.line

        if condition != "bool":
            self.errors.append(
                f"Type Error [Line {line}]: Condition must yield boolean value"
            )
            self.types[ctx] = "error"
            return

        if true != false:
            self.errors.append(
                f"Type Error [Line {line}]: Left a right side must be the same type"
            )
            self.types[ctx] = "error"
            return

        self.types[ctx] = true

    # Exit a parse tree produced by ProjectParser#boolExpr.
    def exitBoolExpr(self, ctx: ProjectParser.BoolExprContext):
        self.types[ctx] = "bool"

    # Exit a parse tree produced by ProjectParser#relExpr.
    def exitRelExpr(self, ctx: ProjectParser.RelExprContext):
        left = self.types.get(ctx.expression()[0], "error")
        right = self.types.get(ctx.expression()[1], "error")
        operator = ctx.op.text
        line = ctx.start.line

        if left == "error" or right == "error":
            self.types[ctx] = "error"
            return

        if (
            (left == "float" and right == "int")
            or (left == "int" and right == "float")
            or (left == right and left in ["float", "int"])
        ):
            self.types[ctx] = "bool"
        else:
            self.errors.append(
                f"Type Error [Line {line}]: Operator {operator} not defined for {left} and {right}"
            )
            self.types[ctx] = "error"

    # Exit a parse tree produced by ProjectParser#assignExpr.
    def exitAssignExpr(self, ctx: ProjectParser.AssignExprContext):
        var_name = ctx.IDENTIFIER().getText().strip()
        line = ctx.start.line
        var_dtype = self.symbol_table.resolve(var_name, line)
        value_dtype = self.types.get(ctx.expression(), "error")

        if var_dtype == "error" or value_dtype == "error":
            self.types[ctx] = "error"
            return

        if var_dtype == value_dtype or var_dtype == "float" and value_dtype == "int":
            self.types[ctx] = var_dtype
        else:
            self.errors.append(
                f"Type Error [Line {line}]: Var '{var_name}' declared as {var_dtype} but got {value_dtype}."
            )
            self.types[ctx] = "error"

    # Exit a parse tree produced by ProjectParser#idExpr.
    def exitIdExpr(self, ctx: ProjectParser.IdExprContext):
        var_name = ctx.IDENTIFIER().getText()
        line = ctx.start.line

        self.types[ctx] = self.symbol_table.resolve(var_name, line)

    # Exit a parse tree produced by ProjectParser#andExpr.
    def exitAndExpr(self, ctx: ProjectParser.AndExprContext):
        left = self.types.get(ctx.expression()[0], "error")
        right = self.types.get(ctx.expression()[1], "error")
        line = ctx.start.line

        if left == "error" or right == "error":
            self.types[ctx] = "error"
            return

        if left == "bool" and right == "bool":
            self.types[ctx] = "bool"
        else:
            self.errors.append(
                f"Type Error [Line {line}]: Logic AND not defined for {left} and {right}"
            )
            self.types[ctx] = "error"
