from class_one_dimention_search.one_dimension_search import search_1D
from class_one_dimention_search.symbols_store import *


def function(x):
    return x ** 3 - 2 * x + 1


a = search_1D(func=function(x), method="newton", x0=2, tol=1e-8, output='table', prec=8)
output = a.start()

