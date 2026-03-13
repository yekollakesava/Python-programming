import re
string="Hello_123"
pattern=r'^[a-zA-Z_0-9]+$'

if re.match(pattern,string):
    print("valid string")
else:
    print("invalid string")