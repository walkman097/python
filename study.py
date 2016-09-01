#!/usr/bin/python3

std1 = {"name" : "Michael", "score" : 98};
std2 = {"name" : "Tracy", "score" : 95}

def print_score(std):
	print("%s: %s" %(std["name"], std["score"]));

print_score(std1);
print_score(std2);


study = {};
for a in range(10):
	study[a] = ("a%d" %(a));
print(study);

class Study(object):
	def __init__(self, name, score):
		self.name = name;
		self.score = score;
		
	def print_score(self):
		print("%s : %s" %(self.name, self.score));

	def get_grade(self):
		if self.score >= 90:
			return "A";
		elif self.score >= 60:
			return "B";
		else:
			return "C";

bart = Study("Bart", 59);
tracy = Study("Tracy", 69);


bart.print_score();
tracy.print_score();

print("%s grade %s" %(bart.name, bart.get_grade()));



