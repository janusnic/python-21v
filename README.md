# python-21v unit 06
# ООП - Object Oriented Programming

В объектно-ориентированных языках программирования вы можете определить классы, которые соединяют связанные между собой данные и модели поведения. Классы могут наследовать некоторые или все характеристики от родительских классов, но в них могут также определяться собственные атрибуты (данные) и методы (модели поведения). В конечном счете классы обычно служат шаблонами для создания экземпляров (иногда также называемых просто объектами). Как правило, в различных экземплярах одного класса содержатся различные данные, но все они находятся в одной форме - например, у обоих объектов сотрудников Employee bob и jane есть заработная плата .salary и комната .room_number, но величина заработной платы и номер комнаты у них различаются.

# Определение класса.

Класс - разновидность абстрактного типа данных в объектно-ориентированном программировании. При использовании классов все элементы кода программы, такие, как переменные, константы, методы, процедуры и функции, могут принадлежать (а во многих языках обязаны принадлежать) тому или иному классу. Сам класс в итоге определяется как список своих членов, а именно полей(свойств) и методов/функций/процедур.

# Пример класса в Python.

    class Contact(object):
        pass

## Demonstrates a basic class and object

               class Contact(object):
                   """A virtual pet"""
                   def talk(self):
                       print "Hi.  I'm an instance of class Contact."

               # main
               crit = Contact()
               crit.talk()


##  "Старые" и "новые" классы:

Обратим внимание на инструкцию OurClass(object). Если вы не хотите определить этот класс как наследованный от какого-то другого класса, то его нужно определить как наследованный от object. Также можно наследовать встроенные классы и классы из модулей расширения. Эта особенность появилась начиная с Python 2.2, классы, наследованные от object или других классов, называются "новыми классами".

До сих пор в коде библиотек Python можно встретить и классы старого образца, которые определяются так:

       class Contact:
           ...

       Они еще работают, но уже помечены как deprecated.


## Метод __init__()

Метод __init__() вызывается сразу же после создания экземпляра класса. Он напоминает конструктор класса в других языках программирования, и является первым блоком кода, который исполняется в контексте только что созданного экземпляра класса, но на момент вызова __init__() объект уже является созданным, и можно оперировать ссылкой на него - self.

Первым аргументом любого метода класса, включая __init__() всегда является ссылка на текущий экземпляр класса. Принято называть этот аргумент self. При вызове метода self указывать не надо, Python добавит его автоматически:

    c = OurClass('1', '2')
    c.print_args()
    >>1
    >>2

# Пример класса в Python.

    class Contact(object):

       def __init___(self,arg1,arg2)
           self.arg1 = arg1
           self.arg2 = arg2

       def print_args(self):
           print self.arg1
           print self.arg2

## Building the address book with classes
           class Contact(object):
               '''
               Building the address book with classes
               '''

                def __init__ (self, first_name, last_name, phone, cell_phone, town, address, age, gender):
                    self.first_name   = first_name
                    self.last_name   = last_name
                    self.phone   = phone
                    self.cell_phone   = cell_phone
                    self.town   = town
                    self.address   = address
                    self.age    = age
                    self.gender = gender

           s = Contact("Your Name", "Your Lasy Name", '1234567', '050 2345678', 'Kyiv', 'Foo st., 123', 20, "f")
           print s

           print s.age

##  Generates a class attribute

        class Contact(object):
            '''
            Building the address book with classes
            '''
            def __init__(self, first_name='', last_name='', phone=None,
                         cell_phone=None, town='Kyiv', address='', age=None, gender=None):
                self.first_name = first_name
                self.last_name = last_name
                self.phone = phone
                self.cell_phone = cell_phone
                self.town = town
                self.address = address
                self.age = age
                self.gender = gender

        x = Contact()                  # make 2 instances
        y = Contact()
        print x.town, y.town         # they inherit and share town

        Contact.town = 'Lviv'
        print x.town, y.town, Contact.town

        x.town = 'Dnipro'
        print x.town, y.town, Contact.town

## 3 Demonstrates get and set methods and properties

        class Contact(object):
            '''
            Building the address book with classes
            '''
            def __init__(
                self,
                first_name='', last_name='',
                phone=None, cell_phone=None,
                town='Kyiv', address='',
                age=None, gender=None
            ):
                self.first_name = first_name
                self.last_name = last_name
                self.phone = phone
                self.cell_phone = cell_phone
                self.town = town
                self.address = address
                self.age = age
                self.gender = gender

            def getFirstName(self):
                return self.first_name

            def setFirstName(self, first_name):
                self.first_name = first_name

            def getLastName(self):
                return self.last_name

            def setLastName(self, last_name):
                self.last_name = last_name

            def getPhone(self):
                return self.phone

            def setPhone(self, phone):
                self.phone = phone

            def getCellPhone(self):
                return self.cell_phone

            def setCellPhone(self, cell_phone):
                self.cell_phone = cell_phone

            def getTown(self):
                return self.town

            def setTown(self, town):
                self.town = town


        c1 = Contact(first_name="Alexander", last_name="Coder")
        c1.setPhone("5551763")
        c1.setTown("Kingston")
        print("c1: {0}".format(c1))
        c2 = Contact(first_name="Michael", cell_phone=5559955)
        print("c2: {0}".format(c2))

