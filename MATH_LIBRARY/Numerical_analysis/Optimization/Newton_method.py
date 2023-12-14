import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import *


def cal_formula(x0):
    return x0 - func_origin(x0) / diff_func(x0)


def func_origin(x):
    return x ** 3


def diff_func(x):
    return 3 * x ** 2


def double_diff_func(x):
    return 6 * x


def cal_e1_e0(e1, e0, judge):
    if judge: return e1 / e0
    return e1 / e0 ** 2


def cal_ei(x_arr, r, judge, prec):
    M_arr = [0]
    e_arr = []

    for i in range(len(x_arr)):
        e_arr.append(round(abs(r - x_arr[i]), prec))
    for i in range(len(x_arr) - 1):
        M_arr.append(round(cal_e1_e0(e_arr[i + 1], e_arr[i], judge), prec))

    return e_arr, M_arr


def plot_modul(x_arr, y_arr, M, r, tol):
    x_origin = np.linspace(min(x_arr) - 2, max(x_arr) + 2,
                           num=3000 if (max(x_arr) - min(x_arr)) <= 10
                           else int((max(x_arr) - min(x_arr))) * 500)
    y_origin = func_origin(x_origin)
    begin_x = x_arr[0]
    begin_y = y_arr[0]

    fig, ax = plt.subplots(figsize=(16, 9), dpi=75, layout="constrained")

    ax.scatter(x_arr, y_arr, c=list(range(len(x_arr))), cmap=plt.cm.Blues, linewidths=2, label="Iterated points")
    ax.plot(x_origin, y_origin, 'r-', label='original function', linewidth=2)
    ax.scatter(x_arr[0], y_arr[0], c='Red', linewidths=4, label="beginning point")

    ax.annotate("BEGINNING", xy=(begin_x, begin_y), xytext=(begin_x + 2, begin_y + 2),
                textcoords="offset points", horizontalalignment="left", verticalalignment="bottom",
                # arrowprops=dict(facecolor="black", shrink=0.5)
                fontsize=16, color="blue")

    ax.set_xlabel('X', fontsize=15)
    ax.set_ylabel('Y', fontsize=15)
    ax.set_title(f"SUCCESS CONVERGENCE M = {M}| r = {r}| tol = {tol}", fontsize=20)

    ax.legend(loc='upper left', fontsize='x-large')
    ax.grid()
    plt.show()

    return 0


def multiple_root_judge(r, prec):
    return round(diff_func(r), prec) != 0


def main(func, x0, tol=1e-4, prec=6, output='table', iter_n=100):
    y0 = func(x0)
    x_arr = [x0]
    y_arr = [y0]
    cal_step_arr = ["i=0"]

    i = 1
    while True:
        x1 = cal_formula(x0)
        y1 = func(x1)
        x_arr.append(round(x1, prec))
        y_arr.append(round(y1, prec))
        cal_step_arr.append(f"i={i}")

        if abs(x_arr[i] - x_arr[i - 1]) <= tol or round(func(x1), prec) == 0:
            r = x_arr[-1]
            judge = multiple_root_judge(r, prec=prec)
            M_pred = double_diff_func(r) / (2 * diff_func(r)) if not judge else 0
            print("success to converge to a root, r = ", r)
            print("The predicted convergent v is , M = ", M_pred)

            e_arr, M_arr = cal_ei(x_arr, r, judge, prec=prec)
            table = pd.DataFrame(data=np.array([cal_step_arr, x_arr, y_arr, e_arr, M_arr]).T,
                                 columns=["step_i", 'x', 'y', 'e_i', 'e(i)/e(i-1)^2'])

            if output == 'table':
                table.to_csv("./prediction.csv")
                print(table)
            elif output == 'plot':
                plot_modul(x_arr, y_arr, round(M_pred, prec), r, tol)

            return None, None, table
        elif i >= iter_n:
            print("Fail to converge to a root")
            break

        x0 = x1
        i += 1

    return x_arr, y_arr, None


x_arr, y_arr, table = main(func_origin, x0=-0.7, tol=1e-8, output='plot', prec=12)
print(table)
