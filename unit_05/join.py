animals = ['Cat', 'Dog', 'Pinguin', 'Crocodile', 'Elephant']
" ".join(animals)

"-<>-".join(animals)

"".join(animals)



animals = ['Cat', 'Dog', 'Pinguin', 'Crocodile', 'Elephant']
" ".join(reversed(animals))

animals[::-1]['Elephant', 'Crocodile', 'Pinguin', 'Dog', 'Cat']
" ".join(animals[::-1]


word = "".join([chr(n) for n in ascii_character_numbers])
word = "".join([chr(n) for n in [115, 97, 109, 112, 108, 101]])
print word
#=> sample
#-----------------------------
hal = "HAL"
ibm = "".join([chr(ord(c)+1) for c in hal]) # add one to each ASCII value
print ibm   
#=> IBM

mystr = "an apple a day"
uniq = sorted(set(mystr))
print "unique chars are: '%s'" % "".join(uniq)
#=> unique chars are: ' adelnpy'


#-----------------------------
# 2.3+ only
revchars = mystr[::-1]  # extended slice - step is -1
revwords = " ".join(mystr.split(" ")[::-1])

# pre 2.3 version:
mylist = list(mystr)
mylist.reverse()
revbytes = "".join(mylist)

mylist = mystr.split()
mylist.reverse()
revwords = ' '.join(mylist)

# Alternative version using reversed():
revchars = "".join(reversed(mystr))
revwords = " ".join(reversed(mystr.split(" ")))



def ContReader(infile):
    lines = []
    for line in infile:
        line = line.rstrip()
        if line.endswith("\\"):
            lines.append(line[:-1])
            continue
        lines.append(line)
        yield "".join(lines)
        lines = []
    if lines:
        yield "".join(lines)

for line in ContReader(datafile):
    pass # process full record in 'line' here
