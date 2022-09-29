#!/usr/bin/python3
"""print out all the states and cities to standard output
    """

if __name__ == '__main__':
    import MySQLdb
    import sys

    my_host = "localhost"
    user_name = sys.argv[1]
    password = sys.argv[2]
    my_db = sys.argv[3]

    db = MySQLdb.Connect(host=my_host, user=user_name,
                         passwd=password, db=my_db, port=3306)

    cur = db.cursor()
    states_num = cur.execute("""SELECT cities.id, cities.name, states.name
                                FROM cities
                                JOIN states
                                    ON cities.state_id = states.id;""")
    states = cur.fetchall()
    cur.close()
    db.close()
    for name in states:
        print(name)
