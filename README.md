# python-21v unit 12
# Generators в Python

# yield

Итераторы

Каждый шаг при циклической обработке списка называется итерацией:

        >>> mylist = [1, 2, 3]
        >>> for i in mylist:
               ... print(i)

Сами списки являются итерируемыми объектами. Списковые выражения (list comprehensions) создают списки, а значит они также являются итерируемыми:

        >>> mylist = [x*x for x in range(3)]
        >>> for i in mylist:
               ...    print(i)

Все объекты, для которых можно использовать конструкцию for ... in ... являются итерируемыми объектами. Все значения итератора хранятся в памяти.

Генераторы

Генераторы — это подмножество итераторов. Разница заключается в том, что с помощью for ... in ... можно пройти по генератору только один раз, так как значения генератора не хранятся в памяти, они генерируются в процессе итерирования, т.е. каждое следующее значение в генераторе вычисляется на лету.

        >>> mygenerator = (x*x for x in range(3))
        >>> for i in mygenerator:
               ...    print(i)

Пример аналогичен предыдущему, за исключением того, что вместо спискового выражения используется выражение-генератор. mygenerator также как и mylist можно итерировать, но только один раз.

Генератор определяется двумя способами: с помощью выражения-генератора и при помощи зарезервированного слова yield.

Yield

Ключевое слово yield в некотором смысле похоже на return, только возвращает оно не какой-то определённый результат работы функции, а объект генератора. Определим простенький генератор:

        def createGenerator():
            mylist = range(3)
            for i in mylist:
                yield i*i

Когда вызывается функция, то код в теле функциине не вычисляется — функция просто вернёт объект генератора:

        mygenerator = createGenerator() # create a generator
        print(mygenerator) # mygenerator is an object!
        <generator object createGenerator at 0xb7555c34>

Код в теле функции будет вычисляться, если передать генератор, к примеру в цикл:

         for i in mygenerator:
             print(i)

Либо вручную вызвать метод next()

        mygenerator.next()

        mygenerator.next()


При первом вызов метода next() (или на первой итерация цикла) вычисляется тело функции и когда достигается yield, то возвращается первое вычисленное значение. На следующих итерациях будет следующее значение и так далее, пока не будет достигнут конец процесса генерирования.

Конец процесса работы генератора наступает тогда, когда генератор считается пустым. Т.е. очередной вызов вычисления определенной нами функции методом next() не добрался до yield по причине того, что либо цикл закончился, либо не были удовлетворены какие-либо другие услвоия для продолжения работы генератора. В этом случае генератор выкидывает исключение StopIteration

С помощью yield можно определить генератор. С помощью генератора можно создавать вычисляемые на лету последовательности. Вычисление на лету с помощью генераторов помогает экономить память и производить вычисления над бесконечными последовательностями.


# Обработка файлов данных

Вычислить число байт, переданных сервером Apache, используя его лог - for-loop.

    200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903
    66.249.65.37 - - [29/Feb/2016:07:31:24 -0600] "GET /dynamic/05ObjectModel.pdf HTTP/1.1" 304 -

str.split(sep[, maxsplit])

sep=None : Строка-разделитель, при помощи которой требуется разбить исходную строку. Может содержать как один, так и несколько символов. Если не указан, то разделителем считается последовательность пробельных символов.

maxsplit=-1 : Максимальное количество разбиений, которое требуется выполнить. Если -1, то количество разбиений не ограничено.

Если указан разделитель, разбиение пустой строки вернёт список с единственным элементом — пустой строкой: [''].

Если разделитель не указан, разбиение пустой строки вернёт пустой список: [].

В случаях, когда требуется, чтобы разбиение строки происходило справа налево, используйте str.rsplit.

        # nongenlog.py
        #
        # Sum up the number of bytes transferred in an Apache log file
        # using a simple for-loop.   We're not using generators here.

        wwwlog = open("access-log")
        total = 0
        for line in wwwlog:
            bytestr = line.rsplit(None,1)[1]
            if bytestr != '-':
                total += int(bytestr)

        print "Total", total


