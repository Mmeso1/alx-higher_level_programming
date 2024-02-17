#!/usr/bin/python3
"""
The script that
lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
            db=argv[3], charset='utf8')
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, states.id FROM cities c\
            INNER JOIN states on c.state_id = states.id""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
