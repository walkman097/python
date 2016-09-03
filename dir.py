#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
	fsize = os.path.getsize(f)
	mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
	flag = '/' if os.path.isdir(f) else ''
	#IndentationError: unindent does not match any outer indentation level
	#这个是代表代码没有问题，但是代码的缩进存在问题
	print("%10d %s %s%s" %(fsize, mtime, f, flag));
