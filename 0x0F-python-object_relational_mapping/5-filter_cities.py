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
    find = sys.argv[4]

    db = MySQLdb.Connect(host=my_host, user=user_name,
                         passwd=password, db=my_db, port=3306)

    cur = db.cursor()
    states_num = cur.execute("""SELECT cities.name
                                FROM cities
                                JOIN states
                                ON cities.state_id = states.id
                                AND states.name = %s;""", (find,))
    states = cur.fetchall()
    cur.close()
    db.close()
    if states_num == 0:
        print('')
    if states_num != 0:
        for pos in range(states_num - 1):
            print(states[pos][0], end=', ')
        print(states[states_num - 1][0])
