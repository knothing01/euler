def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True




# formula n^2 + an + b 
# |a| < 1000 & |b| <= 1000
# n = 0

def quadratic_primes(a, b):
    n = 0
    while True:
        value = n * n + a * n + b
        if value <= 0 or not is_prime(value):
            break
        n += 1

    return n

def find_max():
    max_prime = 0
    a_res = 0
    b_res = 0

    for a in range (-1000, 1001):
        for b in range(-1000, 1001):
            num_prime = quadratic_primes(a, b)
            if num_prime > max_prime:
                max_prime = num_prime
                a_res = a
                b_res = b


    return a_res * b_res


result = find_max()
print(result)
