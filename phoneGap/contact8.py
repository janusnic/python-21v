class Contact(object):
    '''
    Building the address book with classes
    '''
    def __init__(self, *args):
        self.first_name = args[0][0]
        self.last_name = args[0][1]
        self.phone = args[0][2]
        self.cell_phone = args[0][3]
        self.town = args[0][4]
        self.address = args[0][5]
        self.age = args[0][6]
        self.gender = args[0][7]

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
    d = Contact(rec)
    contacts_obj.append(d)


def load_contacts():
    lines = [line.rstrip('\n') for line in open("contacts.db")]
    for line in lines:
        newRecord = line.split(':')
        add_contact(newRecord)


def print_contacts():
    for contact in contacts_obj:
        print(contact)


def save_contact(rec):
    fileHandler = open("contacts.db", 'a')
    fileHandler.write(':'.join(rec)+'\n')
    fileHandler.close()


def makeList(prompt):
    raw = raw_input(prompt + ":> ")
    return newRecord.append(raw)

titles = (
    'Select operation:',
    "Usage operation:"
    )

choices = (
    "Help",
    'Print Phone Numbers',
    'Add a Phone Number',
    'Remove a Phone Number',
    'Lookup a Phone Number',
    'Save Phone Numbers',
    "Quit"
    )

helpers = (
    'Display this usage message',
    'Print Phone Numbers',
    'Add a Phone Number',
    'Remove a Phone Number',
    'Lookup a Phone Number',
    'Save Phone Numbers',
    'Exit programm'
    )


def printMenu(w, j, obj):
    gup = (': ', '| ')

    print("_"*(w+7))
    print(gup[1] + titles[j].ljust(w+3, ' ') + gup[1][::-1])

    for item in obj:
        print(
            gup[1] + item[0].lower() + gup[0] +
            item.ljust(w, ' ') + gup[1][:: -1]
            )

    print("="*(w+7))


def menu():
    tupleLen = [len(i) for i in choices]
    width = max(max(tupleLen), len(titles[0]))

    print 'phonegup'.upper().center(width+7, '=')
    printMenu(width, 0, choices)

    choiceList = [item[0].lower() for item in choices]
    choiceList = ' | '.join(choiceList)

    choice = raw_input("Enter choice "+choiceList+':>')
    return str(choice) if choice != '' else 'h'


def myhelp():
    list1 = list()
    for i in range(len(helpers)):
        list1.append(choices[i]+' - ' + helpers[i])

    listLen = [len(i) for i in list1]
    printMenu(max(listLen), 1, list1)

while True:
    choice = menu()

    if choice == 'q':
        print('{!s:#^40}'.format('Thankyou for using phoneGap.py!'))
        break
    if choice == 'h':
        myhelp()
        continue
    if choice == 'p':
        if len(contacts_obj) == 0:
            load_contacts()
        print_contacts()
    elif choice == 'a':
        if len(contacts_obj) == 0:
            load_contacts()
        newRecord = []
        tup1 = ("First Name", "Last Name", "Phone Number", 'Cell Phone', 'Town',  "Address", 'Age', 'Gender')

        print("Add New Record To PhoneGap")
        for prompt in tup1:
            makeList(prompt)
        add_contact(newRecord)
        save_contact(newRecord)
    else:
        continue
