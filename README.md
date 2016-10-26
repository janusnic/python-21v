# python-21v unit 10
# Python Namespace and Scope
## Python Namespace and scope of a variable

If you have ever read 'The Zen of Python' (type "import this" in Python interpreter), the last line states, Namespaces are one honking great idea -- let's do more of those! So what are these mysterious namespaces? Let us first look at what name is.

Name (also called identifier) is simply a name given to objects. Everything in Python is an object. Name is a way to access the underlying object.

For example, when we do the assignment a = 2, here 2 is an object stored in memory and a is the name we associate it with. We can get the address (in RAM) of some object through the built-in function, id(). Let's check it.

# Note: You may get different value of id

a = 2
# Output: id(2)= 10919424
print('id(2) =', id(2))

# Output: id(a) = 10919424
print('id(a) =', id(a))

Here, both refer to the same object. Let's make things a little more interesting.
# Note: You may get different value of id

a = 2

# Output: id(a) = 10919424
print('id(a) =', id(a))

a = a+1

# Output: id(a) = 10919456
print('id(a) =', id(a))

# Output: id(3) = 10919456
print('id(3) =', id(3))

b = 2

# Output: id(2)= 10919424
print('id(2) =', id(2))

What is happening in the above sequence of steps? A diagram will help us explain this.
Initially, an object 2 is created and the name a is associated with it, when we do a = a+1, a new object 3 is created and now a associates with this object.

Note that id(a) and id(3) have same values.

Furthermore, when we do b = 2, the new name b gets associated with the previous object 2.

This is efficient as Python doesn't have to create a new duplicate object. This dynamic nature of name binding makes Python powerful; a name could refer to any type of object.

>>> a = 5
>>> a = 'Hello World!'
>>> a = [1,2,3]

All these are valid and a will refer to three different types of object at different instances. Functions are objects too, so a name can refer to them as well.
def printHello():
    print("Hello")     
a = printHello()

# Output: Hello
a
Our same name a can refer to a function and we can call the function through it, pretty neat.
What is a namespace?

So now that we understand what names are, we can move on to the concept of namespaces.

To simply put it, namespace is a collection of names.

In Python, you can imagine a namespace as a mapping of every name, you have defined, to corresponding objects.

Different namespaces can co-exist at a given time but are completely isolated.

A namespace containing all the built-in names is created when we start the Python interpreter and exists as long we don't exit.

This is the reason that built-in functions like id(), print() etc. are always available to us from any part of the program. Each module creates its own global namespace.

These different namespaces are isolated. Hence, the same name that may exist in different modules do not collide.

Modules can have various functions and classes. A local namespace is created when a function is called, which has all the names defined in it. Similar, is the case with class. Following diagram may help to clarify this concept.

## Python Variable Scope

Although there are various unique namespaces defined, we may not be able to access all of them from every part of the program. The concept of scope comes into play.

Scope is the portion of the program from where a namespace can be accessed directly without any prefix.

At any given moment, there are at least three nested scopes.

    Scope of the current function which has local names
    Scope of the module which has global names
    Outermost scope which has built-in names

When a reference is made inside a function, the name is searched in the local namespace, then in the global namespace and finally in the built-in namespace.

If there is a function inside another function, a new scope is nested inside the local scope.

def outer_function():
    b = 20
    def inner_func():
        c = 30

a = 10

Here, the variable a is in the global namespace. Variable b is in the local namespace of outer_function() and c is in the nested local namespace of inner_function().

When we are in inner_function(), c is local to us, b is nonlocal and a is global. We can read as well as assign new values to c but can only read b and c from inner_function().

If we try to assign as a value to b, a new variable b is created in the local namespace which is different than the nonlocal b. Same thing happens when we assign a value to a.

However, if we declare a as global, all the reference and assignment go to the global a. Similarly, if we want to rebind the variable b, it must be declared as nonlocal. The following example will further clarify this.

def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)

a = 10
outer_function()
print('a =',a)

As you can see, the output of this program is

a = 30
a = 20
a = 10

In this program, three different variables a are defined in separate namespaces and accessed accordingly. While in the following program,

def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)

a = 10
outer_function()
print('a =',a)

The output of the program is.

a = 30
a = 30
a = 30

Here, all reference and assignment are to the global a due to the use of keyword global.

# Python Inheritance
Inheritance enable us to define a class that takes all the functionality from parent class and allows us to add more. In this article, you will learn to use inheritance in Python.
Creating derived class from a base class using inheritance

Inheritance is a powerful feature in object oriented programming.

It refers to defining a new class with little or no modification to an existing class. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.

