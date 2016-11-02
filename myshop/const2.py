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

d = D('4.12')

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()
cur.execute("create table test(d decimal)")

cur.execute("insert into test(d) values (?)", (d,))
cur.execute("select d from test")
data=cur.fetchone()[0]
print(data)
print(type(data))

cur.close()
con.close()
