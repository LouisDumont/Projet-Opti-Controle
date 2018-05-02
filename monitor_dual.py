#!/usr/bin/python

import numpy as np
from src.oracle_lagrange import *
from src.gradient import *
from src.newton import *
from src.gradient_conjug_polak import *
from src.bfgs import * 

u0 = np.random.normal(size=md)

# Gradient a pas fixe
print("Gradient à pas fixe")
gradient(oracle, u0, default_gradient_step=0.0001, use_wolfe=False)
print()

# Gradient avec Wolfe
print("Gradient à pas optimal (Wolfe)")
gradient(oracle, u0, verbose=True, iter_max=10)
print()

# Gradient avec Polak
print("Gradient conjugé, variante de Polak-Ribières")
gradient_polak(oracle, u0)
print()

# Newton
print("Méthode de Newton")
newton(oracle, u0)
print()

# BFGS
print("Méthode de Newton approchée: BFGS")
bfgs(oracle, u0)
print()
