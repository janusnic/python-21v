# python-21v unit 11

# Итераторы

Итераторы — это специальные объекты, представляющие последовательный доступ к данным из контейнера. При этом немаловажную роль играет то, что память фактически не тратится, так как промежуточные данные выдаются по мере необходимости при запросе, поэтому фактически в памяти останутся только исходные данные и конечный результат и их можно читать и записывать, используя файл на диске.

Итератор удобно использовать вместе с последовательностью. Любой объект, поддерживающий интерфейс итератора, имеет метод next(), позволяющий переходить на следующую ступень вычисления. Чтобы получить итератор по объекту (например, по списку), к нему нужно применить функцию iter(). Для обработки сложных наборов данных можно подключить стандартный модуль itertools.

простейший итератор:

    testIt = iter([1, 2, 3, 4, 5])
    print [x for x in testIt]


функция iter() может принимать не только структуру данных, но и два других аргумента: функцию без аргументов и стоповое значение, на котором итерация остановится. Пример:

    def getSimple(state=[]):
      if len(state) < 4:
        state.append(" ")
        return " "

    testIt2 = iter(getSimple, None)
    print [x for x in testIt2]

Python при отсутствии явного возвращения значения из функции возвращается значение None.

## цикл for тоже задействует итератор.

    for element in iterable:
        # do something with element

    # create an iterator object from that iterable
    iter_obj = iter(iterable)

    # infinite loop
    while True:
        try:
            # get the next item
            element = next(iter_obj)
            # do something with element
        except StopIteration:
            # if StopIteration is raised, break from loop
            break

## enumerate()
Предназначена для нумерации элементов структуры данных (в том числе и другого итератора). Возвращает список кортежей, в каждом из которых первый элемент — номер (начиная с нуля), а второй — элемент исходного итератора. Пример:

    print [x for x in enumerate("abcd")]
    [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]


## sorted()
Итератор, выполняющий сортировку:

    sorted('avdsdf')
    ['a', 'd', 'd', 'f', 's', 'v']


## itertools.chain()
Итератор, позволяющий объединить два разных итератора в один. Пример:

    from itertools import chain
    it1 = iter([1,2,3])
    it2 = iter([8,9,0])
    for i in chain(it1, it2):
      print i,


даст в результате «1 2 3 8 9 0».

## itertools.count()
Итератор, выдающий бесконечные числа, начиная с заданного:

    for i in itertools.count(1):
      print i,
      if i > 100:
        break

## itertools.cycle()
Бесконечно повторяет заданную последовательность:

    tango = [1, 2, 3]
    for i in itertools.cycle(tango):
      print i,

Так же в этом модуле есть аналоги map(), starmap(), filter() и zip(), называются они:  itertools.imap(), itertools.starmap(), itertools.ifilter() и itertools.izip(). Их преимущество в том, что, в отличие от своих «обычных» аналогов тратят гораздо меньше памяти. Существует также пара фильтров: itertools.takewhile() и itertools.dropwhile():

    for i in takewhile(lambda x: x > 0, [1, -2, 3, -3]):
      print i,
    for i in dropwhile(lambda x: x > 0, [1, -2, 3, -3]):
      print i,

takewhile() возвращает значения, пока условие истинно, а остальные значения не берет из итератора. И, наоборот, dropwhile() ничего не выдает, пока выполняется условие.

В Python есть два понятия, которые звучат практически одинаково, но обозначают разные вeщи, — iterator и iterable. Первое — это объект, который реализует интерфейс итератора, а второе — контейнер, кoторый может служить источником данных для итератора.

Чтобы получить объект-итератор, нужно создать объект, который будет иметь два метода со специальными именами:

    __iter__() - метод, который возвращает сам объект.
    next() (в третьем Python __next__() ) - метод, который возвращает следующее значение итератора.

