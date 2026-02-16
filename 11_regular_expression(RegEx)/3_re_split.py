import re
text="i love programming in python cve"
pattern="ve"
print(re.split("\s",text))
print(re.split("\d",text))