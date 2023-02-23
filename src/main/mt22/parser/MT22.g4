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

litarr : LCB exprlist? RCB ;

ERROR_CHAR: .{raise ErrorToken(self.text)};

NCLOSE_STRING: .{raise ErrorToken(self.text)};

ILLEGAL_ESCAPE: .{raise ErrorToken(self.text)};

//==========================================================
// Parser Rules
//==========================================================

program : declist EOF ;

declist : decl declist | decl ;

decl : vardecl | funcdecl ;

vardecl : idlist CL vartyp SM 
		| ID middle expr SM 
 		| idlist CL KWARR LSB idxlist RSB KWOF vartyp (EQL litarr)? SM ;

idlist : ID ids | ID ;

ids : CM ID ids | ;

middle : CM ID middle expr CM | CL (vartyp | KWAUTO) EQL ;

vartyp : KWINT | KWFLOAT | KWBOO | KWSTR ;

idxlist : LITINT idxs | LITINT {self.text = self.text.replace('_','')} ;

idxs : CM LITINT idxs | {self.text = self.text.replace('_','')} ;

funcdecl : ID CL KWFUNC (functyp | KWAUTO) LB paralist RB (KWINHERIT ID)? LCB bodylist RCB
		 | ID CL KWFUNC KWVOID LB paralist RB (KWINHERIT ID)? LCB bodylistvoid RCB ;

paralist : para paras | ;

paras : CM para paras | ;

para :  KWINHERIT? KWOUT? ID CL vartyp ;

functyp :  KWINT | KWFLOAT | KWBOO | KWSTR ;

bodylist : body bodies | rtnstmt ;

bodylistvoid : body bodies | ;

bodies : body bodies | ;

body : vardecl | stmt | ifstmt ;

stmt : assignstmt | forstmt | whilestmt | dowhilestmt | breakstmt | continuestmt | rtnstmt | callstmt | blockstmt ;

assignstmt : (ID | ID idxop)  EQL expr SM ;

ifstmt : matchstmt | unmatchstmt ;

matchstmt : KWIF LB expr RB matchstmt KWELSE matchstmt | stmt ;

unmatchstmt : KWIF LB expr RB ifstmt | KWIF LB expr RB matchstmt KWELSE unmatchstmt ;

forstmt : KWFOR LB ID EQL expr CM expr CM expr RB (stmt | ifstmt) ;

whilestmt : KWWHILE LB expr RB (stmt | ifstmt) ;

dowhilestmt : KWDO blockstmt KWWHILE LB expr RB SM ;

breakstmt : KWBRK SM ;

continuestmt : KWCONT SM ;

rtnstmt : KWRTN (expr)? SM ;

callstmt : funccall SM ;

blockstmt : LCB bodylistvoid RCB ;

exprlist : expr exprs | expr ;

exprs : CM expr exprs | ;

expr : expr1 CONCATOP expr1 | expr1 ;

expr1 : expr2 (EQLOP | DIFOP | LARGEOP | LEQLOP | SMALLOP | SEQLOP)  expr2 | expr2 ;

expr2 : expr2 (ANDOP | OROP) expr3 | expr3 ;

expr3 : expr3 (ADDOP | SUBOP) expr4 | expr4 ;

expr4 : expr4 (MULOP | DIVOP | MODOP) expr5 | expr5 ;

expr5 :  EXCOP expr5 | expr6 ;

expr6 : SUBOP expr6 | operand ;

//expr7 : expr7 idxop | operand ;

operand: LITINT | LITFLOAT | LITBOO | LITSTR | ID idxop? | funccall | subexpr | litarr ;

idxop : LSB idxlist RSB ;

funccall : (specialfunc | ID) LB exprlist? RB ;

specialfunc : 'readInteger' | 'printInteger' | 'readFloat' | 'writeFloat' | 'readBoolean' | 'printBoolean' | 'readString' | 'printString' | 'super' | 'preventDefault' ;

subexpr : LB expr RB ;