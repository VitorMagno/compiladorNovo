grammar BigT;


programa_minipar: ;























// parser rules start with lowercase letters, lexer rules with uppercase
IF :   'IF';
ELSE :   'ELSE';
WHILE :   'WHILE';
AND :   '&&';
OR :   '||';
NOT:    '!';
GE :    '>=';
LE :    '<=';
EQ :    '==';
LT:     '<';
GT :    '>';
MUL :   '*' ;                   // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   [a-zA-Z]+([0-9]*|[a-zA-Z]*);
NEWLINE: '\r'? '\n' ;
SEQ :   'SEQ';
PAR :   'PAR';
INT :   [0-9]+ ;             // Define token INT as one or more digits
WS  :   [ \t]+ -> skip ;    // Define whitespace rule, toss it out
