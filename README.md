# python-21v unit 07
# Модули

По мере возрастания программы у вас наверняка появится необходимость разбить ее на несколько файлов, чтобы их было легче поддерживать. Может возникнуть необходимость в многократном использовании написанных функций в нескольких программах, не копируя их определения в каждую из программ.

Модули выполняют как минимум три важных функции:
- Повторное использование кода: такой код может быть загружен много раз во многих местах.
- Управление адресным пространством: модуль — это высокоуровневая организация программ, это пакет имен, который избавляет вас от конфликтов. Каждый объект «проживает» свой цикл внутри своего модуля, поэтому модуль — это средство для группировки системных компонентов.
- Глобализация сервисов и данных: для реализации объекта, который используется во многих местах, достаточно написать один модуль, который будет импортирован.

# 1. Что такое модуль

Python позволяет поместить классы, функции или данные в отдельный файл и использовать их в других программах. Такой файл называется модулем. Объекты из модуля могут быть импортированы в другие модули. Имя файла образуется путем добавления к имени модуля расширения .py. При импорте модуля интерпретатор ищет файл с именем my_module.py сначала в текущем каталоге, затем в каталогах, указанных в переменной окружения PYTHONPATH, затем в зависящих от платформы путях по умолчанию, а также в специальных файлах с расширением '.pth', которые лежат в стандартных каталогах. Программист может внести изменения в PYTHONPATH и в '.pth', добавив туда свой путь. Каталоги, в которых осуществляется поиск, можно посмотреть в переменной sys.path.

Большие программы, как правило, состоят из стартового файла — файла верхнего уровня, и набора файлов-модулей. Главный файл занимается контролем программы. В то же время модуль — это не только физический файл. Модуль представляет собой коллекцию компонентов. В этом смысле модуль — это пространство имен, — namespace, и все имена внутри модуля еще называются атрибутами — такими, например, как функции и переменные.

# 2. Импорт модуля
Если запустить в каталоге, в котором лежит данный модуль (например, my_module.py), интерпретатор:
    python
и потом сделать импорт модуля:
    import my_module
то мы получаем доступ ко всем функциям, которые в модуле определены:
     my_module.func1()
     my_module.func2()
    ...
Для более короткой записи можно создать локальную переменную:
    f1 = my_module.func1
Второй вариант импорта — взятие непосредственно имени без имени модуля:
    from my_module import func1, func2
    func1()
Третий вариант импорта — включение всех имен, определенных в модуле:
    from my_module import *
    func1()
Для предотвращения конфликта имен можно использовать создание алиаса:
    from my_module import open as my_open
Пример. Импорт на основе from обладает такой особенностью, что он делает импортируемые атрибуты read-only:
    from small import x, y
    x = 42
В данном случае x — это локальная переменная, в то время как переменные x, y в самом модуле small не меняются:
    import small
    small.x = 42
здесь x — глобальная переменная.
Во избежание недоразумений import предпочтительнее без from в тех случаях, когда один и тот же модуль используется в нескольких местах.

Поскольку модуль загружается один раз, для его повторной загрузки можно использовать функцию reload().

Каждый модуль имеет собственное пространство имен, являющееся глобальной областью видимости для всех определенных в нем функций. Для того чтобы переменные этого модуля не попали в конфликт с другими глобальными именами или другими модулями, нужно использовать префикс: _имя_модуля_._имя_переменной_ .
Модули могут импортировать другие модули. Обычно инструкцию import располагают в начале модуля или программы.

## CALCULATOR calc1.py
        '''
         Program make a simple calculator that can add,
         subtract, multiply and divide using functions
        '''
        from functions import add
        from menu import menu, printMenu, myhelp, extacts
        ops = ('+', '-', '*', '/', '//', '%', '**')

## CALCULATOR calc2.py

        from lib.functions import add
        from utils.menu import menu, printMenu, myhelp, extacts

## CALCULATOR calc3.py

        from lib.functions import *
        from utils.menu import menu, printMenu, myhelp, extacts

## lib/__init__.py

        __all__ = ['add', 'subtract', 'multiply', 'divide', 'intdivide', 'modulo']

## contact9.py

    from contact.contact import Contact

