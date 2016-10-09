# python-21v unit 04
# Словари в Python

Словарь — это неупорядоченное множество пар ключ—значение. Когда вы добавляете ключ в словарь, вы также должны добавить и значение для этого ключа. (Значение всегда можно изменить позже.) Словари в Python оптимизированы для получения значения по известному ключу.

        contacts = {
            '1': {
                'firstName': 'Alice',
                'lastName': 'Foo',
                'phone': '23411122',
                'addr': '23 Foo drive',
             },
            '2': {
                'firstName': 'Beth',
                'lastName': 'Bar',
                'phone': '23422255',
                'addr': '44 Bar street',
            },
        }


# in — оператор проверки вхождения.
## Получить список всех телефона в базе данных по id:

        def print_contacts(contacts):
            print("All Contacts in PhoneGup:")
            for id in contacts:
                print(
                    "Name:", contacts[id]['firstName'],
                    "\tNumber:", contacts[id]['phone']
                    )

# How to change or add elements in a dictionary?

Dictionary are mutable. We can add new items or change the value of existing items using assignment operator.

If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.

## update([other]) 	— изменяет значение по key/value
Update the dictionary with the key/value pairs from other, overwriting existing keys.
                    def add_contact(firstName, lastName, phone, address):
                        d = {
                            'firstName': firstName,
                            'lastName': lastName,
                            'phone': phone,
                            'address': address
                            }

                        contacts.update({2: d})

# keys() — возвращает список ключей;

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

        print contacts.keys()
        print len(contacts.keys())
        print max(contacts.keys())

## phoneGup4.py

        def add_contact(firstName, lastName, phone, address):
            d = {
                'firstName': firstName,
                'lastName': lastName,
                'phone': phone,
                'address': address
                }

            contacts.update({len(contacts): d})

## phoneGup5.py

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

            def print_contacts(contacts):
                print("All Contacts in PhoneGup:")
                for item in contacts:
                    print(
                        "Name:", item['firstName'],
                        "\tNumber:", item['phone']
                        )
                print


            def add_contact(firstName, lastName, phone, address):
                d = {
                    'firstName': firstName,
                    'lastName': lastName,
                    'phone': phone,
                    'address': address
                    }

                contacts.append(d)

## phoneGup6.py

        def look_contact():
            fieldList = [item[0] for item in lookup]
            fieldList = ' | '.join(fieldList)
            look = raw_input("Enter Field "+fieldList+':>')
            return str(look) if look != '' else 'h'

        def print_contact(look):
            key = 'phone'
            search = raw_input("Enter Search String " + ':>')
            for contact in contacts:
                if search in contact['firstName']:
                    print("Contact in PhoneGup:")
                    print "%s %s phone is %s" % (contact['firstName'], contact['lastName'], contact[key])
                    print


## phoneGup7.py
        def print_contact(look):
            for lookKey in lookup:
                if lookKey.startswith(look):
                    serchKey = lookKey
            key = 'phone'
            search = raw_input("Enter Search String " + ':>')
            for contact in contacts:
                if search in contact[serchKey]:
                    print("Contact in PhoneGup:")
                    print "%s %s phone is %s" % (contact['firstName'], contact['lastName'], contact[key])
                    print

            if choice == 'l':
                look = look_contact()
                if look == 'h':
                    print 'Use f for First Name or l for LAst Name'
                else:
                    print_contact(look)

# get() — получает значение по ключу, в случае отсутствия дает None:
                    d = {}
                    print d.get('name')

## phoneGup8.py
                    def print_contact(look):
                        for lookKey in lookup:
                            if lookKey.startswith(look):
                                serchKey = lookKey
                        key = 'phone'
                        search = raw_input("Enter Search String " + ':>')
                        for contact in contacts:
                            if search in contact.get(serchKey):
                                print("Contact in PhoneGup:")
                                print "%s %s phone is %s" % (contact.get('firstName'), contact.get('lastName'), contact.get(key))
                                print

## phoneGup8.py
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

# iterkeys() — возвращает итератор ключей:

                    d.iterkeys()

