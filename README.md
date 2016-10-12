# python-21v unit 05
# Files
## Opening and Closing Files
    file object = open(file_name [, access_mode][, buffering])

##  Детали параметров файла:
- file_name: имя файла.
- access_mode: режим доступа к файлу
- buffering: буферизация Если 0 - отключает буферизацию, данные сразу записываются. Если 1 - Построчный режим буферизации. Если больше одного процесс буферизации выполняется с указанным размером буфера. Отрицательное число - размер буфера будет равен системному.

## Режимы работы с файлами
- r  - Открывает файл только для чтения. Указатель стоит в начале файла.
- rb - Открывает файл для чтения в двоичном формате. Указатель стоит в начале файла.
- r+ - Открывает файл для чтения и записи. Указатель стоит в начале файла.
- rb+ - Открывает файл для чтения и записи в двоичном формате. Указатель стоит в начале файла.
- w - Открывает файл только для записи. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
- wb - Открывает файл для записи в двоичном формате. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
- w+ - Открывает файл для чтения и записи. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
- wb+ - Открывает файл для чтения и записи в двоичном формате. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
- a - Открывает файл для добавления информации в файл. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
- ab - Открывает файл для добавления в двоичном формате. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
- a+ - Открывает файл для добавления и чтения. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
- ab+ - Открывает файл для добавления и чтения в двоичном формате. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.

        f1 = open("test") # по умолчанию файл открывается в режиме r(чтение)
        f2 = open("test", "w") # файл открывается для записи
        f2 = open("test", "w", 0) # отключает буферизацию, данные сразу записываются в файл (например при вызове метода write())
        f3 = open("test", "a") # файл открывается для записи в конец
        f4 = open("test", "a+") # файл открывается как для чтения так и для записи в конец
        f5 = open("test", "ab") # добавляя к режиму символ "b" мы можем работать с файлам как с двоичными данными(интерпритация символа новой строки отключена)
        xfile = open("test.txt")

# Атрибуты
## file.closed
Возвращает True если файл был закрыт.
## file.mode
Возвращает режим доступа, с которым был открыт файл.
## file.name
Возвращает имя файла.
## file.softspace
Возвращает False если при выводе содержимого файла следует отдельно добавлять пробел.

# Открытие файла
        fo = open("foo.txt", "wb")
        print "Name of the file: ", fo.name
        print "Closed or not : ", fo.closed
        print "Opening mode : ", fo.mode
        print "Softspace flag : ", fo.softspace

# Закрытие файла в Python. Метод close().
Метод файлового объекта close() автоматически закрывает файл, при этом теряется любая несохраненная информация. Работать с файлом (читать, записывать) после этого нельзя.
Python автоматически закрывает файл если файловый объект к которому он привязан присваивается другому файлу. Однако, хорошей практикой будет вручную закрывать файл командой close().
        my_file = open("some.txt")
        print("Имя файла: ", my_file.name)
        print("Файл закрыт: ", my_file.closed)
        my_file.close()
        print("А теперь закрыт: ", my_file.closed)

# Чтение и запись файлов в Python
Для файлового объекта доступен целый набор методов, чтобы облегчить нашу работу с файлом.
## Запись в файл в Python. Метод write().
Метод write() записывает любую строку в открытый файл. Важно помнить, что строки в Python могут содержать двоичные данные, а не только текст.
Метод write() не добавляет символ переноса строки ('\n') в конец файла.
### Синтаксис метода write().
    my_file.write(string);

        my_file = open("some.txt", "w")
        my_file.write("Мне нравится Python!\nЭто классный язык!")
        my_file.close()

## Чтение из файла в Python. Метод read().
Метод read() читает строку из открытого файла.
### Синтаксис метода read().
    my_file.read([count])
Необязательный параметр count - это количество байт, которые следует прочитать из открытого файла. Этот метод читает информацию с начала файла и, если параметр count не указан, до конца файла.

Например, прочтем созданный нами файл some.txt:
        my_file = open("some.txt")
        my_string = my_file.read()
        print("Было прочитано:")
        print(my_string)
        my_file.close()
### прочитать весь файл в строку
        xString = xfile.read()
### прочитать N-байтов в строку
        xString = xfile.read(N)

        fileHandler = open("contacts.db")
        my_string = fileHandler.read()
        print("Было прочитано:")
        print(my_string)
        fileHandler.close()

        Было прочитано:
        Alice:Foo:23411122:23 Foo drive
        Beth:Bar:23422255:44 Bar street

### прочитать текстовую строку включая символ конца строки
        xString = xfile.readline()

        fileHandler = open("contacts.db")
        # прочитать текстовую строку включая символ конца строки
        xString = fileHandler.readline()
        print("Было прочитано:")
        print(xString)
        fileHandler.close()

        Было прочитано:
        Alice:Foo:23411122:23 Foo drive

### прочитать весь файл целиком в список строк
        xList = xfile.readlines()

        fileHandler = open("contacts.db")
        # прочитать весь файл целиком в список строк
        xList = fileHandler.readlines()
        print("Было прочитано:")
        print(xList)
        fileHandler.close()

        Было прочитано:
        ['Alice:Foo:23411122:23 Foo drive\n', 'Beth:Bar:23422255:44 Bar street\n']

