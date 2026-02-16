import numpy as np
age=np.array([15,25,22,25,10,25,18])
b=np.array(["adult","minor"])

res=np.where(age>18,b[0],b[1])
print(res)