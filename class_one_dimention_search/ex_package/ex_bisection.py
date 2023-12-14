from class_one_dimention_search.one_dimension_search import search_1D
from class_one_dimention_search.symbols_store import *


def function(x):
    return x * (x + 2)


a = search_1D(func=function(x), method="bisection", a1=-3, b1=5, tol=1e-5, output='table', prec=6)
output = a.start()
print(output)
