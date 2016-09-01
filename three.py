#!/usr/bin/python3
age = 18
if age > 20:
	print("age more than 18");
else:
	print("age less than 18");

	
# 请打印出以下变量的值：
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello, Lisa!'''

n = 123
print(n);
f = 456.789
print(f)

s1 = 'Hello, world'
print(s1);

s2 = 'Hello, \'Adam\''
print(s2);

s3 = r'Hello, "Bart"'
print(s3);

s4 = r'''Hello, 
Lisa!'''
print(s4);

print("测试中文字符");

badNews = "hi %s,your score is %d" %("bart", 59)
print(badNews);
