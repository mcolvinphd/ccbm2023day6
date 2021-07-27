import numpy as np
from numpy.linalg import matrix_power
P=np.matrix([[0.25, 0.40],[0.75, 0.60]])
print(P)
N=np.matrix([[50],[50]])
print(N)
N=P*N
print(N)
P10=matrix_power(P,10)
N=P10*N
print(N)
N=P10*N
print(N)
