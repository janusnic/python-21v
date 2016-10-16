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


class Main(object):
    def __init__(self):
        self.contacts_obj = []
        self.titles = (
            'Select operation:',
            "Usage operation:"
            )
        self.choices = (
            "Help",
            'Print Phone Numbers',
            'Add a Phone Number',
            'Remove a Phone Number',
            'Lookup a Phone Number',
            'Save Phone Numbers',
            "Quit"
            )

    def add_contact(self, rec):
        '''
        Add a New Record To Phone Gap
        '''
        d = Contact(rec)
        self.contacts_obj.append(d)

    def load_contacts(self):
        lines = [line.rstrip('\n') for line in open("contacts.db")]
        for line in lines:
            newRecord = line.split(':')
            self.add_contact(newRecord)

    def print_contacts(self):
        for contact in self.contacts_obj:
            print(contact)

    def save_contact(self, rec):
        fileHandler = open("contacts.db", 'a')
        fileHandler.write(':'.join(rec)+'\n')
        fileHandler.close()

    def makeList(self, prompt):
        raw = raw_input(prompt + ":> ")
        return newRecord.append(raw)

    def menu(self):
        tupleLen = [len(i) for i in self.choices]
        width = max(max(tupleLen), len(self.titles[0]))

        print 'phonegup'.upper().center(width+7, '=')
        self.printMenu(width, 0, self.choices)

        choiceList = [item[0].lower() for item in self.choices]
        choiceList = ' | '.join(choiceList)

        choice = raw_input("Enter choice "+choiceList+':>')
        return str(choice) if choice != '' else 'h'

    def printMenu(self, w, j, obj):
        gup = (': ', '| ')

        print("_"*(w+7))
        print(gup[1] + self.titles[j].ljust(w+3, ' ') + gup[1][::-1])

        for item in obj:
            print(
                gup[1] + item[0].lower() + gup[0] +
                item.ljust(w, ' ') + gup[1][:: -1]
                )

        print("="*(w+7))

    def myhelp(self):
        list1 = list()
        helpers = (
            'Display this usage message',
            'Print Phone Numbers',
            'Add a Phone Number',
            'Remove a Phone Number',
            'Lookup a Phone Number',
            'Save Phone Numbers',
            'Exit programm'
            )

        for i in range(len(helpers)):
            list1.append(self.choices[i]+' - ' + helpers[i])

        listLen = [len(i) for i in list1]
        self.printMenu(max(listLen), 1, list1)

while True:
    app = Main()

    choice = app.menu()

    if choice == 'q':
        print('{!s:#^40}'.format('Thankyou for using phoneGap.py!'))
        break
    if choice == 'h':
        app.myhelp()
        continue
    if choice == 'p':
        if len(app.contacts_obj) == 0:
            app.load_contacts()
        app.print_contacts()
    elif choice == 'a':
        if len(app.contacts_obj) == 0:
            app.load_contacts()
        newRecord = []
        tup1 = ("First Name", "Last Name", "Phone Number", 'Cell Phone', 'Town',  "Address", 'Age', 'Gender')

        print("Add New Record To PhoneGap")
        for prompt in tup1:
            app.makeList(prompt)
        app.add_contact(newRecord)
        app.save_contact(newRecord)
    else:
        continue
