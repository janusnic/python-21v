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

contacts = [
    {
        'firstName': 'Alice',
        'lastName': 'Foo',
        'phone': '23411122',
        'address': '23 Foo drive',
     },
    {
        'firstName': 'Beth',
        'lastName': 'Bar',
        'phone': '23422255',
        'address': '44 Bar street',
    },
]
lookup = (
    'firstName',
    'lastName',
    'phone',
    'address'
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


def print_contacts(contacts):
    print("All Contacts in PhoneGup:")
    for item in contacts:
        print(
            "Name:", item['firstName'],
            "\tNumber:", item['phone']
            )
    print


def add_contact(rec):
    #  zip(*iterables) Make an iterator
    # that aggregates elements from each of the iterables.
    d = {x: y for (x, y) in zip(lookup, rec)}
    contacts.append(d)


def look_contact():
    fieldList = [item[0] for item in lookup]
    look = raw_input("Enter Field "+' | '.join(fieldList)+':>')
    return str(look) if (look != '' and look in fieldList) else 'h'


def print_contact(look):
    for lookKey in lookup:
        if lookKey.startswith(look):
            serchKey = lookKey
    key = 'phone'
    search = raw_input("Enter Search String " + ':>')
    for contact in contacts:
        if search.upper() in contact.get(serchKey).upper():
            print("Contact in PhoneGup:")
            print "%s %s phone is %s" % (contact.get('firstName'), contact.get('lastName'), contact.get(key))
            print


def makeList(prompt):
    raw = raw_input(prompt + ":> ")
    return newRecord.append(raw)


def save_contacts():
    pass

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
        newRecord = []
        tup1 = ("First Name", "Last Name", "Phone Number", "Address")
        print("Add New Record To PhoneGap")
        for prompt in tup1:
            makeList(prompt)
        add_contact(newRecord)
    if choice == 'l':
        look = look_contact()
        if look == 'h':
            print 'Use f for First Name or l for LAst Name'
        else:
            print_contact(look)
    if choice == 's':
        save_contacts()
    else:
        continue
