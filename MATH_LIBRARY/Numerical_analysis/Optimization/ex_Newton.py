from MATH_LIBRARY.Numerical_analysis.Optimization.Newton_sympy import Newton_method
import sympy as sp
import numpy as np

def function(x):
    return sp.sin(x) + x ** 2 * sp.cos(x) - x ** 2 - x


# sp.sin(x) + x ** 2 * sp.cos(x) - x ** 2 - x


table = Newton_method(function, x0=1/2, tol=1e-16, output='plot', prec=12)
print(table)
# copy_M_arr = np.array([0,0,4])
# arr = copy_M_arr[(copy_M_arr < 1) & (copy_M_arr > 0)]
# print(arr)
