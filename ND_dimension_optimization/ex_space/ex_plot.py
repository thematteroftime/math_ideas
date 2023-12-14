import numpy as np
import matplotlib.pyplot as plt


def function(x):
    return -0.999999999999889 + 0.000108506944555565 * 2 * 5.12045572347119e-10 * (5.12045572347119e-10 * x - 1)


x_arr = np.linspace(-100, 100, 1000)
y_arr = function(x_arr)
plt.plot(x_arr, y_arr)
plt.grid()
plt.show()
