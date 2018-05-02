#!/usr/bin/python

from .datas_r import *

import numpy as np
from numpy import dot
from numpy import transpose as t

# On écrit "u" dans le programme pour "lambda" dans le lagrangien
# car lambda est un mot clé de python
def q_hat(u):
    a = - (dot(t(Ar), pr) + dot(t(Ad), u)) / r
    s = np.sign(a)
    delta = - np.diag(1/(r*np.sqrt(np.abs(a))))
    return (s*np.sqrt(np.abs(a)), delta)

def oracle(u, compute_gradient=True, compute_hessian=False):
    q, delta = q_hat(u)
    # Critère
    # on prend l'opposée du critère réel pour passer à un problème de minimisation
    loss = -(1./3*dot(q, r*q*np.abs(q)) + dot(pr, dot(Ar, q)) + dot(u, dot(Ad, q) - fd))
    # Dérivée du critère par rapport à u
    # On prend l'opposée du critère réel pour passer à un problème de minimisation
    gradient = -( dot(Ad, q) - fd) if compute_gradient else None
    hessian = -dot(dot(Ad, delta), t(Ad)) if compute_hessian else None
    
    return loss, gradient, hessian
