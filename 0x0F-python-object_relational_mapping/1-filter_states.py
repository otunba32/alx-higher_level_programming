#!/usr/bin/python3
"""script that lists all states with a name startingwith N from the database hbtn_0e_0_usa"""
import MySQLdb 
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            port=3306,
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            )
    
    cur = db.cursor()
    myQuery = "".join([
            "SELECT * FROM states WHERE name LIKE BINARY 'N%'",
            "ORDER BY id ASC"])
    cur.execute(myQuery)
    curs = cur.fetchall()

    for rows in curs:
        print(rows)
        
    cur.close()
    db.close()
