from class_one_dimention_search.symbols_store import *
from ND_dimension_optimization.simulate_no_linear_function import Newton_ND, m1, m2
import matplotlib.pyplot as plt


def function(x):
    return 19 * x ** 3 + 2 * x ** 2 + 5 * x + -9 * np.sin(-1 * x)


def function_(x):
    return A * x ** 3 + B * x ** 2 + C * x + E * sp.sin(D + x)


num = 40
y_noise1 = np.random.rand(1, num).flatten()
y_noise2 = np.random.rand(1, num).flatten()

x_sin = np.linspace(0, 10, num)
y_sin = function(x_sin)

y_sin_with_noise = y_sin + (y_noise1 - y_noise2) / 2

x0_ = np.array([-1, 0, 15, -4, 10])
output = Newton_ND(function_, x0_=x0_, tol=1e-14, method_mod=m2, prec=14,max_iterate=100,
                   no_linear_=True, signal_list=y_sin, time_list=x_sin,
                   A=A, B=B, C=C, D=D, E=E)
print(output)
