#!/usr/bin/python3
import sys 
import MySQLdb
if __name__ == "__main__"
connection=MySQLdb.connect(host='local host',port=3306,user=sys.argv[1],password=sys.argv[2],db=sys.argv[3]])
cursor=connect.cursor()
cur.execute("SELECT id,name FROM states WHERE name like BINARY '{}' \
            ORDER  by states.id ASC".format(argv[4])
rows=rows.fetchall()
for u in rows:
    print(u)
    cur.close()
connect.close()
