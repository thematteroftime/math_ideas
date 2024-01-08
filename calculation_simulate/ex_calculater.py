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


def operate_list_elem(origin_list, max_length):
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


max_length = 10
list2 = ['290890982', '+', '123', '+', '13818', "-", "sin(9)", '=', "9898890089808"]
sign = '='
index_ = list2.index(sign)
part1 = list2[:index_]
part2 = list2[index_:]
output_list = []
for i in range(len(part1)):
    print(part1[:i])
    print(len(string_addition(part1[:i])))
    if len(string_addition(part1[:i])) > max_length:
        output_list.append(string_addition(part1[:i - 1]))
        part1 = part1[i - 1:]
        i = 0
output_list.append(string_addition(part1))
print(output_list)

string_part2 = part2[1]
temp_str = ""
temp_list = []
while len(string_part2) > max_length:
    temp_list.append(string_part2[:max_length + 1])
    string_part2 = string_part2[max_length + 1:]
temp_list.append(string_part2)
print(temp_list)

print(operate_list_elem(list2, max_length=10))

