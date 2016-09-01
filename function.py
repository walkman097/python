#!/usr/bin/python3

# first use function

def circle_arer(x):
	s = 3.14 * x * x;
	return s;

r = float(input("please input your radius:"));
print("the circle square is %f"%(circle_arer(r)));

# 100
# ∑(n2+1)
# n=1

def stack_sum(n):
	a = 0;
	sum = 0;
	for a in range(n):
		sum += (n * n + 1);
		n -= 1;
	return sum;

print("stack sum %d is %d"%(5, stack_sum(5)));


# ∑(n)

def total(n):
	a = 0;
	sum = 0;
	for a in range(n):
		sum += n;
		n -= 1;
	return sum;

print("range %d, sum is %d"%(5, total(5)));	

