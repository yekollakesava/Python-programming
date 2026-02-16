import numpy as np

arr=np.array([1,2,3,4,5])
target=8
for i in arr:
    for j in arr:
        if i+j == target:
            print(i,j)