input = open("./day1_input")

all = []
local = 0
for line in input:
    if line != "\n":
        local += int(line)
    else:
        all.append(local)
        local = 0
all.append(local)
all = sorted(all)
print(all[-1])
# 66616
print(sum(all[-1:-4:-1]))
# 199172
