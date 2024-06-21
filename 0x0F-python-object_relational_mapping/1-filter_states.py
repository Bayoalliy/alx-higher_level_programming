#!/usr/bin/python3

"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], database=args[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE LEFT(name, 1) = %s;", ('N',))
    states = cur.fetchall()

    for state in states:
        print(state)
