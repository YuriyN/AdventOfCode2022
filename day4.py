input = open('./day4_input')

ranges = [line.strip().replace(' ', '').replace(',', '-').split('-') for line in input]
sets = [(set(range(int(r[0]), int(r[1])+1)), set(range(int(r[2]), int(r[3])+1))) for r in ranges]

result = 0
for s in sets:
    result += int(s[0].issubset(s[1])) if len(s[0]) < len(s[1]) else int(s[1].issubset(s[0]))
print(result)
# 536

result = 0
for s in sets:
    result += int(len(s[0] & s[1]) > 0)
print(result)
# 845
