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
        4,1,36,122,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,1,
        1,1,1,1,1,1,1,1,1,1,5,1,46,8,1,10,1,12,1,49,9,1,1,1,1,1,1,1,1,1,
        5,1,55,8,1,10,1,12,1,58,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        68,8,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,76,8,1,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,97,8,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,5,3,117,8,3,10,3,12,3,120,9,3,1,3,0,1,6,4,0,2,4,6,0,5,4,
        0,1,1,3,3,5,5,7,7,1,0,30,32,2,0,28,29,33,33,1,0,21,22,1,0,24,25,
        144,0,11,1,0,0,0,2,75,1,0,0,0,4,77,1,0,0,0,6,96,1,0,0,0,8,10,3,2,
        1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,14,1,
        0,0,0,13,11,1,0,0,0,14,15,5,0,0,1,15,1,1,0,0,0,16,76,5,18,0,0,17,
        18,3,4,2,0,18,23,5,36,0,0,19,20,5,19,0,0,20,22,5,36,0,0,21,19,1,
        0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,
        23,1,0,0,0,26,27,5,18,0,0,27,76,1,0,0,0,28,29,3,6,3,0,29,30,5,18,
        0,0,30,76,1,0,0,0,31,32,5,8,0,0,32,37,5,36,0,0,33,34,5,19,0,0,34,
        36,5,36,0,0,35,33,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,
        0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,76,5,18,0,0,41,42,5,9,0,0,42,
        47,3,6,3,0,43,44,5,19,0,0,44,46,3,6,3,0,45,43,1,0,0,0,46,49,1,0,
        0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,
        5,18,0,0,51,76,1,0,0,0,52,56,5,16,0,0,53,55,3,2,1,0,54,53,1,0,0,
        0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,56,
        1,0,0,0,59,76,5,17,0,0,60,61,5,4,0,0,61,62,5,14,0,0,62,63,3,6,3,
        0,63,64,5,15,0,0,64,67,3,2,1,0,65,66,5,2,0,0,66,68,3,2,1,0,67,65,
        1,0,0,0,67,68,1,0,0,0,68,76,1,0,0,0,69,70,5,6,0,0,70,71,5,14,0,0,
        71,72,3,6,3,0,72,73,5,15,0,0,73,74,3,2,1,0,74,76,1,0,0,0,75,16,1,
        0,0,0,75,17,1,0,0,0,75,28,1,0,0,0,75,31,1,0,0,0,75,41,1,0,0,0,75,
        52,1,0,0,0,75,60,1,0,0,0,75,69,1,0,0,0,76,3,1,0,0,0,77,78,7,0,0,
        0,78,5,1,0,0,0,79,80,6,3,-1,0,80,81,5,29,0,0,81,97,3,6,3,15,82,83,
        5,23,0,0,83,97,3,6,3,14,84,85,5,36,0,0,85,86,5,20,0,0,86,97,3,6,
        3,7,87,88,5,14,0,0,88,89,3,6,3,0,89,90,5,15,0,0,90,97,1,0,0,0,91,
        97,5,36,0,0,92,97,5,10,0,0,93,97,5,11,0,0,94,97,5,12,0,0,95,97,5,
        13,0,0,96,79,1,0,0,0,96,82,1,0,0,0,96,84,1,0,0,0,96,87,1,0,0,0,96,
        91,1,0,0,0,96,92,1,0,0,0,96,93,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,
        0,97,118,1,0,0,0,98,99,10,13,0,0,99,100,7,1,0,0,100,117,3,6,3,14,
        101,102,10,12,0,0,102,103,7,2,0,0,103,117,3,6,3,13,104,105,10,11,
        0,0,105,106,7,3,0,0,106,117,3,6,3,12,107,108,10,10,0,0,108,109,7,
        4,0,0,109,117,3,6,3,11,110,111,10,9,0,0,111,112,5,26,0,0,112,117,
        3,6,3,10,113,114,10,8,0,0,114,115,5,27,0,0,115,117,3,6,3,9,116,98,
        1,0,0,0,116,101,1,0,0,0,116,104,1,0,0,0,116,107,1,0,0,0,116,110,
        1,0,0,0,116,113,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,
        1,0,0,0,119,7,1,0,0,0,120,118,1,0,0,0,10,11,23,37,47,56,67,75,96,
        116,118
    ]

