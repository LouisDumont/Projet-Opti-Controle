#!/usr/bin/python

from .datas_r import *

import numpy as np
from numpy import dot
from numpy import transpose as t

# On écrit "u" dans le programme pour "lambda" dans le lagrangien
# car lambda est un mot clé de python
def q_hat(u):
    a = - (dot(t(Ar), pr) + dot(t(Aq), u)) / r
    s = np.sign(a)
    return s*np.sqrt(np.abs(a))

def oracle(u, compute_gradient=True, compute_hessian=False):
    q = q_hat(u)
    # Critère
    loss = 1./3*dot(q, r*q*np.abs(q)) + dot(pr, dot(Ar, q)) + dot(t(u), dot(Ad, q) - fd)
    # Dérivée du critère par rapport à u
    gradient = dot(Ad, q) - fd if compute_gradient else None
    hessian = 2 * dot(t(B), t(r*abs(q)*t(B))) if compute_hessian else None
    
    return loss, gradient, hessian
