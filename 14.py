def chain (num):
    return num // 2 if num % 2 == 0 else 3 * num + 1

curr = 0

for i in range(1000001):
    x = i
    count = 1
    
    while x != 1:
        x = chain(x)
        count += 1

        if (curr > count):
          curr = count


print(curr)

