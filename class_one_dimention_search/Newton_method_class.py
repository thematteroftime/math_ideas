import matplotlib.pyplot as plt
from class_one_dimention_search.symbols_store import *

diff_func = None
double_diff_func = None
func_origin = None


def cal_formula(x0, tol):
    try:
        division = func_origin(x0) / diff_func(x0)
    except ZeroDivisionError:
        return x0 - tol
    return x0 - division


def cal_e1_e0(e1, e0, judge):
    if e0 != 0:
        if judge: return e1 / e0
        return e1 / (e0 ** 2)
    else:
        return 0


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
    end_x = x_arr[-1]
    begin_y = y_arr[0]
    end_y = y_arr[-1]
    interval_x = (end_x - begin_x) / 4
    interval_y = (end_y - begin_y) / 4

    fig, ax = plt.subplots(figsize=(16, 9), dpi=85, layout="constrained")

    ax.scatter(x_arr, y_arr, c=list(range(len(x_arr))), cmap=plt.cm.Blues, linewidths=2, label="Iterated points")
    ax.plot(x_origin, y_origin, 'r-', label='original function', linewidth=2)
    ax.scatter(x_arr[0], y_arr[0], c='Red', linewidths=4, label="beginning point")

    ax.annotate("BEGINNING", xy=(begin_x, begin_y), xytext=(begin_x + interval_x, begin_y + interval_y),
                textcoords="offset points", horizontalalignment="left", verticalalignment="bottom",
                arrowprops=dict(facecolor="black", shrink=0.5),
                fontsize=14, color="blue")

    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_title(f"SUCCESS CONVERGENCE M = {M}| r = {r}| tol = {tol}", fontsize=16)

    ax.legend(loc='upper left', fontsize='x-large')
    ax.grid()
    plt.show()

    return 0


def multiple_root_judge(r, prec):
    return round(diff_func(r), prec) == 0


output = 0.5
max_inter_n = 10


def iterate_M(r, expr, prec, i=2):
    global output, max_inter_n

    expr_diff = lambdify(x, expr.diff(x, 2), "numpy")
    if i >= max_inter_n:
        output = 1
        return output

    if round(expr_diff(r), prec) != 0:
        output = (i - 1) / i
        return output
    else:
        iterate_M(r, expr, prec, i + 1)

    return output


def Newton_method(func, x0, tol=1e-4, prec=6, output='table', max_iterate=100, num=None):
    global diff_func, double_diff_func, func_origin

    if output not in ["table", "align", "plot"]:
        print("Invalid input of param output")
        return 0

    pd.set_option('display.precision', prec)
    np.set_printoptions(precision=prec)
    func_origin = lambdify(x, func, "numpy")
    diff_func = lambdify(x, func.diff(x), "numpy")
    double_diff_func = lambdify(x, func.diff(x, 2), "numpy")

    y0 = round(func_origin(x0), prec)
    r = 0
    M_pred = 0
    x_arr = [x0]
    y_arr = [y0]
    cal_step_arr = ["i=0"]

    i = 1
    while True:
        x1 = cal_formula(x0, tol)
        if output != "align":
            y1 = func_origin(x1)
            y_arr.append(round(y1, prec))
            cal_step_arr.append(f"i={i}")
        x_arr.append(round(x1, prec))

        if (abs(x_arr[i] - x_arr[i - 1]) <= tol or round(func_origin(x1), prec) == 0) \
                and (num == None or i >= num):
            r = x_arr[-1]
            if output == 'align':
                return r

            judge = multiple_root_judge(r, prec=prec)
            M_pred = double_diff_func(r) / (2 * diff_func(r)) if not judge else iterate_M(r, func, prec=prec)
            e_arr, M_arr = cal_ei(x_arr, r, judge, prec=prec)

            print("In the tolerance: ", tol)
            print("success to converge to a root, r = ", r)
            print("The predicted convergent v is , M = ", M_pred)

            table = pd.DataFrame(data=np.array([cal_step_arr, x_arr, y_arr, e_arr, M_arr]).T,
                                 columns=["step_i", 'x', 'y', 'e_i', 'e(i)/e(i-1)^2'])

            if output == 'table':
                print("----------------- Newton Method -----------------")
                print(table)
            elif output == 'plot':
                plot_modul(x_arr, y_arr, round(M_pred, prec), r, tol)

            break
        elif (i >= max_iterate) and (num == None):
            print("In the tolerance: ", tol)
            print("Fail to converge to a root")
            if output == 'align':
                return round(x_arr[-1], prec)

            table = pd.DataFrame(data=np.array([cal_step_arr, x_arr, y_arr]).T,
                                 columns=["step_i", 'x', 'y'])
            break

        x0 = x1
        i += 1

    return table
