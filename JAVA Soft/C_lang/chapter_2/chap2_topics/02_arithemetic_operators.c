#include<stdio.h>

int main() {
	int a = 4;
	int b = 3;
	int c = a + b;
	printf("The value of a is %d and value of b is %d and sum is\n: $%d\\-\n", a, b, c);
	// modulus operator is used to get the reminder
	printf("The reminder when a is devided by b is\n: $%d\\-", a%b);
	return 0;
}
