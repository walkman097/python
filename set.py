#!/usr/bin/python3

# dict || set == map 


names = ["Michael", "Bob", "Tracy"];
score = [95, 75, 85];
for name in names:
	print(name);

for sc in score:
	print(sc);

gender = {"Michael":95, "Bob":85, "Tracy":75};
gender["Bart"] = 86;
for name in gender:
	print("name is %s, score is %d"%(name ,gender[name]));
	
print(gender.get("Michael"));
