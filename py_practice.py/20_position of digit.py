import re
data="abc1d23e4"
pattern="0123456789"
for i in data:
    if i in pattern:
        print(i,data.index(i))