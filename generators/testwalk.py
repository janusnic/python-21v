# testwalk.py

import os
import fnmatch

tree = os.walk('www')
print(tree)

for d in tree:
    print(d)

for path, dirlist, filelist in os.walk('www'):
    for f in filelist:
        print(f)

path_f = []
for path, dirlist, filelist in os.walk('www'):
    for f in filelist:
        p = os.path.join(path, f)
        path_f.append(p)

for f in path_f:
    print(f)

for path, dirlist, filelist in os.walk('www'):
    print(filelist)

contdir = []
for i in os.walk('www'):
    contdir.append(i)

for i in contdir:
    print(i)
