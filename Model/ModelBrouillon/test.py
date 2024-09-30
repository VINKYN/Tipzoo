import os
import sqlite3
def get_database():
    path = '../Database'
    return os.listdir(path)




def connect_database(dbfile):
    print(dbfile)
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    cursor.execute("Select * from Base;")
    return cursor.fetchall()


test = get_database()[8]
path = '../Database/'+test

print(connect_database(path)[0][0])
