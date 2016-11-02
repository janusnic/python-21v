import sqlite3

db = sqlite3.connect(":memory:")

with db:
    cursor = db.cursor() 
    cursor.execute('CREATE TABLE Customer(CustomerID integer, FirstName text, LastName text, Street text, Town text, PostCode text, TelephoneNumber text, primary key (CustomerID));')
    cursor.execute('INSERT INTO Customer VALUES(1, "Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893");')
    cursor.execute('INSERT INTO Customer VALUES(2, "Nicol","McAdam","2 Cython Street","Cambridge","CB3 2YU","04567 467893");')
    cursor.execute('INSERT INTO Customer VALUES(3, "Nic","Adam","2 Pillow Street","London","BB3 2YU","04567 467888");')
    cursor.execute('INSERT INTO Customer VALUES(4, "Ann","McDonald","55 Flowers Street","Glasgj","DB3 2YU","04567 466666");')
    cursor.execute('INSERT INTO Customer VALUES(5, "Tom","Adams","2 Django Street","Dublin","CE3 2YU","04567 467777");')
    cursor.execute('INSERT INTO Customer VALUES(6, "Trevor","Adams","25 Django Street","Dublin","CE3 5YU","04567 468777");')
    cursor.execute('INSERT INTO Customer VALUES(7, "Tim","Doo","5 Django Street","Dublin","CE3 5YU","04567 468700");')
    cursor.execute('INSERT INTO Customer VALUES(8, "Marry","Ann","7 Django Street","Dublin","CE3 5YU","04567 468700");')

    lid = cursor.lastrowid
    print cursor.lastrowid
