num = int(input('Input:'))


def all_divi(int):
    list_to_num = list(range(1, num + 1))
    new_list = []
    for i in list_to_num:
        if num % i == 0:
            new_list.append(i)
    return new_list


print(all_divi(num))
