#!/usr/bin/python3

# parameter function

def power(x, n = 2):
	sum = 1;
	for a in range(n)	:
		sum *= x;
	return sum;

print("Power %d is %d"%(5, power(5, 3)));

def calc(numbers):
	sum = 0;
	for a in numbers:
		sum += a*a;
	return sum;
numbers = [1,2,3,4];
print("calc numbers", numbers, "is", calc(numbers));

#关键字参数
def calc_p(*members):
	sum = 0;
	for a in members:
		sum += a*a;
	return sum;
print("calc_p", calc_p(1, 2, 3, 4));
