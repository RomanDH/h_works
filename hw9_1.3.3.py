def most_com(str):
    """
    Return most common symbol
    :param str: path
    :return str: most common symbol
    """
    from collections import Counter
    file = open(str)
    read_file = file.read()
    indexes = []
    for i in read_file:
        if i == ' ':
            del (i)
        else:
            indexes.append(ord(i))
    c = Counter(indexes)
    max_val_ = list(c.elements())[0]
    res = chr(max_val_)
    file.close()
    return res

