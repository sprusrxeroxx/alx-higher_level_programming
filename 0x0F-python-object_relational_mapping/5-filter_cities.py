#!/usr/bin/python3
"""
A script that takes state name as an argument \
and displays all matching cities from the city table \
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    if len(argv) != 5:
        print("Usage: script_name.py <username>\
               <password> <database> <state_name>")
        exit(1)
        

    try:
        # a secure connection parameterization method
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()

        # parameterized query with placeholder for state name
        state_name = argv[4]
        sql = "select name from cities where\
                state_id = (select id from states where name = %s)"
        cur.execute(sql, (state_name,))

        rows = cur.fetchall()
        [print(i, sep=", ") for i in rows]

    except MySQLdb.Error as err:
        print("Error connecting to database:", err)

    finally:
        if db:
            db.close()
