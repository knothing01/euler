all_digits = [i for i in range(1,10)]

def to_digit(num):
    tmp = 0
    tmp_arr = []
    while(num):
        tmp = num % 10
        tmp_arr.append(tmp)
        num //= 10

    tmp_arr.reverse()
    for i in range(len(tmp_arr)):
        all_digits.append(tmp_arr[i])
    
    tmp_arr.clear()

def find_index(given):
    given *= 10
    return given

num = 10
while len(all_digits) < 1000000:
    to_digit(num)
    num += 1

sum = 1
given = 1

for _ in range(7):
    sum*= all_digits[given - 1]
    given = find_index(given)


print(sum)