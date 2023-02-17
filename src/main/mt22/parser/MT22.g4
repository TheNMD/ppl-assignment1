grammar MT22;

@lexer::header {
from lexererr import *;
studentID = "2052932";
}

options{
	language=Python3;
}

program:  EOF ;

// Identifiers
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

// Keywords

// Operators
ADDOP : '+' ;

SUBOP : '-' ;

MULOP : '*' ;

DIVOP : '/' ;

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

// Literals
INT : '0' | [1-9][0-9_]* {self.text = self.text.replace('_','')} ;

FLOAT : INT DECIMAL? EXPONENT? ;

DECIMAL : '.' [0-9]* ;

EXPONENT : [eE] [+-]? [0-9]+ ;

BOOLEAN : 'true' | 'false' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;