# 3. Компиляция файлов
Для ускорения запуска программ, использующих большое количество модулей, если уже существует файл с именем my_module.pyc в том же каталоге, где найден my_module.py, считается, что он содержит байт-компилированный модуль my_module. Если такого файла нет, то он создается, и время последнего изменения my_module.py записывается в созданном my_module.pyc. Содержимое байт-компилированных файлов является платформенно-независимым (но может быть разным для разных версий интерпретатора), так что каталог с модулями может совместно использоваться машинами с разными архитектурами.

## Некоторые полезные опции компиляции:
- O — эта опция заставляет интерпретатор компилировать так называемый оптимизированный байт-код и сохранять его в файле с расширением '.pyo'. При этом из кода удаляются ассерты, игнорируется условный дебаг, '.pyc'-файлы игнорируются.
- OO — эта опция делает то же, что и предыдущая опция, плюс удаляет комменты.
Файл, запускаемый непосредственно из командной строки, никогда не компилируется. Для оптимизации его запуска необходимо большую часть кода убрать в модули.
Модуль может загружаться из файлов с расширением '.pyс' или '.pyo', даже если нет файла с расширением '.py'. Это может пригодиться в тех случаях, когда вы не хотите распространять исходный код.
Кроме того, интерпретатор может загружать бинарники, собранные с помощью языка си — файлы с расширением '.so' в линуксе либо '.dll' в Windows.
Модуль можно «зазипповать» в архив с расширением '.zip' и импортировать из архива.
Может быть загружен Java-класс, собранный с помощью Jython.

## phne1.py

    from contact.contact import Contact
    from main import Main

# 4. Стандартные модули
Python распространяется с библиотекой стандартных модулей. Библиотека включает в себя более 200 модулей, которые выполняют платформенно-зависимую поддержку таких задач, как: интерфейс к операционной системе, управление объектами, поиск, сеть + интернет, GUI и т.д. Полный список стандартных модулей можно посмотреть на http://docs.python.org/library/.
Часть модулей встроена в интерпретатор по умолчанию, обеспечивая доступ к операциям; они встроены либо из соображений эффективности, либо для обеспечения доступа к примитивам операционной системы — например, модуль sys.
Переменная sys.path содержит список строк с именами каталогов, в которых происходит поиск модулей. Она инициализируется из значения переменной окружения PYTHONPATH и встроенного значения по умолчанию. Можно добавить путь:
    import sys
    sys.path.append(/home/my/lib/python)

Для выяснения имен, определенных в модуле, можно использовать встроенную функцию dir(). Она возвращает отсортированный список строк:
    dir(sys)
    ['__displayhook__', '__doc__', '__egginsert', '__excepthook__', '__name__',
    ...
    'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_info']

# 5. Пакеты
Пакеты — способ структурирования пространств имен модулей на основе файловой системы. Пакетная организация дает все удобства по управлению большим количеством файлов. Пакетный импорт делает код более читабельным и значительно упрощает поиск. Если весь код структурирован в одном рутовом каталоге, все, что нужно добавить в PYTHONPATH — это рутовый каталог.
Так же, как применение модулей делает безопасным использование глобального пространства имен авторами различных модулей, применение пакетов делает безопасным использование имен модулей авторами многомодульных пакетов.
Например, есть пакет, который лежит в корневой папке TCP. В нем лежат два подкаталога — Server и Client:
    TCP/
       _init_.py
       main.py

       Server/
             _init_.py
             tcp.py
             server.py
             lib.py
       Client/
             _init_.py
             tcp.py
             client.py
             lib.py
Файл _init_.py необходим для того, чтобы интерпретатор распознал каталог, как содержащий пакет. Обычно это пустой файл. Тогда импорт индивидуальных модулей пакета может быть таким:
     import TCP.Server.lib
     import TCP.Client.lib
Ссылка на функцию должна быть полной:
    import TCP.Server.lib.connect()
Можно сделать альтернативную загрузку:
     from TCP.Server import lib as server_lib
     from TCP.Client import lib as client_lib
     server_lib.connect()
     client_lib.connect()

Здесь вместо lib может быть подставлен модуль, подпакет или имя, определенное в TCP.Server — т.е. это может быть функция, класс или переменная.
Что касается варианта с импортом:
    from TCP import *
то в корневом __init__.py может быть определен список __all__ , в котором перечисляются модули, которые импортируются в этом случае. Например:
    __all__ = ["Server", "Client"]
