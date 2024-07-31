def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    i = 3

    while i * i <= num:
        if num % 2 == 0:
            return False
        i += 2

    return True


number = 600851475143
tmp = 2
a = []

while tmp <= number:
    if number % tmp == 0:
        if isPrime(tmp):
            a.append(tmp)
        number //= tmp
    else:
        tmp += 1 if tmp == 2 else 2

print(a)