По коллекции можно итерироваться, но сама по себе коллекция никак не следит, где мы остановились. Следит за этим объект по имени listiterator, который возвращается методом iter() и используется, к примеру, циклом for или вызовом map(). Когда объекты в перебираемoй коллекции кончаются, возбуждается исключение StopIteration.

        # define a list
        my_list = [4, 7, 0, 3]

        # get an iterator using iter()
        my_iter = iter(my_list)

        ## iterate through it using next()

        #prints 4
        print(next(my_iter))

        #prints 7
        print(next(my_iter))

        ## next(obj) is same as obj.__next__()

        #prints 0
        print(my_iter.__next__())

        #prints 3
        print(my_iter.__next__())

        ## This will raise error, no items left
        next(my_iter)

## Мoдуль six.
Six представляет родительский класс, который позволяет не думать, кaкой
next-метод объявлять в объекте, — это всегда __next__()

from __future__ import print_function
from six import Iterator

class MyIterator(Iterator):
    def __init__(self, step=5):
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        self.step -= 1
        if not self.step: # Условие остановки итератора, чтобы он не бежал вeчно
            raise StopIteration()
        return self.step

myiterator = MyIterator()
for item in myiterator:
    print(item)
    print()

## Пример итератора

Предположим, что нам нужно сделать объект, который берет данные из строк очень большого файла. Данные нужны порциями, которые записаны в строках текстового файла, одна порция, одна строка. Обрабатывать нужно в цикле "for...in"

### Создаем такой класс simple.py:

        from __future__ import print_function
        from six import Iterator


        class SimpleIterator(Iterator):

            def __init__(self, fname):
                self.fd = open(fname, 'r')

            def __iter__(self):
                return self

            def __next__(self):
                line = self.fd.readline()
                if line != '':
                    line = line.rstrip('\n')
                    return line.title()
                raise StopIteration

        simple_iter = SimpleIterator('loren.txt')
        for i in simple_iter:
            print(i)

### Файл данных: loren.txt

Главная работа в методе next(). В нем считывается следующая строка файла, обрабатывается и возвращается в операторе return(). Когда файл окончится будет вызвано исключение StopIteration.

### Проверка:
    simple_iter = SimpleIterator('loren.txt')
    for i in simple_iter:
        print i

### enumerate
        print([x for x in enumerate(simple_iter)])

        simple_iter1 = SimpleIterator('loren.txt')
        print([x for x in enumerate(simple_iter1)])

# Итератор последовательности Фибоначчи

        # -*- coding:utf-8 -*-
        from __future__ import print_function
        from six import Iterator


        class Fibonacci(Iterator):
            """Итератор последовательности Фибоначчи до N"""
            def __init__(self, N):
                self.n, self.a, self.b, self.max = 0, 0, 1, N

            def __iter__(self):
                # сами себе итератор: в классе есть метод next()
                return self

            def __next__(self):
                if self.n < self.max:
                    a, self.n, self.a, self.b = self.a, self.n+1, self.b, self.a+self.b
                    return a
                else:
                    raise StopIteration

        # Использование:
        for i in Fibonacci(100):
            print(i)

# SQLite http://sqlite.org/
Страница скачивания: http://sqlite.org/download.html

SQLite это библиотека написанная Gerhard Häring  на языке C, которая предоставляет SQL интерфейс совместимый с DB-API 2.0 спецификациями описанными в PEP 249. SQLite — встраиваемая в процесс реализация SQL-машины. Слово SQL-сервер здесь не используем, потому что как таковой сервер не нужен — весь функционал, который встраивается в SQL-сервер, реализован внутри библиотеки (и, соответственно, внутри программы, которая её использует).

SQLite является открытым и полностью свободным программным обеспечением, распространяющимся как общественное достояние (public domain). Лицензия не накладывает никаких ограничений на то, как будет использоваться код, в том числе она позволяет взять его как часть закрытого проекта. Поэтому, SQLite может использоваться где угодно. В частности, SQLite используется в iPhone и iTunes, в Symbian и Android, встроен в Python и PHP, и используется в клиенте Skype. С учётом того, куда встроена SQLite, вероятно, это сегодня наиболее распространённая в мире СУБД. Также возможно сделать прототип приложения используя SQLite и затем перенести код для больших баз данных, таких как PostgreSQL или Oracle.

