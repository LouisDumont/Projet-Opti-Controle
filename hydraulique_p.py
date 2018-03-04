#!/usr/bin/python

from structure_r import *

def HydrauliqueP(qc):
    # Debits des arcs
    q = q0 + dot(B,qc)
    
    # Pertes de charge des arcs
    z = r * abs(q) * q
    
    # Flux aux noeuds
    f = np.zeros(m)
    f[:mr] = dot(Ar,q)
    f[mr:m] = fd
    
    # Pressions aux noeuds
    temp = dot(np.transpose(Ar),pr)+z
    p = np.zeros(m)
    p[:mr] = pr
    p[mr:]= dot(-np.transpose(AdI),temp[:md])
    
    return(q,z,f,p)
    
if __name__ == '__main__':
    qc = np.random.normal(size=n-md)
    print(HydrauliqueP(qc))