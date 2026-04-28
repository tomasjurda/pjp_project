from ProjectParserVisitor import ProjectParserVisitor
from ProjectParser import ProjectParser
from SymbolTable import SymbolTable


class MyVisitor(ProjectParserVisitor):
    def __init__(self, symbol_table: SymbolTable, types):
        super().__init__()
        self.symbol_table = symbol_table
        self.types = types
        self.label_counter = 0

    def _dtypeIf(self, dtype: str):
        if dtype == "int":
            dtype_if = "I"
        elif dtype == "float":
            dtype_if = "F"
        elif dtype == "string":
            dtype_if = "S"
        else:
            dtype_if = "B"

        return dtype_if

    # Visit a parse tree produced by ProjectParser#program.
    def visitProgram(self, ctx: ProjectParser.ProgramContext):
        instructions = ""

        for statement in ctx.statement():
            instructions += self.visit(statement)
        return instructions

    # Visit a parse tree produced by ProjectParser#emptyStmt.
    def visitEmptyStmt(self, ctx: ProjectParser.EmptyStmtContext):
        return ""

    # Visit a parse tree produced by ProjectParser#declStmt.
    def visitDeclStmt(self, ctx: ProjectParser.DeclStmtContext):
        instructions = ""
        dtype = self.visit(ctx.type_())

        if dtype == "I":
            def_value = "0"
        elif dtype == "F":
            def_value = "0.0"
        elif dtype == "S":
            def_value = '""'
        else:
            def_value = "false"

        for identifier in ctx.IDENTIFIER():
            instructions += f"push {dtype} {def_value} \n"
            instructions += f"save {identifier.getText()} \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#exprStmt.
    def visitExprStmt(self, ctx: ProjectParser.ExprStmtContext):
        instructions = ""
        instructions += self.visit(ctx.expression()) + "pop \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#readStmt.
    def visitReadStmt(self, ctx: ProjectParser.ReadStmtContext):
        instructions = ""

        for identifier in ctx.IDENTIFIER():
            var_name = identifier.getText()
            dtype = self.symbol_table.resolve(var_name)
            dtype_if = self._dtypeIf(dtype)

            instructions += f"read {dtype_if} \n"
            instructions += f"save {var_name} \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#writeStmt.
    def visitWriteStmt(self, ctx: ProjectParser.WriteStmtContext):
        instructions = ""

        for exp in ctx.expression():
            instructions += self.visit(exp)
        instructions += f"print {len(ctx.expression())} \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#blockStmt.
    def visitBlockStmt(self, ctx: ProjectParser.BlockStmtContext):
        instructions = ""

        for statement in ctx.statement():
            instructions += self.visit(statement)
        return instructions

    # Visit a parse tree produced by ProjectParser#ifStmt.
    def visitIfStmt(self, ctx: ProjectParser.IfStmtContext):
        instructions = ""
        label_1 = self.label_counter
        label_2 = label_1 + 1
        self.label_counter += 2

        instructions += self.visit(ctx.expression())
        instructions += f"fjmp {label_1} \n"

        instructions += self.visit(ctx.statement()[0])
        instructions += f"jmp {label_2} \n"
        instructions += f"label {label_1} \n"
        if len(ctx.statement()) > 1:
            instructions += self.visit(ctx.statement()[1])
        instructions += f"label {label_2} \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#whileStmt.
    def visitWhileStmt(self, ctx: ProjectParser.WhileStmtContext):
        instructions = ""
        label_1 = self.label_counter
        label_2 = label_1 + 1
        self.label_counter += 2

        instructions += f"label {label_1} \n"

        instructions += self.visit(ctx.expression())
        instructions += f"fjmp {label_2} \n"

        instructions += self.visit(ctx.statement())

        instructions += f"jmp {label_1} \n"
        instructions += f"label {label_2} \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#type.
    def visitType(self, ctx: ProjectParser.TypeContext):
        dtype = ctx.getText()

        return self._dtypeIf(dtype)

    # Visit a parse tree produced by ProjectParser#intExpr.
    def visitIntExpr(self, ctx: ProjectParser.IntExprContext):
        return f"push I {ctx.INT_LITERAL().getText()} \n"

    # Visit a parse tree produced by ProjectParser#addSubConcatExpr.
    def visitAddSubConcatExpr(self, ctx: ProjectParser.AddSubConcatExprContext):
        left_instructions = self.visit(ctx.expression()[0])
        left_dtype = self.types[ctx.expression()[0]]
        right_instructions = self.visit(ctx.expression()[1])
        right_dtype = self.types[ctx.expression()[1]]

        operator = ctx.op.text

        instructions = ""

        if left_dtype == "int" and right_dtype == "float":
            instructions += left_instructions + "itof \n" + right_instructions
            final_dtype = "F"
        elif left_dtype == "float" and right_dtype == "int":
            instructions += left_instructions + right_instructions + "itof \n"
            final_dtype = "F"
        else:
            instructions += left_instructions + right_instructions
            final_dtype = self._dtypeIf(left_dtype)

        if operator == "+":
            instructions += f"add {final_dtype} \n"
        elif operator == "-":
            instructions += f"sub {final_dtype} \n"
        else:
            instructions += "concat \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#orExpr.
    def visitOrExpr(self, ctx: ProjectParser.OrExprContext):
        left_instructions = self.visit(ctx.expression()[0])
        right_instructions = self.visit(ctx.expression()[1])

        return left_instructions + right_instructions + "or \n"

    # Visit a parse tree produced by ProjectParser#mulDivModExpr.
    def visitMulDivModExpr(self, ctx: ProjectParser.MulDivModExprContext):
        left_instructions = self.visit(ctx.expression()[0])
        left_dtype = self.types[ctx.expression()[0]]
        right_instructions = self.visit(ctx.expression()[1])
        right_dtype = self.types[ctx.expression()[1]]

        operator = ctx.op.text

        instructions = ""

        if left_dtype == "int" and right_dtype == "float":
            instructions += left_instructions + "itof \n" + right_instructions
            final_dtype = "F"
        elif left_dtype == "float" and right_dtype == "int":
            instructions += left_instructions + right_instructions + "itof \n"
            final_dtype = "F"
        else:
            instructions += left_instructions + right_instructions
            final_dtype = self._dtypeIf(left_dtype)

        if operator == "*":
            instructions += f"mul {final_dtype} \n"
        elif operator == "/":
            instructions += f"div {final_dtype} \n"
        else:
            instructions += "mod \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#parensExpr.
    def visitParensExpr(self, ctx: ProjectParser.ParensExprContext):
        return self.visit(ctx.expression())

    # Visit a parse tree produced by ProjectParser#stringExpr.
    def visitStringExpr(self, ctx: ProjectParser.StringExprContext):
        return f"push S {ctx.STRING_LITERAL().getText()} \n"

    # Visit a parse tree produced by ProjectParser#floatExpr.
    def visitFloatExpr(self, ctx: ProjectParser.FloatExprContext):
        return f"push F {ctx.FLOAT_LITERAL().getText()} \n"

    # Visit a parse tree produced by ProjectParser#eqExpr.
    def visitEqExpr(self, ctx: ProjectParser.EqExprContext):
        left_instructions = self.visit(ctx.expression()[0])
        left_dtype = self.types[ctx.expression()[0]]
        right_instructions = self.visit(ctx.expression()[1])
        right_dtype = self.types[ctx.expression()[1]]

        operator = ctx.op.text

        instructions = ""

        if left_dtype == "int" and right_dtype == "float":
            instructions += left_instructions + "itof \n" + right_instructions
            final_dtype = "F"
        elif left_dtype == "float" and right_dtype == "int":
            instructions += left_instructions + right_instructions + "itof \n"
            final_dtype = "F"
        else:
            instructions += left_instructions + right_instructions
            final_dtype = self._dtypeIf(left_dtype)

        if operator == "==":
            instructions += f"eq {final_dtype} \n"
        elif operator == "!=":
            instructions += f"eq {final_dtype} \n" + "not \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#notExpr.
    def visitNotExpr(self, ctx: ProjectParser.NotExprContext):
        expr = self.visit(ctx.expression())

        return expr + "not \n"

    # Visit a parse tree produced by ProjectParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx: ProjectParser.UnaryMinusExprContext):
        dtype = self.types[ctx.expression()]
        dtype_if = "I" if dtype == "int" else "F"
        instructions = ""

        instructions += self.visit(ctx.expression())
        instructions += f"uminus {dtype_if} \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#boolExpr.
    def visitBoolExpr(self, ctx: ProjectParser.BoolExprContext):
        return f"push B {ctx.BOOL_LITERAL().getText()} \n"

    # Visit a parse tree produced by ProjectParser#relExpr.
    def visitRelExpr(self, ctx: ProjectParser.RelExprContext):
        left_instructions = self.visit(ctx.expression()[0])
        left_dtype = self.types[ctx.expression()[0]]
        right_instructions = self.visit(ctx.expression()[1])
        right_dtype = self.types[ctx.expression()[1]]

        operator = ctx.op.text

        instructions = ""

        if left_dtype == "int" and right_dtype == "float":
            instructions += left_instructions + "itof \n" + right_instructions
            final_dtype = "F"
        elif left_dtype == "float" and right_dtype == "int":
            instructions += left_instructions + right_instructions + "itof \n"
            final_dtype = "F"
        else:
            instructions += left_instructions + right_instructions
            final_dtype = self._dtypeIf(left_dtype)

        if operator == ">":
            instructions += f"gt {final_dtype} \n"
        elif operator == "<":
            instructions += f"lt {final_dtype} \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#assignExpr.
    def visitAssignExpr(self, ctx: ProjectParser.AssignExprContext):
        var_name = ctx.IDENTIFIER().getText()
        var_dtype = self.symbol_table.resolve(var_name)
        value_dtype = self.types[ctx.expression()]

        instructions = ""
        instructions += self.visit(ctx.expression())

        if var_dtype == "float" and value_dtype == "int":
            instructions += "itof \n"

        instructions += f"save {var_name} \n"
        instructions += f"load {var_name} \n"

        return instructions

    # Visit a parse tree produced by ProjectParser#idExpr.
    def visitIdExpr(self, ctx: ProjectParser.IdExprContext):
        return f"load {ctx.IDENTIFIER().getText()} \n"

    # Visit a parse tree produced by ProjectParser#andExpr.
    def visitAndExpr(self, ctx: ProjectParser.AndExprContext):
        left_instructions = self.visit(ctx.expression()[0])
        right_instructions = self.visit(ctx.expression()[1])

        return left_instructions + right_instructions + "and \n"