## sqlite3
Доступна консольная утилита для работы с базами (sqlite3.exe, «a command-line shell for accessing and modifying SQLite databases»).

## Особенности реализации
База данных в SQLite представлена в виде отдельного файла. Блокировка на запись реализована очень просто -- файл блокируется целиком. Не поддерживается запись в виды (views). Только частично поддерживаются триггеры.

Как известно, в своем развитии SQL устремился в разные стороны. Крупные производители начали впихивать всякие расширения. И хотя принимаются всякие стандарты (SQL 92), в реальной жизни все крупные БД не поддерживают стандартов полностью + имеют что-то свое. Так вот, SQLite старается жить по принципу «минимальный, но полный набор». Она во многом соответствует SQL 92.

И вводит некие свои особенности, которые очень удобны, но — не стандартны:

- Нельзя удалить или изменить столбец в таблице (ALTER TABLE DROP COLUMN…, ALTER TABLE ALTER COLUMN… ).
- Есть триггеры, но не настолько мощные как у крупных RDBMS.
- Есть поддержка foreign key, но по умолчанию — она ОТКЛЮЧЕНА.
- Нет встроенной поддержки UNICODE (но ее, вообщем, нетрудно добиться).
- Нет хранимых процедур.

a) каждая запись содержит виртуальный столбец rowid, который равен 64-битному номеру (уникальному для таблицы).
Можно объявить свой столбец INTEGER PRIMARY KEY и тогда этот столбец станет rowid (со своим именем, имя rowid все равно работает).
При вставке записи можно указать rowid, а можно — не указывать (и система тогда вставит уникальный).

b) можно без труда организовать БД в памяти;

c) легко переносить: по умолчанию, БД — это один файл (в кроссплатформенном формате);

d) тип столбца не определяет тип хранимого значения в этом поле записи, то есть в любой столбец можно занести любое значение;

e) много встроенных функций (которые можно использовать в SQL): www.sqlite.org/lang_corefunc.html;

## Тип столбца определяет как сравнивать значения.
Но не обязывает заносить значения именно такого типа в столбец. Нечто вроде weak typing.
Допустим, мы объявили столбец как «A INTEGER».
SQlite позволяет занести в этот столбец значения любого типа (999, «abc», «123», 678.525).
Если вставляемое значение — не целое, то SQlite пытается привести его к целому.
Т.е. строка «123» превратится в целое 123, а остальные значения запишутся «как есть».

## можно вообще не задавать тип столбца
Очень часто так и делается: CREATE TABLE foo (a,b,c,d).

## Сервера нету, само приложение является сервером.
Доступ к БД происходит через «подключения» к БД (нечто вроде хэндла файла ОС), которые мы открываем через вызов соот-й функции. При открытии указывается имя файла БД. Если такого нету — он автоматически создается.

    sqlite3 test.db
    sqlite> .tables
    sqlite> .exit

Допустимо открывать множество подключений к одной и тоже БД (через имя файла) в одном или разных приложениях.

Система использует механизмы блокировки доступа к файлу на уровне ОС, чтобы это все работало (эти механизмы обычно плохо работают на сетевых дисках, так что не рекомендуется использовать SQlite с файлом на сети).

Изначально SQlite работал по принципу «многие читают — один пишет».
То есть только одно соединение пишет в БД в данный момент времени. Если другие соединения попробуют тоже записать, то словят ошибку SQLITE_BUSY.
Можно, однако, ввести таймаут операций. Тогда подключение, столкнувшись с занятостью БД, будет ждать N секунду прежде, чем отвалиться с ошибкой SQLITE_BUSY.

