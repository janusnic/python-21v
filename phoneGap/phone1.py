from contact.contact import Contact
from main1 import Main

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
