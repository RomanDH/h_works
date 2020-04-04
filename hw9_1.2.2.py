def second_val(list):
    """
    Takes the list and return second largest value at the list(ASCII)
    :param : list
    :return str: second largest value
    """
    str_list = []
    indexes = []
    for i in list:
        str_list += str(i)

    for j in str_list:
        indexes.append(ord(j))
    to_set = set(indexes)
    res_list = []

    for val in to_set:
        res_list.append(val)
    return chr(res_list[-1])
