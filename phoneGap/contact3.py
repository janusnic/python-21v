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
        return self.phone

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


c1 = Contact(first_name="Alexander", last_name="Coder")
c1.setPhone("5551763")
c1.setTown("Kingston")
print("c1: {0}".format(c1))
c2 = Contact(first_name="Michael", cell_phone=5559955)
print("c2: {0}".format(c2))
