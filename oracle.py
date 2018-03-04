#!/usr/bin/python

import numpy as np
from numpy import dot

from structure_r import *

def oracle_pg(qc):
    Q0 = np.zeros(n)
    Q0[:md] = dot(AdI, fd)
    q = Q0 + dot(B, qc)
    # critère
    loss = 1./3*dot(q, r*q*np.abs(q)) + dot(pr, dot(Ar, q))
    # TODO dérivée du critère par rapport à qc (à calculer)
    gradient = np.array([ 0 ])
    return loss, gradient

if __name__ == '__main__':
    # Test
    qc = np.random.normal(size=n-md)
    loss, gradient = oracle_pg(qc)
    print(loss, gradient)
