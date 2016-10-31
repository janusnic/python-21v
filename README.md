# python-21v unit 10
# Принципы ООП
Согласно Алану Кэю — автору языка программирования Smalltalk — объектно-ориентированным может называться язык, построенный с учетом следующих принципов:

1. Все данные представляются объектами
2. Программа является набором взаимодействующих объектов, посылающих друг другу сообщения
3. Каждый объект имеет собственную часть памяти и может иметь в составе другие объекты
4. Каждый объект имеет тип
5. Объекты одного типа могут принимать одни и те же сообщения (и выполнять одни и те же действия)

# Объекты, типы и классы

Все данные в питоне — это объекты. Каждый объект имеет 2 специальных атрибута __class__ и __dict__.

Классы — это объекты, и у них тоже есть специальные атрибуты __class__ и __dict__.

__class__ — определяет класс или тип, экзмепляром которого является объект. Тип (или класс объекта) определяет его поведение; он есть у всех объектов, в том числе и встроенных. Тип и класс — это разные названия одного и того же. x.__class__ <==> type(x).

__dict__ словарь, дающий доступ к внутреннему пространству имен, он есть почти у всех объектов, у многих встроенных типов его нет.

## car0
        class Car(object):
            cars = 'A'

            def __init__(self, name):
                self.name = name

            def foo(self):
                print 'foo car'

        a = Car('Audi')
        # У a тоже есть __dict__ и __class__:
        print a.__dict__   # {'name': 'Audi'}
        print a.__class__  # <class '__main__.Car'>

        print type(a)  # <class '__main__.Car'>
        print a.__class__ is type(a)  # True

## Класс и тип — это одно и то же.

    a.__class__ is type(a) is Car #True

a.__dict__ — это словарь, в котором находятся внутренние (или специфичные для объекта) атрибуты, в данном случае 'name'. А в a.__class__ класс (тип).

И, например, в методах класса присваивание self.foo = bar практически идентично self.__dict__['foo'] = bar или сводится к аналогичному вызову.

В __dict__ объекта нет методов класса, дескрипторов, классовых переменных, свойств, статических методов класса, все они определяются динамически с помощью класса из __class__ атрибута, и являются специфичными именно для класса (типа) объекта, а не для самого объекта.

### Переопределим класс объекта a:

        class Bus(object):
            cars = 'B'

            def __init__(self):
                self.name = 'B object'

            def bar(self):
                print 'bar Bus'

        print a.__dict__  # {'name': 'Audi'}
        print a.foo()  # foo
        print a.__class__  # <class '__main__.Car'>
        a.__class__ = B
        print a.__class__  # <class '__main__.Bus'>

        # Смотрим, что поменялось.
        # Значение a.name осталось прежним,
        # т.е. __init__ не вызывался при смене класса.
        print a.__dict__  # {'name': 'Audi'}
        # Доступ к классовым переменным и методам «прошлого» класса Car пропал:
        # a.foo() Traceback (most recent call last): File "<stdin>", line 1, in
        #  <module> AttributeError: 'B' object has no attribute 'foo'

        # А вот классовые переменные и методы класса Bus доступы:
        print a.bar()  # bar
        print a.cars  # 'Bus'

        # Работа с атрибутам объекта: установка, удаление и поиск, равносильна
        # вызову встроенных функций settattr, delattr, getattr:

        a.x = 1
        print a.x
        setattr(a, 'x', 1)
        print a.x
        del a.x
        # print a.x
        # delattr(a, 'x')
        # print a.x
        # print a.x
        # getattr(a, 'x')

        # При этом стоит стоит понимать, что setattr и delattr
        # влияют и изменяют только
        # сам объект (точнее a.__dict__), и не изменяют класс объекта.
        # cars — является классовой переменной, т.е. она «принадлежит»
        # классу Bus, а не объекту a:

        print a.cars   # 'Bus'
        print a.__dict__  # {'name': 'Audi'}

Если мы попытаемся удалить этот атрибут, то получим ошибку, т.к. delattr будет пытаться удалить атрибут из a.__dict__

        delattr(a, 'cars')
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AttributeError: cars
        del a.cars
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AttributeError: qux
        a.cars
        'B'

        #  если мы попытаемся изменить (установить) атрибут, setattr поместит его в __dict__, специфичный для данного, конкретного объекта.
        b = Bus()
        print b.cars # 'B'
        a.cars = 'myB'
        print a.cars # 'myB'
        print a.__dict__ # {'cars': 'myB', 'name': 'a'}
        print b.cars # 'B'
        # Ну и раз есть 'qux' в __dict__ объекта, его можно удалить с помощью delattr:
        del a.cars
        # После удаления, a.qux будет возвращать значение классовой переменной:
        print a.cars # 'B'
        print a.__dict__ # {'name': 'a'}

