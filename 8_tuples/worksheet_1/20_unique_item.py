n=(1,2,3,4,5)
dup=()
for i in n:
    if i not in dup:
        dup +=(i,)
if len(n) == len(dup):
    print("True")
else:
    print("False")
 