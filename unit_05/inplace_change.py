#!/usr/bin/python

def inplace_change(filename, old_string, new_string):
        s=open(filename).read()
        if old_string in s:
                print 'Changing "{old_string}" to "{new_string}"'.format(**locals())
                s=s.replace(old_string, new_string)
                f=open(filename, 'w')
                f.write(s)
                f.flush()
                f.close()
        else:
                print 'No occurances of "{old_string}" found.'.format(**locals())

filename = 'file.txt'
old_string = 'Your problem stems from reading from and writing '
new_string = 'You are not a problem to reading from and writing '
inplace_change(filename, old_string, new_string)