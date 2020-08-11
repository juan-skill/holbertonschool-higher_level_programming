#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa """

from MySQLdb import connect
from sys import argv


def execute_query(cur):
    """ Executing a sql query """

    cur.execute(
        """SELECT cities.name FROM states
           JOIN cities
           ON states.id = cities.state_id
           WHERE states.name = %s
           ORDER BY cities.id ASC""", (argv[4],))

    return cur.fetchall()


def print_result(rows):
    """ Printing the records """
    # Each row ('something',) then I take row[0]
    print(", ".join([row[0] for row in rows]))


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
