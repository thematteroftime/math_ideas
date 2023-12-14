from class_one_dimention_search.Newton_method_class import Newton_method
from class_one_dimention_search.compress_interval_class import compress_interval_method
from class_one_dimention_search.Bisection_class import bisection_method
from class_one_dimention_search.symbols_store import *


class search_1D:
    def __init__(self, func, method, tol=1e-4, output="table", prec=6, **kwargs):
        self.method = method

        copy_kwargs = kwargs
        copy_kwargs["tol"] = tol
        copy_kwargs["func"] = func
        copy_kwargs["prec"] = prec
        copy_kwargs["output"] = output

        self.property = copy_kwargs

    def start(self):
        choice = self.method

        if choice == "newton":
            return self.Newton()
        elif choice == "compress":
            return self.Compress()
        elif choice == "bisection":
            return self.Bisection()
        else:
            print("INVALID INPUT")
            return 0

    def Newton(self, **kwargs):
        dict_ = self.property if kwargs == {} else kwargs
        dict_["func"] = dict_["func"].diff(x)
        output = Newton_method(**dict_)

        return output

    def Compress(self, **kwargs):
        dict_ = self.property if kwargs == {} else kwargs
        output = compress_interval_method(**dict_)

        return output

    def Bisection(self, **kwargs):
        dict_ = self.property if kwargs == {} else kwargs
        dict_["func"] = dict_["func"].diff(x)
        output = bisection_method(**dict_)

        return output

    def change_func(self,func_changed):
        self.property["func"] = func_changed
        return 0



