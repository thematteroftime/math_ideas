from class_one_dimention_search.symbols_store import *
from ND_dimension_optimization.Newton_method_ND import Newton_ND, m1, m2


def function(x1, x2):
    return 60 - 10 * x1 - 4 * x2 + x1 ** 2 + x2 ** 2 - x1 * x2


def function2(x1, x2):
    return 4 * (x1 + 1) ** 2 + 2 * (x2 - 1) ** 2 + x1 + x2 + 10


x0__ = np.array([0, 0])
x0_ = np.array([0, 0])
output = Newton_ND(function2, x0_=x0__, tol=1e-8, method_mod=m2, prec=8, x1=x1, x2=x2)
print(output)
