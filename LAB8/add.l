%{
#include<stdio.h>
#include "y.tab.c"
%}

%%
[0-9]+		{yylval.tok=yytext[0]; return NUM;}
[a-z] 		{yylval.tok=yytext[0]; return VAR;}
.			{return yytext[0];}
\n 			{return 0;}
%%

int yywrap(){return 1;}