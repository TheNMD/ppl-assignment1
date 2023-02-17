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
INTLIT : '0' | [1-9][0-9_]* {self.text = self.text.replace('_','')} ;

FLOATLIT: [0-9]+ ('.' [0-9]+ | [eE][+-]? [0-9]+ | '.' [0-9]+ [eE][+-]? [0-9]+) ;

BOOLIT : 'true' | 'false' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;