import numpy as np
import matplotlib.pyplot as plt


def implicit_func(x, y):
    return x ** 4 + 6 * x ** 2 * y ** 2 + y ** 4 - 1


x = np.linspace(-1, 1, 1000)
y = np.linspace(-1, 1, 1000)

X, Y = np.meshgrid(x, y)
Z = implicit_func(X, Y)

plt.contour(X, Y, Z, [0], colors='black')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of x^2 + y^2 + i * 2xy = 1')

plt.grid()
plt.show()
