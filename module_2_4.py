

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Primes = []
Not_Primes = []
for i in numbers:
    is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            continue
    if is_prime == True:
        if numbers[i] > 2:
            Primes.append(i)
    if is_prime == False:
        Not_Primes.append(i)
print(Primes)
print(Not_Primes)