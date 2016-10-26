# Note: You may get different value of id

a = 2
# Output: id(2)= 10919424
print('id(2) =', id(2))

# Output: id(a) = 10919424
print('id(a) =', id(a))

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

# All these are valid and a will refer to three different types
# of object at different instances.
a = 5
print('id(a) =', id(a))
a = 'Hello World!'
print('id(a) =', id(a))
a = [1, 2, 3]
print('id(a) =', id(a))

# Functions are objects too, so a name can refer to them as well.


def printHello():
    print("Hello")
a = printHello()
# Output: Hello
print('id(a) =', id(a))

# If there is a function inside another function,
# a new scope is nested inside the local scope.


def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)
        print('id(a) =', id(a))

    inner_function()
    print('a =', a)
    print('id(a) =', id(a))

a = 10
outer_function()
print('a =', a)
print('id(a) =', id(a))
