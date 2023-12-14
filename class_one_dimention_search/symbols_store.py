from sympy import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sympy as sp


def produce_symbol_list(n):
    return list(symbols(f"x1:{n + 1}"))


x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20 = symbols('x1:21')
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = \
    symbols('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
a, b, c = symbols('a b c')
x = symbols('x')
