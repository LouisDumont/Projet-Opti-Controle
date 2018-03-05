#!/usr/bin/python

from datas_r import *

import numpy as np
from numpy import dot
from numpy import transpose as t


# Calcule les variables hydrauliques pour une solution donnée
def compute_hydraulic_p(qc):
    # Débits des arcs
    q = q0 + dot(B, qc)
    # Pertes de charge des arcs
    z = r * abs(q) * q
    # Flux des noeuds
    f = np.zeros(m)
    f[:mr] = dot(Ar, q)
    f[mr:] = fd
    # Pression aux noeuds
    p = np.zeros(m)
    p[:mr] = pr
    p[mr:] = -dot(t(AdI), (dot(t(Ar), pr) + z)[:md])

    return q, z, f, p

    
def compute_hydraulic_d(pd):
    # Pressions aux noeuds
    p = np.zeros(m)
    p[:mr] = pr
    p[mr:m] = pd
    # Pertes de charge des arcs
    z = dot(-t(A), p)
    # Debits des arcs
    q = z / np.sqrt(r*abs(z))
    # Flux aux noeuds
    f = np.zeros(m)
    f[:mr] = dot(Ar,q)
    f[mr:m]= fd
    
    return q, z, f, p
    

if __name__ == '__main__':
    qc0 = np.random.normal(size=n-md)
    for k in compute_hydraulic_p(qc0):
        print(k)

    pd0 = np.random.normal(size=md)
    for k in compute_hydraulic_d(pd0):
        print(k)
