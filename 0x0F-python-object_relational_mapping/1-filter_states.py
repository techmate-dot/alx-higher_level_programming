#!/usr/bin/python3

"""Filter the  the name of states based on
the first letter of the name
    """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    my_host = "localhost"
    my_user = argv[1]
    my_passwd = argv[2]
    my_db = argv[3]

    db = MySQLdb.Connect(host=my_host, user=my_user,
                         password=my_passwd, db=my_db, port=3306)
cur = db.cursor()

cur.execute("SELECT * from states;")
states = cur.fetchall()

for id, name in states:
    if name[0] == 'N':
        print(f"({id}, '{name}')")
