import sqlite3

db = sqlite3.connect("myshop.db")
cursor = db.cursor()

cursor.execute('''insert into Customer values(2, "Nicol","McAdam","2 Cython Street","Cambridge","CB3 2YU","04567 467893")''') 

db.commit()

cursor.execute('SELECT * FROM Customer')

print cursor.fetchall()

cursor.close()
