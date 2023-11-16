list1 = []
All_list = []

"""
'number_of_list' mean you want to choose elements in n arrays.
[0 , 1], [0 , 1], [0 , 1], [0 , 1], [0 , 1] .... 
the number i in range(*) can be changed to product the particular array which elements in the range of zero to i-1
"""

def product_list(number_of_list, c=0):
    global list1

    if number_of_list == c:
        All_list.append(list1[:c + 1])
        list1.pop()
        return

    for i in range(2):
        list1 = list1[:c] + [i]
        product_list(number_of_list, c + 1)


# product_list(4)
# print(All_list)
# if list1 == []:
#     list1.append(i)
# elif list1[:c] != None:
#     list1 = list1[:c] + [i]
