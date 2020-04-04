def checker(string):
    """checker checks for parentheses

    :type string: str
    :type return: False
    """
    stack = []
    parent_dic = {
        '{': '}',
        '(': ')',
        '[': ']',
    }
    for i in string:
        if i in parent_dic.keys():
            stack.append(i)
        elif i in parent_dic.values():
            if stack and parent_dic[stack[-1]] == i:
                stack.pop()
            else:
                return False
