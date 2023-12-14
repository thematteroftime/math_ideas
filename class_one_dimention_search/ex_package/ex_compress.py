from class_one_dimention_search.compress_interval_class import compress_interval_method
from class_one_dimention_search.symbols_store import *

pd.set_option("display.max_columns", None)


def function(x):
    return x * (x + 2)


def function2(x):
    return 2304 * x ** 2 - 577 * x + 39


def function3(x):
    return x ** 4 - 14 * x ** 3 + 60 * x ** 2 - 70 * x


func = function(x)
func2 = function2(x)
func3 = function3(x)
data = compress_interval_method(0, 2, func2, 1e-8, method_compress="Fibon", e=0.02, output='table')
# print(data.loc[:, ['a1', 'b1', 'a2', 'b2']])
