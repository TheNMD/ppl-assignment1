grammar MT22;

@lexer::header {
from lexererr import *;
studentID = "2052932";
}

options{
	language=Python3;
}

program: decls EOF ;

decls : 'none' ;

// KEYWORD
KWVOID : 'void' ;
KWAUTO : 'auto' ;
KWINT :  'integer' ;
KWFLOAT : 'float' ;
KWBOO : 'boolean' ;
KWSTR : 'string' ;
KWARR : 'array' ;
KWINHERIT : 'inherit' ;
KWFUNC : 'function' ;
KWTRUE : 'true' ;
KWFALSE : 'false' ;
KWFOR : 'for' ;
KWWHILE : 'while' ;
KWDO : 'do' ;
KWBRK : 'break' ;
KWCONT : 'continue' ;
KWRTN : 'return' ;
KWIF : 'if' ;
KWELSE : 'else' ;
KWOF : 'of' ;
KWOUT : 'out' ;

// Identifiers
ID : [a-zA-Z_] [a-zA-Z0-9_]* ;

// Operators
ADDOP : '+' ;

SUBOP : '-' ;

MULOP : '*' ;

DIVOP : '/' ;

MODOP : '%' ;

EXC : '!' ;

ANDOP : '&&' ;

OROP : '||' ;

EQLOP : '==' ;

DIFOP : '!=' ;

LARGEOP : '>' ;

LEQLOP : '>=' ;

SMALLOP : '<' ;

SEQLOP : '<=' ;

CONCATOP : '::' ;

// Separators
DOT : '.' ;

CM : ',' ;

SM : ';' ;

CL : ':' ;

LB : '(' ;

RB : ')' ;

LSB : '[' ;

RSB : ']' ;

LCB : '{' ;

RCB : '}' ;

EQL : '=' ;

// Literals
INT : '0' | [1-9] [0-9_]* {self.text = self.text.replace('_','')} ;

FLOAT : INT DECIMAL? EXPONENT? ;

DECIMAL : '.' [0-9]* ;

EXPONENT : [eE] [+-]? [0-9]+ ;

BOOLEAN : KWTRUE | KWFALSE ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .{raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: .{raise ErrorToken(self.text)};