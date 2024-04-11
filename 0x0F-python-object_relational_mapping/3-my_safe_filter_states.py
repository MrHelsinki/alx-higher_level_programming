#!/usr/bin/python3
""" fetch all data from table and print it """

import MySQLdb
import sys


if __name__ == "__main__":

    argv = sys.argv
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    argument = argv[4]
    if len(argument) < 10:
        exit(-1)

    my_db = MySQLdb.connect(host="localhost",
                            user=user,
                            passwd=passwd,
                            db=db,
                            port=3306)
    cur = my_db.cursor()
    cur.execute("SELECT * FROM states WHERE NAME LIKE BINARY '%{}%'"
                .format(argument))

    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    my_db.close()
