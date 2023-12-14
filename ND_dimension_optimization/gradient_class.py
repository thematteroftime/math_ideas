from class_one_dimention_search.one_dimension_search import search_1D
from class_one_dimention_search.symbols_store import *

default_model = search_1D(func=None, method="newton", x0=0.5, tol=1e-8, output='align', prec=8, max_iterate=500)


# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)

def gradient_formula(func, symbol_arr):
    derivate_arr = []
    expr = func(*symbol_arr)

    for i in range(len(symbol_arr)):
        derivate_arr.append(lambdify(symbol_arr, expr.diff(symbol_arr[i], 1), "numpy"))

    return derivate_arr


def cal_gradient(derivate_arr, symbol_arr, x0):
    output = []
    for i in range(len(symbol_arr)):
        output.append(derivate_arr[i](*x0))

    return output


def produce_symbol_arr(**kwargs):
    symbol_arr = []
    for key, value in kwargs.items():
        symbol_arr.append(value)
    return symbol_arr


def norm(vector):
    sum = 0
    for i in range(len(vector)):
        sum += vector[i] ** 2
    return sum ** 0.5


def gradient_descent(func, x0, model=default_model, tol=1e-8, max_iterate=100, prec=8, *args, **kwargs):
    if model == default_model:
        model.property['tol'] = tol
        model.property['prec'] = prec
    pd.set_option('display.precision', prec)
    np.set_printoptions(precision=prec)

    symbol_arr = list(args) if kwargs == None else produce_symbol_arr(**kwargs)
    derivate_arr = gradient_formula(func, symbol_arr)
    x_arr = [list(x0)]
    i = 1
    print("-------------- Gradient Descent --------------")
    while True:
        grad1 = np.array(cal_gradient(derivate_arr, symbol_arr, x0))
        expr1 = func(*(x0 - x * grad1))

        print(f"---------------- i = {i} ----------------")
        model.change_func(expr1)
        r = model.start()
        print(r)

        x0 = x0 - r * grad1
        x_arr.append(list(x0))

        if abs(norm(np.array(x_arr[i]) - np.array(x_arr[i - 1]))) <= tol:
            print("In the tolerance: ", tol)
            print("success to converge to a root")
            break

        if i >= max_iterate:
            print("In the tolerance: ", tol)
            print("Had been over the max iteration number limits")
            break

        i += 1

    table = pd.DataFrame(data=np.array(x_arr).reshape(len(x_arr), len(x_arr[0])), columns=[symbol_arr])

    return table
