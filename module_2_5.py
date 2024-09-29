

cod = []
list_1 = []
list_2 = []
for i in range(1,20):
    for j in  range(i):
        if i + j == 9:
            list_1.append([i])
            list_2.append([j])
            print(i,j)


print(list_1)
print(list_2)