### python contact3.py

        c1: <__main__.Contact object at 0x7f6d8996fd90>
        c2: <__main__.Contact object at 0x7f6d8996fe90>

## method def __str__(self)

        def __str__(self):
            st = "{0} {1}".format(self.first_name, self.last_name)
            if self.phone is not None:
                st = "{0}\nPhone: {1}".format(st, self.phone)
            if self.cell_phone is not None:
                st = "{0}\nCell: {1}".format(st, self.cell_phone)
            if self.town != "":
                st = "{0}\nTown: {1}".format(st, self.town)
            return st
### python contact4.py
                c1: Alexander Coder
                Phone: 5551763
                Town: Kingston
                c2: Michael
                Cell: 5559955
                Town: Kyiv

                def getPhone(self):
                    if self.phone is None:
                        return None
                    st = str(self.phone)
                    return '{0}-{1}'.format(st[0:3], st[3:])

                    def __str__(self):
                        st = "{0} {1}".format(self.getFirstName(), self.getLastName())
                        if self.getPhone() is not None:
                            st = "{0}\nPhone: {1}".format(st, self.getPhone())
                        if self.cell_phone is not None:
                            st = "{0}\nCell: {1}".format(st, self.cell_phone)
                        if self.town != "":
                            st = "{0}\nTown: {1}".format(st, self.town)
                        return st

### python contact4.py
        c1: Alexander Coder
        Phone: 555-1763
        Town: Kingston
        c2: Michael
        Cell: 5559955
        Town: Kyiv

## 5 contacts_obj
        contacts_obj = [
            Contact(first_name="Alexander", last_name="Coder", phone=5551763, town="Kingston"),
            Contact(first_name="Michael", cell_phone=5559955),
            Contact(first_name="Elaine", last_name="Benes"),
            Contact(first_name="Tobias", town="Newport Beach"),
        ]

        for contact in contacts_obj:
            print(contact)


## contact6.py

        class Contact(object):
            '''
            Building the address book with classes
            '''
            def __init__(self, first_name='', last_name='', phone=None, cell_phone=None,  town='', address='', age=None, gender=None):
                self.first_name = first_name
                self.last_name = last_name
                self.phone = phone
                self.cell_phone = cell_phone
                self.town = town
                self.address = address
                self.age = age
                self.gender = gender

            def getFirstName(self):
                return self.first_name

            def setFirstName(self, first_name):
                self.first_name = first_name

            def getLastName(self):
                return self.last_name

            def setLastName(self, last_name):
                self.last_name = last_name

            def getPhone(self):
                if self.phone is None:
                    return None
                st = str(self.phone)
                return '{0}-{1}'.format(st[0:3], st[3:])

            def setPhone(self, phone):
                self.phone = phone

            def getCellPhone(self):
                return self.cell_phone

            def setCellPhone(self, cell_phone):
                self.cell_phone = cell_phone

            def getTown(self):
                return self.town

            def setTown(self, town):
                self.town = town

            def __str__(self):
                st = "{0} {1}".format(self.getFirstName(), self.getLastName())
                if self.getPhone() is not None:
                    st = "{0}\nPhone: {1}".format(st, self.getPhone())
                if self.getCellPhone() is not None:
                    st = "{0}\nCell: {1}".format(st, self.getCellPhone())
                if self.getTown() != "":
                    st = "{0}\nTown: {1}".format(st, self.getTown())
                return st


        lookup = (
            'first_name',
            'last_name',
            'phone',
            'cell_phone',
            'town',
            'address',
            'age',
            'gender'
        )

        contacts_obj = []


        def add_contact(rec):

            d = Contact()
            for (p, v) in zip(lookup, rec):
                setattr(d, p, v)

            contacts_obj.append(d)


        def load_contacts():
            lines = [line.rstrip('\n') for line in open("contacts.db")]
            for line in lines:
                newRecord = line.split(':')
                add_contact(newRecord)

        load_contacts()
        for contact in contacts_obj:
            print(contact)

