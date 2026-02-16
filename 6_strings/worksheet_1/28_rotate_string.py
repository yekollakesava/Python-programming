def rotatestring(str,k):
    length=len(str)-k
    arr=str[length:]
    arr=arr+str[:length+1]
    return arr

data=str(input("enter string: "))
k=int(input("enter no of steps to rotate: "))
print(f"after rotating {rotatestring(data,k)}")