класс для объекта — это значение специального атрибута __class__ и его можно менять.
почти каждый объект имеет свое пространство имен (атрибутов), доступ (не всегда полный), к которому осуществляется с помощью специального атрибута __dict__
класс фактичеки влияет только на поиск атрибутов, которых нет в __dict__, как-то: методы класса, дескрипторы, магические методы, классовые переменные и прочее.

## Объекты и классы

У класса тип type.

    A.__class__
    <type 'type'>

    # Правда __dict__ у классов не совсем словарь
    print A.__dict__ # <dictproxy object at 0x1111e88>

    # __dict__ ответственен за доступ к внутреннему пространству имен, в котором хранятся методы, дескрипторы, переменные, свойства и прочее:

    print dict(A.__dict__) # {'__module__': '__main__', 'qux': 'A', '__dict__': <attribute '__dict__' of 'A' objects>, 'foo': <function foo at 0x7f7797a25c08>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

    print A.__dict__.keys() # ['__module__', 'qux', '__dict__', 'foo', '__weakref__', '__doc__']<

В классах помимо __class__ и __dict__, имеется еще несколько специальных атрибутов: __bases__ — список прямых родителей, __name__ — имя класса.

Классы можно считать расширениями обычных объектов, которые реализуют интерфейс типа. Множество всех классов (или типов) принадлежат множеству всех объектов, а точнее является его подмножеством. Иначе говоря, любой класс является объектом, но не всякий объект является классом. Договоримся называть обычными объектами(regular objects) те объекты, которые классами не являются.

## Класс является объектом.
        class A(object):
            pass
        print isinstance(A, object) # True

        # Число — это тоже объект.
        print isinstance(42, object) # True

        # Класс — это класс (т.е. тип).
        print isinstance(A, type) # True

        # А вот число классом (типом) не является. (Что такое type будет пояснено позже)
        print isinstance(42, type) # False

        # Ну и a — тоже обычный объект.
        a = A()
        print isinstance(a, A) # True
        print isinstance(a, object) # True
        print isinstance(a, type) # False

        # И у A всего один прямой родительский класс — object.
        print A.__bases__ # (<type 'object'>,)

        # Часть специальных параметров можно даже менять:
        print A.__name__ # 'A'
        A.__name__ = 'B'
        print A # <class '__main__.B'>

        # С помощью getattr получаем доступ к атрибутам класса:
        # print A.qux # 'A'
        # print A.foo # <unbound method A.foo>

## Поиск атрибутов в обычном объекте
В первом приближении алгоритм поиска выглядит так: сначала ищется в __dict__ объекта, потом идет поиск по __dict__ словарям класса объекта (который определяется с помощью __class__) и __dict__ его базовых классов в рекурсивном порядке.

    class A(object):
        qux = 'A'
        def __init__(self, name):
            self.name=name
        def foo(self):
            print 'foo'

    a = A()
    b = A()

Т.к. в обычных объектах a и b нет в __dict__ атрибута 'qux', то поиск продолжается во внутреннем словаре __dict__ их типа (класса), а потом по __dict__ словарям родителей в определенном порядке:
    b.qux
    'A'
    A.qux
    'A'
Меняем атрибут qux у класса A. И соответственно должны поменяться значения, которые возвращают экземпляры класса A — a и b:
    A.qux='B'
    a.qux
    'B'
    b.qux
    'B'

Точно так же в рантайме к классу можно добавить метод:

    A.quux = lambda self: 'i have quux method'
    A.__dict__['quux']
    <function <lambda> at 0x7f7797a25b90>
    A.quux
    <unbound method A.<lambda>>

И доступ к нему появится у экземпляров:

    a.quux()
    'i have quux method'

Точно так же как и с любыми другими объектами, можно удалить атрибут класса, например, классовую переменную qux:

    del A.qux

Она удалиться из __dict__

    A.__dict__['qux']
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 'qux'

