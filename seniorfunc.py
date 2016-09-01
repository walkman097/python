#!/usr/bin/python3

# senior function

def func(n):
	return n*n;

def traceBack(x, y, func):
	return x + func(y);

print("traceBack", traceBack(2, 5, func));
