import re
text="i love9programming in0python cve"
pattern="ve"
print(re.sub("\s"," 9 ",text))
print(re.sub("\d"," 99 ",text,2))