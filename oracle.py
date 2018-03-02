#!/usr/bin/python

import numpy as np
from numpy import dot

from structure_r import *

def OraclePG(qc):
    Q0 = np.zeros(n)
    Q0[:md] = dot(AdI, fd)
    q = Q0 + dot(B, qc) 
    # critère
    F = 1./3*dot(q, r*q*np.abs(q)) + dot(pr, dot(Ar, q))
    # TODO dérivée du critère par rapport à qc
    G = 0 
    return F, G

if __name__ == '__main__':
    F, G = OraclePG(np.random.normal(size=n-md))
    print(F, G)
