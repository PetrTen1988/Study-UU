data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def unziper(data):
    count = 0
    if isinstance(data, int):
        count += data
    elif isinstance(data, str):
        count += len(data)
    elif isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for elem in data:
            count += unziper(elem)
    elif isinstance(data, dict):
        lists_sum = list(data.keys()) + list(data.values())
        count += unziper(lists_sum)

    return count


print(unziper(data_structure))


