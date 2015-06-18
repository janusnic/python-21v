#Python templates disallow in-string calculations (see PEP 292)
import string
from string import Template

values = { 'var':'foo' }

t = string.Template("""
$var
$$
${var}iable
""")

print 'TEMPLATE:', t.substitute(values)

s = """
%(var)s
%%
%(var)siable
"""

print 'INTERPLOATION:', s % values


values = { 'var':'foo' }

t = string.Template("$var is here but $missing is not provided")

try:
    print 'TEMPLATE:', t.substitute(values)
except KeyError, err:
    print 'ERROR:', str(err)
    
print 'TEMPLATE:', t.safe_substitute(values)


email_template = Template("""\
To: $address
From: Your Bank
CC: $cc_number
Date: $date

Dear $name,

Today you bounced check number $checknum to us.
Your account is now closed.

Sincerely,
the management
""")

import random
import datetime

person = {"address":"Joe@somewhere.com",
          "name": "Joe",
          "cc_number" : 1234567890,
          "checknum" : 500+random.randint(0,99)}

print email_template.substitute(person, date=datetime.date.today())