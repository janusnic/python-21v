import sqlite3

db = sqlite3.connect("myshop.db")
cursor = db.cursor()

val = [(6, "Trevor","Adams","25 Django Street","Dublin","CE3 5YU","04567 468777"),(7, "Tim","Doo","5 Django Street","Dublin","CE3 5YU","04567 468700"),(8, "Marry","Ann","7 Django Street","Dublin","CE3 5YU","04567 468700")]

for t in val: 
    cursor.execute('insert into Customer values (?,?,?,?,?,?,?)', t)

db.commit()

cursor.execute('SELECT * FROM Customer')

print cursor.fetchall()

cursor.close()
