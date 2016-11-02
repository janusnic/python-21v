import sqlite3

db = sqlite3.connect("myshop.db")

with db:
    cursor = db.cursor()
    cursor.execute('''insert into Customer values(3, "Nic","Adam","2 Pillow Street","London","BB3 2YU","04567 467888")''') 
    cursor.execute('''insert into Customer values(4, "Ann","McDonald","55 Flowers Street","Glasgj","DB3 2YU","04567 466666")''') 
    cursor.execute('''insert into Customer values(5, "Tom","Adams","2 Django Street","Dublin","CE3 2YU","04567 467777")''') 

db.commit()

cursor.execute('SELECT * FROM Customer')

print cursor.fetchall()

cursor.close()
