#!/usr/bin/python3

"""
lists all states with a specific name
from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
    FROM states JOIN cities\
    ON states.id = cities.state_id"
    cur.execute(query)
    states = cur.fetchall()

    for state in states:
        print(state)
