# -*- coding:utf-8 -*-

# Перегрузка операторов, строковое представление
# использовать кортеж внутри Command для хранения всех Employee.
class Employee(object):
    def __init__(self, name, cost, level):
        self.name = name
        self.cost = cost
        self.level = level

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Command(self, other)

    def __repr__(self):
        return '{u.name} (cost={u.cost}, level={u.level})'.format(u=self)


class Command(object):    
    def __init__(self, *employees):
        self.employees = employees
        self.cost = sum(employee.cost for employee in employees)
        self.level = max(employee.cost for employee in employees)

    def __add__(self, other):
        if isinstance(other, Employee):
            return Command(other, *self.employees)

    def __str__(self):
        return 'Command (cost={b.cost}, level={b.level}) {b.employees}'.format(b=self)


emp1 = Employee('Ivan', 12, 4)
emp2 = Employee('Sidor', 15, 6)
emp3 = Employee('Joe', 26, 8)
com1 = emp1 + emp2
print com1 
# Здесь вывод будет следующий:
# Command (cost=27, level=15) (Ivan (cost=12, level=4), Sidor (cost=15, level=6))