Derived class inherits features from the base class, adding new features to it. This results into re-usability of code.
Python Inheritance Syntax

class DerivedClass(BaseClass):
    body_of_derived_class

Example of Inheritance in Python

To demonstrate the use of inheritance, let us take an example.

A polygon is a closed figure with 3 or more sides. Say, we have a class called Polygon defined as follows.

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

This class has data attributes to store the number of sides, n and magnitude of each side as a list, sides.

Method inputSides() takes in magnitude of each side and similarly, dispSides() will display these properly.

A triangle is a polygon with 3 sides. So, we can created a class called Triangle which inherits from Polygon. This makes all the attributes available in class Polygon readily available in Triangle. We don't need to define them again (code re-usability). Triangle is defined as follows.

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

However, class Triangle has a new method findArea() to find and print the area of the triangle. Here is a sample run.

>>> t = Triangle()

>>> t.inputSides()
Enter side 1 : 3
Enter side 2 : 5
Enter side 3 : 4

>>> t.dispSides()
Side 1 is 3.0
Side 2 is 5.0
Side 3 is 4.0

>>> t.findArea()
The area of the triangle is 6.00

We can see that, even though we did not define methods like inputSides() or dispSides() for class Triangle, we were able to use them.

If an attribute is not found in the class, search continues to the base class. This repeats recursively, if the base class is itself derived from other classes.

Method Overriding in Python

In the above example, notice that __init__() method was defined in both classes, Triangle as well Polygon. When this happens, the method in the derived class overrides that in the base class. This is to say, __init__() in Triangle gets preference over the same in Polygon.

Generally when overriding a base method, we tend to extend the definition rather than simply replace it. The same is being done by calling the method in base class from the one in derived class (calling Polygon.__init__() from __init__() in Triangle).

A better option would be to use the built-in function super(). So, super().__init(3) is equivalent to Polygon.__init__(self,3) and is preferred. You can learn more about the super() function in Python.

Two built-in functions isinstance() and issubclass() are used to check inheritances. Function isinstance() returns True if the object is an instance of the class or other classes derived from it. Each and every class in Python inherits from the base class object.

>>> isinstance(t,Triangle)
True

>>> isinstance(t,Polygon)
True

>>> isinstance(t,int)
False

>>> isinstance(t,object)
True

Similarly, issubclass() is used to check for class inheritance.

>>> issubclass(Polygon,Triangle)
False

>>> issubclass(Triangle,Polygon)
True

>>> issubclass(bool,int)
True
Python Multiple Inheritance
In this article, you'll learn what is multiple inheritance in Python and how to use it in your program. You'll also learn about multilevel inheritance and the method resolution order.
Python Multiple Inheritance

Like C++, a class can be derived from more than one base classes in Python. This is called multiple inheritance.

In multiple inheritance, the features of all the base classes are inherited into the derived class. The syntax for multiple inheritance is similar to single inheritance.
Python Multiple Inheritance Example

class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

Multiple Inheritance in Python

The class MultiDerived inherits from both Base1 and Base2.
Multilevel Inheritance in Python

On the other hand, we can also inherit form a derived class. This is called multilevel inheritance. It can be of any depth in Python.

In multilevel inheritance, features of the base class and the derived class is inherited into the new derived class.

An example with corresponding visualization is given below.

class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass

Multilevel Inheritance in Python
Method Resolution Order in Python

Every class in Python is derived from the class object. It is the most base type in Python.

So technically, all other class, either built-in or user-defines, are derived classes and all objects are instances of object class.

# Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))

In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching same class twice.

So, in the above example of MultiDerived class the search order is [MultiDerived, Base1, Base2, object]. This order is also called linearization of MultiDerived class and the set of rules used to find this order is called Method Resolution Order (MRO).

MRO must prevent local precedence ordering and also provide monotonicity. It ensures that a class always appears before its parents and in case of multiple parents, the order is same as tuple of base classes.

MRO of a class can be viewed as the __mro__ attribute or mro() method. The former returns a tuple while latter returns a list.

>>> MultiDerived.__mro__
(<class '__main__.MultiDerived'>,
 <class '__main__.Base1'>,
 <class '__main__.Base2'>,
 <class 'object'>)

>>> MultiDerived.mro()
[<class '__main__.MultiDerived'>,
 <class '__main__.Base1'>,
 <class '__main__.Base2'>,
 <class 'object'>]

Here is a little more complex multiple inheritance example and its visualization along with the MRO.

class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
# <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>]

print(M.mro())

