from one_dimension_search import search_1D
from ND_dimension_optimization.gradient_class import main
from symbols_store import *
pd.set_option("display.max_rows", None)

def function(x1, x2, x3, x4):
    return (x1 - 2) ** 4 + (x2 - 4) ** 2 + 4 * (x3 + 7) ** 4 + 7 * (x4 + 2) ** 2 + x1 * x4


model = search_1D(func=None, method="bisection", a1=0, b1=100, output='align')
x_arr = main(function, x0=np.array([3, 1, -1, 5]),
             model=model, tol=1e-4, max_iterate=200,
             x1=x1, x2=x2, x3=x3, x4=x4)
print(x_arr)
