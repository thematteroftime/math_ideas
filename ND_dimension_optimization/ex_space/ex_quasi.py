import pandas as pd

from ND_dimension_optimization.quasi_newton_method import quasi_newton_method
from class_one_dimention_search.one_dimension_search import search_1D
from class_one_dimention_search.symbols_store import *

default_model2 = search_1D(func=None, method="newton", x0=0, tol=1e-12, output='align',
                           prec=12, max_iterate=500)
pd.set_option("display.max_rows", None)


def function(x1, x2):
    return 2 * x1 ** 2 + 2 * x1 * x2 + x2 ** 2 + x1 - x2


def function2(x1, x2):
    return 4 * (x1 - 5) ** 2 + (x2 - 6) ** 2 + x1 * x2


def func(x):
    return 4 * (x[0] - 5) ** 2 + (x[1] - 6)


def func_grad(x):
    return [8 * (x[0] - 5), 1]


x0_ = np.array([8, 9])
x0 = np.array([0, 0])
output = quasi_newton_method(function2, x0_, tol=1e-8, prec=8,
                             model=default_model2, method="BFGS",
                             alpha_func=func, alpha_grad=func_grad, scipy_alpha=False,
                             x1=x1, x2=x2)
print(output)
