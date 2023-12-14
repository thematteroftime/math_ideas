from class_one_dimention_search.symbols_store import *
from class_one_dimention_search.one_dimension_search import search_1D
from ND_dimension_optimization.no_linear_simulate_produce_modul import *

pd.set_option('display.max_columns', None)
default_model = search_1D(func=None, method="newton", x0=0.5,
                          tol=1e-8, output='align', prec=8, max_iterate=200)
m1 = "no_modified"
m2 = "L-M"


def gradient(func, symbol_arr):
    gradient_arr = []
    for i in range(len(symbol_arr)):
        gradient_arr.append(func.diff(symbol_arr[i]))

    return gradient_arr


def cal_gradient(gradient_arr, x0_, symbol_arr):
    cal_gradient = []
    for i in range(len(symbol_arr)):
        cal_gradient.append(lambdify(symbol_arr, gradient_arr[i], "numpy")(*x0_))

    return cal_gradient


def Hessian_matrix(symbol_arr, gradient_arr):
    hessian_matrix = []

    for i in range(len(symbol_arr)):
        addition_arr = []

        for j in range(len(symbol_arr)):
            addition_arr.append(gradient_arr[i].diff(symbol_arr[j]))

        hessian_matrix.append(addition_arr)

    return hessian_matrix


def cal_Hessian_matrix(hessian_matrix, x0, symbol_arr):
    caled_hessian_matrix = []
    for i in range(len(symbol_arr)):
        operate_arr = []
        for j in range(len(symbol_arr)):
            operate_arr.append(lambdify(symbol_arr, hessian_matrix[i][j], "numpy")(*x0))

        caled_hessian_matrix.append(operate_arr)

    return caled_hessian_matrix


def norm(vector):
    sum = 0
    for i in range(len(vector)):
        sum += vector[i] ** 2
    return sum ** 0.5


def cal_modify_matrix(cal_hessian_matrix_, u=0.0, h=0.1, method="no_modified"):
    if method == "L-M":
        matrix_Q = []
        max_iter_n = 1000000
        i_count = 0

        while True:
            last_u = float(u)
            matrix_Q = cal_hessian_matrix_ + u * np.eye(int(cal_hessian_matrix_.size ** 0.5))
            eigenvalue, feature_vector = np.linalg.eig(matrix_Q)
            i_count += 1
            for i in eigenvalue:
                if i <= 0:
                    u += h
                    break
            if last_u == u:
                break

            if i_count >= max_iter_n:
                print("Fail to get a modified matrix")
                return matrix_Q

        return matrix_Q

    elif method == "no_modified":
        return cal_hessian_matrix_


def Newton_ND(func, x0_, tol=1e-5, model=default_model, method_mod="no_modified",
              max_iterate=200, prec=5, h=0.1, signal_list=None, time_list=None, no_linear_=False, *args, **kwargs):
    model.property['tol'] = tol
    model.property['prec'] = prec
    pd.set_option('display.precision', prec)
    np.set_printoptions(precision=prec)

    method_choice = ["no_modified", "L-M"]
    if method_mod not in method_choice:
        print("Invalid input of method")
        return 0

    symbol_arr = list(args) if kwargs == {} else [value for key, value in kwargs.items()]
    if no_linear_:
        target_func_list, Jacobian_matrix_ = no_linear_simulate(signal_list, time_list, symbol_arr, func)

    expr = func(*symbol_arr) if not no_linear_ else \
        target_func_list
    cal_expr = lambdify(symbol_arr, expr, "numpy") if not no_linear_ else \
        lambda *args: cal_target_func(target_func_list, symbol_arr, *args)  #

    gradient_arr = gradient(expr, symbol_arr) if not no_linear_ else \
        gradient_np(Jacobian_matrix_, target_func_list).flatten()
    hessian_matrix_ = Hessian_matrix(symbol_arr, gradient_arr) if not no_linear_ else \
        Hessian_np(Jacobian_matrix_)

    print(f"-------------- Newton Method ND with no linear simulate {method_mod} --------------")
    i = 0
    x_arr = [list(x0_)]
    z_arr = [cal_expr(*x0_)]
    while True:
        print(f"---------- i = {i} -----------")
        cal_gradient_ = np.array(cal_gradient(gradient_arr, x0_, symbol_arr))
        cal_hessian_matrix_ = np.array(cal_Hessian_matrix(hessian_matrix_, x0_, symbol_arr))

        modified_matrix = cal_modify_matrix(cal_hessian_matrix_, u=0, h=h, method=method_mod)
        d_ = np.dot(np.linalg.inv(modified_matrix), cal_gradient_)

        if no_linear_:
            x1_ = x0_ - d_
        else:
            model.change_func(func(*(x0_ - x * d_)))
            r = model.start()
            print(r)
            x1_ = x0_ - r * d_

        x_arr.append(list(x1_))
        z_arr.append(cal_expr(*x1_))
        i += 1

        if abs(norm(np.array(x_arr[i - 1]) - np.array(x_arr[i]))) <= tol:
            break
        if i >= max_iterate:
            print(f"After {max_iterate} times iterations ")
            print("Fail to converge to a root")
            break

        x0_ = x1_

    symbol_arr.append("Z")
    table = pd.DataFrame(data=np.hstack((x_arr, [[i] for i in z_arr])).reshape(len(x_arr), len(symbol_arr)),
                         columns=symbol_arr)
    if no_linear_:
        symbol_arr.pop()
        plot_modul(time_list, signal_list, symbol_arr, func, *x_arr[-1])

    return table
