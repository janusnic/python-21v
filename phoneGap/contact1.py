class Contact(object):
    '''
    Building the address book with classes
    '''
    def __init__(self, first_name, last_name, phone,
                 cell_phone, town, address, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.cell_phone = cell_phone
        self.town = town
        self.address = address
        self.age = age
        self.gender = gender

s = Contact("Your Name", "Your Lasy Name", '1234567',
            '050 2345678', 'Kyiv', 'Foo st., 123', 20, "f")
print s

print s.age
