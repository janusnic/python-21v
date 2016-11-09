# retest.py

import re

result = re.findall(r'.', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

result = re.findall(r'\w', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

result = re.findall(r'\w*', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

result = re.findall(r'\w+', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

result = re.findall(r'^\w+', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result
result = re.findall(r'\w+$', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

result = re.findall(r'\w\w', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

result = re.findall(r'\b\w.', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

result = re.findall(r'[fghpbFGHPB]\w+', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

result = re.findall(r'\b[fghpbFGHPB]\w+', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

result = re.findall(r'\b[^fghpbFGHPB]\w+', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

# pattern = re.compile('200')
# result = pattern.findall('200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
# print result
