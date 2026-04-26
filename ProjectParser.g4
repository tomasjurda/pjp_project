parser grammar ProjectParser;

options { tokenVocab=ProjectLexer; }

program : statement* EOF ;

// Statements 
statement
    : SEMI                                                      # emptyStmt
    | type IDENTIFIER (COMMA IDENTIFIER)* SEMI                  # declStmt
    | expression SEMI                                           # exprStmt
    | READ IDENTIFIER (COMMA IDENTIFIER)* SEMI                  # readStmt
    | WRITE expression (COMMA expression)* SEMI                 # writeStmt
    | LBRACE statement* RBRACE                                  # blockStmt
    | IF LPAREN expression RPAREN statement (ELSE statement)?   # ifStmt
    | WHILE LPAREN expression RPAREN statement                  # whileStmt
    ;

// Variable Types
type
    : INT | FLOAT | BOOL | STRING
    ;

// Expressions 
// Top = Highest priority. Bottom = Lowest priority.
expression
    : SUB expression                                            # unaryMinusExpr
    | BANG expression                                           # notExpr
    | expression op=(MUL | DIV | MOD) expression                # mulDivModExpr
    | expression op=(ADD | SUB | DOT) expression                # addSubConcatExpr
    | expression op=(LT | GT) expression                        # relExpr
    | expression op=(EQUAL | NOTEQUAL) expression               # eqExpr
    | expression AND expression                                 # andExpr
    | expression OR expression                                  # orExpr
    | IDENTIFIER ASSIGN expression                              # assignExpr
    | LPAREN expression RPAREN                                  # parensExpr
    | IDENTIFIER                                                # idExpr
    | INT_LITERAL                                               # intExpr
    | FLOAT_LITERAL                                             # floatExpr
    | BOOL_LITERAL                                              # boolExpr
    | STRING_LITERAL                                            # stringExpr
    ;