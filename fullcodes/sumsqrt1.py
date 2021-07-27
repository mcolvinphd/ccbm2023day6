import math, time
t=time.process_time()
max=10000000
sum=0.0
for i in range(1,max+1):
    sum+=math.sqrt(i)
elapsed_time=time.process_time()-t
print("Sum of sqrt of first ",max,"numbers=",sum,"time=",elapsed_time)
