# Generated from ProjectParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,42,155,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,
        1,1,1,1,1,1,1,1,1,1,5,1,46,8,1,10,1,12,1,49,9,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,63,8,1,10,1,12,1,66,9,1,1,1,
        1,1,1,1,1,1,5,1,72,8,1,10,1,12,1,75,9,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,85,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,103,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,124,8,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,150,8,3,10,3,12,3,153,9,3,1,3,0,1,6,4,
        0,2,4,6,0,5,5,0,1,1,3,3,5,5,7,7,10,10,1,0,36,38,2,0,34,35,39,39,
        1,0,27,28,1,0,30,31,182,0,11,1,0,0,0,2,102,1,0,0,0,4,104,1,0,0,0,
        6,123,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,
        0,11,12,1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,15,5,0,0,1,15,1,1,
        0,0,0,16,103,5,23,0,0,17,18,3,4,2,0,18,23,5,42,0,0,19,20,5,25,0,
        0,20,22,5,42,0,0,21,19,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,
        1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,23,0,0,27,103,1,0,0,
        0,28,29,3,6,3,0,29,30,5,23,0,0,30,103,1,0,0,0,31,32,5,8,0,0,32,37,
        5,42,0,0,33,34,5,25,0,0,34,36,5,42,0,0,35,33,1,0,0,0,36,39,1,0,0,
        0,37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,103,
        5,23,0,0,41,42,5,9,0,0,42,47,3,6,3,0,43,44,5,25,0,0,44,46,3,6,3,
        0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,
        1,0,0,0,49,47,1,0,0,0,50,51,5,23,0,0,51,103,1,0,0,0,52,53,5,11,0,
        0,53,54,5,42,0,0,54,55,3,6,3,0,55,56,5,23,0,0,56,103,1,0,0,0,57,
        58,5,12,0,0,58,59,5,42,0,0,59,64,3,6,3,0,60,61,5,25,0,0,61,63,3,
        6,3,0,62,60,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,
        67,1,0,0,0,66,64,1,0,0,0,67,68,5,23,0,0,68,103,1,0,0,0,69,73,5,21,
        0,0,70,72,3,2,1,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,103,5,22,0,0,77,78,5,4,0,
        0,78,79,5,19,0,0,79,80,3,6,3,0,80,81,5,20,0,0,81,84,3,2,1,0,82,83,
        5,2,0,0,83,85,3,2,1,0,84,82,1,0,0,0,84,85,1,0,0,0,85,103,1,0,0,0,
        86,87,5,6,0,0,87,88,5,19,0,0,88,89,3,6,3,0,89,90,5,20,0,0,90,91,
        3,2,1,0,91,103,1,0,0,0,92,93,5,13,0,0,93,94,5,19,0,0,94,95,3,6,3,
        0,95,96,5,23,0,0,96,97,3,6,3,0,97,98,5,23,0,0,98,99,3,6,3,0,99,100,
        5,20,0,0,100,101,3,2,1,0,101,103,1,0,0,0,102,16,1,0,0,0,102,17,1,
        0,0,0,102,28,1,0,0,0,102,31,1,0,0,0,102,41,1,0,0,0,102,52,1,0,0,
        0,102,57,1,0,0,0,102,69,1,0,0,0,102,77,1,0,0,0,102,86,1,0,0,0,102,
        92,1,0,0,0,103,3,1,0,0,0,104,105,7,0,0,0,105,5,1,0,0,0,106,107,6,
        3,-1,0,107,108,5,35,0,0,108,124,3,6,3,16,109,110,5,29,0,0,110,124,
        3,6,3,15,111,112,5,42,0,0,112,113,5,26,0,0,113,124,3,6,3,7,114,115,
        5,19,0,0,115,116,3,6,3,0,116,117,5,20,0,0,117,124,1,0,0,0,118,124,
        5,42,0,0,119,124,5,15,0,0,120,124,5,16,0,0,121,124,5,17,0,0,122,
        124,5,18,0,0,123,106,1,0,0,0,123,109,1,0,0,0,123,111,1,0,0,0,123,
        114,1,0,0,0,123,118,1,0,0,0,123,119,1,0,0,0,123,120,1,0,0,0,123,
        121,1,0,0,0,123,122,1,0,0,0,124,151,1,0,0,0,125,126,10,14,0,0,126,
        127,7,1,0,0,127,150,3,6,3,15,128,129,10,13,0,0,129,130,7,2,0,0,130,
        150,3,6,3,14,131,132,10,12,0,0,132,133,7,3,0,0,133,150,3,6,3,13,
        134,135,10,11,0,0,135,136,7,4,0,0,136,150,3,6,3,12,137,138,10,10,
        0,0,138,139,5,32,0,0,139,150,3,6,3,11,140,141,10,9,0,0,141,142,5,
        33,0,0,142,150,3,6,3,10,143,144,10,8,0,0,144,145,5,14,0,0,145,146,
        3,6,3,0,146,147,5,24,0,0,147,148,3,6,3,9,148,150,1,0,0,0,149,125,
        1,0,0,0,149,128,1,0,0,0,149,131,1,0,0,0,149,134,1,0,0,0,149,137,
        1,0,0,0,149,140,1,0,0,0,149,143,1,0,0,0,150,153,1,0,0,0,151,149,
        1,0,0,0,151,152,1,0,0,0,152,7,1,0,0,0,153,151,1,0,0,0,11,11,23,37,
        47,64,73,84,102,123,149,151
    ]

