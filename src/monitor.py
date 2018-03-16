#!/usr/bin/python

import numpy as np
from oracle import *
<<<<<<< HEAD
from gradient import *

x0 = np.random.normal(size=n-md)

# Gradient a pas fixe
gradient(oracle, x0, use_wolfe=False)

# Gradient avec Wolfe
gradient(oracle, x0)
