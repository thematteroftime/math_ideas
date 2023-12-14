"""
expression:
c1 + (x − r1)(c2 + (x − r2)(c3 + (x − r3)(c4 + (x − r4)(c5))))...
use matrix to represent the coefficients and base points
"""

import numpy as np


def Horner_method(n, c_arr, x_arr, r_arr=[], error_analysis=False, Function=None):
    if r_arr == []:
        for i in range(n):
            r_arr.append(0)

    c_arr.reverse()
    r_arr.reverse()

    y_arr = []

    for i in range(len(x_arr)):
        y = c_arr[0]
        x = x_arr[i]
        for j in range(n):
            y = c_arr[j + 1] + (x - r_arr[j]) * y
        y_arr.append(y)

    for i in range(len(x_arr)):
        print(f"x={x_arr[i]}: y={y_arr[i]}")

    if error_analysis:
        result1 = y_arr.copy()
        result2 = Function(x_arr[0])
        error = abs((result1[0] - result2) / result1[0])
    else:
        error = None

    return y_arr, error


def Function(x):
    return (1 - x ** 100) / (1 + x)


"""
test: −1 + x ∗ (5 + x ∗ (−3 + x ∗ (3 + x ∗ 2)))
"""
c_arr = []
for i in range(100):
    if i % 2 == 0:
        c_arr.append(1)
    else:
        c_arr.append(-1)

x = 1.000001
y_arr, error = Horner_method(99, c_arr=c_arr, x_arr=[x], error_analysis=True, Function=Function)

print(error)

# error:1.3605856627309218e-12 (x ** 51 - 1) / (x - 1)
# error:1.5507803494966424e-11 (1-x**100)/(1+x)
