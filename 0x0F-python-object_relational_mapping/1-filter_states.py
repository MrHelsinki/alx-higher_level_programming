#!/usr/bin/python3
""" fetch all data from db and print those who start with N """

import MySQLdb
import sys


if __name__ == "__main__":

    argv = sys.argv
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    my_db = MySQLdb.connect(host="localhost",
                            user=user,
                            passwd=passwd,
                            db=db,
                            port=3306)
    cur = my_db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        if i[1][0] == 'N':
            print(i)
    cur.close()
    my_db.close()
