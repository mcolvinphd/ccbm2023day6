import numpy as np
arr=np.arange(1,25)
print(arr)
arr=arr.reshape((3,8))
print(arr)
arr=arr.reshape((2,3,4))
print(arr)
arr=arr.reshape((6,4))
print(arr)
colsum=arr.sum(axis=0)
print(colsum)
rowsum=arr.sum(axis=1)
print(rowsum)
rowmax=arr.max(axis=1)
print(rowmax)
colmean=arr.mean(axis=0)
print(colmean)


