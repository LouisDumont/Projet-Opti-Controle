#!/usr/bin/python

import numpy as np
from numpy.linalg import inv
from numpy import dot

# ====================================

# Nom du réseau
nom = 'Realiste'


# Dimensions du réseau

# Nombre d'arcs
n = 22
# Nombre de noeuds
m = 16
mr = 3
md = m - mr


# Numéros des noeuds initiaux et finaux des arcs
orig = np.array([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 13, 1, 2, 4, 5, 7, 8, 14, 2, 10])
orig = orig - 1 # Python commence à 0
dest = np.array([4, 16, 15, 5, 6, 10, 16, 9, 12, 10, 11, 14, 15, 16, 6, 8, 9, 11, 13, 15, 4, 13])
dest = dest - 1 # Python commance à 0


# Coordonnées des noeuds
absn = np.array([11, 18, 38, 4, 8, 15, 26, 4, 10, 19, 26, 7, 21, 33, 33, 16])
ordn = np.array([28, 21, 8, 21, 17, 17, 26, 9, 13, 13, 18, 4, 9, 18, 12, 24])


# Résistances des arcs
r = np.array([100, 10, 1000, 100, 100, 10, 1000, 100, 1000, 100, 1000, 1000, 1000, 10, 10, 100 , 100, 1000, 100, 1000, 100, 10])


# Pressions au pied des réservoirs (en m)
pr = np.array([105, 104, 110])


# Flux aux noeuds de demande (en m3/s)
fd = np.array([+0.08, -1.30, +0.13, +0.09, +0.16, +0.14, +0.12, +0.07, +0.17, +0.11, +0.25, +0.01, +0.13])


# ====================================

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
