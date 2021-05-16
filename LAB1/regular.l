%{
 #include<stdio.h>
 #undef yywrap
 #define yywrap() 1
%}


%%
[\n] {printf("\n\nEnter mobile Number: ");}

[1-9][0-9]{9} {printf("Mobile number Valid.");}

.* {printf("Mobile number Invalid.");}
%%

int main()
{
 printf("\nEnter mobile Number: ");
 yylex();
 return 0;
}