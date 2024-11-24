
def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        log = True
        for i in range(1, res):
            if res % i == 0:
                log = False
        if log == True:
            print('Составное число')
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

