import os
# XXX What is '_PC_CHOWN_RESTRICTED'?

def is_verysafe(path):
    terms = []
    while True:
        path, ending = os.path.split(path)
        if not ending:
            break
        terms.insert(0, ending)
    for term in terms:
        path = os.path.join(path, term)
        if not is_safe(path):
            return False
    return True

print is_verysafe('/home/janus')

def SepReader(infile, sep = "\n\n"):
    text = infile.read(10000)
    if not text:
        return
    while True:
        fields = text.split(sep)
        for field in fields[:-1]:
            yield field
        text = fields[-1]
        new_text = infile.read(10000)
        if not new_text:
            yield text
            break
        text += new_text

filename = 'README.md'
para_count = 0
for para in SepReader(open(filename),'||'):
    para_count += 1
print para_count