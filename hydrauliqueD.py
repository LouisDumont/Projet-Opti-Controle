#!/usr/bin/python

from structure_r import *
from math import *


def HydrauliqueD(pd):
    # Pressions aux noeuds
    p = np.zeros(m)
    p[:mr] = pr
    p[mr:m] = pd
    
    # Pertes de charge des arcs
    z = dot(-np.transpose(A),p)
    
    # Debits des arcs
    q = np.divide(z,np.sqrt(r*abs(z)))
    
    # Flux aux noeuds
    f = np.zeros(m)
    f[:mr] = dot(Ar,q)
    f[mr:m]= fd
    
    return(q,z,f,p)
    
if __name__ == '__main__':
    pd = np.random.normal(size=md)
    print(HydrauliqueD(pd)[2])
    