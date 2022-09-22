#!/usr/bin/python3

""" display the name that
matches the argument
    """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    my_host = "localhost"
    my_user = argv[1]
    my_passwd = argv[2]
    my_db = argv[3]
    find = argv[4]

    db = MySQLdb.Connect(host=my_host, user=my_user,
                         password=my_passwd, port=3306, db=my_db)
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name='{:s}';".format(find))
    found = cur.fetchall()
    for name in found:
        print(name)