class ProjectParser ( Parser ):

    grammarFileName = "ProjectParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'bool'", "'else'", "'float'", "'if'", 
                     "'int'", "'while'", "'string'", "'read'", "'write'", 
                     "'FILE'", "'fopen'", "'fwrite'", "'for'", "'?'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "';'", "':'", "','", "'='", "'>'", "'<'", 
                     "'!'", "'=='", "'!='", "'&&'", "'||'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'.'" ]

    symbolicNames = [ "<INVALID>", "BOOL", "ELSE", "FLOAT", "IF", "INT", 
                      "WHILE", "STRING", "READ", "WRITE", "FILE", "FOPEN", 
                      "FWRITE", "FOR", "TERN", "INT_LITERAL", "FLOAT_LITERAL", 
                      "BOOL_LITERAL", "STRING_LITERAL", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "SEMI", "COLON", "COMMA", "ASSIGN", 
                      "GT", "LT", "BANG", "EQUAL", "NOTEQUAL", "AND", "OR", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "DOT", "WS", "LINE_COMMENT", 
                      "IDENTIFIER" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_type = 2
    RULE_expression = 3

    ruleNames =  [ "program", "statement", "type", "expression" ]

    EOF = Token.EOF
    BOOL=1
    ELSE=2
    FLOAT=3
    IF=4
    INT=5
    WHILE=6
    STRING=7
    READ=8
    WRITE=9
    FILE=10
    FOPEN=11
    FWRITE=12
    FOR=13
    TERN=14
    INT_LITERAL=15
    FLOAT_LITERAL=16
    BOOL_LITERAL=17
    STRING_LITERAL=18
    LPAREN=19
    RPAREN=20
    LBRACE=21
    RBRACE=22
    SEMI=23
    COLON=24
    COMMA=25
    ASSIGN=26
    GT=27
    LT=28
    BANG=29
    EQUAL=30
    NOTEQUAL=31
    AND=32
    OR=33
    ADD=34
    SUB=35
    MUL=36
    DIV=37
    MOD=38
    DOT=39
    WS=40
    LINE_COMMENT=41
    IDENTIFIER=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ProjectParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProjectParser.StatementContext,i)


        def getRuleIndex(self):
            return ProjectParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ProjectParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4432954638330) != 0):
                self.state = 8
                self.statement()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.match(ProjectParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProjectParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ProjectParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(ProjectParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class ForStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(ProjectParser.FOR, 0)
        def LPAREN(self):
            return self.getToken(ProjectParser.LPAREN, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectParser.SEMI)
            else:
                return self.getToken(ProjectParser.SEMI, i)
        def RPAREN(self):
            return self.getToken(ProjectParser.RPAREN, 0)
        def statement(self):
            return self.getTypedRuleContext(ProjectParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(ProjectParser.WHILE, 0)
        def LPAREN(self):
            return self.getToken(ProjectParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(ProjectParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(ProjectParser.RPAREN, 0)
        def statement(self):
            return self.getTypedRuleContext(ProjectParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReadStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(ProjectParser.READ, 0)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectParser.IDENTIFIER)
            else:
                return self.getToken(ProjectParser.IDENTIFIER, i)
        def SEMI(self):
            return self.getToken(ProjectParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectParser.COMMA)
            else:
                return self.getToken(ProjectParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)


    class IfStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ProjectParser.IF, 0)
        def LPAREN(self):
            return self.getToken(ProjectParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(ProjectParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(ProjectParser.RPAREN, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProjectParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(ProjectParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)


    class BlockStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(ProjectParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(ProjectParser.RBRACE, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.StatementContext)
            else:
                return self.getTypedRuleContext(ProjectParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStmt" ):
                listener.enterBlockStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStmt" ):
                listener.exitBlockStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)


    class DeclStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(ProjectParser.TypeContext,0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectParser.IDENTIFIER)
            else:
                return self.getToken(ProjectParser.IDENTIFIER, i)
        def SEMI(self):
            return self.getToken(ProjectParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectParser.COMMA)
            else:
                return self.getToken(ProjectParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclStmt" ):
                listener.enterDeclStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclStmt" ):
                listener.exitDeclStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclStmt" ):
                return visitor.visitDeclStmt(self)
            else:
                return visitor.visitChildren(self)


    class FopenStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOPEN(self):
            return self.getToken(ProjectParser.FOPEN, 0)
        def IDENTIFIER(self):
            return self.getToken(ProjectParser.IDENTIFIER, 0)
        def expression(self):
            return self.getTypedRuleContext(ProjectParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(ProjectParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFopenStmt" ):
                listener.enterFopenStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFopenStmt" ):
                listener.exitFopenStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFopenStmt" ):
                return visitor.visitFopenStmt(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(ProjectParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStmt" ):
                listener.enterEmptyStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStmt" ):
                listener.exitEmptyStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStmt" ):
                return visitor.visitEmptyStmt(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(ProjectParser.WRITE, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)

        def SEMI(self):
            return self.getToken(ProjectParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectParser.COMMA)
            else:
                return self.getToken(ProjectParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStmt" ):
                listener.enterWriteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStmt" ):
                listener.exitWriteStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)


    class FwriteStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FWRITE(self):
            return self.getToken(ProjectParser.FWRITE, 0)
        def IDENTIFIER(self):
            return self.getToken(ProjectParser.IDENTIFIER, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)

        def SEMI(self):
            return self.getToken(ProjectParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ProjectParser.COMMA)
            else:
                return self.getToken(ProjectParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFwriteStmt" ):
                listener.enterFwriteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFwriteStmt" ):
                listener.exitFwriteStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFwriteStmt" ):
                return visitor.visitFwriteStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ProjectParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = ProjectParser.EmptyStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(ProjectParser.SEMI)
                pass
            elif token in [1, 3, 5, 7, 10]:
                localctx = ProjectParser.DeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.type_()
                self.state = 18
                self.match(ProjectParser.IDENTIFIER)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 19
                    self.match(ProjectParser.COMMA)
                    self.state = 20
                    self.match(ProjectParser.IDENTIFIER)
                    self.state = 25
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 26
                self.match(ProjectParser.SEMI)
                pass
            elif token in [15, 16, 17, 18, 19, 29, 35, 42]:
                localctx = ProjectParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.expression(0)
                self.state = 29
                self.match(ProjectParser.SEMI)
                pass
            elif token in [8]:
                localctx = ProjectParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.match(ProjectParser.READ)
                self.state = 32
                self.match(ProjectParser.IDENTIFIER)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 33
                    self.match(ProjectParser.COMMA)
                    self.state = 34
                    self.match(ProjectParser.IDENTIFIER)
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 40
                self.match(ProjectParser.SEMI)
                pass
            elif token in [9]:
                localctx = ProjectParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.match(ProjectParser.WRITE)
                self.state = 42
                self.expression(0)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 43
                    self.match(ProjectParser.COMMA)
                    self.state = 44
                    self.expression(0)
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
                self.match(ProjectParser.SEMI)
                pass
            elif token in [11]:
                localctx = ProjectParser.FopenStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.match(ProjectParser.FOPEN)
                self.state = 53
                self.match(ProjectParser.IDENTIFIER)
                self.state = 54
                self.expression(0)
                self.state = 55
                self.match(ProjectParser.SEMI)
                pass
            elif token in [12]:
                localctx = ProjectParser.FwriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.match(ProjectParser.FWRITE)
                self.state = 58
                self.match(ProjectParser.IDENTIFIER)
                self.state = 59
                self.expression(0)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 60
                    self.match(ProjectParser.COMMA)
                    self.state = 61
                    self.expression(0)
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 67
                self.match(ProjectParser.SEMI)
                pass
            elif token in [21]:
                localctx = ProjectParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                self.match(ProjectParser.LBRACE)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4432954638330) != 0):
                    self.state = 70
                    self.statement()
                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 76
                self.match(ProjectParser.RBRACE)
                pass
            elif token in [4]:
                localctx = ProjectParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 77
                self.match(ProjectParser.IF)
                self.state = 78
                self.match(ProjectParser.LPAREN)
                self.state = 79
                self.expression(0)
                self.state = 80
                self.match(ProjectParser.RPAREN)
                self.state = 81
                self.statement()
                self.state = 84
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 82
                    self.match(ProjectParser.ELSE)
                    self.state = 83
                    self.statement()


                pass
            elif token in [6]:
                localctx = ProjectParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 86
                self.match(ProjectParser.WHILE)
                self.state = 87
                self.match(ProjectParser.LPAREN)
                self.state = 88
                self.expression(0)
                self.state = 89
                self.match(ProjectParser.RPAREN)
                self.state = 90
                self.statement()
                pass
            elif token in [13]:
                localctx = ProjectParser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 92
                self.match(ProjectParser.FOR)
                self.state = 93
                self.match(ProjectParser.LPAREN)
                self.state = 94
                self.expression(0)
                self.state = 95
                self.match(ProjectParser.SEMI)
                self.state = 96
                self.expression(0)
                self.state = 97
                self.match(ProjectParser.SEMI)
                self.state = 98
                self.expression(0)
                self.state = 99
                self.match(ProjectParser.RPAREN)
                self.state = 100
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ProjectParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ProjectParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(ProjectParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ProjectParser.STRING, 0)

        def FILE(self):
            return self.getToken(ProjectParser.FILE, 0)

        def getRuleIndex(self):
            return ProjectParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ProjectParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1194) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProjectParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IntExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_LITERAL(self):
            return self.getToken(ProjectParser.INT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubConcatExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(ProjectParser.ADD, 0)
        def SUB(self):
            return self.getToken(ProjectParser.SUB, 0)
        def DOT(self):
            return self.getToken(ProjectParser.DOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubConcatExpr" ):
                listener.enterAddSubConcatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubConcatExpr" ):
                listener.exitAddSubConcatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubConcatExpr" ):
                return visitor.visitAddSubConcatExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(ProjectParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivModExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(ProjectParser.MUL, 0)
        def DIV(self):
            return self.getToken(ProjectParser.DIV, 0)
        def MOD(self):
            return self.getToken(ProjectParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivModExpr" ):
                listener.enterMulDivModExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivModExpr" ):
                listener.exitMulDivModExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivModExpr" ):
                return visitor.visitMulDivModExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ProjectParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(ProjectParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(ProjectParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(ProjectParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LITERAL(self):
            return self.getToken(ProjectParser.FLOAT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)

        def EQUAL(self):
            return self.getToken(ProjectParser.EQUAL, 0)
        def NOTEQUAL(self):
            return self.getToken(ProjectParser.NOTEQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqExpr" ):
                listener.enterEqExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqExpr" ):
                listener.exitEqExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BANG(self):
            return self.getToken(ProjectParser.BANG, 0)
        def expression(self):
            return self.getTypedRuleContext(ProjectParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(ProjectParser.SUB, 0)
        def expression(self):
            return self.getTypedRuleContext(ProjectParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpr" ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpr" ):
                listener.exitUnaryMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class TernExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)

        def TERN(self):
            return self.getToken(ProjectParser.TERN, 0)
        def COLON(self):
            return self.getToken(ProjectParser.COLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernExpr" ):
                listener.enterTernExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernExpr" ):
                listener.exitTernExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernExpr" ):
                return visitor.visitTernExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_LITERAL(self):
            return self.getToken(ProjectParser.BOOL_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)

        def LT(self):
            return self.getToken(ProjectParser.LT, 0)
        def GT(self):
            return self.getToken(ProjectParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ProjectParser.IDENTIFIER, 0)
        def ASSIGN(self):
            return self.getToken(ProjectParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(ProjectParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ProjectParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProjectParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProjectParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ProjectParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(ProjectParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ProjectParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = ProjectParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 107
                self.match(ProjectParser.SUB)
                self.state = 108
                self.expression(16)
                pass

            elif la_ == 2:
                localctx = ProjectParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(ProjectParser.BANG)
                self.state = 110
                self.expression(15)
                pass

            elif la_ == 3:
                localctx = ProjectParser.AssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(ProjectParser.IDENTIFIER)
                self.state = 112
                self.match(ProjectParser.ASSIGN)
                self.state = 113
                self.expression(7)
                pass

            elif la_ == 4:
                localctx = ProjectParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(ProjectParser.LPAREN)
                self.state = 115
                self.expression(0)
                self.state = 116
                self.match(ProjectParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = ProjectParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.match(ProjectParser.IDENTIFIER)
                pass

            elif la_ == 6:
                localctx = ProjectParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(ProjectParser.INT_LITERAL)
                pass

            elif la_ == 7:
                localctx = ProjectParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(ProjectParser.FLOAT_LITERAL)
                pass

            elif la_ == 8:
                localctx = ProjectParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.match(ProjectParser.BOOL_LITERAL)
                pass

            elif la_ == 9:
                localctx = ProjectParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(ProjectParser.STRING_LITERAL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 149
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ProjectParser.MulDivModExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 125
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 126
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 481036337152) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expression(15)
                        pass

                    elif la_ == 2:
                        localctx = ProjectParser.AddSubConcatExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 128
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 129
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 601295421440) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 130
                        self.expression(14)
                        pass

                    elif la_ == 3:
                        localctx = ProjectParser.RelExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 131
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 132
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 133
                        self.expression(13)
                        pass

                    elif la_ == 4:
                        localctx = ProjectParser.EqExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 134
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 135
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==30 or _la==31):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 136
                        self.expression(12)
                        pass

                    elif la_ == 5:
                        localctx = ProjectParser.AndExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 137
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 138
                        self.match(ProjectParser.AND)
                        self.state = 139
                        self.expression(11)
                        pass

                    elif la_ == 6:
                        localctx = ProjectParser.OrExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 140
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 141
                        self.match(ProjectParser.OR)
                        self.state = 142
                        self.expression(10)
                        pass

                    elif la_ == 7:
                        localctx = ProjectParser.TernExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 143
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 144
                        self.match(ProjectParser.TERN)
                        self.state = 145
                        self.expression(0)
                        self.state = 146
                        self.match(ProjectParser.COLON)
                        self.state = 147
                        self.expression(9)
                        pass

             
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




