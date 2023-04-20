#!/usr/bin/python3
"""
A script (safe from MySQL injections) that displays
all values in the states table of the database
where name matches the argument and it is safe 
from MySQL injections
"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    myQuery = "SELECT * FROM states WHERE name=%(name)s ORDER BY states.id"
    cur.execute(myQuery, {'name': sys.argv[4]})
    res = cur.fetchall()
    for rows in res:
        print(rows)
    
    cur.close()
    db.close()
