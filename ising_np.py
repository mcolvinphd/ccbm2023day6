from random import choice,random
import numpy as np
from math import exp
def neighbors(arr,x,y,n):
    arr=np.roll(np.roll(arr,shift=-x+n//2,axis=0),shift=-y+n//2,axis=1)
    return arr[:n,:n]

Temp=0.0             # Temperature
n=20                  # Sites per edge for n x n system
zone=3                # zone of interacting spins (3,5,7,...)
n2=n*n                # Precalculate n*n
nlist=list(range(n))  # List of sites
ntrials=200000        # Number Trials
nequil=100000         # Equilibration steps

while Temp<10.:
    Temp+=0.2
    # Initialize sums for averages
    E_sum=0.0
    E2_sum=0.0

    # Create initial matrix of spins all up
    ## Add one line from lecture notes here

    # Run simulation
    for trial in range(1,(ntrials+nequil+1)):
        # Randomly pick a site
        i=choice(nlist)
        j=choice(nlist)

        #Calculate the change in energy if we flip this spin
        ## Add one line from lecture notes here

        #Flip the spin using Metropolis MC
        if exp(-deltaE/Temp)>random():
            spins[i][j]=-spins[i][j]
        else:
            deltaE=0.0

        # Calculate system energy ONCE
        if trial == nequil:
            energy=0.0
            for i in range(n):
                for j in range(n):
                    ## Add one line from lecture notes here
            energy/=n2

        # Update energy based on deltaE per spin
        if trial > nequil:
            energy+=2*deltaE/n2
            E_sum+=energy
            E2_sum+=energy*energy

    E_ave=E_sum/ntrials
    E2_ave=E2_sum/ntrials
    Cv=1./(Temp**2)*(E2_ave-E_ave*E_ave)
    print('%8.4f %10.6f %10.6f'%(Temp, E_ave, Cv))
