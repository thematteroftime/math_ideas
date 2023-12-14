from class_one_dimention_search.symbols_store import *
from class_one_dimention_search.one_dimension_search import search_1D

pd.set_option('display.max_columns', None)
default_model = search_1D(func=None, method="newton", x0=0.5, tol=1e-8, output='align', prec=8, max_iterate=80)
m1 = "Hestenes_Stiefel"
m2 = "Polak_Ribiere"
m3 = "Flectcher_Reeves"


def gradient_sp(expr, symbols_list):
    gradient_output_list = []
    for i in range(len(symbols_list)):
        gradient_output_list.append(expr.diff(symbols_list[i]))

    return gradient_output_list


def cal_gradient_np(x0_, gradient_list, symbols_list):
    cal_gradient_output = []
    for i in range(len(symbols_list)):
        cal_gradient_output.append(lambdify(symbols_list, gradient_list[i], "numpy")(*x0_))

    return np.array(cal_gradient_output)


def cal_vector_norm(vector):
    sum = 0
    for i in range(len(vector)):
        sum += vector[i] ** 2
    return sum ** 0.5


def cal_beta_formula(gradient_0, gradient_1, d_0, method_coff):
    save = 0
    if method_coff == m1:
        part1 = gradient_1 - gradient_0
        numerator = np.dot(gradient_1, part1)
        denominator = np.dot(d_0, part1)
        save = numerator / denominator
    elif method_coff == m2:
        part1 = gradient_1 - gradient_0
        numerator = np.dot(gradient_1, part1)
        denominator = np.dot(gradient_0, gradient_0)
        save = numerator / denominator
    elif method_coff == m3:
        numerator = np.dot(gradient_1, gradient_1)
        denominator = np.dot(gradient_0, gradient_0)
        save = numerator / denominator

    return save


def initialize_condition(d0_vec, g0_vec):
    return np.dot(d0_vec, g0_vec) / \
        (cal_vector_norm(d0_vec) * cal_vector_norm(g0_vec))


def conjugate_gradient_method(func, x0_, tol=1e-4, prec=4, model=default_model, init_cond=0.2,
                              method_coff="Hestenes_Stiefel", no_linear=False, max_iterate=200,
                              check=False, *args, **kwargs):
    method_choice = ["Hestenes_Stiefel",
                     "Polak_Ribiere",
                     "Flectcher_Reeves"]
    if method_coff not in method_choice:
        print("Invalid input of method")
        return 0

    model.property['tol'] = tol
    model.property['prec'] = prec
    pd.set_option('display.precision', prec)
    np.set_printoptions(precision=prec)

    symbols_list = list(args) if kwargs == {} else [value for key, value in kwargs.items()]
    expr1 = func(*symbols_list)
    cal_expr1 = lambdify(symbols_list, expr1, "numpy")
    gradient_ = gradient_sp(expr1, symbols_list)
    gradient_0 = cal_gradient_np(x0_, gradient_, symbols_list)
    d_0 = -gradient_0
    x_arr = [x0_]
    z_arr = [cal_expr1(*x0_)]
    alpha_arr = [0]
    beta_arr = [0]
    i = 0
    print(f"-------------- Conjugate Gradient Method {method_coff} --------------")
    while True:
        i += 1
        print(f"-------------- i = {i} --------------")
        model.change_func(func(*(x0_ + x * d_0)))
        alpha = model.start()
        x1_ = x0_ + alpha * d_0
        x_arr.append(x1_)
        z_arr.append(cal_expr1(*x1_))

        if abs(cal_vector_norm(np.array(x_arr[i - 1]) - np.array(x_arr[i]))) <= tol:
            print("In the tolerance :", tol)
            print("success to converge to a optimal solution")
            if check:
                alpha_arr.append(alpha)
                beta_arr.append(0)

            break
        elif i >= max_iterate:
            print("In the tolerance :", tol)
            print("fail to converge to a optimal solution")
            if check:
                alpha_arr.append(alpha)
                beta_arr.append(0)

            break

        gradient_1 = cal_gradient_np(x1_, gradient_, symbols_list)
        if no_linear and (initialize_condition(d_0, gradient_0) <= init_cond):
            d_0 = -gradient_1
        else:
            beta = cal_beta_formula(gradient_0, gradient_1, d_0, method_coff)
            d_0 = -gradient_1 + beta * d_0
        gradient_0 = gradient_1
        x0_ = x1_

        if check:
            alpha_arr.append(alpha)
            beta_arr.append(beta)

    if check:
        symbols_list.append("α")
        symbols_list.append("β")
        x_arr = np.hstack((x_arr, [[i] for i in alpha_arr]))
        x_arr = np.hstack((x_arr, [[i] for i in beta_arr]))

    symbols_list.append("Z")
    table = pd.DataFrame(data=np.hstack((x_arr, [[i] for i in z_arr])).reshape(len(x_arr), len(symbols_list)),
                         columns=symbols_list)

    return table
