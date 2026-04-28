lexer grammar ProjectLexer;

// Keywords
BOOL:               'bool';
ELSE:               'else';
FLOAT:              'float';
IF:                 'if';
INT:                'int';
WHILE:              'while';
STRING:             'string';
READ:               'read';
WRITE:              'write';


// Literals

INT_LITERAL:        [0-9]+;
FLOAT_LITERAL:      [0-9]+ '.' [0-9]+;

BOOL_LITERAL:       'true'
            |       'false'
            ;

STRING_LITERAL:     '"' (~["\\] | '\\' .)* '"';

// Separators

LPAREN:             '(';
RPAREN:             ')';
LBRACE:             '{';
RBRACE:             '}';
LBRACKET:           '[';
RBRACKET:           ']';
SEMI:               ';';
COMMA:              ',';

// Operators

ASSIGN:             '=';
GT:                 '>';
LT:                 '<';
BANG:               '!';
EQUAL:              '==';
NOTEQUAL:           '!=';
AND:                '&&';
OR:                 '||';
ADD:                '+';
SUB:                '-';
MUL:                '*';
DIV:                '/';
MOD:                '%';
DOT:                '.';



// Whitespace and comments

WS:                 [ \t\r\n\u000C]+ -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*    -> channel(HIDDEN);

// Identifiers
IDENTIFIER:         [a-zA-Z] [a-zA-Z0-9]*;
