# retest.py

import re

result = re.match(r'200', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result
print result.group(0)
print result.start()
print result.end()


result = re.search(r'200', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')

print result.group(0)

result = re.findall(r'200', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')

print result


result = re.split(r'200', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result


result = re.split(r'200', '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903',maxsplit=1)
print result

result = re.sub(r'200', '188',  '200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result

pattern = re.compile('200')
result = pattern.findall('200.19.92.58 - - [29/Feb/2016:07:31:09 -0600] "GET /ply/bookplug.gif HTTP/1.0" 200 23903')
print result
