#!/usr/bin/python

import numpy as np
from scipy.optimize import minimize

from structure_r import *
from oracle import oracle_pg

qc0 = np.random.normal(size=n-md)
optimize_result = minimize(lambda qc: oracle_pg(qc)[0], qc0, jac=lambda qc: oracle_pg(qc)[1])

print(optimize_result)
