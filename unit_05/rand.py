import random
def randcase_one(letter):
    if random.randint(0,5):   # True on 1, 2, 3, 4
        return letter.lower()
    else:
        return letter.upper()

def randcase(myfile):
    for line in myfile:
        yield "".join(randcase_one(letter) for letter in line[:-1])

myfile = 'dom.py'
for line in randcase(open(myfile)):
    print line