И доступ у экземляров пропадет.

    a.qux
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'A' object has no attribute 'qux'

У классов почти такой же поиск атрибутов, как и у обычных объектов, но есть отличия: поиск начинается с собственного __dict__ словаря, а потом идет поиск по __dict__ словарям суперклассов (которые хранятся в __bases__) по опредленному алгоритму, а затем по классу в __class__ и его суперклассах.

## Переменная self
Внутри конструктора __init__ аргумент self это переменная, содержащая создаваемый экземпляр. Когда мы пишем

    class Car(object):

        wheels = 4
        def __init__(self, make, model):
            self.make = make
            self.model = model

    mustang = Car('Ford', 'Mustang')
    print mustang.wheels
    # 4
    print Car.wheels

мы определяем два новых атрибута в этом экземпляре. Записывая mustang = Car('Ford', 'Mustang') мы не только передаем make, model, но и имя экземпляра, то есть этот вызов можно представить как

    Car.__init__(mustang, 'Ford', 'Mustang')

Когда мы пишем в теле конструктора self.model = model, мы в действительности инициализируем mustang.model.

## Правила касательно self следующие:
- Любой метод класса содержит self в качестве первого аргумента.
- self представляет в своем лице (произвольный) экземпляр класса.
- Другой метод или атрибут класса используют self в виде self.name, где name имя этого атрибута или метода.
- self в качестве аргумента пропускается при вызове методов класса

## Инкапсуляция и доступ к свойствам
Все значения в Python являются объектами, инкапсулирующими код (методы) и данные и предоставляющими пользователям общедоступный интерфейс. Методы и данные объекта доступны через его атрибуты.

## Сокрытие информации о внутреннем устройстве объекта
Сокрытие информации о внутреннем устройстве объекта выполняется в Python на уровне соглашения между программистами о том, какие атрибуты относятся к общедоступному интерфейсу класса, а какие — к его внутренней реализации. Одиночное подчеркивание в начале имени атрибута говорит о том, что метод не предназначен для использования вне методов класса (или вне функций и классов модуля), однако, атрибут все-таки доступен по этому имени. Два подчеркивания в начале имени дают несколько большую защиту: атрибут перестает быть доступен по этому имени.

Особым случаем является наличие двух подчеркиваний в начале и в конце имени атрибута. Они используются для специальных свойств и функций класса (например, для перегрузки операции). Такие атрибуты доступны по своему имени, но их использование зарезервировано для специальных атрибутов, изменяющих поведение объекта.

## Доступ к атрибуту

может быть прямой:

    class Y:
        """The  vertical  motion  of  a  ball."""

        def __init__(self, v0):
            self.v0 = v0 # атрибут получает значение в конструкторе
            self.g = 9.81

    a = Y(5)
    print a.v0
    a.v0 = 5

Доступ к атрибуту с использованием свойств с заданными методами для получения, установки и удаления атрибута:

    class Y:
        """The  vertical  motion  of  a  ball."""

        def __init__(self, v0):
            self.v0 = v0 # атрибут получает значение в конструкторе
            self.g = 9.81

        def getv0(self):                 # метод для получения значения
            return self._v0

        def setv0(self, value):          # присваивания нового значения
            self._v0 = value

        def delv0(self):                 # удаления атрибута
            del self._v0                 

        v0 = property(getv0, setv0, delv0, "Свойство v0")    # определяем v0 как свойство

    a = Y(5)      
    print a.v0      # Синтаксис доступа к атрибуту при этом прежний
    a.v0 = 5 #_


## Строки документации

Классы, как и функции, могут быть описаны простым человеческим языком сразу в следующей строке после заголовка с помощью doc strings — строк документации. Вводятся они абсолютно таким же образом, с помощью тройки двойных кавычек с каждой стороны:

    class Y:
        """The vertical motion of a ball."""

        def __init__(self, v0):
            ...

В случае объемного конечного продукта обычно пишут более исчерпывающее объяснение о том как этот класс может быть использован, какие методы и атрибуты включает, примеры использования класса 9.py:

    class Y:
        """Mathematical function for the vertical motion of a ball.

        Methods:
            constructor(v0): set initial velocity v0.
            value(t): compute the height as function of t.
            formula(): print out the formula for the height.

        Attributes:
            v0: the initial velocity of the ball (time 0).
            g: acceleration of gravity (fixed).

        Usage:
        >>> y  =  Y(3)
        >>> position1 = y.value(0.1)
        >>> position2 = y.value(0.3)
        >>> print  y.formula()
        v0*t - 0.5*g*t**2; v0=3
        """

