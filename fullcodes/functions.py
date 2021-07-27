import numpy as np
def f1(x):
    x+=10
    print("Inside f1",x)
def f2(y):
    y.append(10)
    print("Inside f2",y)
def f3(z):
    z=np.append(z,10)
    print("Inside f3",z)
a=10
f1(a)
print(a)
b=[1,3,5]
f2(b)
print(b)
c=np.array([1,2,3])
f3(c)
print(c)
