#!/usr/bin/python3
"""
This module lists all states with a name starting with
N (upper N) from the database
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
