


def apply_all_func(int_list, *functions):
    res = {}
    for i in functions:
        res[str(i.__name__)] = i(int_list)
    return res


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 20, 15, 9], any, format))
