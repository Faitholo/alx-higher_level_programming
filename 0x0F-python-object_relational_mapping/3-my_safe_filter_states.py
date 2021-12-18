#!/usr/bin/python3
import sys
import MySQLdb


def get_states(username, password, db_name, search_value):
    '''
        all values in the states table where name matches the argument
    '''
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`\
                   WHERE `name`=(%s) ORDER BY `id` ASC", (search_value,))
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
    search_value = sys.argv[4]
    get_states(username, passwd, db_name, search_value)
