import string
input = open("./day3_input")

dict1 = {a: b for a, b in zip(string.ascii_lowercase, range(1, 26+1))}
dict2 = {a: b for a, b in zip(string.ascii_uppercase, range(26+1, 26*2+1))}
dict1.update(dict2)

result = 0
for line in input:
    line = line.strip().replace(' ', '').replace('\n', '')
    half = len(line)//2
    line_1, line_2 = line[:half], line[half:]
    common = list(set(line_1) & set(line_2))
    result += dict1[common[0]]

print(result)
# 8053

result = 0
# dirty
input = open("./day3_input")
for line_1, line_2, line_3 in zip(input, input, input):
    line_1 = line_1.strip().replace(' ', '').replace('\n', '')
    line_2 = line_2.strip().replace(' ', '').replace('\n', '')
    line_3 = line_3.strip().replace(' ', '').replace('\n', '')
    common = list(set(line_1) & set(line_2) & set(line_3))
    result += dict1[common[0]]
print(result)
# 2425
