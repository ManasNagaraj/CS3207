%{
#include <stdio.h>
%}
%option noyywrap 
%%
.*a\n ECHO;
a.*\n ECHO;
.*\n ;
%%
int main() 
{
yyin = fopen("astar.txt","r"); 
printf("\nLines that START or END with 'a' are:\n");
printf("----------------------------------------\n");
yylex(); 
return 0; 
}
