#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

#create table and insert data
conn = sqlite3.connect("test.db");
cursor = conn.cursor();
#cursor.execute("create table user(id varchar(20) primary key, name varchar(20))");
#cursor.execute("insert into user(id, name) values (\"10\", \"Tracy\")");
cursor.close();

conn.commit();
conn.close();

#get data from table
conn = sqlite3.connect("test.db");
cursor = conn.cursor();
cursor.execute("select * from user where id = 10");	
values = cursor.fetchall();
print(values);

cursor.close();
conn.close();
