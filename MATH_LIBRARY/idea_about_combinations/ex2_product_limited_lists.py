"""
'number_of_list' mean you want to choose elements among n arrays.
c is pedometer
the number,e , can be changed to product the particular array which elements in the range of zero to e
"""
list1 = []
All_list = []


def product_list(number_of_list, e, c=0):
    global list1

    if number_of_list == c:
        All_list.append(list1[:c + 1])
        list1.pop()
        return

    for i in range(e + 1):
        list1 = list1[:c] + [i]
        product_list(number_of_list, e, c + 1)


def get_All_lists(number_of_list, e):
    product_list(number_of_list, e)
    return All_list

# product_list(3, 5)
# print(All_list)
