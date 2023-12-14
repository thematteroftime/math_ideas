import matplotlib.pyplot as plt
import numpy as np
from operate_data.operate_digits import centerlize_number

c = 8

def function(x):
    return np.sin(x)


def diff_function(x):
    return np.cos(x)



fig, ax = plt.subplots(figsize=(16, 9), dpi=85)
X = np.arange(0, 10, 0.2)
Y = function(X)
x_plot = np.linspace(0, 10, 1000)
y_plot = function(x_plot)
diff_Y = diff_function(X)
o = np.arctan(diff_Y)

c = centerlize_number((min(diff_Y)+max(diff_Y))/2) * 4

U = np.cos(o) * diff_Y * c
V = np.sin(o) * diff_Y * c
M = np.hypot(U, V)
ax.plot(x_plot, y_plot, 'r-', linewidth=2)
step = 3
Q = ax.quiver(X[::step], Y[::step], U[::step], V[::step], M[::step], units='x', angles='xy', width=0.022, scale=1/0.15)
ax.grid()
plt.show()
