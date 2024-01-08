def string_addition(str_list):
    sum = ""
    for i in str_list:
        sum += i

    return sum


def list_addition(list_list):
    sum = []
    for i in list_list:
        sum += i

    return sum


def seperate_single_elem(origin_list, max_length):
    copy_list1 = origin_list[:]

    for i in range(len(origin_list)):
        elem = origin_list[i]
        temp_list = []
        while len(elem) > max_length:
            temp_list.append(elem[:max_length])
            elem = elem[max_length:]
        temp_list.append(elem)
        copy_list1[i] = temp_list

    return list_addition(copy_list1)


def standard_string(str_list, max_length=15):
    # max_length = max(len(s) for s in str_list)
    s = '\n'.join(item.rjust(max_length) for item in str_list)

    return s


max_length = 15
list2 = ['29089900982', '+', '100923', '+', '1387898918', "-", "sin(9)", '=', "9898890089808"]
sign = '='
list2 = seperate_single_elem(list2, max_length=max_length)
index_ = list2.index(sign)
part1 = list2[:index_]
part2 = list2[index_:]
output_list = []
print(part1)
print(part2)
i = 1
while len(part1) >= i:
    if len(string_addition(part1[:i])) > max_length:
        output_list.append(string_addition(part1[:i - 1]))
        part1 = part1[i - 1:]
        i = 0
        continue
    i += 1
output_list.append(string_addition(part1))
s_part1 = standard_string(output_list)
s_part2 = standard_string(part2)
print(output_list)
print(part2)
print(s_part1)
print(s_part2)
print()
print(s_part1 + '\n' + s_part2)
