import numpy as np
arr=np.array([1,2,3,2,3,4])
count=0
print("duplicates in array are: ")
for i in range(len(arr)-1):
    j=i+1
    count=1
    while j<=len(arr)-1:
        if arr[i] == arr[j]:
            count=count+1
        j+=1
    if(count>=2):
        print(arr[i])