Refer to this, for further discussion on MRO and to know the actual algorithm how it is calculated.


Python 3 OOP Part 3 - Delegation: composition and inheritance

This post is available as an IPython Notebook here
The Delegation Run

If classes are objects what is the difference between types and instances?

When I talk about "my cat" I am referring to a concrete instance of the "cat" concept, which is a subtype of "animal". So, despite being both objects, while types can be specialized, instances cannot.

Usually an object B is said to be a specialization of an object A when:

    B has all the features of A
    B can provide new features
    B can perform some or all the tasks performed by A in a different way

Those targets are very general and valid for any system and the key to achieve them with the maximum reuse of already existing components is delegation. Delegation means that an object shall perform only what it knows best, and leave the rest to other objects.

Delegation can be implemented with two different mechanisms: composition and inheritance. Sadly, very often only inheritance is listed among the pillars of OOP techniques, forgetting that it is an implementation of the more generic and fundamental mechanism of delegation; perhaps a better nomenclature for the two techniques could be explicit delegation (composition) and implicit delegation (inheritance).

Please note that, again, when talking about composition and inheritance we are talking about focusing on a behavioural or structural delegation. Another way to think about the difference between composition and inheritance is to consider if the object knows who can satisfy your request or if the object is the one that satisfy the request.

Please, please, please do not forget composition: in many cases, composition can lead to simpler systems, with benefits on maintainability and changeability.

Usually composition is said to be a very generic technique that needs no special syntax, while inheritance and its rules are strongly dependent on the language of choice. Actually, the strong dynamic nature of Python softens the boundary line between the two techniques.
Inheritance Now

In Python a class can be declared as an extension of one or more different classes, through the class inheritance mechanism. The child class (the one that inherits) has the same internal structure of the parent class (the one that is inherited), and for the case of multiple inheritance the language has very specific rules to manage possible conflicts or redefinitions among the parent classes. A very simple example of inheritance is

class SecurityDoor(Door):
    pass

where we declare a new class SecurityDoor that, at the moment, is a perfect copy of the Door class. Let us investigate what happens when we access attributes and methods. First we instance the class

>>> sdoor = SecurityDoor(1, 'closed')

The first check we can do is that class attributes are still global and shared

>>> SecurityDoor.colour is Door.colour
True
>>> sdoor.colour is Door.colour
True

This shows us that Python tries to resolve instance members not only looking into the class the instance comes from, but also investigating the parent classes. In this case sdoor.colour becomes SecurityDoor.colour, that in turn becomes Door.colour. SecurityDoor is a Door.

If we investigate the content of __dict__ we can catch a glimpse of the inheritance mechanism in action

>>> sdoor.__dict__
{'number': 1, 'status': 'closed'}
>>> sdoor.__class__.__dict__
mappingproxy({'__doc__': None, '__module__': '__main__'})
>>> Door.__dict__
mappingproxy({'__dict__': <attribute '__dict__' of 'Door' objects>,
    'colour': 'yellow',
    'open': <function Door.open at 0xb687e224>,
    '__init__': <function Door.__init__ at 0xb687e14c>,
    '__doc__': None,
    'close': <function Door.close at 0xb687e1dc>,
    'knock': <classmethod object at 0xb67ff6ac>,
    '__weakref__': <attribute '__weakref__' of 'Door' objects>,
    '__module__': '__main__',
    'paint': <classmethod object at 0xb67ff6ec>})

As you can see the content of __dict__ for SecurityDoor is very narrow compared to that of Door. The inheritance mechanism takes care of the missing elements by climbing up the classes tree. Where does Python get the parent classes? A class always contains a __bases__ tuple that lists them

>>> SecurityDoor.__bases__
(<class '__main__.Door'>,)

So an example of what Python does to resolve a class method call through the inheritance tree is

>>> sdoor.__class__.__bases__[0].__dict__['knock'].__get__(sdoor)
<bound method type.knock of <class '__main__.SecurityDoor'>>
>>> sdoor.knock
<bound method type.knock of <class '__main__.SecurityDoor'>>

Please note that this is just an example that does not consider multiple inheritance.

Let us try now to override some methods and attributes. In Python you can override (redefine) a parent class member simply by redefining it in the child class.

class SecurityDoor(Door):
    colour = 'gray'
    locked = True

    def open(self):
        if not self.locked:
            self.status = 'open'

As you can forecast, the overridden members now are present in the __dict__ of the SecurityDoor class

>>> SecurityDoor.__dict__
mappingproxy({'__doc__': None,
    '__module__': '__main__',
    'open': <function SecurityDoor.open at 0xb6fcf89c>,
    'colour': 'gray',
    'locked': True})

