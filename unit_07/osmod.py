# -*- coding: utf-8 -*-
import sys

mypath = sys.path

#print mypath[2:6]
print mypath.__len__()
print mypath.__sizeof__()
print len(mypath)
#print repr(mypath)
print mypath.index('/usr/lib/python2.7/dist-packages')
print mypath.count('/usr/lib/python2.7/dist-packages')