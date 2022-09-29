#!/usr/bin/python3

""" Sql injection protected scripts
    """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    my_user = argv[1]
    my_passwd = argv[2]
    my_db = argv[3]
    my_host = "localhost"
    my_port = 3306
    find = argv[4]
    db = MySQLdb.connect(user=my_user, password=my_passwd,
                         db=my_db, port=my_port)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s;", (find,))
    found = cur.fetchall()

    for state in found:
        if state[1] == find:
            print(state)
