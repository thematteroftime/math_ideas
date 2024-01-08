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


def operate_history_single_str(str_list, max_length, sign='='):
    str_list = seperate_single_elem(str_list, max_length=max_length)
    index_ = str_list.index(sign)
    part1 = str_list[:index_]
    part2 = str_list[index_:]
    combine_list = []
    i = 1

    while len(part1) >= i:
        if len(string_addition(part1[:i])) > max_length:
            combine_list.append(string_addition(part1[:i - 1]))
            part1 = part1[i - 1:]
            i = 0
            continue
        i += 1
    combine_list.append(string_addition(part1))
    part2[1] = part2[0] + part2[1]

    s_part1 = standard_string(combine_list)
    s_part2 = standard_string(part2[1:])

    output_string = s_part1 + '\n' + s_part2

    return output_string



# list_try = ['29089900982', '+', '100923', '+', '1387898918', "-", "sin(9)", '=', "9898890089808"]
# print(operate_history_single_str(list_try, 15))

"""


    # operate history
    def string_addition(self, str_list):
        sum = ""
        for i in str_list:
            sum += i

        return sum

    def list_addition(self, list_list):
        sum = []
        for i in list_list:
            sum += i

        return sum

    def seperate_single_elem(self, origin_list, max_length):
        copy_list1 = origin_list[:]

        for i in range(len(origin_list)):
            elem = origin_list[i]
            temp_list = []
            while len(elem) > max_length:
                temp_list.append(elem[:max_length])
                elem = elem[max_length:]
            temp_list.append(elem)
            copy_list1[i] = temp_list

        return self.list_addition(copy_list1)

    def standard_string(self, str_list, max_length=15):
        # max_length = max(len(s) for s in str_list)
        s = '\n'.join(item.rjust(max_length) for item in str_list)

        return s

    # main module
    def operate_history_single_str(self, str_list, max_length, sign='='):
        str_list = self.seperate_single_elem(str_list, max_length=max_length)
        index_ = str_list.index(sign)
        part1 = str_list[:index_]
        part2 = str_list[index_:]
        combine_list = []
        i = 1

        while len(part1) >= i:
            if len(self.string_addition(part1[:i])) > max_length:
                combine_list.append(self.string_addition(part1[:i - 1]))
                part1 = part1[i - 1:]
                i = 0
                continue
            i += 1
        combine_list.append(self.string_addition(part1))

        s_part1 = self.standard_string(combine_list)
        s_part2 = self.standard_string(part2)
        output_string = s_part1 + '\n' + s_part2

        return output_string

"""
