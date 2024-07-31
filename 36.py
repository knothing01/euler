def is_palindrome(num):
    tmp = str(num)
    bin_tmp = bin(num)[2:]

    if (tmp == tmp[::-1]) and (bin_tmp == bin_tmp[::-1]):
        return True 
    return False

sum = 0
for i in range(1, 1000000):
    if is_palindrome(i):
        sum += i

print(sum) 

