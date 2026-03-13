st="hi@123#worls!"
st=list(st)
for i in range(len(st)):
    if st[i] =='@' or st[i]=='!':
        st[i] = '#'
st="".join(st)
print(st)