def num_dig(num):
    if num == 0:
        return 1
    count = 0
    while(num):
        count += 1
        num //= 10

    return count 

arr = []

def fib():
    a = 1
    b = 1
    count = 2
    while(num_dig(b) < 1000):
        a, b = b, a + b
        arr.append(a)
        count += 1
    return count

res = fib()
print(res)
print(num_dig(arr[-1]))