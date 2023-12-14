from class_one_dimention_search.one_dimension_search import search_1D
from class_one_dimention_search.symbols_store import *
from ND_dimension_optimization.gradient_class import gradient_descent


def function(x1, x2):
    return x1 ** 2 + 25 * x2 ** 2


model = search_1D(func=None, method="bisection", a1=0, b1=50,
                  tol=1e-16, output='align',
                  prec=16, max_iterate=500)
x0_ = np.array([2, 2])
x_arr = gradient_descent(function, x0_, prec=12,
                         model=model, tol=1e-8, max_iterate=200,
                         x1=x1, x2=x2)
# -0.250000000000 -2.366582715663e-29  1.500000000000 -0.125000000000
print(x_arr)
