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

// Whitespace
WS : [ \t\n\r\f\b]+ -> skip ;

// COMMENT
CCOMMENT :  '/*' .*? '*/' -> skip;

CPPCOMMENT : '//' ~ [\r\n]* -> skip;

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
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

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
LITINT : '0' | [1-9][0-9_]* {self.text = self.text.replace('_','')} ;

LITFLOAT : LITINT Decimal? Exponent?  {self.text = self.text.replace('_','')} ;

fragment Decimal : '.'[0-9]* ;

fragment Exponent : [eE][+-]?[0-9]+ ;

LITBOO : KWTRUE | KWFALSE ;

LITSTR : '"' ('\\' [bfrnt'\\"] | ~[\b\f\r\n\t'\\"])* '"' {self.text = self.text.replace('"','')} {self.text = self.text.replace('\\','\\"')}  ;

litarr : LCB exprlist RCB ;

//ERROR_CHAR: .{raise ErrorToken(self.text)};

//NCLOSE_STRING: .{raise ErrorToken(self.text)};

//ILLEGAL_ESCAPE: .{raise ErrorToken(self.text)};

//==========================================================
// Parser Rules
//==========================================================

program : declist EOF ;

declist : decl declist | decl ;

decl : vardecl | funcdecl ;

vardecl : idlist CL vartyp (EQL exprlist)? SM ;

idlist : ID ids | ID ;

ids : CM ID ids | ;

vartyp : KWAUTO | KWINT | KWFLOAT | KWBOO | KWSTR | KWARR ;

funcdecl : funcproto funcbody ;

funcproto : ID CL KWFUNC functyp LB paralist RB (KWINHERIT ID)? ;

paralist : para paras | ;

paras : CM para paras | ;

para :  KWINHERIT? KWOUT? ID CL vartyp ;

functyp : KWAUTO | KWINT | KWFLOAT | KWBOO | KWSTR | KWVOID ;

funcbody : LCB bodylist RCB ;

bodylist : bodydecl bodylist | ;

bodydecl : vardecl | stmt ;

stmt : (assignstmt | callstmt | returnstmt) SM ;

assignstmt : ID '=' expr ;

callstmt : ID LB exprlist RB ;

exprlist : expr exprs | ;

exprs : CM expr exprs | ;

returnstmt : 'return' expr ;

expr: expr1 ADDOP expr | expr1 ;

expr1: expr2 SUBOP expr2 | expr2 ;

expr2: expr2 (MULOP | DIVOP) operand | operand ;

operand: LITINT | LITFLOAT | LITBOO | LITSTR | litarr | ID | callstmt | subexpr ;

subexpr: LB expr RB ;