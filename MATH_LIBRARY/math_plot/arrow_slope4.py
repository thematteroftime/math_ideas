import matplotlib.pyplot as plt
import numpy as np
from operate_data.operate_digits import centerlize_number

c = 2e-1


def function(X, Y):
    return c / (X ** 2 + Y ** 2) ** 0.5


def x_func(x, y):
    return c * x / (x ** 2 + y ** 2) ** 1.5


def y_func(x, y):
    return c * y / (x ** 2 + y ** 2) ** 1.5


def X_dirction(X, Y):
    return X / (X ** 2 + Y ** 2) ** 0.5


def Y_dirction(X, Y):
    return Y / (X ** 2 + Y ** 2) ** 0.5


left = -6.2
right = 6.2
step = 0.4
pro_c = 1

fig, ax = plt.subplots(figsize=(16, 9), dpi=85)
X, Y = np.meshgrid(np.arange(left, right, 0.4), np.arange(left, right, 0.4))
func_value = function(X, Y)
x_grad = x_func(X, Y)
y_grad = y_func(X, Y)

pro_c = centerlize_number((abs(np.max(func_value)) + abs(np.min(func_value))) / 2)
U = X_dirction(x_grad, y_grad) * func_value * pro_c
V = Y_dirction(x_grad, y_grad) * func_value * pro_c
M = np.hypot(U, V)
a = np.array([[0], [9]])
print(type(a) == np.ndarray)
print([i for i in a.shape])
Q = ax.quiver(X, Y, U, V, M, units='xy', angles='xy', width=0.022, scale=1 / 0.2)
ax.grid()
plt.show()
