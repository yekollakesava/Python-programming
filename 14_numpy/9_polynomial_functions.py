import numpy as np
a=np.poly1d([1,2,3])
b=np.poly1d([5,6,7,8,9])
print(a)
print(b)
print(f"co efficents:{b.c}")
print(f"order:{a.o}")