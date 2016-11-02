import sqlite3


customers = (
    (1, "Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893"),
    (2, "Nicol","McAdam","2 Cython Street","Cambridge","CB3 2YU","04567 467893"),
    (3, "Nic","Adam","2 Pillow Street","London","BB3 2YU","04567 467888"),
    (4, "Ann","McDonald","55 Flowers Street","Glasgj","DB3 2YU","04567 466666"),
    (5, "Tom","Adams","2 Django Street","Dublin","CE3 2YU","04567 467777"),
    (6, "Trevor","Adams","25 Django Street","Dublin","CE3 5YU","04567 468777"),
    (7, "Tim","Doo","5 Django Street","Dublin","CE3 5YU","04567 468700"),
    (8, "Marry","Ann","7 Django Street","Dublin","CE3 5YU","04567 468700")
    )

sql = """create table Customer (
             CustomerID integer,
             FirstName text,
             LastName text,
             Street text,
             Town text,
             PostCode text,
             TelephoneNumber text,
             primary key (CustomerID))"""

db = sqlite3.connect(":memory:")

with db:
    
    cursor = db.cursor()
        
    cursor.execute(sql)
    cursor.executemany("INSERT INTO Customer VALUES(?, ?, ?, ?, ?, ?, ?)", customers)

# Note that lastrowid returns None when you insert more than one row at a time with executemany.
lid = cursor.lastrowid
print cursor.lastrowid

cursor.execute('SELECT * FROM Customer order by Town')
while True: 
    tmp=cursor.fetchone() 
    if tmp: 
        print tmp 

    else: 

        break 
cursor.close()
db.close()
