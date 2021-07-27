import numpy as np
def neighbors(arr,x,y,n):
    arr=np.roll(np.roll(arr,shift=-x+n//2,axis=0),shift=-y+n//2,axis=1)
    return arr[:n,:n]
N=10
window=3
loops=5
import numpy as np
def neighbors(arr,x,y,n):
    arr=np.roll(np.roll(arr,shift=-x+n//2,axis=0),shift=-y+n//2,axis=1)
    return arr[:n,:n]
N=10
window=3
loops=5
ar=np.random.choice((0,5),(N,N))
print(ar)
newar=np.zeros((N,N)) 
np.set_printoptions(precision=3)
print(ar)
for loop in range(loops):
    for i in range(N):
        for j in range(N):
            newar[i][j]=np.mean(neighbors(ar,i,j,window))
    ar=np.copy(newar)
print(ar)
