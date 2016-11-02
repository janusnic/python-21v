import sqlite3

db = sqlite3.connect("myshop.db")
cursor = db.cursor()

cursor.execute('SELECT * FROM Customer order by Town')
while True: 
    tmp=cursor.fetchone() 
    if tmp: 
        print tmp 
    else: 
        break 
cursor.close()
db.close()