Импорт всех имен может привести к конфликтам. При этом глобальные переменные становятся доступными только на чтение — вместо них будут созданы локальные.

Импорт модулей — это основа программной архитектуры в питоне. Большие программы состоят из большого количества файлов, и объединяет их линковка во время исполнения на основе импорта. Модули структурируют программу, разбивая логику на отдельные компоненты. Код внутри одного модуля изолирован от остальных модулей, что минимизирует коллизию имен внутри программы.
Пакетный импорт упрощает поиск путей, на уровне файловой системы организует управление модульными библиотеками с многоуровневой вложенностью.

#  __main__ — Top-level script environment
https://docs.python.org/3/library/__main__.html

# Тестирование модулей

Модули в языке Python также являются объектами и имеют несколько полезных атрибутов. Вы можете использовать их, например, для тестирования.

## Прием с if __name__

    if __name__ == "__main__":

Выражение в инструкции if совсем не обязательно заключать в скобки. Во-вторых, заголовок инструкции закачивается двоеточием, после которого следует код, выделенный отступами.

Аналогично C, Python использует == для проверки равенства и = для присваивания. Но, в отличии от C, Python не поддерживает присваивание внутри выражения, поэтому исключена возможность случайного присваивания значения, когда имеется ввиду проверка на равенство.

Модули являются объектами и имеют атрибут __name__. Значение этого атрибута зависит от того, как используется модуль. Если вы импортируете модуль, атрибут __name__ равен имени файла без каталога и расширения. Но если вы запускаете модуль как отдельную программу, __name__ будет иметь специальное значение — __main__.

##  __name__ импортированного модуля

     import odbchelper
     odbchelper.__name__
     'odbchelper'

Зная об этом, вы можете определить код для тестирования модуля непосредственно в самом модуле. При непосредственном запуске модуля __name__ будет равен __main__, что приведет к выполнению теста. При импортировании же модуля __name__ будет иметь другое значение, и тест будет проигнорирован. Такой подход облегчает разработку и отладку новых модулей перед включением их в большую программу.

## main2.py
        from contact.contact import Contact
        class Main(object):
            def __init__(self):
                self.contacts_obj = []
                self.titles = (
                    'Select operation:',
                    "Usage operation:"
                    )
                self.choices = (
                    "Help",
                    'Print Phone Numbers',
                    'Add a Phone Number',
                    'Remove a Phone Number',
                    'Lookup a Phone Number',
                    'Save Phone Numbers',
                    "Quit"
                    )

            def add_contact(self, rec):
                '''
                Add a New Record To Phone Gap
                '''
                d = Contact(rec)
                self.contacts_obj.append(d)

            def load_contacts(self):
                lines = [line.rstrip('\n') for line in open("contacts.db")]
                for line in lines:
                    newRecord = line.split(':')
                    self.add_contact(newRecord)

            def print_contacts(self):
                for contact in self.contacts_obj:
                    print(contact)

            def save_contact(self, rec):
                fileHandler = open("contacts.db", 'a')
                fileHandler.write(':'.join(rec)+'\n')
                fileHandler.close()

            def makeList(self, prompt):
                raw = raw_input(prompt + ":> ")
                return newRecord.append(raw)

            def menu(self):
                tupleLen = [len(i) for i in self.choices]
                width = max(max(tupleLen), len(self.titles[0]))

                print 'phonegup'.upper().center(width+7, '=')
                self.printMenu(width, 0, self.choices)

                choiceList = [item[0].lower() for item in self.choices]
                choiceList = ' | '.join(choiceList)

                choice = raw_input("Enter choice "+choiceList+':>')
                return str(choice) if choice != '' else 'h'

            def printMenu(self, w, j, obj):
                gup = (': ', '| ')

                print("_"*(w+7))
                print(gup[1] + self.titles[j].ljust(w+3, ' ') + gup[1][::-1])

                for item in obj:
                    print(
                        gup[1] + item[0].lower() + gup[0] +
                        item.ljust(w, ' ') + gup[1][:: -1]
                        )

                print("="*(w+7))

            def myhelp(self):
                list1 = list()
                helpers = (
                    'Display this usage message',
                    'Print Phone Numbers',
                    'Add a Phone Number',
                    'Remove a Phone Number',
                    'Lookup a Phone Number',
                    'Save Phone Numbers',
                    'Exit programm'
                    )

                for i in range(len(helpers)):
                    list1.append(self.choices[i]+' - ' + helpers[i])

                listLen = [len(i) for i in list1]
                self.printMenu(max(listLen), 1, list1)


        def main():
            while True:
                app = Main()
                choice = app.menu()
                if choice == 'q':
                    print('{!s:#^40}'.format('Thankyou for using phoneGap.py!'))
                    break
                if choice == 'h':
                    app.myhelp()
                    continue
                if choice == 'p':
                    if len(app.contacts_obj) == 0:
                        app.load_contacts()
                    app.print_contacts()
                elif choice == 'a':
                    if len(app.contacts_obj) == 0:
                        app.load_contacts()
                    newRecord = []
                    tup1 = ("First Name", "Last Name", "Phone Number", 'Cell Phone', 'Town',  "Address", 'Age', 'Gender')
                    print("Add New Record To PhoneGap")
                    for prompt in tup1:
                        app.makeList(prompt)
                    app.add_contact(newRecord)
                    app.save_contact(newRecord)
                else:
                    continue


