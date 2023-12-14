import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

choice = '2D'
# o = np.pi / 4
close = 1
# [[np.cos(o), -np.sin(o)], [np.sin(o), np.cos(o)]]
input_a = [[0.75, 0.1875], [0, 1]]
A = np.array(input_a)

input_x = [[0, 0], [0.5, 0], [0.5, 6.42], [6, 0], [6, 8], [5.5, 8], [5.5, 1.58], [0, 8]]
X = np.array(input_x)

new_X = np.dot(A, X.T).T

x = []
y = []
x_new = []
y_new = []

for i in range(len(X) + close):
    index = i % len(X)
    elem = X[index]
    x.append([elem[0]])
    y.append([elem[1]])

for i in range(len(new_X) + close):
    index = i % len(new_X)
    elem = new_X[index]
    x_new.append([elem[0]])
    y_new.append([elem[1]])

if choice == '2D':
    plt.figure(figsize=(12, 12))
    plt.plot(x, y, 'r-', linewidth=2, label="plot_old")
    plt.scatter(x, y, c='red', label='point_old')

    plt.plot(x_new, y_new, 'b--', linewidth=2, label="plot_new")
    plt.scatter(x_new, y_new, c='blue', label='point_new')

    plt.xlabel(xlabel="X", fontsize=14)
    plt.ylabel(ylabel="Y", fontsize=14)

elif choice == '3D':
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(projection="3d")
    z = []
    z_new = []
    for i in range(len(X) + close):
        index = i % len(X)
        elem = X[index]
        z.append([elem[2]])
    for i in range(len(new_X) + close):
        index = i % len(new_X)
        elem = new_X[index]
        z_new.append([elem[2]])

    ax.plot(x, y, z, 'r-', linewidth=2, label="plot_old")
    ax.scatter(x, y, z, c='red', label="point_old")

    ax.plot(x_new, y_new, z_new, 'b--', linewidth=2, label="plot_new")
    ax.scatter(x_new, y_new, z_new, c='blue', label="point_new")

    plt.xlabel(xlabel='X', fontsize=14)
    plt.ylabel(ylabel='Y', fontsize=14)

plt.legend()
plt.grid()
plt.show()
