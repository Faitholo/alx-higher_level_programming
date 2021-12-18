#!/usr/bin/python3
import sys
import MySQLdb


def get_states(username, password, db_name, state_name):
    '''
        lists all cities from the database from a specific state.
    '''
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.name\
                    FROM `cities`\
                    JOIN `states` ON state_id=states.id\
                    WHERE states.name=(%s)\
                    ORDER BY cities.id", [state_name])
    rows = cursor.fetchall()
    cities = ""
    for row in rows:
        for col in row:
            cities += (col) + ", "
    print(cities[:-2])
    cursor.close()
    db.close()

if __name__ == "__main__":
    credentials = sys.argv
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    get_states(username, passwd, db_name, state_name)