## phone2.py
        from main2 import main
        if __name__ == "__main__":
            main()

#   Обработка исключений

Обработка исключений поддерживается в Python посредством операторов try, except, else, finally, raise, образующих блок обработки исключения. В общем случае блок выглядит следующим образом:

            try:
                # Здесь код, который может вызвать исключение
                raise Exception("message")  
                        # Exception, это один из стандартных
                        # типов исключения (всего лишь класс),
                # может использоваться любой другой, в том числе свой

            except (Тип исключения1, Тип исключения2, …) as Переменная:
                # Код в блоке выполняется, если тип исключения
                # совпадает с одним из типов

                # (Тип исключения1, Тип исключения2, …)
                # или является наследником одного из этих типов.
                # Полученное исключение доступно в необязательной Переменной.

            except (Тип исключения3, Тип исключения4, …) as Переменная:
                # Количество блоков except не ограничено
                raise  # Сгенерировать исключение "поверх" полученного;
                         # без параметров - повторно сгенерировать полученное

            except:
                # Будет выполнено при любом исключении,
                # не обработанном типизированными блоками except

            else:
                # Код блока выполняется, если не было поймано исключений.

            finally:
                # Будет исполнено в любом случае, возможно после
                # соответствующего блока except или else

Совместное использование else, except и finally стало возможно только начиная с Python 2.5. Информация о текущем исключении всегда доступна через sys.exc_info(). Кроме значения исключения, Python также сохраняет состояние стека вплоть до точки возбуждения исключения — так называемый traceback.

В отличие от компилируемых языков программирования, в Python использование исключения не приводит к значительным накладным расходам (а зачастую даже позволяет ускорить исполнение программ) и очень широко используется. Исключения согласуются с философией Python (10-й пункт «дзена Python» — «Ошибки никогда не должны умалчиваться») и являются одним из средств поддержки «утиной типизации».

Иногда вместо явной обработки исключений удобнее использовать блок with (доступен, начиная с Python 2.5).


# функция main()

        """Описание модуля.

        Подробное описание использования.
        """
        import sys
        import getopt

        def main():
            # Разбираем аргументы командной строки
            try:
                opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
            except getopt.error, msg:
                print msg
                print "для справки используйте --help"
                sys.exit(2)
            # process options
            for o, a in opts:
                if o in ("-h", "--help"):
                    print __doc__
                    sys.exit(0)
            # Анализируем
            for arg in args:
                process(arg) # process() определен в другом месте

        if __name__ == "__main__":
            main()

Во первых, добавим дополнительный аргумент argv. Так, чтобы можно было вызывать функцию в интерактивном режиме:

    def main(argv=None):
        if argv is None:
            argv = sys.argv
            # и т.д. заменяя sys.argv на argv в getopt запросах

мы заполняем значения по умолчанию динамически. Это более гибко, чем:

    def main(argv=sys.argv):
        # и т.д.

Таким образом теперь мы можем изменить параметры вызова в любой момент времени.

Вызов sys.exit() закрывает сессию интерпретатора. Доработаем программу:

    if __name__ == "__main__":
        sys.exit(main())

Вызов sys.exit(main()) вернет результат функции.

