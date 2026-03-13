import re
string="hello Hello Hello"
string=string.lower()
sub="hello"
res=[i.start() for i in re.finditer(sub,string)]
print(res)

