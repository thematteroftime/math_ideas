import numpy as np
import pandas as pd
import plotly.graph_objects as go
from MATH_LIBRARY.Learn_from_books.Fibonacci import produce_p


def cal_a2(a1, b1, p):
    return a1 + p * (b1 - a1)


def cal_b2(a1, b1, p):
    return b1 - p * (b1 - a1)


def get_p(method, a1, b1, tol, e):
    if method == "gold":
        return 0.382
    elif method == "Fibon":
        return produce_p((1 + 2 * e) * (b1 - a1) / tol, e)
    else:
        print("invalid input")
        return -1


def add_prec(x, prec):
    return round(x, prec)


def plot_inter(a_arr, b_arr, fun):
    left = min(a_arr)
    right = max(b_arr)

    colorscale = ["rgba(20,20,255,{})".format(i) for i in np.linspace(0.2, 1, len(a_arr))]
    x = np.linspace(left, right, num=1000)
    y = fun(x)

    plot1 = go.Scatter(x=x, y=y, name="Function plot",
                       mode="lines", line=dict(color="rgba(255, 20, 20, 1)", width=2))

    # choose_number = lambda a, b: fun(a) if fun(a) < fun(b) else fun(b)
    center_point = fun((max(a_arr) + min(b_arr)) / 2)
    increment = abs(fun(min(a_arr)) - fun(min(b_arr))) / 2

    lines = []
    length = len(a_arr)
    for i in range(length):
        prop = 1 - i / (length + 5)
        increment *= prop
        y_ceil = center_point + increment
        y_floor = center_point - increment
        y_plot = [y_floor, y_ceil]
        lines.append(go.Scatter(x=[a_arr[i], a_arr[i]], y=y_plot, name=f"line {i}",
                                mode="lines", line=dict(color=colorscale[i], dash="dot", width=2)))
        lines.append(go.Scatter(x=[b_arr[i], b_arr[i]], y=y_plot, name=f"line {i}",
                                mode="lines", line=dict(color=colorscale[i], dash="dot", width=2)))
    print("add data OK")

    data = [plot1] + lines
    layout = go.Layout(title="picture")

    fig = go.Figure(data=data, layout=layout)
    fig.show()
    print("produce picture OK")


def plot_stat(a_arr, b_arr, fun):
    print()


def compress_interval_method(tol, a1, b1, fun, method="gold", prec=6, e=0.1):
    n = 1
    a1_arr = [a1]
    b1_arr = [b1]
    b1_minus_a1_arr = [b1 - a1]
    p = get_p(method, a1, b1, tol, e)
    if p == -1:
        return 0

    if method == "Fibon":
        a2 = cal_a2(a1, b1, p[0])
        b2 = cal_b2(a1, b1, p[0])
        p.append(0.382)
    else:
        a2 = cal_a2(a1, b1, p)
        b2 = cal_b2(a1, b1, p)

    a2_arr = [add_prec(a2, prec)]
    b2_arr = [add_prec(b2, prec)]
    fun_a2_arr = []
    fun_b2_arr = []

    while (b1 - a1) > tol:
        if method == "Fibon":
            p_run = p[n]
        else:
            p_run = p
        fun_a = fun(a2)
        fun_b = fun(b2)
        if fun_a < fun_b:
            b1 = b2
            b2 = a2
            a2 = cal_a2(a1, b1, p_run)
        elif fun_a > fun_b:
            a1 = a2
            a2 = b2
            b2 = cal_b2(a1, b1, p_run)
        else:
            a1 = a2
            b1 = b2

        n += 1
        a1_arr.append(add_prec(a1, prec))
        b1_arr.append(add_prec(b1, prec))
        a2_arr.append(add_prec(a2, prec))
        b2_arr.append(add_prec(b2, prec))
        b1_minus_a1_arr.append(add_prec(b1 - a1, prec))
        fun_a2_arr.append(add_prec(fun_a, prec))
        fun_b2_arr.append(add_prec(fun_b, prec))

    fun_a2_arr.append(add_prec(fun(a1), prec))
    fun_b2_arr.append(add_prec(fun(b1), prec))
    fun_a1_arr = list(fun(np.array(a1_arr.copy())))
    fun_b1_arr = list(fun(np.array(b1_arr.copy())))

    plot_inter(a1_arr, b1_arr, fun)

    data = [a1_arr, b1_arr, a2_arr, b2_arr,
            fun_a1_arr, fun_b1_arr, fun_a2_arr, fun_b2_arr,
            b1_minus_a1_arr]
    columns = ['a1', 'b1', 'a2', 'b2',
               'fun(a1)', 'fun(b1)', 'fun(a2)', 'fun(b2)',
               'b1-a1']

    if method == "Fibon":
        data.append(p)
        columns.append('p')

    print("\t \t \t \t \t--------- ", method, "method ---------")
    data = pd.DataFrame(data=np.array(data).T, columns=columns)

    print(data)

    return round(a1, prec), round(b1, prec), data


def function(x):
    return x ** 4 - 14 * x ** 3 + 60 * x ** 2 - 70 * x


a, b, data = compress_interval_method(0.01, 0, 2, function, method="Fibon", e=-0.05)
data.to_csv("./output/result.csv")
