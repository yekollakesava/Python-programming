'''import re
text="i love programming in python cve"
pattern="ve"
print(re.findall(pattern,text))
'''

import re
text ="Hello_123"
pattern=r'^[a-zA-Z0-9_]+$'
if re.match(pattern,text):
    print("exist")
else:
    print("not exist")    