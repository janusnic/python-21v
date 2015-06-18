#!/usr/bin/python
# laston - find out when given user last logged on
import sys
import struct
import pwd
import time
import re

f = open("/var/log/lastlog","rb")

fmt = "L32s256s"
rec_size = struct.calcsize(fmt)

for user in sys.argv[1:]:
    if re.match(r"^\d+$", user):
        user_id = int(user)
    else:
        try:
            user_id = pwd.getpwnam(user)[2]
        except:
            print "no such uid %s" % (user)
            continue
    f.seek(rec_size * user_id)
    bin = f.read(rec_size)
    if len(bin) == rec_size:
        data = struct.unpack(fmt, bin)
        if data[0]:
            logged_in = "at %s" % (time.strftime("%a %H:%M:%S %Y-%m-%d",
                                    time.localtime(data[0])))
            line = " on %s" % (data[1])
            host = " from %s" % (data[2])
        else:
            logged_in = "never logged in"
            line = ""
            host = ""
        print "%-8s UID %5d %s%s%s" % (user, user_id, logged_in, line, host)
    else:
        print "Read failed."
f.close()