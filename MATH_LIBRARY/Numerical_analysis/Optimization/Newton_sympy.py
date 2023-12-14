import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import *

x = symbols("x")
diff_func = None
double_diff_func = None
func_origin = None


def cal_formula(x0):
    return x0 - func_origin(x0) / diff_func(x0)


def cal_e1_e0(e1, e0, judge):
    if judge: return e1 / e0
    try:
        output = e1 / e0 ** 2
    except ZeroDivisionError:
        return 0
    else:
        return output


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
    return round(diff_func(r), prec) == 0


def multiple_M(r, prec):
    if round(double_diff_func(r), prec) == 0: return 2 / 3
    return 1 / 2

output = 0
def iterate_M(r, expr, prec, i=1):
    global output
    expr_diff = lambdify(x, expr.diff(x, i), "numpy")

    if round(expr_diff(r), prec) != 0:
        output = (i - 1) / i
        return output
    else:
        iterate_M(r, expr, prec, i + 1)
    return output


def Newton_method(func, x0, tol=1e-4, prec=6, output='table', iter_n=100, num=None):
    global diff_func, double_diff_func, func_origin
    expr = func(x)
    func_origin = lambdify(x, expr, "numpy")
    diff_func = lambdify(x, expr.diff(x), "numpy")
    double_diff_func = lambdify(x, expr.diff(x, 2), "numpy")

    y0 = round(func(x0), prec)
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

        if (abs(x_arr[i] - x_arr[i - 1]) <= tol or round(func(x1), prec) == 0) \
                and (num == None or i >= num):
            r = x_arr[-1]
            judge = multiple_root_judge(r, prec=prec)
            M_pred = double_diff_func(r) / (2 * diff_func(r)) if not judge else iterate_M(r, expr, prec=prec)
            e_arr, M_arr = cal_ei(x_arr, r, judge, prec=prec)
            # copy_M_arr = np.array(M_arr[:])
            # copy_M_arr[(copy_M_arr < 1) & (copy_M_arr > 0)]
            # choose mean value

            print("success to converge to a root, r = ", r)
            print("The predicted convergent v is , M = ", M_pred)

            table = pd.DataFrame(data=np.array([cal_step_arr, x_arr, y_arr, e_arr, M_arr]).T,
                                 columns=["step_i", 'x', 'y', 'e_i', 'e(i)/e(i-1)^2'])

            if output == 'table':
                print(table)
            elif output == 'plot':
                plot_modul(x_arr, y_arr, round(M_pred, prec), r, tol)
            elif output == 'align':
                return r
            else:
                print("Invalid input")
                return 0

            return table
        elif (i >= iter_n) and (num == None):
            table = pd.DataFrame(data=np.array([cal_step_arr,x_arr, y_arr]).T,
                                 columns=["step_i", 'x', 'y'])
            print("Fail to converge to a root")
            break

        x0 = x1
        i += 1

    return table

# x_arr, y_arr, table = Newton_method(func_origin, x0=-0.7, tol=1e-8, output='plot', prec=12)
# print(table)