## Write Ahead Log, WAL.
Если включить для БД именно этот режим лога, то несколько подключений смогут одновременно модифицировать БД.
Но в этом режиме БД уже занимает несколько файлов.

## у SQlite нет ГЛОБАЛЬНОГО КЭША
все современные RDBMS немыслимы без глобального разделяемого кэша, который может хранить несколько скомпилированных параметризованных запросов. Этим занят сервер, которого тут нет. Однако, в рамках одного приложения SQlite может разделять кэш между несколькими подключениями (www.sqlite.org/sharedcache.html) и немного сэкономить память.

## настройки по умолчанию.
Они работают на надежность, а не на производительность.

## непонимание механизма фиксации транзакций.
По умолчанию после любой команды SQlite будет фиксировать транзакцию (то есть ожидать пока БД окажется в целостном состоянии для отключения питания). В зависимости от режима паранойи SQLite потратит на это от 50 до 300 мс (ожидая окончания записи данных на диск).

## Мне нужно вставить 100 тыс записей и быстро!
Удалить индексы, включить режим синхронизации OFF (или NORMAL), вставлять порциями по N тысяч (N — подобрать, для начала взять 5000). Перед вставкой порции сделать BEGIN TRANSACTION, после — COMMIT.

## sqlite> .help

```
.backup ?DB? FILE      Backup DB (default "main") to FILE
.bail ON|OFF           Stop after hitting an error.  Default OFF
.databases             List names and files of attached databases
.dump ?TABLE? ...      Dump the database in an SQL text format
                         If TABLE specified, only dump tables matching
                         LIKE pattern TABLE.
.echo ON|OFF           Turn command echo on or off
.exit                  Exit this program
.explain ?ON|OFF?      Turn output mode suitable for EXPLAIN on or off.
                         With no args, it turns EXPLAIN on.
.header(s) ON|OFF      Turn display of headers on or off
.help                  Show this message
.import FILE TABLE     Import data from FILE into TABLE
.indices ?TABLE?       Show names of all indices
                         If TABLE specified, only show indices for tables
                         matching LIKE pattern TABLE.
.load FILE ?ENTRY?     Load an extension library
.log FILE|off          Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?TABLE?     Set output mode where MODE is one of:
                         csv      Comma-separated values
                         column   Left-aligned columns.  (See .width)
                         html     HTML <table> code
                         insert   SQL insert statements for TABLE
                         line     One value per line
                         list     Values delimited by .separator string
                         tabs     Tab-separated values
                         tcl      TCL list elements
.nullvalue STRING      Use STRING in place of NULL values
.open ?FILENAME?       Close existing database and reopen FILENAME
.output FILENAME       Send output to FILENAME
.output stdout         Send output to the screen
.print STRING...       Print literal STRING
.prompt MAIN CONTINUE  Replace the standard prompts
.quit                  Exit this program
.read FILENAME         Execute SQL in FILENAME
.restore ?DB? FILE     Restore content of DB (default "main") from FILE
.schema ?TABLE?        Show the CREATE statements
                         If TABLE specified, only show tables matching
                         LIKE pattern TABLE.
.separator STRING      Change separator used by output mode and .import
.show                  Show the current values for various settings
.stats ON|OFF          Turn stats on or off
.tables ?TABLE?        List names of tables
                         If TABLE specified, only list tables matching
                         LIKE pattern TABLE.
.timeout MS            Try opening locked tables for MS milliseconds
.trace FILE|off        Output each SQL statement as it is run
.vfsname ?AUX?         Print the name of the VFS stack
.width NUM1 NUM2 ...   Set column widths for "column" mode
.timer ON|OFF          Turn the CPU timer measurement on or off
```

## CREATE

```
sqlite> create table mytable (id INTEGER PRIMARY KEY,f TEXT,l TEXT);
```
## .table

```
sqlite> .table
mytable
```

