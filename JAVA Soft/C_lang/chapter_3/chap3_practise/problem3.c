#include<stdio.h>

int main(){
	int i = 5 ;
	printf("The value of i is %d\n", i);
	
	i = i + 5;  // 10
	printf("The value of i is %d\n", i);
	
	printf("The value of i is %d\n", i++);
	printf("The value of i is %d\n", i); 
	 
	 i +=2;
	 printf("The value of i is %d\n", i);
	 
//	 i++ prints i first and then increment i (post increment operator)
//++i increment i first and then prints i (post increment operator)

	 return 0;
	}