## contact7.py

        class Contact(object):
            '''
            Building the address book with classes
            '''
            def __init__(self, *args):
                self.first_name = args[0][0]
                self.last_name = args[0][1]
                self.phone = args[0][2]
                self.cell_phone = args[0][3]
                self.town = args[0][4]
                self.address = args[0][5]
                self.age = args[0][6]
                self.gender = args[0][7]

            def getFirstName(self):
                return self.first_name

            def setFirstName(self, first_name):
                self.first_name = first_name

            def getLastName(self):
                return self.last_name

            def setLastName(self, last_name):
                self.last_name = last_name

            def getPhone(self):
                if self.phone is None:
                    return None
                st = str(self.phone)
                return '{0}-{1}'.format(st[0:3], st[3:])

            def setPhone(self, phone):
                self.phone = phone

            def getCellPhone(self):
                return self.cell_phone

            def setCellPhone(self, cell_phone):
                self.cell_phone = cell_phone

            def getTown(self):
                return self.town

            def setTown(self, town):
                self.town = town

            def __str__(self):
                st = "{0} {1}".format(self.getFirstName(), self.getLastName())
                if self.getPhone() is not None:
                    st = "{0}\nPhone: {1}".format(st, self.getPhone())
                if self.getCellPhone() is not None:
                    st = "{0}\nCell: {1}".format(st, self.getCellPhone())
                if self.getTown() != "":
                    st = "{0}\nTown: {1}".format(st, self.getTown())
                return st


        lookup = (
            'first_name',
            'last_name',
            'phone',
            'cell_phone',
            'town',
            'address',
            'age',
            'gender'
        )

        contacts_obj = []

        def add_contact(rec):
            d = Contact(rec)
            contacts_obj.append(d)


        def load_contacts():
            lines = [line.rstrip('\n') for line in open("contacts.db")]
            for line in lines:
                newRecord = line.split(':')
                add_contact(newRecord)

        load_contacts()
        for contact in contacts_obj:
            print(contact)


## contact8.py

        contacts_obj = []

        def add_contact(rec):
            d = Contact(rec)
            contacts_obj.append(d)

        def load_contacts():
            lines = [line.rstrip('\n') for line in open("contacts.db")]
            for line in lines:
                newRecord = line.split(':')
                add_contact(newRecord)

        def print_contacts():
            for contact in contacts_obj:
                print(contact)

        def save_contact(rec):
            fileHandler = open("contacts.db", 'a')
            fileHandler.write(':'.join(rec)+'\n')
            fileHandler.close()

        def makeList(prompt):
            raw = raw_input(prompt + ":> ")
            return newRecord.append(raw)

        titles = (
            'Select operation:',
            "Usage operation:"
            )

        choices = (
            "Help",
            'Print Phone Numbers',
            'Add a Phone Number',
            'Remove a Phone Number',
            'Lookup a Phone Number',
            'Save Phone Numbers',
            "Quit"
            )

        helpers = (
            'Display this usage message',
            'Print Phone Numbers',
            'Add a Phone Number',
            'Remove a Phone Number',
            'Lookup a Phone Number',
            'Save Phone Numbers',
            'Exit programm'
            )

        def printMenu(w, j, obj):
            gup = (': ', '| ')

            print("_"*(w+7))
            print(gup[1] + titles[j].ljust(w+3, ' ') + gup[1][::-1])

            for item in obj:
                print(
                    gup[1] + item[0].lower() + gup[0] +
                    item.ljust(w, ' ') + gup[1][:: -1]
                    )

            print("="*(w+7))


        def menu():
            tupleLen = [len(i) for i in choices]
            width = max(max(tupleLen), len(titles[0]))

            print 'phonegup'.upper().center(width+7, '=')
            printMenu(width, 0, choices)

            choiceList = [item[0].lower() for item in choices]
            choiceList = ' | '.join(choiceList)

            choice = raw_input("Enter choice "+choiceList+':>')
            return str(choice) if choice != '' else 'h'


        def myhelp():
            list1 = list()
            for i in range(len(helpers)):
                list1.append(choices[i]+' - ' + helpers[i])

            listLen = [len(i) for i in list1]
            printMenu(max(listLen), 1, list1)

        while True:
            choice = menu()

            if choice == 'q':
                print('{!s:#^40}'.format('Thankyou for using phoneGap.py!'))
                break
            if choice == 'h':
                myhelp()
                continue
            if choice == 'p':
                if len(contacts_obj) == 0:
                    load_contacts()
                print_contacts()
            elif choice == 'a':
                if len(contacts_obj) == 0:
                    load_contacts()
                newRecord = []
                tup1 = ("First Name", "Last Name", "Phone Number", 'Cell Phone', 'Town',  "Address", 'Age', 'Gender')

                print("Add New Record To PhoneGap")
                for prompt in tup1:
                    makeList(prompt)
                add_contact(newRecord)
                save_contact(newRecord)
            else:
                continue


## contact9.py

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


В языке Python реализовано автоматическое управление памятью, поэтому деструктор требуется достаточно редко. Вот пример класса с деструктором:

    class Line(object):
         def __init__(self, p1, p2):
              self.line = (p1, p2)
         def __del__(self):
              print "Удаляется линия %s - %s" % self.line
