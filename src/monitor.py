#!/usr/bin/python

import numpy as np
from oracle import *
from gradient import *
from newton import *

x0 = np.random.normal(size=n-md)

# Gradient a pas fixe
print("Gradient à pas fixe")
gradient(oracle, x0, default_gradient_step=0.0001, use_wolfe=False)
print()

# Gradient avec Wolfe
print("Gradient à pas optimal (Wolfe)")
gradient(oracle, x0)
print()

# Gradient avec Polak
gradient_polak(oracle, x0)
print()

# Newton
print("Méthode de Newton")
newton(oracle, x0)
print()
