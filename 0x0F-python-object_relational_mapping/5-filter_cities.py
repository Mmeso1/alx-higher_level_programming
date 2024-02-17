#!/usr/bin/python3
"""
This module takes in the name of a state as an argument and
lists all cities of that state, using the database 
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
            db=argv[3], charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT c.name from cities c JOIN states s on \
                 c.state_id = s.id WHERE s.name = %s", (argv[4],))
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    db.close()