# copy()
Пример создания копии словаря:

        x = {"user":'admin','attr':[1,2,3]}
        y = x.copy()

Метод copy() не делает полного копирования: если мы, например, сделаем операцию:
        x['attr'].remove(1)
то обнаружим, что удаление атрибута произойдет также и в копии.
Чтобы этого не произошло, нужно использовать метод deepcopy().
        from copy import deepcopy
        y = x.deepcopy()

# fromkeys() — создает словарь по заданным ключам с пустыми значениями:
    {}.fromkeys(['name', 'age'])

# Можно все значения заполнить по умолчанию:
    {}.fromkeys(['name', 'age'],123)

    marks = {}.fromkeys(['Math','English','Science'], 0)

    # Output: {'English': 0, 'Math': 0, 'Science': 0}
    print(marks)

    for item in marks.items():
        print(item)

    # Output: ['English', 'Math', 'Science']
    list(sorted(marks.keys()))

# has_key() — проверяет, есть ли в словаре значение по данному ключу:
    d = {}
    d.has_key('name')

# items() — возвращает список значений:

    for key, value in d.items():
            print(key, value)

# iteriyems() — возвращает итератор — выдает тот же результат:

    for k, v in d.iteritems():
    ...     print k, v


# pop() — извлекает значение по ключу с последующим удалением:
    d.pop('title')

# popitem() — извлекает произвольное значение с последующим удалением:
    d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'www': 'python'}
    d.popitem()

# values() — возвращает список значений:

    d={}
    d[1]=1
    d[2]=2
    d[3]=3
    d

    d.values()

# del — оператор удаляет пару ключ: значение по ключу:
    del d[2]


# Python Dictionary Comprehension

Dictionary comprehension is an elegant and concise way to create new dictionary from an iterable in Python.

Dictionary comprehension consists of an expression pair (key: value) followed by for statement inside curly braces {}.

Here is an example to make a dictionary with each item being a pair of a number and its square.

    squares = {x: x*x for x in range(6)}

    # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    print(squares)

This code is equivalent to

        squares = {}
        for x in range(6):
           squares[x] = x*x

A dictionary comprehension can optionally contain more for or if statements.

An optional if statement can filter out items to form the new dictionary.

Here are some examples to make dictionary with only odd items.

    odd_squares = {x: x*x for x in range(11) if x%2 == 1}

    # Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
    print(odd_squares)

## phoneGup9.py

        def add_contact(rec):
            #  zip(*iterables) Make an iterator
            # that aggregates elements from each of the iterables.
            d = {x: y for (x, y) in zip(lookup, rec)}
            contacts.append(d)


        def makeList(prompt):
            raw = raw_input(prompt + ":> ")
            return newRecord.append(raw)

        elif choice == 'a':
            newRecord = []
            tup1 = ("First Name", "Last Name", "Phone Number", "Address")
            print("Add New Record To PhoneGap")
            for prompt in tup1:
                makeList(prompt)
            add_contact(newRecord)

# Dictionary Membership Test

We can test if a key is in a dictionary or not using the keyword in. Notice that membership test is for keys only, not for values.

        squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

        # Output: True
        print(1 in squares)

        # Output: True
        print(2 not in squares)

        # membership tests for key only not value
        # Output: False
        print(49 in squares)

# Iterating Through a Dictionary

Using a for loop we can iterate though each key in a dictionary.

    squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
    for i in squares:
        print(squares[i])

# Built-in Functions with Dictionary

 Built-in functions like all(), any(), len(), cmp(), sorted() etc. are commonly used with dictionary to perform different tasks.

   all() 	Return True if all keys of the dictionary are true (or if the dictionary is empty).
   any() 	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
   len() 	Return the length (the number of items) in the dictionary.
   cmp() 	Compares items of two dictionaries.
   sorted() 	Return a new sorted list of keys in the dictionary.

Here are some examples that uses built-in functions to work with dictionary.

   squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

    # Output: 5
    print(len(squares))

    # Output: [1, 3, 5, 7, 9]
    print(sorted(squares))


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
