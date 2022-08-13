from functools import singledispatch
from multiprocessing.sharedctypes import Value


@singledispatch
def count_down(data_type):
    # TODO: Learn how to use singledispatch!
    if not isinstance(data_type, (int, str, list, tuple, set, dict, float, range)):
        raise ValueError()
    print(data_type)

@count_down.register(int)
def _int(data_type):
    i = 1
    while i <= 1000:
        print(data_type // i)
        i *= 10

@count_down.register(str)
def _str(data_type):
    for i in range(len(data_type), 0, -1):
        print(data_type[:i])

@count_down.register(list)
def _list(data_type):
    data_type = [str(char) if isinstance(char, int) else char for char in data_type]
    for i in range(len(data_type), 0, -1):
        print("".join(data_type[:i]))

@count_down.register(tuple)
def _tuple(data_type):
    data_type = list(data_type)
    count_down(data_type)

@count_down.register(set)
def _set(data_type):
    data_type = list(data_type)
    count_down(data_type)

@count_down.register(dict)
def _dict(data_type):
    data_type = {str(key) if isinstance(key, int) else key for key in data_type.keys()}
    data_type = sorted(list(data_type))
    count_down(data_type)

@count_down.register(range)
def _range(data_type):
    data_type = "".join([str(data_type[i -1]) for i in data_type])
    count_down(data_type)

@count_down.register(float)
def _float(data_type):
    count_down(str(data_type))