from ex1_product_lists import product_list
from ex1_product_lists import All_list

arr_species = [[0, 0], [0, 1], [1, 0], [1, 1]]
arr_power = [1, 1000, 1000000, 1000000000]

n = 15

"""
生成由n个[0,1]数组生成的大集合,元素为:[0,0],[0,1],[1,0],[1,1]  
并且对其中的元素权重进行统计
"""


def statistic_combinations(arr):
    list_statistic = []
    for i in range(len(arr) - 1):
        list_statistic.append([arr[i]] + [arr[i + 1]])
    return list_statistic


def statistic_combinations_number(arr):
    total = 0
    for e in range(len(arr)):
        total += get_power(arr[e])
    return total
    # print(total)


def get_power(arr):
    for p in range(len(arr_species)):
        if arr == arr_species[p]:
            return arr_power[p]


product_list(n, 0)

for i in range(len(All_list)):
    list1 = []
    list1 = statistic_combinations(All_list[i])
    list1_power = 0
    list1_power = statistic_combinations_number(list1)
    print(list1, end=': ')
    print(list1_power)
