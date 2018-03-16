#!/usr/bin/python

import numpy as np
from oracle import *
from gradient import *

x0 = np.random.normal(size=n-md)
gradient(oracle,x0)