import numpy as np
def neighbors(arr,x,y,n):
    arr=np.roll(np.roll(arr,shift=-x+n//2,axis=0), shift=-y+n//2,axis=1)
    return arr[:n,:n]
a=np.arange(0,100).reshape(10,10)
print(a)
print(neighbors(a,0,0,3))
print(neighbors(a,0,0,5))
