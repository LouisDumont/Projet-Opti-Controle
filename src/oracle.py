#!/usr/bin/python

from .datas_r import *

import numpy as np
from numpy import dot
from numpy import transpose as t

def oracle(qc, compute_gradient=True, compute_hessian=False):
    Q0 = np.zeros(n)
    Q0[:md] = dot(AdI, fd)
    q = Q0 + dot(B, qc)
    # Critère
    loss = 1./3*dot(q, r*q*np.abs(q)) + dot(pr, dot(Ar, q))
    # Dérivée du critère par rapport à qc (à calculer)
    gradient = dot(t(B), r*q*abs(q)) + dot(dot(t(B), t(Ar)), pr) if compute_gradient else None
    hessian = 2 * dot(t(B), t(r*abs(q)*t(B))) if compute_hessian else None
    
    return loss, gradient, hessian
