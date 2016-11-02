import sqlite3
import decimal
D=decimal.Decimal

def adapt_decimal(d):
    return str(d)

def convert_decimal(s):
    return D(s)

# Register the adapter
sqlite3.register_adapter(D, adapt_decimal)

# Register the converter
sqlite3.register_converter("decimal", convert_decimal)

sql = """create table Product (
             ProductID integer,
             Name text,
             Price decimal,
             ProductTypeID integer,
             primary key (ProductID))
             """

db = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = db.cursor()
cur.execute(sql)

d = D('4.12')

cur.execute("insert into Product values (?, ?, ?, ?)", (1, 'test', d, 1,))
cur.execute("select * from Product")
data=cur.fetchone()
print data
print data[2]
print(type(data))

cur.close()
db.close()
