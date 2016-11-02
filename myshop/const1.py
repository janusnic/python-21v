import sqlite3

db = sqlite3.connect("myshop.db")

with db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Customer')
    print cursor.fetchmany(2)

print sqlite3.PARSE_DECLTYPES
print sqlite3.PARSE_COLNAMES
cursor.close()
db.close()