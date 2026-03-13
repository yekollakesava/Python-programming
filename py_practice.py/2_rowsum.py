import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

rowsum=[]
colsum=[]

'''for i in range(3):
    s=0
    for j in range(3):
        s+=arr[i][j]
    rowsum.append(int(s))

for i in range(3):
    s=0
    for j in range(3):
        s+=arr[j][i]
    colsum.append(int(s))

print(f"row sum:{rowsum}")
print(f"col sum:{colsum}")
        '''

rowsum=np.sum(arr,axis=1)
colsum=np.sum(arr,axis=0)
print(f"row sum:{rowsum}")
print(f"col sum:{colsum}")