import re
str= "my number is 1234567890"
res=re.findall(r'\d+',str)
print(res)