Другое усовершенствование касается использования исключения Usage(), которое мы перехватываем в main:

        import sys
        import getopt

        class Usage(Exception):
            def __init__(self, msg):
                self.msg = msg

        def main(argv=None):
            if argv is None:
                argv = sys.argv
            try:
                try:
                    opts, args = getopt.getopt(argv[1:], "h", ["help"])
                except getopt.error, msg:
                     raise Usage(msg)
                # more code, unchanged
            except Usage, err:
                print >>sys.stderr, err.msg
                print >>sys.stderr, "for help use --help"
                return 2

        if __name__ == "__main__":
            sys.exit(main())

Теперь мы имеем единственную точку выхода из функции, что предпочтительнее множественных return 2. Это также облегчает повторный анализ параметров: raise Usage вызывается просто во вспомогательной функции.

Вы можете возразить, что можно перенести конструкцию try/except из main() в конец модуля (if __name__ == "__main__": ...). Но это привело бы к возникновению ошибки при вызове в интерактивном режиме интерпретатора.

Определите другое исключение (возможно Error), которое обрабатывается так же, как и Usage, но возвращает 1. Его можно применять для ожидаемых ошибок типа отказа открыть необходимые файлы. Не ситаксические ошибки командной строки, но ожидаемые ситуации. Т.к. traceback не очень дружественное средство в таких случаях.

Очень часто конструкция try .. . except ... finally используется для обработки ошибок, возникающих при работе с файлами.

## main5.py

        def read_data(self, filename):
            lines = []
            fh = None
            try:
                fh = io.open(filename, 'r', encoding='utf-8')
                for line in fh:
                    if line.rstrip('\n'):
                        lines.append(line)
            except (IOError, OSError) as err:
                print(err)
                return []
            finally:
                if fh is not None:
                    fh.close()
            return lines

        def load_contacts(self):
            lines = self.read_data(self.filename)
            for line in lines:
                newRecord = line.split(':')
                self.add_contact(newRecord)

Изначально функция записывает в переменную fh значение None, так как вполне возможно, что вызов функции ореп() потерпит неудачу, тогда переменной fh ничего не будет присвоено (и в ней останется значение None) и будет возбуждено исключение. Если возникнет одно из исключений, которые мы определили (lOError или OSError), обработчик выведет сообщение об ошибке и вернет пустой список. Но прежде, чем функция действительно вернет управление, будет выполнен блок finally и файл будет закрыт, если перед этим он был благополучно открыт. Обратите также внимание, что если возникнет ошибка, связанная с кодировкой символов, файл все равно будет закрыт, хотя функция не предусматривает обработку соответствующего исключения (ValueError). Если это произойдет, интерпретатор сначала выполнит блок finally, а затем передаст исключение вверх по стеку вызовов, при этом возвращаемое значение будет отброшено, так как функция завершится в результате необработанного исключения. А так как в данном примере нет соответствующего блока except, который обрабатывал бы ошибки, связанные с кодировкой, программа завершит свою работу с выводом диагностической информации.
Предложение except в данном примере можно было бы записать более кратко:

except EnvironmentError as err:
  print(err)
  return []

Этот прием будет работать, так как EnvironmentError является базовым классом как для класса lOError, так и для класса OSError.

        def write_data(self, filename, rec):
            lines = []
            fh = None
            try:
                fh = io.open(filename, 'a', encoding='utf-8')
                fh.write(unicode(':'.join(rec)+'\n', 'UTF-8'))
            except (IOError, OSError) as err:
                print(err)
                return []
            finally:
                if fh is not None:
                    fh.close()
            return lines

            def save_contact(self, rec):
                self.write_data(self.filename, rec)


