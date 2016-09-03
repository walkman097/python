#!/usr/bin/python3

#  read/write file

try:
	f = open("chmod.sh", "r");
	print(f.read());
finally:
	if f:
		f.close();

print("\nuser with close file\n");
with open("chmod.sh", "r") as f:
	print(f.read());

print("\nwrite some to file\n");
with open("chmod.sh", "a+") as f:
	f.write("#use python add some to file");
	