## [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
        print("Было прочитано:")
        with open("contacts.db") as f:
            lines = f.readlines()
        print(lines)

        Было прочитано:
        ['Alice:Foo:23411122:23 Foo drive\n', 'Beth:Bar:23422255:44 Bar street\n']

        or with stripping the newline character:

        print("Было прочитано:")
        lines = [line.rstrip('\n') for line in open("contacts.db")]
        print(lines)

        line.strip() would remove all leading and trailing whitespace, not just the trailing \n.

        Было прочитано:
        ['Alice:Foo:23411122:23 Foo drive', 'Beth:Bar:23422255:44 Bar street']

### phoneGup11.py

    contacts = []

        if choice == 'p':
            lines = [line.rstrip('\n') for line in open("contacts.db")]
            for line in lines:
                newRecord = line.split(':')
                add_contact(newRecord)
            print_contacts(contacts)

### записать строку в файл
        xfile.write(xString)

        def save_contact():
            pass
### закрытие файла в ручную (выполняется по окончанию работы с файлом)
        xfile.close()

### phoneGup12.py
    def save_contact(rec):
        fileHandler = open("contacts.db", 'a')
        fileHandler.write(':'.join(rec))
        fileHandler.close()

        elif choice == 'a':
            newRecord = []
            tup1 = ("First Name", "Last Name", "Phone Number", "Address")
            print("Add New Record To PhoneGap")
            for prompt in tup1:
                makeList(prompt)
            add_contact(newRecord)
            save_contact(newRecord)

### phoneGup13.py
    def save_contact(rec):
        fileHandler = open("contacts.db", 'a')
        fileHandler.write(':'.join(rec)+'\n')
        fileHandler.close()


    def load_contacts():
        lines = [line.rstrip('\n') for line in open("contacts.db")]
        for line in lines:
            newRecord = line.split(':')
            add_contact(newRecord)

        if choice == 'p':
            if len(contacts) == 0:
                load_contacts()
            print_contacts(contacts)


        xfile.writelines(xList) # записать строки из списка в файл

        xfile.flush() # выталкивает выходные буферы на диск, файл остается открытым

        xfile.seek(N) # изменяет текущую позицию в файле для следующей операции, смещая ее на N-байтов от начала файла


## Как узнать позицию указателя в файле в Python.
После того как вы вызвали метод read() на файловом объекте, если вы повторно вызовете read(), то увидите лишь пустую строку. Это происходит потому, что после первого прочтения указатель находится вконце файла. Для того чтобы узнать позицию указателя можно использовать метод tell().
        my_file = open("some.txt")
        my_file.read(10)
        print ("Я на позиции:", my_file.tell())
        my_file.close()
метод tell() сообщает в скольки байтах от начала файла мы сейчас находимся.
Чтобы перейти на нужную нам позицию, следует использовать другой метод - seek().
### Синтаксис метода seek().
    my_file.seek(offset, [from])
Аргумент offset указывет на сколько байт перейти.  опциональный аргумент from означает позицию, с которой начинается движение. 0 - означает начало файла, 1 нынешняя позиция, 2 - конец файла.
    my_file = open("some.txt", "r")
    print(my_file.read(10))
    print("Мы находимся на позиции: ", my_file.tell())
### Возвращаемся в начало
    my_file.seek(0)
    print(my_file.read(10))
    my_file.close()
## Добавление в файл. Метод write()
Если вы хотите не перезаписать файл полностью (что делает метод write в случае открытия файла в режиме 'w'), а только добаить какой-либо текст, то файл следует открывать в режиме 'a' - appending. После чего использовать все тот же метод write.
### Удалит существующую информацию в some.txt и запишет "Hello".
    my_file = open("some.txt", 'w')
    my_file.write("Hello")
    my_file.close()
### Оставит существующую информацию в some.txt и добавит "Hello".
    my_file = open("some.txt", 'a')
    my_file.write("Hello")
    my_file.close()
## Расширенная работа с файлами в Python.
Для доступа к более широкому функционалу в работе с файлами в Python, как то удаление файлов, создание директорий и т.д. Следует подключить библиотеку os.
    import os
## Переименовать или удалить файл
    os.rename(current_file_name, new_file_name)
## Rename a file from test1.txt to test2.txt
    os.rename( "test1.txt", "test2.txt" )
## Delete file test2.txt
    os.remove("text2.txt")
## Create a directory "test"
    os.mkdir("newdir")
    os.mkdir("test")
    os.chdir("newdir")
## Changing a directory to "/home/newdir"
    os.chdir("/home/newdir")
    os.getcwd()
    import os
    os.getcwd()
    os.rmdir('dirname')
## This would  remove "/tmp/test"  directory.
    os.rmdir( "/tmp/test"  )
## Пример скрипта который сам создает файлы Python c баш-строкой.
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    myfile = open("newfile.py", "w")
    myfile.write("#!/usr/bin/env python\n# -*- coding: utf-8 -*-")
    myfile.close()
## Скачать и сохранить файл, используя Python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import urllib

    url = "http://www.google.ru/index.html"

    webFile = urllib.urlopen(url)
    localFile = open(url.split('/')[-1], 'wb')
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()
