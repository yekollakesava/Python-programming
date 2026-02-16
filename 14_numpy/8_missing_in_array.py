import numpy as np
a=np.array([8,7,5,4,3,2,1])

a=np.sort(a)
for i in range(len(a)-1):
    if a[i+1] != a[i]+1:
        print(f"missing element: {a[i]+1}")



