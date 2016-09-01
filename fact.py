#!/usr/bin/python3

#fact
def fact(n):
	if n == 1:
		return 1;
	return n * fact(n - 1);

print("%d fact is %d"%(5,fact(5)));
print("%d fact is %d"%(9,fact(9)));
print("%d fact is %d"%(1,fact(1)));


# sum = 1 + 2 + ... + 100
def fact(n):
	if n == 1:
		return 1;
	return n + fact(n - 1);

print("1 + .. + 10 =", fact(10));


L = [];
n = 0;
while n < 20:
	L.append(n);
	n += 2;

print(L);
def calc(members):
	sum = 0;
	for a in members:
		sum += a;
	return sum;
print("L",L, "cala(L)", calc(L));


for ch in "ABC":
	print("ch is", ch);