import numpy as np
N=1000
m3=np.arange(0,N,3)
m5=np.arange(0,N,5)
m35=np.concatenate([m3,m5])
m35u=np.unique(m35)
print("Sum of 3 and 5 multiples below %d is %d"%(N,m35u.sum()))
