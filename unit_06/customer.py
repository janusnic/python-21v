class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount &gt; self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

print Customer.__dict__
print Customer.__class__

print dict(Customer.__dict__)
print Customer.__dict__.keys()
print Customer.__dict__['__doc__']
print Customer.__dict__['__dict__']
print Customer.__dict__['__weakref__']
print Customer.__dict__['__module__']
print Customer.__dict__['__init__'] 

# __init__
# jeff = Customer('Jeff Knupp', 1000.0)
jeff = Customer(jeff, 'Jeff Knupp', 1000.0);
# properties
print jeff.name
print jeff.balance
# method
print jeff.withdraw(100.0)
# self
print Customer.withdraw(jeff,100.0)
# __dict__
print jeff.__dict__

print jeff.__dict__['name']
print jeff.__dict__['balance']


