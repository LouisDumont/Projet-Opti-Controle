#!/usr/bin/python

import numpy as np
from oracle import *
from gradient import *
from gradient_conjug_polak import *

x0 = np.random.normal(size=n-md)
gradient_polak(oracle,x0)