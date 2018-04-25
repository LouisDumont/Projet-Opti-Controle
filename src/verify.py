#!/usr/bin/python

from .datas_r import *

from hydraulic import compute_hydraulic_p

import numpy as np
from numpy import dot, transpose as t

def verify_equilibrum(q, z, f, p):
    # Ecarts maximaux sur les lois de Kirschoff
    tol_debits = max(abs(dot(A, q) - f))
    tol_pression = max(abs(dot(t(A), p) + z))
    # Affichage
    print("Vérification des équations d'équilibre du réseau")
    print("Sur les débits : {}".format(tol_debits))
    print("Sur les pressions : {}".format(tol_pression))

if __name__ == '__main__':
    qc0 = np.random.normal(size=n-md)
    q, z, f, p = compute_hydraulic_p(qc0)
    verify_equilibrum(q, z, f, p)
