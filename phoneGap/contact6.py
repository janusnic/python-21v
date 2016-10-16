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
    #  zip(*iterables) Make an iterator
    # that aggregates elements from each of the iterables.
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
