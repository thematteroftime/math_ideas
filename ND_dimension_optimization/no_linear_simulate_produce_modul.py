from class_one_dimention_search.symbols_store import *
import matplotlib.pyplot as plt


def target_function(y_arr, x_arr, func):
    target_list = []
    for i in range(len(y_arr)):
        target_list.append(y_arr[i] - func(x_arr[i]))

    return target_list


def Jacobian_matrix_np(symbols_list, func_list):
    Jacobian_output = []
    for i in range(len(func_list)):
        added_ = []
        for j in range(len(symbols_list)):
            added_.append(func_list[i].diff(symbols_list[j]))
        Jacobian_output.append(added_)

    return np.array(Jacobian_output)


def gradient_np(Jacobian_np, func_list):
    return 2 * np.dot(Jacobian_np.T, np.array(func_list))


def Hessian_np(Jacobian_np):
    return 2 * np.dot(Jacobian_np.T, Jacobian_np)


def no_linear_simulate(signal_list, time_list, symbols_list, func):
    target_func_list = target_function(signal_list, time_list, func)
    Jacobian_matrix_global = Jacobian_matrix_np(symbols_list, target_func_list)

    return target_func_list, Jacobian_matrix_global


def plot_modul(x_arr, y_arr, symbols_list, func, *args):
    var_list = []
    value_list = list(args)
    print(len(value_list))
    print(len(symbols_list))
    for i in range(len(symbols_list)):
        var_list.append((symbols_list[i], value_list[i]))

    expr1 = func(x)
    res_expr = expr1.subs(var_list)
    expr2 = lambdify(x, res_expr, "numpy")

    left = min(x_arr)
    right = max(x_arr)
    x_plot = np.linspace(left, right, num=int(right - left) * 200)
    y_plot = expr2(x_plot)

    fig, ax = plt.subplots(figsize=(16, 9), dpi=78, layout="constrained")
    ax.plot(x_plot, y_plot, 'r-', label="measurement", linewidth=2)
    ax.plot(x_arr, y_arr, 'b--', label="original data plot", linewidth=2)
    ax.scatter(x_arr, y_arr, s=35, label="original data points")
    ax.set_title("simulate no linear function", fontsize=24)
    ax.set_xlabel("X", fontsize=18)
    ax.set_ylabel("Y", fontsize=18)
    ax.grid()

    plt.show()
    return 0


def cal_target_func(target_func_list, symbols_list, *args):
    sum = 0
    for i in range(len(target_func_list)):
        sum += (lambdify(symbols_list, target_func_list[i], "numpy")(*args)) ** 2

    return sum
