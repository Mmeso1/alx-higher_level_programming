#!/usr/bin/python3
"""
This module takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
zthis time we are making it SQL injection attack free.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) == 5:
        db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                             db=argv[3], charset='utf8')
        cur = db.cursor()
        cur.execute("""SELECT * FROM states WHERE name = %s""",
                    (argv[4],))
        states = cur.fetchall()
        for state in states:
            print(state)
        cur.close()
        db.close()
