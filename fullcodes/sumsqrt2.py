import math, time
import numpy as np
t=time.process_time()
max=100000000
sum=np.sum(np.sqrt(np.arange(1,max+1)))
elapsed_time=time.process_time()-t
print("Sum of sqrt of first ",max,"numbers=",sum,"time=",elapsed_time)
