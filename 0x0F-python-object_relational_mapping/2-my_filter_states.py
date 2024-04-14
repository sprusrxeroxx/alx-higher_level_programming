#!/usr/bin/python3
""" a script that takes in an argument\
    and displays all values in the states \
    table of hbtn_0e_0_usa \
    where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    
  try:
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                        passwd=argv[2], db=argv[3]) 
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{argv[4]}'".format)
    rows = cur.fetchall()
    [print(i) for i in rows]
    
    
  except MySQLdb.Error as err:
    print("Error connecting to database:", err)

  finally:
    if db:
      db.close()