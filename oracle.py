#!/usr/bin/python

import numpy as np
from numpy import dot

from structure_r import *

def OraclePG(qc,indice):
    Q0 = np.zeros(n)
    Q0[:md] = dot(AdI, fd)
    q = Q0 + dot(B, qc) 
    # critère
    F = 1./3*dot(q, r*q*np.abs(q)) + dot(pr, dot(Ar, q))
    # TODO dérivée du critère par rapport à qc
    G = np.zeros(n-md)
    G = (1/3)*dot(np.transpose(B),r*q*abs(q))
    G += (2/3)*dot(np.transpose(B),r*q*abs(q))
    G += dot(dot(np.transpose(B),np.transpose(Ar)),pr)
    return F, G

if __name__ == '__main__':
    F, G = OraclePG(np.random.normal(size=n-md),1)
    print(F, G)
