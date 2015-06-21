in = open('path/to/input/file').read()
out = open('path/to/input/file', 'w')
replacements = {'zero':'0', 'temp':'bob', 'garbage':'nothing'}
for i in replacements.keys():
    in = in.replace(i, replacements[i])
out.write(in)
out.close
This eliminated a lot of the iterations that the other answers suggest, and will speed up the process for longer files.

Reading from standard input, write 'code.py' as follows:

import sys

rep = {'zero':'0', 'temp':'bob', 'garbage':'nothing'}

for line in sys.stdin:
    for k, v in rep.iteritems():
        line = line.replace(k, v)
    print line
Then, execute the script with redirection or piping (http://en.wikipedia.org/wiki/Redirection_(computing))

python code.py < infile > outfile

I might consider using a dict and re.sub for something like this:

import re
repldict = {'zero':'0','temp':'bob','garage':'nothing'}
def replfunc(match):
    return repldict[match.group(0)]

regex = re.compile('|'.join(re.escape(x) for x in repldict)
with open('file.txt') as fin, open('fout.txt','w') as fout:
    for line in fin:
        fout.write(regex.sub(replfunc,line))
This has a slight advantage to replace in that it is a bit more robust to overlapping matches.