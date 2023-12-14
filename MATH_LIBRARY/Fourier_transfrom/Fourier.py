import matplotlib.pyplot as plt
import numpy as np


# def formula_latter(a_k, b_k, k, x, l):
#     x = (np.pi * x) / l
#     a_term = (np.sin((k + 0.5) * x)) / (2 * np.sin(x / 2)) - 0.5
#     b_term = (np.cos(x / 2) - np.cos((k + 0.5) * x)) / (2 * np.sin(x / 2))
#     return a_k * a_term + b_k * b_term


def formula_latter_single(a_k_fun, b_k_fun, k_i, x, l):
    x = (k_i * np.pi * x) / l
    a_term = np.cos(x)
    b_term = np.sin(x)
    return a_k_fun(k_i, l) * a_term + \
        b_k_fun(k_i, l) * b_term


def formula_latter_all(a_k_fun, b_k_fun, k, x, l):
    sum = 0
    for i in range(1, k + 1):
        sum += formula_latter_single(a_k_fun, b_k_fun, i, x, l)
    return sum


def formula_former(a_0_fun, l):
    return a_0_fun(l)


def formula(a_0_fun, a_k_fun, b_k_fun, k, x, l):
    return formula_former(a_0_fun, l) + formula_latter_all(a_k_fun, b_k_fun, k, x, l)


"""
######################################################
"""


def a_0_fun(l):
    return 1


def a_k_fun(k_i, l):
    return 0


def b_k_fun(k_i, l):
    return -2 / (k_i * np.pi)


def origin_fun_x_y(l, T):
    x_arr = []
    y_arr = []
    x0 = np.linspace(0, 2 * l, 100)
    y0 = original_function(x0)
    for i in range(min(T), max(T)):
        x1 = x0 + i * 2 * l
        x_arr.extend(list(x1))
        y_arr.extend(list(y0))
    return x_arr, y_arr


def original_function(x):
    return 2 / np.pi * x

class get_y_arr():
    def __init__(self, y_arr):
        self.y_arr = y_arr
    def get_y_arr(self):
        return self.y_arr


"""
######################################################
"""

num = 5000
k = 400
l = np.pi / 2
T = 2 * l
left = -10
right = 10

order = list(range(1, num + 1))
size_of_points = list(np.linspace(5, 8, num))
x = np.linspace(left * T, right * T, num)
x_fun, y_fun = origin_fun_x_y(l, T=[left, right])
x = list(x)

y_arr = []
for i in range(num):
    y_arr.append(formula(a_0_fun, a_k_fun, b_k_fun, k, x[i], l))
output = get_y_arr(y_arr=y_arr)

plt.figure(dpi=85, figsize=(16, 9))
plt.plot(x, y_arr, 'r-', label='Fourier')
plt.plot(x_fun, y_fun, 'b--', label="Original")
plt.scatter(x, y_arr, c=order, cmap=plt.cm.Reds, edgecolors='none', s=size_of_points)
plt.title("Stimulate Fourier Series", fontsize=24)
plt.xlabel('x', fontsize=20)
plt.ylabel("F(x)", fontsize=20)
plt.legend(loc='lower right')
plt.grid()
plt.show()

# condition1 = (x >= 0) & (x % (2 * l) <= l)
# condition2 = (x <= 0) & (np.abs(x) % (2 * l) >= l)
# bool_array = condition1 | condition2
# x_fun = list(x[bool_array])
# y_fun = list(original_function(np.array(x))[bool_array])
