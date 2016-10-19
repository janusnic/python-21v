from contact.contact import Contact


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
