#include<stdio.h>


int main(){
int age = 8;

if(age>5){
	printf("We are inside if\n");
	printf("Your age is greater than : 5\n");
	printf("So you can't enter in this child garden\n'");
}	
if(age%2==0){
	printf("We are inside another if\n");
	printf("Your age is divisible by 5\n");
//	printf("So you can't enter in this child garden\n'");	
}
	return 0;
}
