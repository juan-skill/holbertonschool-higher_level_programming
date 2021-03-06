#!/usr/bin/python3
""" displays all values in the states (Injection SQL) """

from MySQLdb import connect
from sys import argv


def execute_query(cur):
    """ Executing a sql query """

    cur.execute(
        """SELECT * FROM states
           WHERE name = %s
           ORDER BY id ASC""", (argv[4],))
    return cur.fetchall()


def print_result(rows):
    """ Printring the records """
    for row in rows:
        print(row)


if __name__ == '__main__':

    # Connect to a MySQL database
    db = connect(
        user=argv[1], passwd=argv[2], db=argv[3], host="localhost", port=3306)

    # Create a cursor handle
    cur = db.cursor()

    # Execute a sql query
    rows = execute_query(cur)

    # Prints the records
    print_result(rows)

    # Close all cursors
    cur.close()

    # Close all database
    db.close()
