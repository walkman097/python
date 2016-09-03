#!/usr/bin/python2


import urllib2  
response = urllib2.urlopen('http://www.baidu.com/')  
html = response.read()  

with open("baidu.html", "wb") as f:
	f.write(html);

