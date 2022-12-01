input = open("./day1_input")

all = []
local = []
for line in input:
    if line != "\n":
        local.append(int(line))
    else:
        all.append(sum(local))
        local = []
all.append(sum(local))
all = sorted(all)
print(all[-1])
# 66616
print(sum(all[-1:-4:-1]))
# 199172
