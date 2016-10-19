import io
from contact.contact import Contact


class Main(object):
    def __init__(self):
        self.contacts_obj = []
        self.filename = "contacts.db"
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

    def read_data(self, filename):
        lines = []
        fh = None
        try:
            # fh = open(filename, encoding='utf-8')
            fh = io.open(filename, 'r', encoding='utf-8')
            for line in fh:
                if line.rstrip('\n'):
                    lines.append(line)
        except (IOError, OSError) as err:
            print(err)
            return []
        finally:
            if fh is not None:
                fh.close()
        return lines

    def write_data(self, filename, rec):
        lines = []
        fh = None
        try:
            fh = io.open(filename, 'a', encoding='utf-8')
            fh.write(unicode(':'.join(rec)+'\n', 'UTF-8'))
        except (IOError, OSError) as err:
            print(err)
            return []
        finally:
            if fh is not None:
                fh.close()
        return lines

    def load_contacts(self):
        # lines = [line.rstrip('\n') for line in open("contacts.db")]
        lines = self.read_data(self.filename)
        for line in lines:
            newRecord = line.split(':')
            self.add_contact(newRecord)

    def print_contacts(self):
        for contact in self.contacts_obj:
            print(contact)

    def save_contact(self, rec):
        self.write_data(self.filename, rec)

    def makeList(self, prompt, newRecord):
        raw = raw_input(prompt + ":> ")
        return newRecord.append(raw)

    def menu(self):
        tupleLen = [len(i) for i in self.choices]
        width = max(max(tupleLen), len(self.titles[0]))

        print 'phonegap'.upper().center(width+7, '=')
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
        '''
        'Display this usage message',
        'Print Phone Numbers',
        'Add a Phone Number',
        'Remove a Phone Number',
        'Lookup a Phone Number',
        'Save Phone Numbers',
        'Exit programm'
        '''

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


def runapp():
    while True:
        app = Main()

        choice = app.menu()

        if choice == 'q':
            print('{!s:#^40}'.format('Thankyou for using phoneGap.py!'))
            break
        if choice == 'h':
            app.myhelp()
            print app.myhelp.__doc__
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
                app.makeList(prompt, newRecord)
            app.add_contact(newRecord)
            app.save_contact(newRecord)
        else:
            continue

if __name__ == "__main__":
    runapp()
