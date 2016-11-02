#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os


cwd = os.getcwd()
con = lite.connect(cwd + '/db/test.db')

with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data
