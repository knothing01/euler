res = 0
sum = 0

with open("0022_names.txt", 'r') as file:
    content = file.read()

names = [name.strip().strip('"') for name in content.split(',')]
uppercase_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

names.sort()

for name in names:
    curr_score = 0
    for char in name:
        curr_score += uppercase_alphabet.index(char) + 1
        
    res += (curr_score * (names.index(name) + 1))

print(res)