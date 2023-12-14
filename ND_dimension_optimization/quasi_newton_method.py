from class_one_dimention_search.symbols_store import *
from class_one_dimention_search.one_dimension_search import search_1D
from scipy.optimize import line_search

pd.set_option('display.max_columns', None)
default_model = search_1D(func=None, method="newton", x0=0.5, tol=1e-8, output='align', prec=8, max_iterate=500)


def gradient(func: sp.Symbol,
             symbol_arr: list) -> list:
    gradient_arr = []
    for i in range(len(symbol_arr)):
        gradient_arr.append(func.diff(symbol_arr[i]))

    return gradient_arr


def cal_gradient(gradient_arr: list,
                 symbol_arr: list,
                 x0_: np.ndarray) -> np.ndarray:
    cal_gradient = []
    for i in range(len(symbol_arr)):
        cal_gradient.append([lambdify(symbol_arr, gradient_arr[i], "numpy")(*x0_)])

    return np.array(cal_gradient)


def cal_H_approximate_matrix(H0_: np.ndarray,
                             delta_x: np.ndarray,
                             delta_g: np.ndarray,
                             method: str) -> np.ndarray:
    DFP_part1 = np.dot(delta_x, delta_x.T) / np.dot(delta_x.T, delta_g)
    DFP_denominator = np.dot(np.dot(delta_g.T, H0_), delta_g)

    if method == "DFP":
        numerator = np.dot(np.dot(H0_, delta_g), np.dot(H0_, delta_g).T)
        return H0_ + DFP_part1 - numerator / DFP_denominator

    elif method == "BFGS":
        second_part_deno = np.dot(delta_g.T, delta_x)
        BFGS_part1 = (1 + DFP_denominator / second_part_deno) * DFP_part1
        second_part_numer = np.dot(np.dot(H0_, delta_g), delta_x.T)
        BFGS_part2 = (second_part_numer + second_part_numer.T) / second_part_deno
        return H0_ + BFGS_part1 - BFGS_part2


def norm(vector: np.ndarray | list):
    sum = 0
    for i in range(len(vector)):
        sum += vector[i] ** 2
    return sum ** 0.5


def quasi_newton_method(func: "function", x0_: np.ndarray | list, tol: float = 1e-4,
                        prec: int = 4, tol_model: float = 1e-8, method: str = "DFP",
                        model=default_model, max_iterate=200, alpha_func=None, alpha_grad=None, scipy_alpha=False,
                        *args, **kwargs):
    method_list = ["DFP", "BFGS"]
    if method not in method_list:
        print("Invalid Input")
        return 0

    if model == default_model:
        model.property['tol'] = tol_model
        model.property['prec'] = prec
    pd.set_option('display.precision', prec)
    np.set_printoptions(precision=prec)

    symbols_list = list(args) if kwargs == {} else [value for key, value in kwargs.items()]
    expr = func(*symbols_list)
    H0_ = np.eye(len(symbols_list))
    cal_expr = lambdify(symbols_list, expr, "numpy")
    gradient_ = gradient(expr, symbols_list)

    print(f"-------------- Quasi Newton Method ND {method} --------------")
    i = 0
    x_list = [list(x0_)]
    z_list = [cal_expr(*x0_)]
    cal_gradient_0 = cal_gradient(gradient_, symbols_list, x0_)

    while True:
        i += 1
        d0_ = -np.dot(H0_, cal_gradient_0)
        print(f"--------- i = {i} ---------")
        if scipy_alpha:
            alpha = line_search(alpha_func, alpha_grad, x0_, d0_.flatten())[0]
        else:
            model.change_func(func(*(x0_ + x * d0_.flatten())))
            alpha = model.start()
        print("alpha:", alpha)

        x1_ = x0_ + alpha * d0_.flatten()
        x_list.append(list(x1_))
        z_list.append(cal_expr(*x1_))

        if abs(norm(np.array(x_list[i - 1]) - np.array(x_list[i]))) <= tol:
            break
        if i >= max_iterate:
            print(f"After {max_iterate} times iterations ")
            print("Fail to converge to a root")
            break

        cal_gradient_1 = cal_gradient(gradient_, symbols_list, x1_)
        H0_ = cal_H_approximate_matrix(H0_, alpha * d0_,
                                       cal_gradient_1 - cal_gradient_0,
                                       method)
        x0_ = x1_
        cal_gradient_0 = cal_gradient_1

    symbols_list.append("Z")
    table = pd.DataFrame(data=np.hstack((x_list, [[i] for i in z_list])).reshape(len(x_list), len(symbols_list)),
                         columns=symbols_list)

    return table
