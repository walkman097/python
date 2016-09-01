#!/usr/bin/python3

L = list(range(1,11));
print("list is", L);

L = []
for x in range(1, 11):
	L.append(x);
print("L is", L);


import os 
import math
for d in os.listdir("."):
	print("dir is", d);

L1 = ['Hello', 'World', 18, 'Apple', None];
L2 = [];

# 期待输出: ['hello', 'world', 'apple']
for x in L1:
	if isinstance(x, str):
		L2.append(x.lower());
print(L2);

