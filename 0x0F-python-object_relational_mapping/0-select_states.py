#!/usr/bin/python3

# fetch all data from table and print it

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)

    argv = sys.argv
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    my_db = MySQLdb.connect(host="localhost",
                            port=3306, user=user,
                            passwd=passwd,
                            db=db)
    cur = my_db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)
