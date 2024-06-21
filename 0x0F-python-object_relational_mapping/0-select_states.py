#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import MySQLdb

    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], database=args[3])

    cur = db.cursor()
    cur.execute(f"SELECT * FROM states  ORDER BY states.id ASC")
    states = cur.fetchall()

    for i in states:
        print(i)

