#!/usr/bin/python

import numpy as np
from numpy.linalg import inv
from numpy import dot

np.set_printoptions(linewidth=np.inf)

from problem_r import *

# Matrice d'incidence noeuds-arcs du graphe
A = np.zeros((m, n))
for i in range(m):
    A[i, orig == i] = -1
    A[i, dest == i] = +1

# Partition de A suivant le type des noeuds
Ar = A[:mr,:]
Ad = A[mr:m,:]

# Sous-matrice de Ad associee a un arbre et inverse
AdT = Ad[:,:md]
AdI = inv(AdT)

# Sous matrice de Ad associee a un coarbre
AdC = Ad[:,md:n]

# Matrice d'incidence arcs-cycles
B = np.zeros((n, n-md))
B[:md,:] = -dot(AdI, AdC)
B[md:,:] = np.eye(n-md)

# Vecteur des debits admissibles
q0 = np.zeros(n)
q0[:md] = dot(AdI,fd)
