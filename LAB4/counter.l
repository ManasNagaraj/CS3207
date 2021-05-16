%{
    int lines=1, words=0, characters=0;
%}
%option noyywrap
%%

\n  { lines++; words++;}
[\t ' ']    words++;
.   characters++;

%%

int main()
{
    yyin= fopen("count.c","r");
    yylex();
    printf("Number of Characters: %d", characters);
    printf("\nNumber of Words : %d",words);
    printf("\nNumber of Lines : %d\n", lines);
    return 0;
}