С помощью генератора

        # genlog.py
        #
        # Sum up the bytes transferred in an Apache server log using
        # generator expressions

        wwwlog     = open("access-log")
        bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
        bytes      = (int(x) for x in bytecolumn if x != '-')

        print "Total", sum(bytes)


# Сделать большой лог-файл для тестирования Make a big log file for testing makebig.py.

        import sys

        if len(sys.argv) != 2:
            print >>sys.stderr,"Usage : makebig.py repetitions"
            raise SystemExit(1)

        data = open("access-log").read()

        f = open("big-access-log","w")
        for i in xrange(int(sys.argv[1])):
            f.write(data)


# Работа с файловой системой

## os.walk()

Функция walk модуля os возвращает объект-генератор. Из полученного объекта можно получить кортежи для каждого каталога в переданной walk файловой иерархии. Каждый кортеж состоит из трех элементов:

- Абсолютный адрес очередного каталога (строка).
- Имена (без адреса) подкаталогов первого уровня для текущего каталога (список).
- Имена (без адреса) файлов данного каталога.

Дерево каталогов www:

Пусть переменная tree является ссылкой на объект-генератор, полученный в результате выполнения метода walk, которому, в свою очередь был передан в качестве аргумента адрес тестируемого каталога.

### testwalk.py

    tree = os.walk('/home/pl/mydir')
    print (tree)

В результате мы увидим следующее:

```
<generator object walk at 0x00A8B620>
```

Итак, есть объект-генератор. Поскольку полученный объект-генератор генерирует кортежи, количество которых равно количеству каталогов в дереве, то можно их получить с помощью цикла for и, например, вывести на экран

    for d in tree:
    	print (d)

получится следующее:

Каждый кортеж включает три элемента. Первый – это адрес каталога, второй – список поддиректорий не глубже первого уровня, третий – список имен файлов. Если вложенных каталогов или файлов нет, то соответствующий им список будет пуст.

Если мы еще раз запустим цикл с переменной tree, то уже ничего не получим. Дело в том, что объект-генератор, с которым переменная была связана, уже был использован, он выдал свое содержимое и больше его не содержит. Поэтому, если требуется сохранить кортежи для последующий обработки, то лучше сохранить их, например, в списке:

        contdir = []
        for i in os.walk('www'):
            contdir.append(i)

        for i in contdir:
            print(i)

С помощью функции walk() можно получить имена файлов с тем, чтобы в дальнейшем с ними что-нибудь делать с помощью других методов Python и его модулей. Получить их можно, извлекая из третьего элемента каждого кортежа.

    for path, dirlist, filelist in os.walk('www'):
        for f in filelist:
            print(f)

Переменная path в каждой итерации связывается с первым элементом каждого кортежа (строкой, содержащей адрес каталога), dirlist – со вторым элементом (списком подкаталогов), а filelist - со списками файлов очередного каталога. Чтобы извлечь списки файлов целиком, а не выделять каждый файл по отдельности, можно сделать так:

    for path, dirlist, filelist in os.walk('www'):
    	print (filelist)

Имена файлов не полные. Они не содержат адреса, следовательно, для операций с файлами таких списков не достаточно. Для получения полных адресов подойдет функция os.path.join(). С ее помощью можно объединить первый элемент кортежа, содержащий полный путь, с именем каждого файла:

        path_f = []
        for path, dirlist, filelist in os.walk('www'):
            for f in filelist:
                p = os.path.join(path, f)
                path_f.append(p)

        for f in path_f:
            print(f)

## Модуль fnmatch - соответствие шаблонам имен файлов UNIX.
Модуль предоставляет поддержку подстановок в стиле оболочки UNIX, которые не являются тем же самым что и регулярные выражения, описанные в модуле re.

### Специальными символами являются:

        * 	Совпадает любое количество (включая ноль) символов
        ? 	Совпадает любой одиночный символ
        [foo] 	Совпадает любой символ из заданной последовательности
        [!foo] 	Совпадает любой символ не входящий в заданную последовательность

