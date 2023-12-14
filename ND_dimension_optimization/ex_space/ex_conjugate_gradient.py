from class_one_dimention_search.symbols_store import *
from ND_dimension_optimization.conjugate_gradient_method import conjugate_gradient_method, m1, m2, m3

pd.set_option("display.max_rows", None)


def function(x1, x2):
    return (3 * x1 - 2 * x2) ** 2 + (x1 - 1) ** 4


x0_ = np.array([4, -2])
output = conjugate_gradient_method(function, x0_, tol=1e-8, prec=8, method_coff=m2, x1=x1, x2=x2)
print(output)
