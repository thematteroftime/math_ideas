import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# from decimal import Decimal, getcontext

# getcontext().prec = 15

def Fixed_point(func, x0, tol, interval=0, plot_choice="static"):
    x_arr = [x0]
    g_arr = []
    e_arr = []
    e_arr_prop = [0]
    plot_x = [x0, x0]
    plot_y = [0]

    count = 1
    max_iter = 200
    x1 = func(x0)

    x_arr.append(x1)
    g_arr.append(x1)
    plot_x.append(x1)
    plot_y.append(x1)
    plot_x.append(x1)
    plot_y.append(x1)

    while (abs(
            x_arr[count] - x_arr[count - 1]
    )) > tol:
        if max_iter <= count:
            print("Have been iterated ", max_iter)
            print("Not converge to a root")
            break
        try:
            x1 = func(x1)
        except OverflowError:
            print("The increment of this function is too large")
            print("Here is its plot")
            x = np.linspace(x0 - interval, x0 + interval, num=1000)
            y = func(x)
            plt.plot(x, y, 'r-', linewidth=2, label="Check Error")
            plt.title("FAILS", fontsize=24)
            plt.xlabel("X", fontsize=18)
            plt.ylabel("Y", fontsize=18)
            plt.grid()
            plt.legend()
            plt.show()
            return None
        else:
            x_arr.append(x1)
            g_arr.append(x1)
            count += 1

            plot_x.append(x1)
            plot_y.append(x1)
            plot_x.append(x1)
            plot_y.append(x1)

    g_arr.append(x1)
    plot_y.append(x1)
    r = x_arr[-1]

    for i in range(len(x_arr)):
        e_arr.append(abs(x_arr[i] - r))
    for i in range(len(e_arr)):
        if i == len(e_arr) - 1:
            break
        try:
            added = e_arr[i + 1] / e_arr[i]
        except ZeroDivisionError:
            e_arr_prop.append(0)
            print("Zero appear")
        else:
            e_arr_prop.append(added)

    table_lists = pd.DataFrame(data=np.array([x_arr, g_arr, e_arr, e_arr_prop]).T,
                               columns=['x0', 'g(x0)', 'ei', 'ei/ei-1'])
    # _______________________________mark___________________
    table_lists.round(8)
    table_lists.round({'ei': 10})
    print(table_lists)

    if count < max_iter:
        rate = dev_function(x_arr[-1])
        print("\nFE: ", e_arr[-1])
        print("BE: ", func(x_arr[-1]))
        print("Predicted rate is ", rate)
    print("\nKeep 15 decimal digits ", "{:.15f}".format(x_arr[-1]))
    print("Original data ", x_arr[-1])
    # print(Decimal(x_arr[-1]))

    if plot_choice == "static":
        plot_function(plot_x, plot_y, x_arr, interval, func)
    else:
        interactive_plot(plot_x, plot_y, x_arr, interval, func)

    return table_lists


def plot_function(plot_x, plot_y, x_arr, interval, func):
    plt.figure(dpi=80, figsize=(16, 9))
    plt.plot(plot_x, plot_y, 'b--', linewidth=1, label='Iteration plot')
    plt.scatter(plot_x, plot_y, c=range(len(plot_x)),
                edgecolors='none', cmap=plt.cm.Blues, s=80,
                label='Iteration point')

    x = np.linspace(min(x_arr) - interval / 10, max(x_arr) + interval / 10, num=1000)
    y_func = func(x)
    plt.plot(x, y_func, 'r-', linewidth=2, label='Function')
    plt.plot(x, x, 'b-', linewidth=2, label='diagonal line')
    plt.title("SUCCESS", fontsize=24)
    plt.xlabel("X", fontsize=18)
    plt.ylabel("Y", fontsize=18)

    plt.grid()
    plt.legend()
    plt.show()


def interactive_plot(plot_x, plot_y, x_arr, interval, func):
    x = np.array(plot_x)
    y = np.array(plot_y)

    x_func = np.linspace(min(x_arr) - interval, max(x_arr) + interval, num=2000)
    y_func = func(x_func)

    line_func = go.Scatter(x=x_func, y=y_func, name=f"line function",
                           mode="lines", line=dict(color="rgba(0,0,255, 1)", width=2))
    line_x = go.Scatter(x=x_func, y=x_func, name=f"line diagonal",
                        mode="lines", line=dict(color="rgba(255, 0, 0, 1)", width=2))

    colorscale = ['rgba(0,0,255,{})'.format(i) for i in np.linspace(0, 1, len(x))]

    scatter = go.Scatter(x=x, y=y, mode='markers', marker=dict(
        size=8,
        color=y,
        colorscale="Greys",
        opacity=0.8
    ))

    lines = []
    for i in range(1, len(x)):
        lines.append(
            go.Scatter(x=x[i - 1: i + 1], y=y[i - 1: i + 1], name=f"line Segment{i}",
                       mode="lines", line=dict(color=colorscale[i], width=2)))

    data = [scatter] + lines + [line_x, line_func]
    layout = go.Layout(title="function figure")

    fig = go.Figure(data=data, layout=layout)
    fig.show()


def function(x):
    try:
        fun_r = -4 * np.sin(x) + 2 * x
    except RuntimeWarning:
        print("It's too large or too tiny, please check your function expression")
        return None
    else:
        return fun_r


def dev_function(x):
    return abs(2 - 4 * np.cos(x))


a_list = Fixed_point(function, 1.5, 10 ** -8, interval=4, plot_choice='inter')
a_list.to_csv('prediction.csv')
"""
RuntimeWarning: divide by zero encountered in divide
    fun_r = 2.5 * (1 / (x ** 2 + x - 2)) + 1
"""