## fnmatch.fnmatch(filename, pattern)

Проверяет соответствие строки filename строке шаблону pattern, возвращает True в случае соответствия. Если операционная система чуствительна к регистру, то оба параметра будут приведены к нижнему или верхнему регистру перед тем как произойдет сравнение. Если необходимо сравнение учитываающее регистр, то необходимо воспользоваться fnmatchcase().

Следующий пример выведет на экран все имена файлов в текущей директории с расширением .txt:

        import fnmatch, os

        for file in os.listdir('.'):
            if fnmatch.fnmatch(file, '*.txt'): # *.*
                print file

## fnmatch.fnmatchcase(filename, pattern)
Проверяет соответствие строки filename строке шаблону pattern учитывая регистр символов.

## fnmatch.filter(names, pattern)
Возвращает список элементов в names которые соответствуют шаблону pattern. Это тоже самое что и [n for n in names if fnmatch(n, pattern)], но выполняется более эффективно.

## fnmatch.translate(pattern)
Возвращает преобразованный в регулярное выражение шаблон pattern

## genfind.py. Генератор имен файлов, соответствующих заданному шаблону.

        # genfind.py
        #
        # A function that generates files that match a given filename pattern

        import os
        import fnmatch

        def gen_find(filepat,top):
            for path, dirlist, filelist in os.walk(top):
                for name in fnmatch.filter(filelist,filepat):
                    yield os.path.join(path,name)

        # Example use

        if __name__ == '__main__':
            lognames = gen_find("access-log*","www")
            for name in lognames:
                print name

## genopen.py. Функция генератор, которая отдает объект открытых файлов  из последовательности имен файлов.
        # genopen.py
        #
        # Takes a sequence of filenames as input and yields a sequence of file
        # objects that have been suitably open

        import gzip, bz2

        def gen_open(filenames):
            for name in filenames:
                if name.endswith(".gz"):
                    yield gzip.open(name)
                elif name.endswith(".bz2"):
                    yield bz2.BZ2File(name)
                else:
                    yield open(name)

        # Example use

        if __name__ == '__main__':
            from genfind import  gen_find
            lognames = gen_find("access-log*","www")
            logfiles = gen_open(lognames)
            for f in logfiles:
                print f

## gencat.py. Функция генератор, объединяющая последовательность генераторов в одну последовательность.
        # gencat.py
        #
        # Concatenate multiple generators into a single sequence

        def gen_cat(sources):
            for s in sources:
                for item in s:
                    yield item

        # Example use

        if __name__ == '__main__':
            from genfind import  gen_find
            from genopen import  gen_open

            lognames = gen_find("access-log*","www")
            logfiles = gen_open(lognames)
            loglines = gen_cat(logfiles)
            for line in loglines:
                print line,

# Регулярное выражение

Регулярное выражение — это последовательность символов, используемая для поиска и замены текста в строке или файле.

## Регулярные выражения используют два типа символов:

- специальные символы: у этих символов есть специальные значения, например, * означает «любой символ»;
- литералы (например: a, b, 1, 2 и т. д.).

### В Python для работы с регулярными выражениями есть модуль re.
Для использования его нужно импортировать:

    import re

Чаще всего регулярные выражения используются для:

- поиска в строке;
- разбиения строки на подстроки;
- замены части строки.

### Иетоды, которые предоставляет библиотека re:

                    re.match()
                    re.search()
                    re.findall()
                    re.split()
                    re.sub()
                    re.compile()

## re.match(pattern, string):

