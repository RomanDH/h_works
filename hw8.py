import os


def check_dir(path):"""
    Shows the contents of the directory [path, dirs, files]
    :param str: path
    :return list: [path, dirs, files]
    """
    var_dir = []
    var_files = []
    for i in os.listdir(path):
        new_path = path + '/' + i
        if os.path.isdir(new_path):
            var_dir.append(new_path)
        else:
            var_files.append(new_path)
    return [path, var_dir, var_files]


def my_walk(path):
    dir_cont = []
    files = []
    result = []
    if os.path.isfile(path):
        files.append(path)
    else:
        if os.path.isdir(path):
            dir_cont.append(path)
            result.append(check_dir(path))  # в result вернёт списки вложенные в список.
            # для решения проблемы вложенности списков,...
            # ...вероятно необходима еще одна рекурсия

    for next_step in result:
        if next_step != []:
    # return my_walk(next_step), result
    # путь my_walk() должен быть строкой, а не списком..
    # ..тем более c вложенным списком

