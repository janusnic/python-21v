# -*- coding: utf-8 -*-
import sqlite3

# создаем базу и заполянем ее одним значением
conn = sqlite3.connect(":memory:")
c = conn.cursor()

c.execute('''create table stocks(date text, trans text, symbol text, qty real, price real)''')

c.execute("""insert into stocks values ('2006-01-05','BUY','RHAT',100,35.14)""")

conn.commit()
c.close()

# Демонстрируем возможности Row
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('select * from stocks')
r = c.fetchone()
print 'type(r) = ', type(r)
print 'r = ', r
print 'len(r) = ', len(r)
print 'r[2] = ', r[2]
print 'r.keys() = ', r.keys()
print 'r[qry] = ', r['qty']
for member in r:
    print member
