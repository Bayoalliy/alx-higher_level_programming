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
    query = "SELECT cities.name\
    FROM states JOIN cities\
    ON states.id = cities.state_id WHERE states.name = %s"
    cur.execute(query, (args[4],))
    states = cur.fetchall()
    i = 0
    while (i < len(states)):
        for elem in states[i]:
            print(elem, end="")
            if i != (len(states) - 1):
                print(", ", end="")
        i += 1
    print("")
