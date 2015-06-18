#!/usr/bin/env/python
s = "Today is a good day"
print s.partition("good")

print s.rpartition("day")


s = "/usr/local/bin/firefox"
result = s.rpartition("/")
print(result)



s = "/usr/local/bin/firefox"
i = s.rfind("/")
if i == -1:
    result = s, "", ""
else:
    result = s[:i], s[i], s[i + 1:]
print(result)