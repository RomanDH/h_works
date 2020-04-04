def my_map(func, iterable):
    return functools.reduce(lambda accum, val: accum + [func(val)], iterable, [])
