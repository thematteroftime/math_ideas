from scipy.optimize import line_search
from class_one_dimention_search.symbols_store import *


def func(x):
    return 4 * (x[0] - 5) ** 2 + (x[1] - 6)


def func_grad(x):
    return [8 * (x[0] - 5), 1]


print(line_search(func, func_grad, np.array([4.994791666664, 8.874782986111]),
                  np.array([[2.666904024007e-12], [-9.999999999999e-01]]).flatten())[0])
