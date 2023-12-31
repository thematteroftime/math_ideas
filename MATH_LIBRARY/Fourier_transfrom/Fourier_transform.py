import numpy as np
import matplotlib.pyplot as plt
import random
import time
from tqdm import trange


def origin_fun_x_y(l, T):
    x_arr = []
    y_arr = []
    x0 = np.linspace(0, 2 * l, 100)
    y0 = original_function(x0)
    for i in range(min(T), max(T)):
        x1 = x0 + i * 2 * l
        x_arr.extend(list(x1))
        y_arr.extend(list(y0))
    return x_arr, y_arr


def original_function(x):
    y_arr = []
    for i in range(len(x)):
        if x[i] >= 2 or x[i] <= 1:
            y_arr.append(10)
        else:
            y_arr.append(0)
    return y_arr


def cal_mass_center(x_arr, y_arr):
    return sum(x_arr) / len(x_arr), sum(y_arr) / len(y_arr)


def random_init_fun(W_arr, x_input):
    y_output = 0
    for i in range(len(W_arr)):
        choice = random.choice(['sin', 'cos'])
        if choice == 'sin':
            y_output += np.sin(W_arr[i] * x_input)
        else:
            y_output += np.cos(W_arr[i] * x_input)
    return y_output + len(W_arr)


# module choose frequency spectrum(x -> T) (y -> the distance of center point)
def module_choose_plot_T(T_init_arr, T_chosen_arr, num_left, num_right, prec=6):
    init_max = max(T_init_arr)
    chosen_max = max(T_chosen_arr)
    T_max_fun = lambda x, y: x if x >= y else y
    T_max = T_max_fun(init_max, chosen_max)

    T_ouput_arr = []
    if T_max <= 1:
        T_left = list(np.round(np.linspace(0, 1, num_left + num_right), prec))
        T_right = []
    else:
        T_left = list(np.round(np.linspace(0, 1, num_left), prec))
        T_right = list(np.round(np.linspace(1, T_max, num_right), prec))

    T_ouput_arr.extend(T_left)
    T_ouput_arr.extend(T_right)

    return T_ouput_arr


# module choose T
def module_choose_T(T_init_arr, num, way):
    if way == "range":
        T_arr = user_choose_T_range(T_init_arr, num)
    elif way == "single":
        T_arr = user_choose_T_single(T_init_arr, num)
    else:
        T_arr = default_choose_T(T_init_arr, num)
    return T_arr


# 'default'
def default_choose_T(T_init_arr, num):
    if len(T_init_arr) == 1:
        elem = T_init_arr[0]
        return list(np.linspace(elem - elem / 2, elem + elem / 2, num=num))
    T_min = min(T_init_arr)
    T_max = max(T_init_arr)
    center_T = (T_min + T_max) / 2
    interval = (T_max - T_min) / len(T_init_arr)
    T_arr_chosen = list(np.linspace(center_T - interval, center_T + interval, num=num))
    return T_arr_chosen


# 'range'
def user_choose_T_range(T_init_arr, num):
    print("please tap the range of T which you want to choose")
    print("The original T array: ")
    print(sorted(T_init_arr))

    T_min = float(input("MIN: "))
    T_max = float(input("MAX: "))
    if T_min > T_max:
        term = T_min
        T_min = T_max
        T_max = term

    T_arr_chosen = list(np.linspace(T_min, T_max, num=num))

    return T_arr_chosen


# 'single'
def user_choose_T_single(T_init_arr, num):
    T_arr_chosen = []
    print("please tap T you had chosen: ")
    print("The original T array: ")
    print(sorted(T_init_arr))

    for i in range(num):
        T_chosen = float(input())
        T_arr_chosen.append(T_chosen)

    return T_arr_chosen


# initial T, W (type : array)
T_arr = [2, 0.5, 0.8, 1, 2.5]
W_arr = []
for i in range(len(T_arr)):
    W_arr.append(2 * np.pi / T_arr[i])

# excitement function
num = 20000
x_init = np.linspace(-500, 500, num)
y_init_fun = random_init_fun(W_arr, x_init)

# plot the init function
# create row * columns container to save the plots
row = 2
columns = 3
fig = plt.figure(dpi=85, figsize=(16, 16))
ax = plt.subplot(row + 2, 1, row + 1)
ax.plot(x_init, y_init_fun, 'r-', linewidth=1)
ax.grid()

# 'range' mean choose the range of T
# 'single' mean choose T one by one
# 'default' mean choose one range around middle point
choice = 'single'
T_arr_chosen = module_choose_T(T_arr, row * columns, way=choice)
W_arr_chosen = []
for i in range(len(T_arr_chosen)):
    W_arr_chosen.append(2 * np.pi / T_arr_chosen[i])

mass_x = []
mass_y = []

for i in trange(row * columns, desc="plot polar", unit="epoch"):
    ax = plt.subplot(row + 2, columns, i + 1)
    x_arr = []
    y_arr = []
    for j in range(len(x_init)):
        x_arr.append(y_init_fun[j] * np.cos(W_arr_chosen[i] * x_init[j]))
        y_arr.append(y_init_fun[j] * np.sin(W_arr_chosen[i] * x_init[j]))

    # from rectangular coordinate system to polar coordinate
    ax.scatter(x_arr, y_arr, c=list(range(len(x_arr))), cmap=plt.cm.Blues, s=10, label=f'T={round(T_arr_chosen[i], 4)}')
    ax.set_title(f'T={round(T_arr_chosen[i], 4)}')
    ax.legend(loc="lower right")
    ax.grid()

    # set the center point you can let it be a mass point
    center_x, center_y = cal_mass_center(x_arr, y_arr)
    ax.plot([0, center_x], [0, center_y], 'r-')
    ax.scatter(center_x, center_y, s=30)
    mass_x.append(T_arr_chosen[i])
    mass_y.append((center_x ** 2 + center_y ** 2) ** 0.5)

ax = plt.subplot(row + 2, 1, row + 2)
ax.scatter(mass_x, mass_y, s=50, label="chosen point")

mass_x = []
mass_y = []
num_left = 3000
num_right = 1000
T_chosen_plot = module_choose_plot_T(T_arr, T_arr_chosen, num_left, num_right, prec=4)
W_chosen_plot = []

for i in range(len(T_chosen_plot)):
    if T_chosen_plot[i] == 0.0:
        W_chosen_plot.append(0)
        continue
    W_chosen_plot.append(2 * np.pi / T_chosen_plot[i])

for i in trange(num_right + num_left, desc="plot x=T y=origin_y", unit="epoch"):
    x_arr = []
    y_arr = []

    for j in range(len(x_init)):
        x_arr.append(y_init_fun[j] * np.cos(W_chosen_plot[i] * x_init[j]))
        y_arr.append(y_init_fun[j] * np.sin(W_chosen_plot[i] * x_init[j]))

    center_x, center_y = cal_mass_center(x_arr, y_arr)
    mass_x.append(T_chosen_plot[i])
    mass_y.append((center_x ** 2 + center_y ** 2) ** 0.5)

print(mass_x)
print(mass_y)
start = 1
ax.scatter(mass_x[start:], mass_y[start:], c=list(range(len(mass_x[start:]))), cmap=plt.cm.Reds, s=10)
ax.plot(mass_x[start:], mass_y[start:], 'r--')
ax.grid()
plt.tight_layout()
plt.show()
