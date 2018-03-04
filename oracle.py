#!/usr/bin/python

from datas import *

import numpy as np
from numpy import dot


def oracle(qc, compute_gradient=True, compute_hessian=False):
    Q0 = np.zeros(n)
    Q0[:md] = dot(AdI, fd)
    q = Q0 + dot(B, qc)
    # critère
    loss = 1./3*dot(q, r*q*np.abs(q)) + dot(pr, dot(Ar, q))
    # TODO dérivée du critère par rapport à qc (à calculer)
    gradient = np.zeros((len(qc), len(qc))) if compute_gradient else None
    hessian = np.zeros((len(qc), len(qc))) if compute_hessian else None
    return loss, gradient, hessian

if __name__ == '__main__':
    # Test
    qc = np.random.normal(size=n-md)
    loss, gradient, hessian = oracle(qc)
    print(loss)
    print(gradient)
    print(hessian)
