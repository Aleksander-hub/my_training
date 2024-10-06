
data = [[1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),"Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data):
    summa = 0
    if isinstance(data, (list, tuple, set)):
        for i in data:
            summa += calculate_structure_sum(i)  #
    elif isinstance(data, dict):
        for j, value in data.items():
            summa += calculate_structure_sum(j)
            summa += calculate_structure_sum(value)
    elif isinstance(data, (int, float)):
        summa += data
    elif isinstance(data, str):
        summa += len(data)
    return summa


result = calculate_structure_sum(data)
print(result)