So when you override a member, the one you put in the child class is used instead of the one in the parent class simply because the former is found before the latter while climbing the class hierarchy. This also shows you that Python does not implicitly call the parent implementation when you override a method. So, overriding is a way to block implicit delegation.

If we want to call the parent implementation we have to do it explicitly. In the former example we could write

class SecurityDoor(Door):
    colour = 'gray'
    locked = True

    def open(self):
        if self.locked:
            return
        Door.open(self)

You can easily test that this implementation is working correctly.

>>> sdoor = SecurityDoor(1, 'closed')
>>> sdoor.status
'closed'
>>> sdoor.open()
>>> sdoor.status
'closed'
>>> sdoor.locked = False
>>> sdoor.open()
>>> sdoor.status
'open'

This form of explicit parent delegation is heavily discouraged, however.

The first reason is because of the very high coupling that results from explicitly naming the parent class again when calling the method. Coupling, in the computer science lingo, means to link two parts of a system, so that changes in one of them directly affect the other one, and is usually avoided as much as possible. In this case if you decide to use a new parent class you have to manually propagate the change to every method that calls it. Moreover, since in Python the class hierarchy can be dynamically changed (i.e. at runtime), this form of explicit delegation could be not only annoying but also wrong.

The second reason is that in general you need to deal with multiple inheritance, where you do not know a priori which parent class implements the original form of the method you are overriding.

To solve these issues, Python supplies the super() built-in function, that climbs the class hierarchy and returns the correct class that shall be called. The syntax for calling super() is

class SecurityDoor(Door):
    colour = 'gray'
    locked = True

    def open(self):
        if self.locked:
            return
        super().open()

The output of super() is not exactly the Door class. It returns a super object which representation is <super: <class 'SecurityDoor'>, <SecurityDoor object>>. This object however acts like the parent class, so you can safely ignore its custom nature and use it just like you would do with the Door class in this case.
Enter the Composition

Composition means that an object knows another object, and explicitly delegates some tasks to it. While inheritance is implicit, composition is explicit: in Python, however, things are far more interesting than this =).

First of all let us implement classic composition, which simply makes an object part of the other as an attribute

class SecurityDoor:
    colour = 'gray'
    locked = True

    def __init__(self, number, status):
        self.door = Door(number, status)

    def open(self):
        if self.locked:
            return
        self.door.open()

    def close(self):
        self.door.close()

The primary goal of composition is to relax the coupling between objects. This little example shows that now SecurityDoor is an object and no more a Door, which means that the internal structure of Door is not copied. For this very simple example both Door and SecurityDoor are not big classes, but in a real system objects can very complex; this means that their allocation consumes a lot of memory and if a system contains thousands or millions of objects that could be an issue.

The composed SecurityDoor has to redefine the colour attribute since the concept of delegation applies only to methods and not to attributes, doesn't it?

Well, no. Python provides a very high degree of indirection for objects manipulation and attribute access is one of the most useful. As you already discovered, accessing attributes is ruled by a special method called __getattribute__() that is called whenever an attribute of the object is accessed. Overriding __getattribute__(), however, is overkill; it is a very complex method, and, being called on every attribute access, any change makes the whole thing slower.

The method we have to leverage to delegate attribute access is __getattr__(), which is a special method that is called whenever the requested attribute is not found in the object. So basically it is the right place to dispatch all attribute and method access our object cannot handle. The previous example becomes

class SecurityDoor:
    locked = True

    def __init__(self, number, status):
        self.door = Door(number, status)

    def open(self):
        if self.locked:
            return
        self.door.open()

    def __getattr__(self, attr):
        return getattr(self.door, attr)

Using __getattr__() blends the separation line between inheritance and composition since after all the former is a form of automatic delegation of every member access.

class ComposedDoor:
    def __init__(self, number, status):
        self.door = Door(number, status)

    def __getattr__(self, attr):
        return getattr(self.door, attr)

As this last example shows, delegating every member access through __getattr__() is very simple. Pay attention to getattr() which is different from __getattr__(). The former is a built-in that is equivalent to the dotted syntax, i.e. getattr(obj, 'someattr') is the same as obj.someattr, but you have to use it since the name of the attribute is contained in a string.

Composition provides a superior way to manage delegation since it can selectively delegate the access, even mask some attributes or methods, while inheritance cannot. In Python you also avoid the memory problems that might arise when you put many objects inside another; Python handles everything through its reference, i.e. through a pointer to the memory position of the thing, so the size of an attribute is constant and very limited.
