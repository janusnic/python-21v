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