## .schema ?TABLE?        Show the CREATE statements
If TABLE specified, only show tables matching LIKE pattern TABLE.
```
sqlite> .schema mytable
CREATE TABLE mytable (id INTEGER PRIMARY KEY,f TEXT,l TEXT);
```
## INSERT INTO

```
insert into mytable (f,l) values ('john','smith');
```
## SELECT
```
sqlite> select * from mytable;
1|john|smith

```
## .read

```
sqlite> .read my.sql
```
## my.sql

```
insert into mytable (f,l) values ('Mary','Ann');
insert into mytable (f,l) values ('Sam','Broun');
insert into mytable (f,l) values ('Chat','Gor');
```

## sqlite> select * from mytable;
```
1|john|smith
2|Mary|Ann
3|Sam|Broun
4|Chat|Gor
```

## .show Show the current values for various settings

```
     echo: off
  explain: off
  headers: off
     mode: list
nullvalue: ""
   output: stdout
separator: "|"
    stats: off
    width:
```
## .explain

```
sqlite> .explain on
sqlite> select * from mytable;
id    f              l   
----  -------------  ----
1     john           smith
2     Mary           Ann
3     Sam            Broun
4     Chat           Gor
```
## .dump

```
sqlite> .dump mytable
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE mytable (id INTEGER PRIMARY KEY,f TEXT,l TEXT);
INSERT INTO "mytable" VALUES(1,'john','smith');
INSERT INTO "mytable" VALUES(2,'Mary','Ann');
INSERT INTO "mytable" VALUES(3,'Sam','Broun');
INSERT INTO "mytable" VALUES(4,'Chat','Gor');
COMMIT;
```
# Python и база данных sqlite

```
python
Python 2.7.6 (default, Mar 22 2014, 22:59:56)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sqlite3
>>> sqlite3.version
'2.6.0'

```
## Connection объект
Для использования модуля, сначала нужно создать Connection объект олицетворяет базу данных.

```
con = sqlite3.connect('test.db')
```
## cwd+'/db/test.db'
```
import os
cwd = os.getcwd()
print cwd
conn=sqlite3.connect(cwd+'/db/test.db')
```
Также можно использовать специальное имя :memory: для создания базы данных в ОЗУ

## version1.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('test.db')

    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print "SQLite version: %s" % data                

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()

```
## python version1.py

```
SQLite version: 3.8.2
```
## version2.py

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:

    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print "SQLite version: %s" % data  
```

## creating a new database with SQLite3 python3:

```
import sqlite3

def create_database(db_name):
    with sqlite3.connect(db_name) as db:
        print("new database called {0} created".format(db_name))

if __name__ == "__main__":
    name = input("Please enter the name of the database you wish to create: ")
    create_database(name)
```
## creating a new database with SQLite3 python2

```
import sqlite3

def create_database(db_name):
    with sqlite3.connect(db_name) as db:
        print("new database called {0} created".format(db_name))

if __name__ == "__main__":
    name = raw_input("Please enter the name of the database you wish to create: ")
    create_database(name)
```

# объект Cursor

Создав объект Connection можно создать объект Cursor и вызвать его метод execute() для выполнения SQL команд:
```
db = sqlite3.connect("myshop.db")
cursor = db.cursor()

```
# Создание таблицы

```
    sql = """create table Customer (
             CustomerID integer,
             FirstName text,
             LastName text,
             Street text,
             Town text,
             PostCode text,
             TelephoneNumber text,
             primary key (CustomerID))"""

    cursor.execute(sql)

```
# Вставка ряда данных
```
cursor.execute('''insert into Customer values(1, "Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893")''')

```
# Сохранение (commit) изменений

```
    db.commit()
```
# Закрытие курсора, в случае если он больше не нужен

```
cursor.close()
```
# Test myshop.py

