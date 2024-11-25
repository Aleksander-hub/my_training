
def is_prime(func):
    def wrapper(*args):
        res = func(*args)

        for i in range(2, res):
            if res % i == 0:
                print('Составное число')
                return res
            else:
                print('Простое число')
                return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a+b+c


result = sum_three(2, 3, 6)
print(result)

# Не виноватая я!, он сам пришел

