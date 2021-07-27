from random import choice
import math
state=0
states=[0]*nstates
nstates=4
T=3
ntrials=10000
for trial in range(ntrials):
    newstate=choice(nstates)
    x=exp(-(newstate-state)/T)
    if x>random():
        state=newstate
    states[state]+=1
Boltz=[0]*nstates
for i in range(nstates):
    Boltz[i]=exp(-i/T)
    partition+=exp(-i/T)
for i in range(nstates-1,-1,1)
print("%d   %6.3f  %6.3f"%(i,states[i]/ntrial,Boltz[i]/partition))
