import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
arr1=np.array([1,2,3])
print(arr*arr1)
print(arr.shape)

'''for i in range(2):
    for j in range(3):
        print(arr[i,j])
print(arr + arr1)'''

print(arr[0,:])