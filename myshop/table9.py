import sqlite3

db = sqlite3.connect("myshop.db")

with db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Customer')
    print cursor.fetchmany(2)

cursor.close()
db.close()