```
python myshop.py

sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>


sqlite> .open myshop.db
sqlite> .table
Customer
sqlite> select * from Customer;
1|Adam|McNicol|1 Python Street|Cambridge|CB3 2YU|01223 467893
sqlite> .explain on
sqlite> select * from Customer;
Cust  FirstName      Last  Stre  Town  PostCode       Te
----  -------------  ----  ----  ----  -------------  --
1     Adam           McNicol  1 Python Street  Cambridge  CB3 2YU        01223 467893


```

Чтобы получить данные, после выполнения оператора SELECT, можно обработать курсор как итератор, вызвать метод fetchone() чтобы получить одиночный ряд, или вызвать fetchall() чтобы получить список соответствующих строк. Например:

### курсор как итератор

```
for row in cursor:
     print row

```
### fetchall

```
import sqlite3

db = sqlite3.connect("myshop.db")
cursor = db.cursor()

cursor.execute('''insert into Customer values(2, "Nicol","McAdam","2 Cython Street","Cambridge","CB3 2YU","04567 467893")''')

db.commit()

cursor.execute('SELECT * FROM Customer')

print cursor.fetchall()

cursor.close()

python table1.py

```

### with connect: table2.py

```
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

```
## DB-API подстановка параметров

Обычно для выполнения SQL операций необходимо использовать значения из переменных Python. Не рекомендуется собирать запрос используя строковые операции Питона потому что это может быть не безопасным, это делает программу уязвимой к инъекционным SQL атакам.

Вместо этого используйте DB-API подстановку параметров. Вставьте символ ? в качестве заполнителя в месте где вы хотите использовать значение и предоставьте кортеж значений в качестве второго аргумента метода курсора execute(). (Другие модули баз данных могут использовать другие заполнители, такие как %s или :l). Пример:

```
# Никогда не делайте так – это небезопасно!
FirstName = 'Adam'
cursor.execute("select * from Customer where FirstName = '%s'" % FirstName)
# Вместо этого делайте так
t = (FirstName,)
cursor.execute('select * from Customer where FirstName=?', t)
```

### values (?,?,?,?,?)', t) table3.py

```
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

```
### fetchone() table4.py

```
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
```

## DROP TABLE IF EXISTS

### table5.py
```
import sqlite3

db = sqlite3.connect("myshop.db")


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
with db:

    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS Customer")
    cursor.execute(sql)
    cursor.executemany("INSERT INTO Customer VALUES(?, ?, ?, ?, ?, ?, ?)", customers)

cursor.execute('SELECT * FROM Customer order by Town')
while True:
    tmp=cursor.fetchone()
    if tmp:
        print tmp
    else:
        break
cursor.close()
db.close()
```

### table6.py executescript()

```
import sqlite3
import sys

try:
    db = sqlite3.connect("myshop.db")

    cursor = db.cursor()  

    cursor.executescript("""
        DROP TABLE IF EXISTS Customer,
        create table Customer(CustomerID integer, FirstName text, LastName text, Street text, Town text, PostCode text, TelephoneNumber text, primary key (CustomerID));
        INSERT INTO Customer VALUES(1, "Adam","McNicol","1 Python Street","Cambridge","CB3 2YU","01223 467893");
        INSERT INTO Customer VALUES(2, "Nicol","McAdam","2 Cython Street","Cambridge","CB3 2YU","04567 467893");
        INSERT INTO Customer VALUES(3, "Nic","Adam","2 Pillow Street","London","BB3 2YU","04567 467888");
        INSERT INTO Customer VALUES(4, "Ann","McDonald","55 Flowers Street","Glasgj","DB3 2YU","04567 466666");
        INSERT INTO Customer VALUES(5, "Tom","Adams","2 Django Street","Dublin","CE3 2YU","04567 467777");
        INSERT INTO Customer VALUES(6, "Trevor","Adams","25 Django Street","Dublin","CE3 5YU","04567 468777");
        INSERT INTO Customer VALUES(7, "Tim","Doo","5 Django Street","Dublin","CE3 5YU","04567 468700");
        INSERT INTO Customer VALUES(8, "Marry","Ann","7 Django Street","Dublin","CE3 5YU","04567 468700");
        """)

    cursor.commit()

except sqlite3.Error, e:

    if db:
        db.rollback()

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if db:
        cursor.execute('SELECT * FROM Customer order by Town')
        while True:
            tmp=cursor.fetchone()
            if tmp:
                print tmp
            else:
                break
        cursor.close()
        db.close()

```
## Порядок работы:

- Создание соединения с базой данных. Если БД не существует то она будет создана, иначе файл будет открыт.
- Создание объекта курсора для взаимодействия с БД.
- Вставка кортежа со значениями
- db.commit()

# Выборка данных

### Выборка нескольких строк с данными table7.py:

```
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
```

### Выборка одной строки с данными table8.py:

    import sqlite3

    db = sqlite3.connect("myshop.db")

    with db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM Customer')
        data = cursor.fetchone()
        print data[0]

    cursor.close()
    db.close()


Есть возможность выбрать заданное количество строк, передав желаемое значение в курсор:

### table9.py

```
import sqlite3

db = sqlite3.connect("myshop.db")

with db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Customer')
    print cursor.fetchmany(2)

cursor.close()
db.close()
```

# База данных в памяти

Если в вызове sqlite3_open() передать имя файла как ":memory:", то SQLite создаст соединение к новой (чистой) БД в памяти.

Это соединение абсолютно неотличимо от соединения к БД в файле по логике использования: доступен тот же набор SQL команд.

### можно открыть два соединения к одной БД в памяти.

```
rc = sqlite3_open("file:memdb1?mode=memory&cache=shared", &db);

ATTACH DATABASE 'file:memdb1?mode=memory&cache=shared' AS aux1;
```

# last inserted row id
### mem0.py
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect(':memory:')

with con:

    cur = con.cursor()    
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")

    lid = cur.lastrowid
    print "The last Id of the inserted row is %d" % lid
```

lastrowid returns None when you insert more than one row at a time with executemany

### memory1.py:
```
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

```
### memory2.py

```
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