# maib5.py

        import io
        from contact.contact import Contact


        class Main(object):
            def __init__(self):
                self.contacts_obj = []
                self.filename = "contacts.db"
                self.titles = (
                    'Select operation:',
                    "Usage operation:"
                    )
                self.choices = (
                    "Help",
                    'Print Phone Numbers',
                    'Add a Phone Number',
                    'Remove a Phone Number',
                    'Lookup a Phone Number',
                    'Save Phone Numbers',
                    "Quit"
                    )

            def add_contact(self, rec):
                '''
                Add a New Record To Phone Gap
                '''
                d = Contact(rec)
                self.contacts_obj.append(d)

            def read_data(self, filename):
                lines = []
                fh = None
                try:
                    # fh = open(filename, encoding='utf-8')
                    fh = io.open(filename, 'r', encoding='utf-8')
                    for line in fh:
                        if line.rstrip('\n'):
                            lines.append(line)
                except (IOError, OSError) as err:
                    print(err)
                    return []
                finally:
                    if fh is not None:
                        fh.close()
                return lines

            def write_data(self, filename, rec):
                lines = []
                fh = None
                try:
                    fh = io.open(filename, 'a', encoding='utf-8')
                    fh.write(unicode(':'.join(rec)+'\n', 'UTF-8'))
                except (IOError, OSError) as err:
                    print(err)
                    return []
                finally:
                    if fh is not None:
                        fh.close()
                return lines

            def load_contacts(self):
                # lines = [line.rstrip('\n') for line in open("contacts.db")]
                lines = self.read_data(self.filename)
                for line in lines:
                    newRecord = line.split(':')
                    self.add_contact(newRecord)

            def print_contacts(self):
                for contact in self.contacts_obj:
                    print(contact)

            def save_contact(self, rec):
                self.write_data(self.filename, rec)

            def makeList(self, prompt, newRecord):
                raw = raw_input(prompt + ":> ")
                return newRecord.append(raw)

            def menu(self):
                tupleLen = [len(i) for i in self.choices]
                width = max(max(tupleLen), len(self.titles[0]))

                print 'phonegap'.upper().center(width+7, '=')
                self.printMenu(width, 0, self.choices)

                choiceList = [item[0].lower() for item in self.choices]
                choiceList = ' | '.join(choiceList)

                choice = raw_input("Enter choice "+choiceList+':>')
                return str(choice) if choice != '' else 'h'

            def printMenu(self, w, j, obj):
                gup = (': ', '| ')

                print("_"*(w+7))
                print(gup[1] + self.titles[j].ljust(w+3, ' ') + gup[1][::-1])

                for item in obj:
                    print(
                        gup[1] + item[0].lower() + gup[0] +
                        item.ljust(w, ' ') + gup[1][:: -1]
                        )

                print("="*(w+7))

            def myhelp(self):
                '''
                'Display this usage message',
                'Print Phone Numbers',
                'Add a Phone Number',
                'Remove a Phone Number',
                'Lookup a Phone Number',
                'Save Phone Numbers',
                'Exit programm'
                '''

                list1 = list()
                helpers = (
                    'Display this usage message',
                    'Print Phone Numbers',
                    'Add a Phone Number',
                    'Remove a Phone Number',
                    'Lookup a Phone Number',
                    'Save Phone Numbers',
                    'Exit programm'
                    )

                for i in range(len(helpers)):
                    list1.append(self.choices[i]+' - ' + helpers[i])

                listLen = [len(i) for i in list1]
                self.printMenu(max(listLen), 1, list1)


        def runapp():
            while True:
                app = Main()

                choice = app.menu()

                if choice == 'q':
                    print('{!s:#^40}'.format('Thankyou for using phoneGap.py!'))
                    break
                if choice == 'h':
                    app.myhelp()
                    print app.myhelp.__doc__
                    continue
                if choice == 'p':
                    if len(app.contacts_obj) == 0:
                        app.load_contacts()
                    app.print_contacts()
                elif choice == 'a':
                    if len(app.contacts_obj) == 0:
                        app.load_contacts()
                    newRecord = []
                    tup1 = ("First Name", "Last Name", "Phone Number", 'Cell Phone', 'Town',  "Address", 'Age', 'Gender')

                    print("Add New Record To PhoneGap")
                    for prompt in tup1:
                        app.makeList(prompt, newRecord)
                    app.add_contact(newRecord)
                    app.save_contact(newRecord)
                else:
                    continue

        if __name__ == "__main__":
            runapp()

# phone5.py
        # -*- coding:utf-8 -*-
        """Описание модуля.

        Подробное описание использования.
        """
        import sys
        import getopt
        from main5 import runapp

        def main():
            # Разбираем аргументы командной строки
            try:
                opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
            except getopt.error, msg:
                print msg
                print "для справки используйте --help"
                sys.exit(2)
            # process options
            for o, a in opts:
                if o in ("-h", "--help"):
                    print __doc__
                    sys.exit(0)

            runapp()

        if __name__ == "__main__":
            main()
