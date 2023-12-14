from one_dimension_search import search_1D
from symbols_store import *


def function(x):
    return sp.sin(x) + x ** 2 * sp.cos(x) - x ** 2 - x


a = search_1D(func=function(x), method="newton", x0=4, tol=1e-10, output='table', prec=6)
b = search_1D(tol=1e-10, a1=-5, b1=10, func=function(x), method="compress", e=-0.05, output='table', prec=6)
c = search_1D(func=function(x), method="bisection", a1=0, b1=5, tol=1e-10, output='table',
              interval=1, points_number=10000, prec=6)
# d = search_1D(func=function(x), method="newton", x0=4, tol=1e-10, output='plot', prec=6)
# e = d.Newton()

print(a.start())
print(b.start())
print(c.start())
# print(d)
