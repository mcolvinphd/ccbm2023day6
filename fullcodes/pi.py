import time
import math
import random
trials=int(input("Enter the number of trials: "))
t=time.process_time()
inside=0
for i in range(trials):
    x=random.random()
    y=random.random()
    if (x*x+y*y)<1:
        inside+=1
pi=4.*inside/trials
et=time.process_time()-t
print("pi est=%9.6f error=%9.6f time=%f"%(pi,pi-math.pi,et))
