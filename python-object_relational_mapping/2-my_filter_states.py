#!/usr/bin/python3
""" this is the tals"""


import sys 
import MySQLdb
if __name__ == "__main__":
    connection=MySQLdb.connect(host='local host',port=3306,user=sys.argv[1],password=sys.argv[2],db=sys.argv[3]])
    cursor=connection.cursor()
    cur.execute("SELECT id,name FROM states WHERE name like BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows=cur.fetchall()
    for u in rows:
        print(u)
    cur.close()
    connect.close()
