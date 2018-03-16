#!/usr/bin/python

import numpy as np
from oracle import *
from gradient_fixe import *

x0 = np.random.normal(size=n-md)
gradient(oracle,x0,iter_max=10)