Классы (типы) — это объектные фабрики. Их главная задача — создавать объекты, обладающие определенным поведением.

Классы определяют поведение объектов с помощью своих атрибутов (которые хранятся в __dict__ класса): методов, свойств, классовых переменные, дескрипторов, а также с помощью атрибутов, унаследованных от родительских классов.

Инстанцирование обычного объекта происходит в 2 этапа: сначала его создание, потом инициализация. Соответственно, сначала запускается метод класса __new__, который возвращает объект данного класса, потом выполняется метод класса __init__, который инициализирует уже созданный объект.

def __new__(cls, ...) — статический метод (но его можно таковым не объявлять), который создает объект класса cls.

def __init__(self, ...) — метод класса, который инициализирует созданный объект.

# Статические методы

Статические методы в Python являются синтаксическими аналогами статических функций в основных языках программирования. Они не получают ни экземпляр (self), ни класс (cls) первым параметром. Для создания статического метода (только «новые» классы могут иметь статические методы) используется декоратор staticmethod

    class Car(object):

        wheels = 4
        def __init__(self, make, model):
            self.make = make
            self.model = model

        @staticmethod
        def test(x):
            return x == 0


    Car.test(1)    # доступ к статическому методу можно получать и через класс
    False
    f = Car()
    f.test(0)    # и через экземпляр класса
    True

Статические методы реализованы с помощью свойств (property).

# Static Methods car2
    class Car(object):

        wheels = 4

        #Static Methods
        @staticmethod
        def make_car_sound():
            print 'VRooooommmm!'


        def __init__(self, make, model):
            self.make = make
            self.model = model


    mustang = Car('Ford', 'Mustang')
    print mustang.wheels
    # 4
    print Car.wheels
    # 4
    mustang.make_car_sound()
    Car.make_car_sound()


## Метод класса

Классовые методы в Python занимают промежуточное положение между статическими и обычными. В то время как обычные методы получают первым параметром экземпляр класса, а статические не получают ничего, в классовые методы передается класс. Возможность создания классовых методов является одним из следствий того, что в Python классы также являются объектами. Для создания классового (только «новые» классы могут иметь классовые методы) метода можно использовать декоратор classmethod

# Static Methods car3
    class Car(object):

        wheels = 4

        #Static Methods
        @staticmethod
        def make_car_sound():
            print 'VRooooommmm!'

        # Class Methods
        @classmethod
        def is_motorcycle(cls):
            return cls.wheels == 2

        def __init__(self, make, model):
            self.make = make
            self.model = model


    mustang = Car('Ford', 'Mustang')
    print mustang.wheels
    # 4
    print Car.wheels
    # 4
    mustang.make_car_sound()
    Car.make_car_sound()

    if mustang.is_motorcycle():
        print 'it is not a car'
    else:
        print 'mustang is a car'

Классовые методы достаточно часто используются для перегрузки конструктора. Классовые методы, как и статические, реализуются через свойства (property).

## car4.py
    class Car(object):
        """A car for sale by Jeffco Car Dealership.

        Attributes:
            wheels: An integer representing the number of wheels the car has.
            miles: The integral number of miles driven on the car.
            make: The make of the car as a string.
            model: The model of the car as a string.
            year: The integral year the car was built.
            sold_on: The date the vehicle was sold.
        """

        def __init__(self, wheels, miles, make, model, year, sold_on):
            """Return a new Car object."""
            self.wheels = wheels
            self.miles = miles
            self.make = make
            self.model = model
            self.year = year
            self.sold_on = sold_on

        def sale_price(self):
            """Return the sale price for this car as a float amount."""
            if self.sold_on is not None:
                return 0.0  # Already sold
            return 5000.0 * self.wheels

        def purchase_price(self):
            """Return the price for which we would pay to purchase the car."""
            if self.sold_on is None:
                return 0.0  # Not yet sold
            return 8000 - (.10 * self.miles)

    class Truck(object):
        """A truck for sale by Jeffco Car Dealership.

        Attributes:
            wheels: An integer representing the number of wheels the truck has.
            miles: The integral number of miles driven on the truck.
            make: The make of the truck as a string.
            model: The model of the truck as a string.
            year: The integral year the truck was built.
            sold_on: The date the vehicle was sold.
        """

        def __init__(self, wheels, miles, make, model, year, sold_on):
            """Return a new Truck object."""
            self.wheels = wheels
            self.miles = miles
            self.make = make
            self.model = model
            self.year = year
            self.sold_on = sold_on

        def sale_price(self):
            """Return the sale price for this truck as a float amount."""
            if self.sold_on is not None:
                return 0.0  # Already sold
            return 5000.0 * self.wheels

        def purchase_price(self):
            """Return the price for which we would pay to purchase the truck."""
            if self.sold_on is None:
                return 0.0  # Not yet sold
            return 10000 - (.10 * self.miles)

    v = Car(4,10000,'Ford','Rodeo',2014,1)
    print v.purchase_price()

    t = Truck(4,10000,'Honda','Accord',2014,1)
    print t.purchase_price()


