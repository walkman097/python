#!/usr/bin/python3

# user json
import json
import pickle

d = dict(name = "Bob", age = 20, score = 88);
pickle.dumps(d);
with open("dump.txt", "wb") as f:
	pickle.dump(d, f);


json.dumps(d);
with open("test.json", "w") as f:
	json.dump(d, f);


json_str = "{\"data\":{\"currentDate\":\"2016-09-03 14:25:00\",\"systemDate\":\"1472883900477\"},\"status\":{\"code\":10003,\"message\":\"未登录用户！\"}}";
with open("test.json", "w") as f:
	json.dump(json.loads(json_str), f);


class Student(object):
	def __init__(self , name, age, score):
		self.name = name;
		self.age = age;
		self.score = score;


def StudentToDict(stdudy):
	return {
		"name" : stdudy.name,
		"age" : stdudy.age,
		"score" : stdudy.score
	};

s  = Student("Bart", 18, 85);
print(json.dumps(s, default = StudentToDict));










