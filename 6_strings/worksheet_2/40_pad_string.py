def pad_string(str,n,ch):
    length=len(str)
    n=abs(n-length)
    str=ch*n+str
    return str

data=str(input("enter the string: "))
n=int(input("enter required length:"))
ch='*'
print(pad_string(data,n,ch))