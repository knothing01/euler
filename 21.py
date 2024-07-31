def check(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    
    return sum

sum = 0

for i in range(1, 10000):
    num = i
    tmp = check(num)
    tmp1 = check(tmp)
    if num != tmp and num == tmp1:
        sum += tmp1 

print(sum)