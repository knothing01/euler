def isPalindrome(num):
    tmp = num
    reverse = 0
    remainder = 0
    while num:
       remainder = num % 10 
       reverse = reverse * 10 + remainder
       num //= 10

    if (tmp == reverse):
        return True
    else:
        return False

maximum = 0
tmp = list()

for i in range(100, 1000):
    for j in range(100, 1000):
        number = i * j
        if (isPalindrome(number)):
            tmp.append(number)
            maximum = max(tmp)

print(maximum)