class ProjectParser ( Parser ):

    grammarFileName = "ProjectParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'bool'", "'else'", "'float'", "'if'", 
                     "'int'", "'while'", "'string'", "'read'", "'write'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "';'", "','", "'='", "'>'", 
                     "'<'", "'!'", "'=='", "'!='", "'&&'", "'||'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'.'" ]

    symbolicNames = [ "<INVALID>", "BOOL", "ELSE", "FLOAT", "IF", "INT", 
                      "WHILE", "STRING", "READ", "WRITE", "INT_LITERAL", 
                      "FLOAT_LITERAL", "BOOL_LITERAL", "STRING_LITERAL", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "COMMA", 
                      "ASSIGN", "GT", "LT", "BANG", "EQUAL", "NOTEQUAL", 
                      "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "DOT", 
                      "WS", "LINE_COMMENT", "IDENTIFIER" ]

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
    INT_LITERAL=10
    FLOAT_LITERAL=11
    BOOL_LITERAL=12
    STRING_LITERAL=13
    LPAREN=14
    RPAREN=15
    LBRACE=16
    RBRACE=17
    SEMI=18
    COMMA=19
    ASSIGN=20
    GT=21
    LT=22
    BANG=23
    EQUAL=24
    NOTEQUAL=25
    AND=26
    OR=27
    ADD=28
    SUB=29
    MUL=30
    DIV=31
    MOD=32
    DOT=33
    WS=34
    LINE_COMMENT=35
    IDENTIFIER=36

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 69265096698) != 0):
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



    def statement(self):

        localctx = ProjectParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = ProjectParser.EmptyStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(ProjectParser.SEMI)
                pass
            elif token in [1, 3, 5, 7]:
                localctx = ProjectParser.DeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.type_()
                self.state = 18
                self.match(ProjectParser.IDENTIFIER)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==19:
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
            elif token in [10, 11, 12, 13, 14, 23, 29, 36]:
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
                while _la==19:
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
                while _la==19:
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
            elif token in [16]:
                localctx = ProjectParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.match(ProjectParser.LBRACE)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 69265096698) != 0):
                    self.state = 53
                    self.statement()
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 59
                self.match(ProjectParser.RBRACE)
                pass
            elif token in [4]:
                localctx = ProjectParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.match(ProjectParser.IF)
                self.state = 61
                self.match(ProjectParser.LPAREN)
                self.state = 62
                self.expression(0)
                self.state = 63
                self.match(ProjectParser.RPAREN)
                self.state = 64
                self.statement()
                self.state = 67
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 65
                    self.match(ProjectParser.ELSE)
                    self.state = 66
                    self.statement()


                pass
            elif token in [6]:
                localctx = ProjectParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                self.match(ProjectParser.WHILE)
                self.state = 70
                self.match(ProjectParser.LPAREN)
                self.state = 71
                self.expression(0)
                self.state = 72
                self.match(ProjectParser.RPAREN)
                self.state = 73
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
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 170) != 0)):
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
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = ProjectParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.match(ProjectParser.SUB)
                self.state = 81
                self.expression(15)
                pass

            elif la_ == 2:
                localctx = ProjectParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.match(ProjectParser.BANG)
                self.state = 83
                self.expression(14)
                pass

            elif la_ == 3:
                localctx = ProjectParser.AssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.match(ProjectParser.IDENTIFIER)
                self.state = 85
                self.match(ProjectParser.ASSIGN)
                self.state = 86
                self.expression(7)
                pass

            elif la_ == 4:
                localctx = ProjectParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 87
                self.match(ProjectParser.LPAREN)
                self.state = 88
                self.expression(0)
                self.state = 89
                self.match(ProjectParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = ProjectParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.match(ProjectParser.IDENTIFIER)
                pass

            elif la_ == 6:
                localctx = ProjectParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                self.match(ProjectParser.INT_LITERAL)
                pass

            elif la_ == 7:
                localctx = ProjectParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(ProjectParser.FLOAT_LITERAL)
                pass

            elif la_ == 8:
                localctx = ProjectParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 94
                self.match(ProjectParser.BOOL_LITERAL)
                pass

            elif la_ == 9:
                localctx = ProjectParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(ProjectParser.STRING_LITERAL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 116
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = ProjectParser.MulDivModExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 98
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 99
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 100
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = ProjectParser.AddSubConcatExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 101
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 102
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9395240960) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 103
                        self.expression(13)
                        pass

                    elif la_ == 3:
                        localctx = ProjectParser.RelExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 104
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 105
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        self.expression(12)
                        pass

                    elif la_ == 4:
                        localctx = ProjectParser.EqExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 107
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 108
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 109
                        self.expression(11)
                        pass

                    elif la_ == 5:
                        localctx = ProjectParser.AndExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 110
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 111
                        self.match(ProjectParser.AND)
                        self.state = 112
                        self.expression(10)
                        pass

                    elif la_ == 6:
                        localctx = ProjectParser.OrExprContext(self, ProjectParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 113
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 114
                        self.match(ProjectParser.OR)
                        self.state = 115
                        self.expression(9)
                        pass

             
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         




