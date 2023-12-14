from class_one_dimention_search.symbols_store import *
import matplotlib.pyplot as plt
import math


# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)

def bisection_method(func, a1, b1, tol=1e-8, interval=1, points_number=1000, output="table", prec=8, max_iterate=200):
    if output not in ["table", "align", "plot"]:
        print("Invalid input of param output")
        return 0

    func = lambdify(x, func, "numpy")
    try:
        if func(a1) * func(b1) > 0:
            # plot_function(func, a1, b1, interval=interval, points_number=points_number)

            print("a = ", a1)
            print("fun(a) =  ", func(a1))
            print("b = ", b1)
            print("fun(b) =  ", func(b1))

            return 0.1

    except OverflowError:
        print("OverflowError")
        return 0.1

    pd.set_option('display.precision', prec)
    np.set_printoptions(precision=prec)
    a_arr = []
    b_arr = []
    c_arr = []
    c = 0

    pred_n = math.ceil(np.log2((b1 - a1) / tol) - 1) + 1
    count = 0

    while (b1 - a1) / 2 > tol:
        if count >= max_iterate:
            print("Overtime")
            if output == "align":
                return round((a_arr[-1] + b_arr[-1]) / 2, prec)
            break

        c = (b1 + a1) / 2
        count += 1

        a_arr.append(round(a1, prec))
        b_arr.append(round(b1, prec))
        c_arr.append(round(c, prec))

        if func(c) == 0:
            print("In the tolerance: ", tol)
            print("converge to a root directly:", c)
            return c

        if func(c) * func(a1) < 0:
            b1 = c
        else:
            a1 = c

    a_arr.append(round(a1, prec))
    b_arr.append(round(b1, prec))
    c_arr.append(round(c, prec))

    table = pd.DataFrame(data=np.array([a_arr, b_arr, c_arr]).T, columns=['a', 'b', 'c'],
                         index=list(range(1, count + 2)))

    if output == "plot":
        plot_function(func, a_arr, b_arr, c_arr, interval=interval, points_number=points_number)
    elif output == "table":
        print("-------------- Bisection Method --------------")
        print("In the tolerance: ", tol)
        print(table)
        print("total number of iterating: ", count)
        print("predicted iteration number: ", pred_n)
    elif output == "align":
        return round((a_arr[-1] + b_arr[-1]) / 2, prec)

    return table


def plot_function(func, a_arr, b_arr, c_arr, interval=1, points_number=1000):
    x_l = a_arr[0]
    x_r = b_arr[0]
    x = np.linspace(x_l - interval, x_r + interval, points_number)
    y = func(x)

    fig, ax = plt.subplots(dpi=85, figsize=(16, 9), layout="constrained")

    ax.plot(x, y, 'r-', linewidth=2, label='original curve')
    ax.scatter(c_arr, list(func(np.array(c_arr))), c=list(range(len(c_arr))), cmap=plt.cm.Blues, linewidths=1,
               label="middle point")

    ax.set_xlabel("X", fontsize=14)
    ax.set_ylabel("Y", fontsize=14)
    ax.set_title("Bisection method", fontsize=20)
    ax.legend(loc="upper left")
    ax.grid()
    plt.show()

    return 0
