def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    
    return True

num = 41
sum = 0

for i in range(1, num):
    if(is_prime(i) and sum != num):
        sum += i

print(sum)

