#!/usr/bin/python3
from sys import argv
import MySQLdb
mydb=MySQLdb.connect(host='localhost',
                          user='argv[0]',
                          password='argv[1]',
                          database='hbtn_0e_0_usa',
                          port=3306)

cur=mydb.cursor()
wcur.execute("select * from states ORDER BY id ASC")
for u in cur:
    print(u)

cur.close()
connect.close()
