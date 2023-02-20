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

EXCOP : '!' ;

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

//ERROR_CHAR: .{raise ErrorToken(self.text)};

//NCLOSE_STRING: .{raise ErrorToken(self.text)};

//ILLEGAL_ESCAPE: .{raise ErrorToken(self.text)};

//==========================================================
// Parser Rules
//==========================================================

program : declist EOF ;

declist : decl declist | decl ;

decl : vardecl | funcdecl ;

vardecl : idlist CL vartyp (EQL exprlist)? SM | idlist CL KWAUTO EQL exprlist SM | idlist CL KWARR LSB idxlist RSB 'of' vartyp (EQL arraylist)? SM ;

idlist : ID ids | ID ;

ids : CM ID ids | ;

vartyp : KWINT | KWFLOAT | KWBOO | KWSTR ;

idxlist : idx idxs | idx {self.text = self.text.replace('_','')} ;

idxs : CM idx idxs | {self.text = self.text.replace('_','')} ;

idx : LITINT ;

arraylist : array arrays | array ;

arrays : CM array arrays | ;

array : LCB exprlist RCB ;

funcdecl : ID CL KWFUNC functyp LB paralist RB (KWINHERIT ID)? LCB bodylist RCB 
		 | ID CL KWFUNC KWAUTO LB paralist RB (KWINHERIT ID)? LCB bodylistauto RCB 
		 | ID CL KWFUNC KWVOID LB paralist RB (KWINHERIT ID)? LCB bodylistvoid RCB ;

paralist : para paras | ;

paras : CM para paras | ;

para :  KWINHERIT? KWOUT? ID CL vartyp ;

functyp :  KWINT | KWFLOAT | KWBOO | KWSTR ;

bodylist : bodydecl bodylist | ;

stmt : (assignstmt | callstmt | rtnstmt) SM ;

bodydecl : vardecl | stmt ;

bodylistauto : bodydecl bodylistauto | rtnstmt SM ;

bodylistvoid : bodydeclvoid bodylistvoid | ;

bodydeclvoid : vardecl | stmtvoid ;

stmtvoid : (assignstmt | callstmt | 'return') SM ;

assignstmt : (ID | ID idxop)  '=' expr ;

callstmt : ID LB exprlist RB ;

rtnstmt : 'return' expr ;

exprlist : expr exprs | ;

exprs : CM expr exprs | ;

expr : unexpr | biexpr ;

unexpr :  EXCOP unexpr | unexpr1 ;

unexpr1 : SUBOP unexpr1 | unexpr2 ;

unexpr2 : unexpr2 idxop | operand ;

idxop : LSB idxlist RSB ;

biexpr : biexpr1 CONCATOP biexpr1 | biexpr1 ;

biexpr1 : biexpr2 (EQLOP | DIFOP | LARGEOP | LEQLOP | SMALLOP | SEQLOP)  biexpr2 | biexpr2 ;

biexpr2 : biexpr2 (ANDOP | OROP) biexpr3 | biexpr3 ;

biexpr3 : biexpr3 (ADDOP | SUBOP) biexpr4 | biexpr4 ;

biexpr4 : biexpr4 (MULOP | DIVOP | MODOP) operand | operand ;

operand: LITINT | LITFLOAT | LITBOO | LITSTR | ID | callstmt | subexpr | ID idxop | LCB exprlist RCB ;

subexpr: LB expr RB ;