Этот метод ищет по заданному шаблону в начале строки. Например, если мы вызовем метод match() на строке «200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903» с шаблоном «200», то он завершится успешно. Однако если мы будем искать HTTP, то результат будет отрицательный.

                import re
                result = re.match(r'200', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
                print result

Чтобы вывести ее содержимое, используем метод group(). (r перед строкой шаблона означает, что это «сырая» строка).

                print result.group(0)

Также есть методы start() и end() для того, чтобы узнать начальную и конечную позицию найденной строки.

                print result.start()
                print result.end()

## re.search(pattern, string):
Этот метод похож на match(), но он ищет не только в начале строки.

    result = re.search(r'200', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')

    print result.group(0)

Метод search() ищет по всей строке, но возвращает только первое найденное совпадение.

## re.findall(pattern, string):

Этот метод возвращает список всех найденных совпадений. У метода findall() нет ограничений на поиск в начале или конце строки. Для поиска рекомендуется использовать именно findall(), так как он может работать и как re.search(), и как re.match().

    result = re.findall(r'200', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')

    print result

## re.split(pattern, string, [maxsplit=0]):
Этот метод разделяет строку по заданному шаблону.

    result = re.split(r'200', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
    print result

Метод split() принимает также аргумент maxsplit со значением по умолчанию, равным 0. В данном случае он разделит строку столько раз, сколько возможно, но если указать этот аргумент, то разделение будет произведено не более указанного количества раз.

    result = re.split(r'200', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903',maxsplit=1)
    print result

Мы установили параметр maxsplit равным 1, и в результате строка была разделена на две части вместо трех.

## re.sub(pattern, repl, string):

Этот метод ищет шаблон в строке и заменяет его на указанную подстроку. Если шаблон не найден, строка остается неизменной.

    result = re.sub(r'200', '188',  '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
    print result

## re.compile(pattern, repl, string):

Мы можем собрать регулярное выражение в отдельный объект, который может быть использован для поиска. Это также избавляет от переписывания одного и того же выражения.

                import re
                pattern = re.compile('200')
                result = pattern.findall('200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
                print result

Но что, если у нас нет определенного шаблона, и нам надо вернуть набор символов из строки, отвечающий определенным правилам? Такая задача часто стоит при извлечении информации из строк. Это можно сделать, написав выражение с использованием специальных символов.

Вот наиболее часто используемые из них:

                .	Один любой символ, кроме новой строки \n.
                ?	0 или 1 вхождение шаблона слева
                +	1 и более вхождений шаблона слева
                *	0 и более вхождений шаблона слева
                \w	Любая цифра или буква (\W — все, кроме буквы или цифры)
                \d	Любая цифра [0-9] (\D — все, кроме цифры)
                \s	Любой пробельный символ (\S — любой непробельнй символ)
                \b	Граница слова
                [..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
                \	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
                ^ и $	Начало и конец строки соответственно
                {n,m}	От n до m вхождений ({,m} — от 0 до m)
                a|b	Соответствует a или b
                ()	Группирует выражение и возвращает найденный текст
                \t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно

## Примеры использования регулярных выражений
### Вернуть первое слово из строки

Сначала попробуем вытащить каждый символ (используя \w)

                import re
                result = re.findall(r'.', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
                print result

Для того, чтобы в конечный результат не попал пробел, используем вместо . \w.

    result = re.findall(r'\w', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
    print result

Теперь попробуем достать каждое слово (используя * или +)

    result = re.findall(r'\w*', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
    print result

И снова в результат попали пробелы, так как * означает «ноль или более символов». Для того, чтобы их убрать, используем +:

    result = re.findall(r'\w+', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
    print result

Теперь вытащим первое слово, используя ^:

    result = re.findall(r'^\w+', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
    print result

Если мы используем $ вместо ^, то мы получим последнее слово, а не первое:

    result = re.findall(r'\w+$', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
    print result

## Вернуть первые два символа каждого слова

Вариант 1: используя \w, вытащить два последовательных символа, кроме пробельных, из каждого слова:

                result = re.findall(r'\w\w', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
                print result

Вариант 2: вытащить два последовательных символа, используя символ границы слова (\b):

        result = re.findall(r'\b\w.', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')

        print result

## вернуть список доменов из списка адресов электронной почты

Сначала вернем все символы после «@»:

                result = re.findall(r'@\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
                print result

Как видим, части «.com», «.in» и т. д. не попали в результат. Изменим наш код:

                result = re.findall(r'@\w+.\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
                print result

Второй вариант — вытащить только домен, используя группировку — ( ):

                result = re.findall(r'@\w+.(\w+)', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
                print result

## Извлечь дату из строки

Используем \d для извлечения цифр.

                result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
                print result

Для извлечения только года нам опять помогут скобки:

                result = re.findall(r'\d{2}-\d{2}-(\d{4})', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
                print result

## Извлечь все слова, начинающиеся на гласную

Для начала вернем все слова, которые начинаются на определенные буквы (используя []):

                result = re.findall(r'[fghpbFGHPB]\w+', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
                print result

используем \b для обозначения границы слова:

                result = re.findall(r'[fghpbFGHPB]\w+', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
                print result

Также мы можем использовать ^ внутри квадратных скобок для инвертирования группы:

                result = re.findall(r'[^fghpbFGHPB]\w+', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
                print result

В результат попали слова, «начинающиеся» с пробела. Уберем их, включив пробел в диапазон в квадратных скобках:

                r'[^fghpbFGHPB ]\w+'

## Проверить телефонный номер (номер должен быть длиной 10 знаков и начинаться с 8 или 9)

                import re
                li = ['9999999999', '999999-999', '99999x9999']

                for val in li:
                 if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:
                     print 'yes'
                 else:
                     print 'no'


## Разбить строку по нескольким разделителям

                import re
                line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").
                result = re.split(r'[;,\s]', line)
                print result

Также мы можем использовать метод re.sub() для замены всех разделителей пробелами:

                import re
                line = 'asdf fjdk;afed,fjek,asdf,foo'
                result = re.sub(r'[;,\s]',' ', line)
                print result

## Извлечь информацию из html-файла

Допустим, нам надо извлечь информацию из html-файла, заключенную между <td> и </td>, кроме первого столбца с номером. Также будем считать, что html-код содержится в строке.

                result = re.findall(r'\w+\s(\w+)\s(\w+)',str)
                print result

Прочитать содержимое html-файла можно с помощью библиотеки urllib2:

                import urllib2
                response = urllib2.urlopen('')
                html = response.read()

## gengrep.py. Генератор группирует последовательности строк, которые соответствуют шаблону регулярного выражения.
        # gengrep.py
        #
        # Grep a sequence of lines that match a re pattern

        import re
        def gen_grep(pat,lines):
            patc = re.compile(pat)
            for line in lines:
                if patc.search(line): yield line

        # Example use

        if __name__ == '__main__':
            from genfind import  gen_find
            from genopen import  gen_open
            from gencat  import  gen_cat

            lognames = gen_find("access-log*","www")
            logfiles = gen_open(lognames)
            loglines = gen_cat(logfiles)

            # Look for ply downloads (PLY is Python package)
            plylines = gen_grep(r'ply-.*\.gz',loglines) # *.*
            for line in plylines:
                print line,

## bytesgen.py. Сколько байт было передано для конкретного файла в директории лог-файлов.
        # bytesgen.py
        #
        # An example of chaining together different generators into a processing
        # pipeline.    

        from genfind import *
        from genopen import *
        from gencat import *
        from gengrep import *

        pat    = r'ply-.*\.gz'
        logdir = 'www'

        filenames = gen_find("access-log*",logdir)
        logfiles  = gen_open(filenames)
        loglines  = gen_cat(logfiles)
        patlines  = gen_grep(pat,loglines)
        bytecol   = (line.rsplit(None,1)[1] for line in patlines)
        bytes     = (int(x) for x in bytecol if x != '-')

        print "Total", sum(bytes)


# Анализ и обработка данных
## retuple.py. Преобразовать последовательность строк в последовательность кортежей с использованием регулярных выражений.
        # retuple.py
        #
        # Read a sequence of log lines and parse them into a sequence of tuples

        loglines = open("access-log")

        import re

        logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
                   r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

        logpat   = re.compile(logpats)

        groups   = (logpat.match(line) for line in loglines)
        tuples   = (g.groups() for g in groups if g)

        if __name__ == '__main__':
            for t in tuples:
                print t

## redict.py. Преобразовать последовательность строк в последовательность словарей с именованными полями.
        # redict.py
        #
        # Read a sequence of log lines and parse them into a sequence of dictionaries

        loglines = open("access-log")

        import re

        logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
                   r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

        logpat   = re.compile(logpats)

        groups   = (logpat.match(line) for line in loglines)
        tuples   = (g.groups() for g in groups if g)

        colnames = ('host','referrer','user','datetime',
                    'method', 'request','proto','status','bytes')

        log      = (dict(zip(colnames,t)) for t in tuples)

        if __name__ == '__main__':
            for x in log:
                print x

## fieldmap.py. Переопределить поля в последовательности словарей.
        # fieldmap.py
        #
        # Take a sequence of dictionaries and remap one of the fields

        def field_map(dictseq, name, func):
            for d in dictseq:
                d[name] = func(d[name])
                yield d

        # Example

        if __name__ == '__main__':

            loglines = open("access-log")

            import re

            logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
                       r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

            logpat   = re.compile(logpats)

            groups   = (logpat.match(line) for line in loglines)
            tuples   = (g.groups() for g in groups if g)

            colnames = ('host','referrer','user','datetime',
                        'method', 'request','proto','status','bytes')

            log      = (dict(zip(colnames,t)) for t in tuples)

            log      = field_map(log,"status",int)
            log      = field_map(log,"bytes",
                                 lambda s: int(s) if s != '-' else 0)


            for x in log:
                print x

## linesdir.py. Генерация строк из файлов в каталоге.
        # linesdir.py
        #
        # Generate a sequence of lines from files in a directory

        from genfind import *
        from gencat import *
        from genopen import *

        def lines_from_dir(filepat, dirname):
            names = gen_find(filepat,dirname)
            files = gen_open(names)
            lines = gen_cat(files)
            return lines

        # Example use

        if __name__ == '__main__':
            loglines = lines_from_dir("access-log*","www")
            for line in loglines:
                print line,

## apachelog.py. Разобрать файл журнала Apache.
        # apachelog.py
        #
        # Parse an apache log file into a sequence of dictionaries

        from fieldmap import *

        import re

        logpats  = r'(\S+) (\S+) (\S+) \[(.*?)\] ' \
                   r'"(\S+) (\S+) (\S+)" (\S+) (\S+)'

        logpat   = re.compile(logpats)

        def apache_log(lines):
            groups = (logpat.match(line) for line in lines)
            tuples = (g.groups() for g in groups if g)

            colnames = ('host','referrer','user','datetime',
                    'method', 'request','proto','status','bytes')

            log      = (dict(zip(colnames,t)) for t in tuples)
            log      = field_map(log,"status",int)
            log      = field_map(log,"bytes",
                                 lambda s: int(s) if s != '-' else 0)

            return log

        # Example use:

        if __name__ == '__main__':
            from linesdir import *
            lines = lines_from_dir("access-log*","www")
            log = apache_log(lines)
            for r in log:
                print r

# Множество в python
Множество в python - "контейнер", содержащий не повторяющиеся элементы в случайном порядке.

Создаём множества:
                >>> a = set()
                >>> a
                set()
                >>> a = set('hello')
                >>> a
                {'h', 'o', 'l', 'e'}
                >>> a = {'a', 'b', 'c', 'd'}
                >>> a
                {'b', 'c', 'a', 'd'}
                >>> a = {i ** 2 for i in range(10)} # генератор множеств
                >>> a
                {0, 1, 4, 81, 64, 9, 16, 49, 25, 36}
                >>> a = {}  # А так нельзя!
                >>> type(a)
                <class 'dict'>

Как видно из примера, множества имеет тот же литерал, что и словарь, но пустое множество с помощью литерала создать нельзя.

Множества удобно использовать для удаления повторяющихся элементов:
                >>> words = ['hello', 'daddy', 'hello', 'mum']
                >>> set(words)
                {'hello', 'daddy', 'mum'}

С множествами можно выполнять множество операций: находить объединение, пересечение...

    len(s) - число элементов в множестве (размер множества).
    x in s - принадлежит ли x множеству s.
    set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
    set == other - все элементы set принадлежат other, все элементы other принадлежат set.
    set.issubset(other) или set <= other - все элементы set принадлежат other.
    set.issuperset(other) или set >= other - аналогично.
    set.union(other, ...) или set | other | ... - объединение нескольких множеств.
    set.intersection(other, ...) или set & other & ... - пересечение.
    set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
    set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
    set.copy() - копия множества.

И операции, непосредственно изменяющие множество:

    set.update(other, ...); set |= other | ... - объединение.
    set.intersection_update(other, ...); set &= other & ... - пересечение.
    set.difference_update(other, ...); set -= other | ... - вычитание.
    set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
    set.add(elem) - добавляет элемент в множество.
    set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
    set.discard(elem) - удаляет элемент, если он находится в множестве.
    set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
    set.clear() - очистка множества.

## query404.py. Найдите множество всех документов, которые отсутствуют (404).
        # query404.py
        #
        # Find the set of all documents that 404 in a log file

        from linesdir import *
        from apachelog import *

        lines = lines_from_dir("access-log*","www")
        log = apache_log(lines)

        stat404 = set(r['request'] for r in log
                      if r['status'] == 404)

        for r in sorted(stat404):
            print r

## largefiles.py. Найти все переданые запросы, которые свыше мегабайта.
        # largefiles.py
        #
        # Find all transfers over a megabyte

        from linesdir import *
        from apachelog import *

        lines = lines_from_dir("access-log*","www")
        log = apache_log(lines)

        large = (r for r in log
                 if r['bytes'] > 1000000)

        for r in large:
            print r['request'],r['bytes']


## largest.py. Найти самый большой документ.
        # largest.py
        #
        # Find the largest file

        from linesdir import *
        from apachelog import *

        lines = lines_from_dir("access-log*","www")
        log = apache_log(lines)

        print "%d %s" % max((r['bytes'],r['request'])
                            for r in log)

## hosts.py. Найти уникальные IP-адреса
        # hosts.py
        #
        # Find unique host IP addresses

        from linesdir import *
        from apachelog import *

        lines = lines_from_dir("access-log*","www")
        log = apache_log(lines)

        hosts = set(r['host'] for r in log)
        for h in hosts:
            print h

## downloads.py. Найти количество загрузок определенного файла.
        # downloads.py
        #
        # Find out how many downloads of a specific request

        from linesdir import *
        from apachelog import *

        lines = lines_from_dir("access-log*","www")
        log = apache_log(lines)

        request = 'ply/ply-2.3.tar.gz'

        total = sum(1 for r in log
                      if r['request'] == '/ply/ply-2.3.tar.gz')

        print "Total", total

## robots.py. Узнать, кто вызывал robots.txt
        # robots.py
        #
        # Find out who has been hitting robots.txt

        from linesdir import *
        from apachelog import *

        lines = lines_from_dir("access-log*","www")
        log = apache_log(lines)

        addrs = set(r['host'] for r in log
                    if 'robots.txt' in r['request'])

        import socket
        for addr in addrs:
            try:
                print socket.gethostbyaddr(addr)[0]
            except socket.herror:
                print addr

## robotsfast.py. Узнать, кто вызывал robots.txt (более быстрый вариант).
        # robotsfast.py
        #
        # Find out who has been hitting robots.txt

        from linesdir import *
        from apachelog import *

        lines = lines_from_dir("access-log*","www")
        lines = (line for line in lines if 'robots.txt' in line)
        log = apache_log(lines)

        addrs = set(r['host'] for r in log
                    if 'robots.txt' in r['request'])

        import socket
        for addr in addrs:
            try:
                print socket.gethostbyaddr(addr)[0]
            except socket.herror:
                print addr


# Следует прочитать:

   PEP 234
   PEP 289
   PEP 289
   PEP 342
   PEP 289
   Understanding Python's "for" statement
   PEP 380
   A Curious Course on Coroutines and Concurrency
   Generator Tricks for Systems Programmers, v2.0.
