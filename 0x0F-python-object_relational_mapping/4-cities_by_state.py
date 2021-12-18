#!/usr/bin/python3
import sys
import MySQLdb


def get_states(username, password, db_name):
    '''
        lists all cities from the database.
    '''
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM `cities`\
                    JOIN `states` ON state_id=states.id\
                    ORDER BY cities.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    credentials = sys.argv
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    get_states(username, passwd, db_name)