## Наследование
Python поддерживает как одиночное наследование, так и множественное, позволяющее классу быть производным от любого количества базовых классов.

    class Car(object):                # наследуем один базовый класс - object
            def name1(self): return 'Car'
    class Truck(object):
            def name2(self): return 'Truck'
    class Child(Car, Truck):           # создадим класс, наследующий Car, Truck (и, опосредованно, object)
            pass
    x = Child()
    x.name1(), x.name2()               # экземпляру Child доступны методы из Car и Truck
    'Par1','Par2'

## одиночное наследование car5.py
    class Vehicle(object):
        """A vehicle for sale by Jeffco Car Dealership.

        Attributes:
            wheels: An integer representing the number of wheels the vehicle has.
            miles: The integral number of miles driven on the vehicle.
            make: The make of the vehicle as a string.
            model: The model of the vehicle as a string.
            year: The integral year the vehicle was built.
            sold_on: The date the vehicle was sold.
        """

        base_sale_price = 0

        def __init__(self, wheels, miles, make, model, year, sold_on):
            """Return a new Vehicle object."""
            self.wheels = wheels
            self.miles = miles
            self.make = make
            self.model = model
            self.year = year
            self.sold_on = sold_on


        def sale_price(self):
            """Return the sale price for this vehicle as a float amount."""
            if self.sold_on is not None:
                return 0.0  # Already sold
            return 5000.0 * self.wheels

        def purchase_price(self):
            """Return the price for which we would pay to purchase the vehicle."""
            if self.sold_on is None:
                return 0.0  # Not yet sold
            return self.base_sale_price - (.10 * self.miles)

    class Car(Vehicle):

        def __init__(self, wheels, miles, make, model, year, sold_on):
            """Return a new Car object."""
            self.wheels = wheels
            self.miles = miles
            self.make = make
            self.model = model
            self.year = year
            self.sold_on = sold_on
            self.base_sale_price = 8000


    class Truck(Vehicle):

        def __init__(self, wheels, miles, make, model, year, sold_on):
            """Return a new Truck object."""
            self.wheels = wheels
            self.miles = miles
            self.make = make
            self.model = model
            self.year = year
            self.sold_on = sold_on
            self.base_sale_price = 10000

    v = Car(4,10000,'Ford','Rodeo',2014,1)
    print v.purchase_price()

    t = Truck(4,10000,'Honda','Accord',2014,1)
    print t.purchase_price()


Начиная с версии языка 2.6 в стандартную библиотеку включается модуль abc, добавляющий в язык абстрактные базовые классы

позволяют определить класс, указав при этом, какие методы или свойства обязательно переопределить в классах-наследниках:

        @abstractmethod
        def vehicle_type():
            """"Return a string representing the type of vehicle this is."""
            pass

        @abstractproperty
            def speed():
            """Скорость объекта"""

