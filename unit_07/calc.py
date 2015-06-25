from collections import OrderedDict

class BinaryOperation:
    def __init__(self, op):
        self.op = op

    def go(self):
        x = self._prompt("First number: ")
        y = self._prompt("Second number: ")
        print(self.op(x, y))

    def _prompt(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Make sure to enter a number...")

def get_operation(operations):
    while True:
        op_name = input("What would you like to do? " +
                        '/'.join(operations.keys()) + ' ').title()
        try:
            return operations[op_name]
        except KeyError:
            print("That was not an option.")

operations = OrderedDict([
    ('Multiply', BinaryOperation(lambda x, y: x * y)),
    ('Divide',   BinaryOperation(lambda x, y: x / y)),
    ('Add',      BinaryOperation(lambda x, y: x + y)),
    ('Subtract', BinaryOperation(lambda x, y: x - y)),
])
get_operation(operations).go()