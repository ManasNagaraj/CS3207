/* LEX code for lowercase conversion */

upper [A-Z]
%%
{upper}           {printf("%c",yytext[0]+32);}
[//][a-zA-Z]*     {printf(yytext);}
"/*"(.|\n)*"*/"    {printf(yytext);}
%%
int main(void)
{
    printf("---------------------------------\n");
    printf("Enter Input in UPPERCASE\n");
    yylex();
    return 0;
}
int yywrap()
{
    return 1;
}