## car6.py
    from abc import ABCMeta, abstractmethod
    class Vehicle(object):
        """A vehicle for sale by Jeffco Car Dealership.

        Attributes:
            wheels: An integer representing the number of wheels the vehicle has.
            miles: The integral number of miles driven on the vehicle.
            make: The make of the vehicle as a string.
            model: The model of the vehicle as a string.
            year: The integral year the vehicle was built.
            sold_on: The date the vehicle was sold.
        """

        __metaclass__ = ABCMeta

        base_sale_price = 0

        def sale_price(self):
            """Return the sale price for this vehicle as a float amount."""
            if self.sold_on is not None:
                return 0.0  # Already sold
            return 5000.0 * self.wheels

        def purchase_price(self):
            """Return the price for which we would pay to purchase the vehicle."""
            if self.sold_on is None:
                return 0.0  # Not yet sold
            return self.base_sale_price - (.10 * self.miles)

        @abstractmethod
        def vehicle_type():
            """"Return a string representing the type of vehicle this is."""
            pass

        @abstractproperty
            def speed():
            """Скорость объекта"""

    class Car(Vehicle):

        def __init__(self, wheels, miles, make, model, year, sold_on):
            """Return a new Car object."""
            self.wheels = wheels
            self.miles = miles
            self.make = make
            self.model = model
            self.year = year
            self.sold_on = sold_on
            self.base_sale_price = 8000

        def vehicle_type(self):
            """"Return a string representing the type of vehicle this is."""
            return 'car'


    class Truck(Vehicle):

        def __init__(self, wheels, miles, make, model, year, sold_on):
            """Return a new Truck object."""
            self.wheels = wheels
            self.miles = miles
            self.make = make
            self.model = model
            self.year = year
            self.sold_on = sold_on
            self.base_sale_price = 10000

        def vehicle_type(self):
            """"Return a string representing the type of vehicle this is."""
            return 'truck'

    v = Car(4,10000,'Ford','Rodeo',2014,1)
    print v.purchase_price()

    t = Truck(4,10000,'Honda','Accord',2014,1)
    print t.purchase_price()


## app0
        # -*- coding:utf-8 -*-
        # ---------- Cars Shop ----------
        '''
         Program make a simple Cars Shop
        '''
        # импортирование модулей python
        try:
            # for Python2
            from Tkinter import *   # notice capitalized T in Tkinter
            import tkFont
            import tkMessageBox
        except ImportError:
            # for Python3
            from tkinter import *   # notice lowercase 't' in tkinter here
            from tkinter import font
            from tkinter import messagebox


        class Application(Frame):

            def __init__(self, master=None):
                Frame.__init__(self, master)
                self._init_gridbox()

            def _init_gridbox(self):
                for i in range(5):
                    for j in range(4):
                        l = Label(text='%d.%d' % (i, j), relief=RIDGE)
                        l.grid(row=i, column=j, sticky=NSEW)

            def about(self):
                tkMessageBox.showinfo("Old Cars Shop", "Old Cars Shop")


        def main():
            # Создать приложение
            app = Application()
            # Вызов методов класса менеджера окон (Wm)
            app.master.title("Old Cars Shop")
            app.master.maxsize(1000, 400)
            # Запуск программы
            app.mainloop()


        if __name__ == '__main__':
            main()

## app1

        def _init_gridbox(self):
            for i in range(5):
                cols = []
                for j in range(4):
                    e = Entry(relief=RIDGE)
                    e.grid(row=i, column=j, sticky=NSEW)
                    e.insert(END, '%d.%d' % (i, j))

## app2

        def _init_gridbox(self):
            for j in range(4):
                l = Label(text='%d.%d' % (0, j), relief=RIDGE)
                l.grid(row=0, column=j, sticky=NSEW)
            for i in range(5):
                cols = []
                for j in range(4):
                    e = Entry(relief=RIDGE)
                    e.grid(row=i+1, column=j, sticky=NSEW)
                    e.insert(END, '%d.%d' % (i+1, j))

## app3
        def _init_gridbox(self):
            labels = ('make', 'model', 'year', 'wheels', 'mileage', 'sold_on')
            data = [
                ('Ford', 'Rodeo', 2014, 4, 10000, 1),
                ('Toyota', 'Camry CE (Classic Edition)', 2011, 4, 17000, 0),
                ('Toyota', 'Camry LE (Luxury Edition)', 2013, 4, 20000, 1),
                ('Toyota', 'Camry', 2000, 4, 12000, 0),
                ('Ford', 'Rodeo', 2014, 4, 10000, 0),
              ]
            j = 0
            for txt in labels:
                l = Label(text='%s' % txt, relief=RIDGE)
                l.grid(row=0, column=j, sticky=NSEW)
                j += 1

            for i in range(len(data)):
                cols = []
                j = 0
                for d in data[i]:
                    e = Entry(relief=RIDGE)
                    e.grid(row=i+1, column=j, sticky=NSEW)
                    e.insert(END, d)
                    j += 1