```

# Функции и константы модуля.

## sqlite3.PARSE_DECLTYPES
Эта константа предназначена для использования с параметром detect_types функции connect().

Установка ее позволяет модулю sqlite3 разбирать заявленный тип для каждой возвращаемой колонки. Разбор первого слова объявленного типа, такого как «целочисленное значение первичного ключа» будет воспринято как целочисленное число или для «number(10)» будет воспринято как «число». Далее для выбранной колонки будет просмотрен словарь конвертеров и будет использована та функция конвертера что зарегистрирована для данного типа.

## sqlite3.PARSE_COLNAMES
Эта константа предназначена для использования с параметром detect_types функции connect().
Установка этого параметра позволяет интерфейсу SQLite проанализировать имя каждого возвращаемого столбца. Он будет искать строки сформированные [mytype], и затем решит, что ‘mytype’ - тип столбца. Он попытается найти запись ‘mytype’ в словаре преобразователей и затем использует функцию преобразователя что бы возвратить значение. Имя столбца, найденное в Cursor.description, является только первым словом имени столбца, то есть если Вы используете что-то наподобие ‘as "x [datetime]"’ в SQL-запросе, тогда будет проанализировано все до первого пробела для имени столбца: имя столбца просто было бы “x”.

## sqlite3.connect
    sqlite3.connect(database[, timeout, detect_types, isolation_level, check_same_thread,factory, cached_statements])
Создает соединение с файлом database базы данных SQLite. Возможно использование “:memory:” для открытия соединения с базой данных находящейся в оперативной памяти вместо жесткого диска.

Когда к базе данных получают доступ многократные соединения, и один из процессов изменяет базу данных, база данных SQLite блокируется, до тех пор пока та транзакция не зафиксируется (commit). Параметр timeout определяет, сколько времени соединение должно ждать блокировки, чтобы уйти до возбуждения исключения. Значение по умолчанию для параметра тайм-аута 5.0 (пять секунд).

SQLite нативно поддерживает только следующие типы данных: TEXT, INTEGER, FLOAT, BLOB, NULL. Если имеется необходимость использовать другие типы, то реализация их поддержки является самостоятельной задачей. Использование параметра detect_types и специальных конверторов, зарегистрированных с помощью функции register_convertor(), позволит легко сделать это.

detect_types по умолчанию равен 0 (т.е., обнаружение типов выключено), возможные значения представляют собой любые комбинации PARSE_DECLTYPES и PARSE_COLNAMES.

По умолчанию модуль sqlite3 использует класс Connection для соединений. Тем не менее, возможно разделить на подклассы класс Connection и сделать connect() используя свой класс, указав его в параметре factory.
sqlite3 модуль использует внутренний кэш операторов что бы избежать издержек при парсинге SQL запросов. Что бы явно задать число операторов для кеширования, необходимо задать параметр cashed_statements. По умолчанию он равен значению 100.

## sqlite3.register_convertor(typename, callable)
Регистрирует вызываемый объект для преобразования строки байтов из базы данных в специальный тип данных Питона. Вызываемый объект будет вызываться для всех значений базы данных которые являются типа typename. Присвойте параметр detect_type функции connect() что бы посмотреть как работает детектирование типов. Помните что в случае typename и имя типа должны совпадать в вашем запросе.

## sqlite3.register_adapter(type, callable)
Регистрирует вызываемый объект для преобразования специального Питоновского типа данных type в один из типов поддерживаемых SQLite. Вызываемый объект callable принимает в качестве одиночного параметра значение Питона и должно возвращать значение следующих типов: int, long, float, str (в кодировке UTF-8), unicode, buffer.

## convert Python decimal to SQLite numeric const2.py

```
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
```

### regtype1.py:

```
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

```

## sqlite3.complete_statement(sql)
Возвращает True если строка sql содержит одно или более SQL операторов оканчивающихся точкой с запятой. Это не проверяет корректность синтаксиса SQL запроса, только то что не содержится не закрытых строковых символов и выражение заканчивается точкой с запятой.

## sqlite3.enable_callback_tracebacks(flag)
По умолчанию вы не будете получать traceback информацию в функциях определяемых пользователем преобразователях и т.д. Если вы хотите отладить их, то нужно вызвать эту функцию с параметром flag равным True. После этого вы будете получать traceback информацию на стандартное устройство вывода ошибок sys.stderr. Использование значения параметра flag равным False отключит данную функцию.

# Объекты Connection
## Class sqlite3.Connection
Класс соединения базы данных SQLite имеет следующие атрибуты и методы:
### Connection.isolation_level
Возвращает или устанавливает текущий уровень изоляции. Принимает значение None для режима автоматического принятия изменений (autocommit) или один из «DEFFERED», «IMMEDIATE», «EXCLUSIVE».

### Connection.cursor([cursorClass])
Параметр cursorClass должен быть частным классом курсора который бы расширил sqlite3.Cursor.

### Connection.commit()
Этот метод фиксирует текущую транзакцию. Если не вызвать этот метод, то все изменения сделанные с момента прошлого вызова commit() не будут видимы другим соединениям.

### Connection.rollback()
Этот метод отменяет все изменения сделанные прошлым вызовом commit().

### Connection.close()
Закрытие соединения с базой данных. Внимание!Этот метод не вызывает автоматически commit(), поэтмоу для сохранения всех изменений следует сперва вызывать commit().
```
Connection.execute(sql[,parameters])
Connection.executemany(sql[,parameters])
Connection.executescript(sql_script)
```
Это не стандартный ярлык, который создает промежуточный объект курсора вызывая метод курсора. Затем вызывая метод курсора execute/executemany/executescript с заданными параметрами.
