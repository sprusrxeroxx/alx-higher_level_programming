#!/usr/bin/python3
"""
A script that takes state name as an argument \
and displays all matching values from the states table \
in hbtn_0e_0_usa database securely.
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
        sql = "SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON \
                cities.state_id=states.id;"
        cur.execute(sql)

        rows = cur.fetchall()
        [print(i) for i in rows]

    except MySQLdb.Error as err:
        print("Error connecting to database:", err)

    finally:
        if db:
            db.close()