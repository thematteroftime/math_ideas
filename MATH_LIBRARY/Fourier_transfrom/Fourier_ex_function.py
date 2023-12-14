import numpy as np
import matplotlib.pyplot as plt


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
    y_arr = []
    for i in range(len(x)):
        if x[i] >= 2 or x[i] <= 1:
            y_arr.append(1)
        else:
            y_arr.append(0)
    return y_arr


# x=np.linspace(0,3,100)
x, y = origin_fun_x_y(1.5, T=[-5, 5])
print(len(x))
plt.plot(x, y)
plt.show()
