import sqlite3

db = sqlite3.connect("myshop.db")
cursor = db.cursor()

cursor.execute('SELECT * FROM Customer order by Town')

for row in cursor:
    print '-'*10
    print 'ID:', row[0]
    print 'First name:', row[1]
    print 'Second name:', row[2]
    print '-'*10

cursor.close()
db.close()