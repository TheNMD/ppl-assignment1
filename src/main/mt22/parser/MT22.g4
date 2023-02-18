grammar MT22;

@lexer::header {
from lexererr import *;
studentID = "2052932";
}

options{
	language=Python3;
}

//==========================================================
// Lexer Rules
//==========================================================

// COMMENT
CCOMMENT :  '//' .*? ;
CPPCOMMENT : '/*' .*? '*/' ;

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
LITINT : '0' | [1-9] [0-9_]* {self.text = self.text.replace('_','')} ;

LITFLOAT : LITINT Decimal? Exponent?  {self.text = self.text.replace('_','')} ;

fragment Decimal : '.' [0-9]* ;

fragment Exponent : [eE] [+-]? [0-9]+ ;

LITBOO : KWTRUE | KWFALSE ;

fragment DoubleQuote : '"' ;

fragment InvDoubleQuote : ~ '"' ;

LITSTR : '"' ('\\' DoubleQuote | InvDoubleQuote)* '"' {self.text = self.text.replace('"','')} {self.text = self.text.replace('\\','\\"')}  ;

LITARR : LCB 'none' RCB ;

//==========================================================
// Parser Rules
//==========================================================

program : declist EOF ;

declist : decl declist | decl ;

decl : vardecl | funcdecl ;

vardecl : idlist CL typ init SM ;

idlist : ID ids | ID ;

ids : CM ID ids | ;

typ : 'integer' | 'float' | 'boolean' | 'string' | LITARR ;

init : (EQL exprlist)? ;

funcdecl : typ ID paradecl body ;

paradecl: LB paralist RB ;

paralist : para paras | ;

paras : SM para paras | ;

para : typ idlist ;

body : LCB bodylist RCB ;

bodylist : bodydecl bodylist | ;

bodydecl : vardecl | stmt ;

stmt : (assignstmt | callstmt | returnstmt) SM ;

assignstmt : ID '=' expr ;

callstmt : ID LB exprlist RB ;

exprlist : expr exprs | ;

exprs : CM expr exprs | ;

returnstmt : 'return' expr ;

expr : 'expr' ;

WS : [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .{raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: .{raise ErrorToken(self.text)};