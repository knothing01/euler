def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2

    return True


sum = 0
for i in range(1, 2000000):
    if isPrime(i):
        sum += i

print(sum)
