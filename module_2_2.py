first = int (input('введите число №1: '))
second = int (input('введите число №2: '))
third = int (input('введите число №3: '))
if first == second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')
