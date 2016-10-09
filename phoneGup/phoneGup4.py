# -*- coding:utf-8 -*-
# ---------- PhoneGup ----------
'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''
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

contacts = {
    0: {
        'firstName': 'Alice',
        'lastName': 'Foo',
        'phone': '23411122',
        'address': '23 Foo drive',
     },
    1: {
        'firstName': 'Beth',
        'lastName': 'Bar',
        'phone': '23422255',
        'address': '44 Bar street',
    },
}


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

phone_list = [
    ['Bob', '1234567'],
    ['Mary', '2345671'],
]


def print_contacts(contacts):
    print("All Contacts in PhoneGup:")
    for id in contacts:
        print(
            "Name:", contacts[id]['firstName'],
            "\tNumber:", contacts[id]['phone']
            )
    print


def add_contact(firstName, lastName, phone, address):
    d = {
        'firstName': firstName,
        'lastName': lastName,
        'phone': phone,
        'address': address
        }

    contacts.update({len(contacts): d})


while True:

    choice = menu()

    if choice == 'q':
        print('{!s:#^40}'.format('Thankyou for using phoneGup.py!'))
        break
    if choice == 'h':
        myhelp()
        continue
    if choice == 'p':
        print_contacts(contacts)
    elif choice == 'a':
        print("Add New Record To PhoneGap")
        firstName = raw_input("First Name: ")
        lastName = raw_input("Last Name: ")
        phone = raw_input("Phone Number: ")
        address = raw_input("Address: ")

        add_contact(firstName, lastName, phone, address)
    else:
        myhelp()
        continue
