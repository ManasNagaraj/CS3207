%{
#include<stdio.h>
char makeexpr(char op1, char operator, char op2);
void threeAddr();
struct expr{char op1,op2,operator, res;};
int index=0;
char temp = 'A';
%}
%union{char tok;}
%token <tok> NUM VAR
%type <tok> exp stmt
%left '+' '-'
%left '*' '/'
%%
stmt: VAR '=' exp ';'	{makeexpr((char)$1,'=',(char)$3); threeAddr();}
exp: exp '+' exp		{$$ = makeexpr((char)$1,'+',(char)$3);}
   | exp '-' exp 		{$$ = makeexpr((char)$1,'-',(char)$3);}
   | exp '*' exp 		{$$ = makeexpr((char)$1,'*',(char)$3);}
   | exp '/' exp 		{$$ = makeexpr((char)$1,'/',(char)$3);}
   | '(' exp ')' 		{$$ = (char)$2;}
   | NUM 				{$$ = makeexpr((char)$1,'\0','\0');}
   | VAR 				{$$ = (char)$1;}
%%
struct expr arr[25];
void yyerror(char *s){
	printf("Error %s",s);
}
char makeexpr(char op1, char operator, char op2){
	if(op1>=65 && op1<=91)
        temp--;
    if(op2>=65 && op2<=91)
        temp--;
    if(operator=='='){
		arr[index].res=op1;
		arr[index].operator=operator;
		arr[index].op1=op2;
		arr[index++].op2='\0';
        //temp++;
		return op1;	
	}
    
	arr[index].op1=op1;
	arr[index].operator=operator;
	arr[index].op2=op2;
	arr[index++].res=temp;
	return temp++;
}
void threeAddr(){
	int i;
	for(i=0;i<index;i++){
		if(arr[i].operator=='='){
			printf("%c := %c\n",arr[i].res,arr[i].op1);
		}
		else
			printf("%c := %c %c %c\n",arr[i].res,arr[i].op1,arr[i].operator,arr[i].op2);
	}
}
int main(){
	printf("Enter Expression:\n");
	yyparse();
	return 0;
}