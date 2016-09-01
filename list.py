#!/usr/bin/python3

badNews = "hi %s,your score is %d"%("bart", 59);
print(badNews);

#list
classMember = ["Michael", "Bob", "Tracy"]
print(classMember);
print("classMember len is", len(classMember));
print("classMember 1 is", classMember[1]);

#当索引超出了范围时，Python会报一个IndexError错误，
#所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print("classMember -1 is", classMember[-1]);


#tuple 

