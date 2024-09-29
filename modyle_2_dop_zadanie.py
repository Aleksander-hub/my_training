
def g_code(n):
    code = ''
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n %(i + j) == 0:
                code += f'{i}{j}'

    return code
for n in range(3, 20):
    code = g_code(n)
    print(f'{n} - {code}')







