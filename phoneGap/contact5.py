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

contacts_obj = [
    Contact(first_name="Alexander", last_name="Coder", phone=5551763, town="Kingston"),
    Contact(first_name="Michael", cell_phone=5559955),
    Contact(first_name="Elaine", last_name="Benes"),
    Contact(first_name="Tobias", town="Newport Beach"),
]

for contact in contacts_obj:
    print(contact)
