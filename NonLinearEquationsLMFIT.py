#!/usr/bin/env python

"""
Parameters needed to modify:
1. Target function
    def func(pars):...
    Also: helping functions such as Theta2d(theta)
2. Initial guess and parameters
"""

import numpy as np
from lmfit import Parameters, minimize, fit_report

def Theta2d(theta):
    Cu_lambda = 0.154056
    d = Cu_lambda / (2 * np.sin(theta*np.pi/180))
    return d

def func(pars):
    '''
    For (101), (200), (111), (210)
    1/d = sqrt((h^2 + k^2)/a^2) + l^2/c^2)

    x[0] -> a
    x[1] -> c
    '''
    parvals = pars.valuesdict()
    a = parvals["a"]
    c = parvals["c"]

    theta1 = 37.3134268
    theta2 = 40.9382663
    theta3 = 42.7843101
    theta4 = 46.0587182
    
    res1 = np.sqrt(1.0/a**2 + 1.0/c**2) - 1.0/Theta2d(theta1/2)
    res2 = np.sqrt(4.0/a**2 + 0.0/c**2) - 1.0/Theta2d(theta2/2)
    res3 = np.sqrt(2.0/a**2 + 1.0/c**2) - 1.0/Theta2d(theta3/2)
    res4 = np.sqrt(5.0/a**2 + 0.0/c**2) - 1.0/Theta2d(theta4/2)
    return np.array([res1, res2, res3, res4])

# Initial guess
params = Parameters()
params.add("a", value = 4.3999, min = 0)
params.add("c", value = 2.8740, min = 0)

# Calculation
out = minimize(func, params)

# Output
print(fit_report(out))