#!/usr/bin/python

from .datas_r import *
from .oracle import oracle

import numpy as np
from scipy.optimize import minimize


qc0 = np.random.normal(size=n-md)
optimize_result = minimize(lambda qc: oracle(qc)[0], qc0, jac=lambda qc: oracle(qc)[1])

print(optimize_result)
