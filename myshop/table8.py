import sqlite3

db = sqlite3.connect("myshop.db")

with db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Customer')
    data = cursor.fetchone()
    print data[0]

cursor.close()
db.close()