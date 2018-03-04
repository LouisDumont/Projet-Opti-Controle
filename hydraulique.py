#!/usr/bin/python

from datas import *

import numpy as np
from numpy import dot
from numpy import transpose as t

# Calcule les variables hydrauliques pour une solution donnée
def compute_hydraulique(qc):
    # Débits des arcs
    q = q0 + dot(B, qc)
    # Pertes de charge
    z = r * np.abs(q) * q
    # Flux des noeuds
    f = np.zeros(m)
    f[:mr] = dot(Ar, q)
    f[mr:] = fd
    # Pression aux noeuds
    p = np.zeros(m)
    p[:mr] = pr
    p[mr:] = -dot(t(AdI), (dot(t(Ar), pr) + z)[:md])

    return q, z, f, p

if __name__ == '__main__':
    qc0 = np.random.normal(size=n-md)
    for k in compute_hydraulique(qc0):
        print(k)
    
