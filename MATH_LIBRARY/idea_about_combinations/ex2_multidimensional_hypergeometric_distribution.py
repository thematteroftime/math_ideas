from ex2_product_limited_lists import get_All_lists
from permutation_and_combination import combination

n = 5  # chosen numbers
elem_array = ['X', 'Y', 'Z']
elem_number = 3

n_total = 100
x_total = 50
y_total = 30
z_total = 20

total_array = [n_total, x_total, y_total, z_total]


def choose_particular_array(sum_n, elem_number):
    if elem_number > sum_n:
        print("*****ERROR*****")
        return 0

    All_list = get_All_lists(elem_number, sum_n)
    chosen_list = []

    for i in range(len(All_list)):
        list = All_list[i]
        total = 0
        for j in range(elem_number):
            total += list[j]
        if total == sum_n:
            chosen_list.append(list)

    return chosen_list


P_total = 0

p_array = []
operated_list = choose_particular_array(n, elem_number)
for i in range(len(operated_list)):
    list = operated_list[i]
    p = 1
    for j in range(elem_number):
        p *= combination(total_array[j + 1], list[j])

    result = p / combination(total_array[0], n)
    P_total += result
    p_array.append(result)

    print('elements: ', end=' ')
    for z in range(elem_number):
        print(f"{str(elem_array[z]) + '=' + str(list[z])}", end=' ')
    print(f"{'| P = ' + str(result)}")

if P_total >= 0.9999999999:
    print("result is convinced")
else:
    print("the answer has some mistakes")
