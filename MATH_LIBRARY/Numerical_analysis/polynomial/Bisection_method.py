import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def bisection_method(fun, a, b, tol, interval=1, points_number=1000):
    if fun(a) * fun(b) > 0:
        plot_function(fun, a, b, interval=interval, points_number=points_number)

        print("a = ", a)
        print("fun(a) =  ", fun(a))
        print("b = ", b)
        print("fun(b) =  ", fun(b))

        return 0

    all_data = [['a', 'b', 'c']]
    pred_n = math.ceil(np.log2((b - a) / tol) - 1) + 1
    iterate = 200
    count = 0

    while (b - a) / 2 > tol:
        if count >= iterate:
            print("Overtime")
            return
        c = (b + a) / 2

        all_data.append([a, b, c])

        if fun(c) == 0:
            print("converge to a root:", c)
            return c

        if fun(c) * fun(a) < 0:
            b = c
        else:
            a = c

        count += 1
    all_data.append([a, b, c])

    print(pd.DataFrame(data=all_data))
    print("total number of iterating:", pred_n)
    print(all_data[-1][-1])

    plot_function(fun, all_data[1][0], all_data[1][1], interval=interval, points_number=points_number)

    return all_data


def function(x):
    return x ** 3 + x - 1


def plot_function(fun, x_l, x_r, interval=1, points_number=1000):
    x = np.linspace(x_l - interval, x_r + interval, points_number)
    y = fun(x)

    plt.figure(dpi=80, figsize=(16, 9))
    plt.plot(x, y, 'r-', linewidth=2, label='predicted value')
    plt.grid()
    plt.legend()
    plt.show()


bisection_method(function, 5, 10, 10 ** -5, interval=1, points_number=10000)
"""
(x - 1) * (x - 2) * (x - 3) * (x - 4) * (x - 5) * (x - 6) * (x - 7) * (x - 8) * (x - 9) * (x - 10) * (
            x - 11) * (x - 12) * (x - 13) * (x - 14) * (x - 15) * (x - 16) * (x - 17) * (x - 18) * (x - 19) * (
            x - 20) - 2 * 10 ** -15 * x ** 15
"""
